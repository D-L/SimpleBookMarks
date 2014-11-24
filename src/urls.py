#coding: utf8
import urllib
from bottle import get,post,request,template,redirect
from utils import wrapdb,ulen,refineTag,utf8,login
from dbutils import getUrls,getCategory,versionupdated
from collections import defaultdict
from archive import needarchive

RECORD_PER_PAGE = 60

@get("/my/")
@login
@wrapdb
def my(db):
	def getparams():
		#返回catid(str),pageno
		cid = int(request.GET.get('cid','0'))
		pn = int(request.GET.get('pn','1'))
		tag = request.GET.get('tag','').lower()
		return cid,pn,tag
	def buildurl(cid,tag,pn):
		url = '/my/'
		v = []
		if cid:
			v.append('cid=%s' % cid)
		if tag:
			v.append('tag=%s' % tag)
		if pn != 0:
			v.append('pn=%s' % pn)
		if v:
			return url+'?'+'&'.join(v)
		return url
	def buildtagurl(cid,tag):
		url = '/my/'
		v = []
		if cid:
			v.append('cid=%s' % cid)
		if tag:
			v.append('tag=%s' % urllib.quote(tag))
		if v:
			return url+'?'+'&'.join(v)
		return url

	updatemsg = versionupdated(db)
	curcid,curpn,curtag = getparams() #当前的catid,当前的curpn,当前的书签.
	#---列出全部的类目信息以及书签---
	data = []
	cats = defaultdict(int) #已经被使用的Category{id:count}
	alltags = set()

	for urlid,cid,url,title,tags,notes,pt,thisarchive,isheart in getUrls(db):
		cats[cid] += 1

		for x in tags:
			alltags.add('"%s"' % x.replace('"','\\"'))

		#选择了类目的
		if curcid and curcid != cid: continue
		#选择了Tag
		if curtag and (curtag not in tags): continue

		thistags = []
		for t in tags:
			thistags.append( (t,buildtagurl(0,t)) ) #全局的Tag

		data.append( (urlid,url,title,cid,tags,notes,pt,thistags,isheart,thisarchive) )

	if not data: #没有数据
		if curcid or curtag: #可能是这个目录/Tag下没了（最后一条）
			redirect("/my/")

	categorys = [] #[ [(url,title,count)] ]  #全部有数据的Category的信息.
	allcats   = {} #全部的Category信息.
	emptycats = {} #空的Category信息

	if cats: #用户全部的有效目录信息.
		defaultcatid = 0
		for cid,title in getCategory(db):
			defaultcatid = cid

			allcats[cid]=title
			if cid not in cats: #有收藏的
				emptycats[cid]=title

		#这里按照真正的categoryid排下，免得出现不断位置排列的问题.
		v = [(count,catid) for catid,count in cats.iteritems()]
		v.sort(reverse=True)
		tmp = []
		for count,catid in v:
			if catid not in allcats: continue #有这个发生，就说明用户删除了含有收藏的收藏夹.
			tmp.append( (buildurl(catid,'',0),allcats[catid],count) )
			if len(tmp) == 6:
				categorys.append(tmp)
				tmp = []
		if tmp:
			cnt = 6 - len(tmp)
			for x in xrange(cnt):
				tmp.append( ('',0,0) )
			categorys.append(tmp)
		#--禁止删除默认收藏夹--
		if defaultcatid in emptycats:
			del emptycats[defaultcatid]
	#计算pagecount	
	pagecount = 1+(len(data)-1)/RECORD_PER_PAGE
	prevurl = buildurl(curcid,curtag,curpn-1)
	nexturl = buildurl(curcid,curtag,curpn+1)

	pages = (curpn,pagecount,prevurl,nexturl)

	s = RECORD_PER_PAGE*(curpn-1)
	bookmarks = data[s:s+RECORD_PER_PAGE]

	ret = template('my',
		categorys=categorys, #当前已经有收藏的收藏夹
		curcatinfo=(allcats.get(curcid,''),len(data)),
		allcategorys=allcats,
		emptycategorys=emptycats,
		bookmarks=bookmarks,
		pages=pages,
		updatemsg=updatemsg,
		disabled = not needarchive(db),
		tags=','.join(list(alltags)))
	return ret

