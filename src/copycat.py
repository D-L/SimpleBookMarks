#coding: utf8
import json,os,hashlib
import urllib,urllib2,urlparse

def md5(content):
	return hashlib.md5(content).hexdigest()

def unpacksnapshotfile(snapshotfile,cb):
	"""
		解开一个快照文件.
		cb -> func(filename,content-type,data)
		如:
		def writeone(filename,ct,data):
			#生成一个个单独的文件，文件内容为
			#第一行为 content-type
			#后面的为数据内容
			open(filename,"w").write("%s\n%s" % (ct,data))
		#解开快照文件
		unpacksnapshotfile('baidu.dat',writeone)

		更多使用:
		def userinwebtoshowfilename(filename):
			#用来在Web上显示文件的内容
			fd = open(filename)
			ct = fd.readline().strip()
			data = fd.read()
			fd.close()
			#返回给客户的浏览器
			response['Content-Type'] = ct
			return data
	"""
	fd = open(snapshotfile)
	cnt = int(fd.readline().strip())
	meta = {}
	for x in xrange(cnt):
		name = fd.readline().strip()
		contenttype = fd.readline().strip()
		offset,size = map(int,fd.readline().strip().split())
		meta[name] = (contenttype,offset,size)

	dataoffset=fd.tell()
	for name,value in meta.iteritems():
		ct,offset,size= value
		fd.seek(dataoffset+offset,os.SEEK_SET)
		data = fd.read(size)
		cb(name,ct,data) #callbacker
	fd.close()

def getpage(url,postdata=None,writer=None):
	if postdata:
		d = urllib.urlencode(postdata)
		r = urllib2.urlopen(url,data=d,timeout=5)
	else:
		r = urllib2.urlopen(url,timeout=5)

	content = r.read()
	if writer:
		writer(content)
		return r.getcode(),None

	return r.getcode(),content

class ccError(Exception):
	def __init__(self,msgid,msg):
		self.msgid = msgid
		self.msg = msg
	def __str__(self):
		return "MsgID:%s  Msg:%s" % (self.msgid,self.msg)

class CopyCat(object):
	"""
		鲜活镜像API
		更多请察看网站上的协议文档.
	"""
	def __init__(self,appid,securitykey,rooturl):
		"""
			appid/securitykey/rooturl 请登陆系统可见
		"""
		self._appid= appid
		self._security = securitykey

		self._root = rooturl
	def snap(self,url,cb=''):
		"""
			作用:
				发送一个快照请求
			参数:
				url -> 需要快照的页面地址
				cb  -> 回调地址，一旦快照完成后。系统将回调这个地址通知快照已完成。
			返回:
				最终的jobid值
                jobid,int类型
		"""
		URL= urlparse.urljoin(self._root ,'/copycat/snapshot/')
		token = md5(url+self._security)
		param = {
			'appid' : self._appid,
			'token':token,
			'url':url
		}
		if cb:
			param['cb'] = cb
		code,data = getpage(URL,param)
		if code == 200:
			obj = json.loads(data)
			if obj['ok']:
				return obj['jobid']
			raise ccError(int(obj['msgid']),obj['msg'].encode('utf8'))
		raise Exception("Response code:%s \n%s" % (code,data))
	def query(self,jobid):
		"""
			查询快照的状态
			返回:
				-1 : 任务不存在
				1  : 还在处理中
				2  : 已完成
		"""
		URL= urlparse.urljoin(self._root,'/copycat/querysnapshot/')
		token = md5('%s' % jobid+self._security)
		param = {
			'appid' : self._appid,
			'token':token,
			'jobid':jobid
		}
		p = urllib.urlencode(param)
		code,data = getpage('%s?%s'%(URL,p))
		if code == 200:
			obj = json.loads(data)
			if obj['ok']:
				st = obj['status']
				if st in [-1,1,2]: return st
				raise Exception("unknown job status:%s" % st)
			raise ccError(int(obj['msgid']),obj['msg'].encode('utf8'))
		raise Exception("Response code:%s \n%s" % (code,data))
	def isfinished(self,jobid):
		"""
			任务是否已经完成
		"""
		return self.query(jobid) == 2

	def get(self,jobid):
		"""
			获取快照结果数据,返回的是一个SnapshotFile格式的文件。
		"""
		URL=urlparse.urljoin(self._root,'/copycat/getsnapshot/')

		token = md5('%s' % jobid+self._security)
		param = {
			'appid' : self._appid,
			'token':token,
			'jobid':jobid
		}
		p = urllib.urlencode(param)
		code,data = getpage('%s?%s'%(URL,p))
		if code == 200:
			return data
		raise Exception("Response code:%s \n%s" % (code,data))

	def get2file(self,jobid,filename):
		"""
			获取快照结果到文件filename中
		"""
		URL=urlparse.urljoin(self._root,'/copycat/getsnapshot/')

		token = md5('%s' % jobid+self._security)
		param = {
			'appid' : self._appid,
			'token':token,
			'jobid':jobid
		}
		p = urllib.urlencode(param)
		fd = open(filename,'wb')
		code,data = getpage('%s?%s'%(URL,p),None,fd.write)
		fd.close()
		if code == 200:
			return
		raise Exception("Response code:%s \n%s" % (code,data))
