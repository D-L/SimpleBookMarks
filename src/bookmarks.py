#coding: utf8

from bottle import get,post,redirect,response,request,template
from utils import wrapdb,compressit,html_escape,refineTag,ulen,ulenget,nt,getshorturlid
from dbutils import createnewcat
import re,StringIO

bookmarkHead="""<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
    It will be read and overwritten.
    Do Not Edit! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<Title>Bookmarks</Title>
<H1>Bookmarks</H1>
<DL><p>"""
bookmarkEnd="</DL><p>"

CATNAME=re.compile('>([^\<]+)</H3>',re.I)
LINKNAME=re.compile('>([^\<]+)</A>',re.I)
LINKHREF=re.compile('<DT><A\sHREF="([^\"]+)\"',re.I)

class bookmarkParser(object):
	def __init__(self):
		#links: (title,url,tags)
		self.cats = []
		self.curcat = None #当前的category {'title' : title,'links':}
		self.tags = []     #当前的Tags

	def parse(self,content):
		"""
			分析这个文件的内容
		"""
		for line in StringIO.StringIO(content):
			self.processline(line)

		return self.cats
		
	def processline(self,line):
		line = line.strip()
		if line.find('<DT><H3')==0: #开始一个新的Category了.
			n = self.getcatname(line)
			if not self.curcat:
				if n: self.curcat = {'title':n,'links':[]}
				else: self.curcat = {'title':'空目录名','links':[]}
				self.cats.append(self.curcat)
			else:
				self.tags.append(n) #增加到Tag中
		elif line == '<DL><p>': #进入Category
			pass
		elif line == '</DL><p>': #退出Category
			if self.tags:
				self.tags.pop()	
			else:
				self.curcat = None
		elif line.find('<DT><A') == 0: #一个Link
			if not self.curcat: return
			v = self.getlink(line)
			if not v: return
			title,href = v
			link = (title,href,refineTag(','.join(self.tags)))
			self.curcat['links'].append(link)
	def getlink(self,line):
		"""
			得到链接的具体信息.
		"""
		def dotitle(title):
			return title.replace('&amp;','&').replace('&gt;','>').replace('&lt;','<').replace('&nbsp;',' ').replace('&quot;','"').replace('&copy;','©').replace('&sect;','§').replace('&trade;','™').replace('&pound;','£')

		def validlink(link):
			link =  link.lower()
			if (link.find('http://') != 0) and (link.find('https://') !=0): return False
			return True

		title = ''
		href =''
		r=LINKNAME.search(line)
		if r: title = dotitle(r.group(1))
		r = LINKHREF.search(line)
		if r: href = r.group(1)

		if not validlink(href): return None
		return (title,href)
			
	def getcatname(self,line):
		#<DT><H3 ADD_DATE="1347859436" LAST_MODIFIED="1352946109" PERSONAL_TOOLBAR_FOLDER="true">Bookmarks Bar</H3>
		ret = CATNAME.search(line)
		if not ret:return ''
		return ret.group(1)
			
		
def importBookmark(content):
	"""
		接受用户上传的数据.
		只接收Category和URL,Title，其他的不接受了.
		返回一个完整的结果
		[
			{
				'title' : title,
				'links':[(title,url,tag)]
			}
		]
	"""
	p = bookmarkParser()
	return p.parse(content)

def exportBookmark(bookmarks):
	"""
		导出某人的书签，形成HTML格式的问题
		bookmarks:
		[
			(categoryname,adddate,[(url,title,adddate)])
			(categoryname,adddate,[(url,title,adddate)])
			(categoryname,adddate,[(url,title,adddate)])
		]
		urlid -> 获取favicon.ico用
	"""
	def exportUrls(urls):
		#[(url,title,adddate)]
		htmlcode.append('    <DL><p>');
		for url,title,adddate in urls:
			htmlcode.append('      <DT><A HREF="%s" ADD_DATE="%s">%s</A>' % (url,adddate,title))
		htmlcode.append('    </DL><p>');
	htmlcode = [bookmarkHead]
	for categoryname,adddate,urls in bookmarks:
		#创建一层Category
		htmlcode.append('  <DT><H3 ADD_DATE="%s" LAST_MODIFIED="0">%s</H3>' % (adddate,categoryname))
		exportUrls(urls)
	htmlcode.append(bookmarkEnd)
	return '\n'.join(htmlcode)

@get("/export/")
@wrapdb
def export(db):
	"""
		输出书签下载
	"""
	#--导出数据--
	cats = {}
	db.execute('SELECT ID,TITLE FROM CATEGORY')
	for cid,title in db.getall():
		cats[int(cid)]=html_escape(title)

	db.execute('SELECT CATEGORY_ID,URL,TITLE,1304560792 FROM URLS')
	data = {} #
	dt = {}
	for cid,url,title,adddate in db.getall():
		cid = int(cid)
		if cid in data:
			data[cid].append((html_escape(url),html_escape(title),int(adddate)))
		else:
			data[cid]= [(html_escape(url),html_escape(title),int(adddate))]
		if cid in dt: dt[cid] = min(dt[cid],int(adddate))
		else: dt[cid] = int(adddate)
	#开始合并最终结果
	#(categoryname,adddate,[(url,title,adddate)])
	content = []
	for cid in cats:
		if cid in data:
			content.append( (cats[cid],dt[cid],data[cid]) )

	htmlcode = exportBookmark(content)
	response['Content-Type'] = 'text/html'
	response['Content-Disposition'] = 'attachment; filename="bookmarks.html"'
	return compressit(htmlcode)

@post("/import/")
@wrapdb
def importbookmark(db):
	"""
		导入外部的文件
	"""
	def importalink(db,catid,alink):
		title,url,tag = alink
		shortid = getshorturlid(url)
		db.execute('INSERT INTO URLS(IS_HEART,IS_ARCHIVED,ARCHIVED_OK,CATEGORY_ID,URL,SHORT_URL_ID,TITLE,TAG,NOTES,TIE_TIME) VALUES(0,0,0,%s,%s,%s,%s,%s,%s,%s)',(catid,url,shortid,title,tag,'',nt()))
	def importonecat(db,cat):
		catname = cat['title']
		if ulen(catname) > 128: catname = ulenget(catname,128)
		catid = createnewcat(db,catname)
		for alink in cat['links']:
			importalink(db,catid,alink)
	f = request.files.get('name')
	if not f:
		return template('error',msg='请选择文件')
	try:
		data = f.file.read() #http server must set the max post data size
		for cat in importBookmark(data):
			importonecat(db,cat)
		db.commit()
	except Exception,msg:
		return template('error',msg='某个地方出错了，请与我们联系')
	redirect("/",301)