@post("/0.1/update/")
@login
@wrapdb
def update(db):
	bid = int(request.POST.get('bookmarkid',''))
	cid = int(request.POST.get('category','0'))
	title = request.POST.get('title','')
	tag = request.POST.get('tag','')
	notes = request.POST.get('notes','')

	if ulen(title) > 512: return {'error' : '你对标题也太有爱了 这么长的标题'}
	if ulen(tag) > 1024: return {'error' : '你的标签太有爱了 这么丰富的'}
	if ulen(notes) > 1024: return {'error' : '你的备注也超长的，您一定是细心的人'}

	tag = refineTag(tag)
	#检查这个书签是否存在
	db.execute('SELECT CATEGORY_ID,URL FROM URLS WHERE ID=%s',bid)
	v = db.getone()
	if not v:
		return {'noauth' : 1}
	catid,url = v
	isnewcat = (cid != int(catid))
	if isnewcat: #变更类目了
		#检查这个catid是否存在
		db.execute('SELECT 1 FROM CATEGORY WHERE ID=%s',cid)
		v = db.getone()
		if not v:
			return {'noauth' : 1}
	if isnewcat:
		db.execute('UPDATE URLS SET CATEGORY_ID=%s,TITLE=%s,TAG=%s,NOTES=%s WHERE ID=%s',(cid,title,tag,notes,bid))
	else:
		db.execute('UPDATE URLS SET TITLE=%s,TAG=%s,NOTES=%s WHERE ID=%s',(title,tag,notes,bid))
	db.commit()
	return {'ok':1}

@post("/0.1/delete/")
@login
@wrapdb
def deletebookmark(db):
	"""
		删除书签，可以批量删除的了。
		参数为bookmarkid的,连接表示.
	"""
	bids = request.POST.get('bookmarkid','')
	todo = []
	try:
		for bid in bids.split(','):
			todo.append( int(bid) )
		if not todo or len(todo) > RECORD_PER_PAGE: #最多一次
			return {'error' : '参数错误'}
	except:
		return {'error' : '参数错误'}

	if todo:
		todostr = ','.join(['%s' % x for x in todo])
		db.execute('DELETE FROM URLS WHERE ID IN (%s)' % todostr)
		db.commit()
	return {'ok':1}

@post("/0.1/move/")
@login
@wrapdb
def movebookmark(db):	
	bid = request.POST.get('bookmarkid','')
	cid = int(request.POST.get('category','0'))

	todo = []
	try:
		for bid in bid.split(','):
			todo.append(int(bid))
		if not todo or len(todo) > RECORD_PER_PAGE:
			return {'error' : '参数错误'}
	except:
		return {'error' : '参数错误'}
	if todo:
		todostr = ','.join(['%s' % x for x in todo])
		db.execute('UPDATE URLS SET CATEGORY_ID=%s  WHERE ID IN (%s)' % (cid,todostr))
		db.commit()
	return {'ok':1}

@post("/0.1/get/")
@login
@wrapdb
def apigetbookmark(db):
	"""
		得到某个书签的详细信息
		参数为bookmarkid
	"""
	bid = request.POST.get('bookmarkid','')
	try:
		bid = int(bid)
	except:
		return {'error' : '参数错误'}

	#检查这书签是否存在
	db.execute('SELECT CATEGORY_ID,TITLE,URL,TAG,NOTES FROM URLS WHERE ID = %s' % bid)
	v = db.getone()
	if not v:
		return {'noauth' :1}

	cid,title,url,tag,notes =v
	return {'ok':1,
			'id':bid,'cid':cid,
			'title':title,'url':url,
			'tag':refineTag(tag).lower(),
			'notes':notes}
