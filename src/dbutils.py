#coding: utf8
from utils import html_escape,refineTag,utf8
from archive import needarchive,archiveapiok
import re

def versionupdated(db):
	"""
		是否有新版本的更新了
	"""
	db.execute('SELECT CUR,LATEST,MSG FROM VERSION')
	for cur,latest,msg in db.getall():
		if latest > cur:
			return msg
	return ''

def createnewcat(db,catname):
	"""
		用catname来创建新类目，返回新的类目ID
		如果此类目存在，则返回原有的类目ID
	"""
	cname = catname.lower()
	
	ret = getCategory(db)
	for cid,title in ret:
		if title.lower() == cname:
			return cid
	db.execute('INSERT INTO CATEGORY(TITLE) VALUES(%s)',catname)
	cid = db.insert_id()
	db.commit()
	return cid

def getdefaultcatid(db):
	"""得到用户默认的类目ID"""
	db.execute('SELECT min(ID) FROM CATEGORY')
	v = db.getone()
	if v: 
		cid, = v
		return int(cid)
	raise Exception("未发现默认的类目")

def getCategory(db):
	"""
		得到用户的全部可用类目
		#返回的数据列表
		#1. categoryid
		#2. 类目title
	"""
	ret = []
	db.execute('SELECT ID,TITLE FROM CATEGORY ORDER BY ID DESC')
	for cid,title in db.getall():
		ret.append( (int(cid),title) )
	return ret

def getUrls(db):
	#得到全部合法URL列表
	#返回的数据列表
	#1. urlid
	#2. categoryid
	#3. url
	#4. title
	#5. tag数组
	#6. notes
	#7. posttime(字符串) 2013-01-01格式
	#8. 此条的Archive状态(int)(-1:用户无权限,0:没提交的,1:提交了正在Archiving,2:等待提交Archining,3:Archived完成了)
	#9. isheart (int)
	data = []
	iscan = needarchive(db) and archiveapiok(db)

	db.execute('SELECT ID,CATEGORY_ID,URL,TITLE,TAG,NOTES,TIE_TIME,IS_HEART,IS_ARCHIVED,ARCHIVED_OK FROM URLS ORDER BY ID DESC')
	for urlid,cid,url,title,tag,notes,pt,isheart,isarchive,archivedok in db.getall():
		tag = refineTag(tag).lower()
		tags = [x for x in tag.split(',') if x]
		
		notes =	"\n&nbsp;&nbsp;".join(filter(None,re.split("\n|\r",html_escape(notes))))

		if iscan:
			thisarchive = 0  #用户开启
		else:
			thisarchive = -1 #用户未启用Archive的
		if int(archivedok) == 1: #说明提交并完成了的
			thisarchive = 3 #可以看Archive结果了
		elif int(isarchive) in [1,2]: #提交了，还未成功的/正在等待提交的
			thisarchive = int(isarchive) #running中

		data.append((
			int(urlid),int(cid),
			url,title,tags,notes,pt,
			thisarchive,int(isheart) ))
	return data
