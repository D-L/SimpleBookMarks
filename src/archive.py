#coding: utf8
"""
	归档镜像功能
"""
import os.path
from bottle import post,get,request,abort,response,redirect
from utils import wrapdb,login

from config import ARCHIVED_DIR

def readone(packedfile,name):
	if not os.path.exists(packedfile):
		return None
	fd = open(packedfile,"rb")
	cnt = int(fd.readline().strip())
	meta = {}
	for x in xrange(cnt):
		n = fd.readline().strip()
		ct = fd.readline().strip()
		b = map(int,fd.readline().strip().split())
		meta[n] = (ct,b[0],b[1])

	if name not in meta:
		fd.close()
		return None#未发现
	ct,offset,size= meta[name]
	fd.seek(offset,os.SEEK_CUR)
	data = fd.read(size)
	fd.close()
	return ct,data

def needarchive(db):
	"""
		需要存档服务吗?也就是Enable是否打开了的
	"""
	db.execute('SELECT COUNT(0) FROM SERVICES WHERE SERVICE_ID=1 AND ENABLED=1')
	cnt, = db.getone()
	if cnt < 1: return False
	return True

def archiveapiok(db):
	"""
		存档服务是否设定好了API
	"""
	db.execute('SELECT COUNT(0) FROM API WHERE VALID=1')
	cnt, = db.getone()
	if cnt < 1: return False
	return True

@get("/disablecopycat/")
@login
@wrapdb
def disablecopycat(db):
	db.execute('UPDATE SERVICES SET ENABLED=0,MSG=%s WHERE SERVICE_ID=1',"手工关闭")
	db.commit()
	redirect("/info/")

@get("/enablecopycat/")
@login
@wrapdb
def enablecopycat(db):
	db.execute('UPDATE SERVICES SET ENABLED=1,MSG=%s WHERE SERVICE_ID=1',"手工激活")
	db.commit()
	redirect("/info/")

@post("/0.1/snapshot/")
@login
@wrapdb
def snapshot(db):
	bid = request.POST.get('bookmarkid','')
	if not needarchive(db):
		return {'error' : '请启用CopyCat服务信息'}
	if not archiveapiok(db):
		return {'error' : '请设置CopyCat服务信息'}

	db.execute('SELECT URL,IS_ARCHIVED FROM URLS WHERE ID=%s',bid)
	v = db.getone()
	if not v:
		return {'error': 'access deny'}
	url,flag = v
	if int(flag) in [1,2]: #已经提交了的或者正准备真实提交的
		return {'ok': 1}
	db.execute('UPDATE URLS SET IS_ARCHIVED=2 WHERE ID=%s',bid)
	db.commit()
	return {'ok': 1}

@get("/vss/:bid#[0-9a-zA-Z]+#/<name:re:.*>")
@login
def vss(bid,name):
	"""
		显示某个收藏的快照
	"""
	if not name:
		name = 'index.html'

	dataname = os.path.join(ARCHIVED_DIR,'%s.dat' % bid)
	v = readone(dataname,name)
	if not v:
		abort(404,"NO Found")

	response['Content-Type'] = v[0]
	if v[0].find('html') >=0 or v[0].find('css') >=0:
		return v[1]
	return v[1]
