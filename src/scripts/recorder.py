#coding: utf8
import json,urllib

def getpage(url):
	r = urllib.urlopen(url)
	return r.getcode(),r.read()

class recordError(Exception):
	pass

ST_NO_EXIST = -1
ST_RUNNING  = 1
ST_DONE     = 2

def statusText(st):
	if st == -1:
		return "不存在"
	if st == 1:
		return "运行中"
	if st == 2:
		return "已完成"
	return "未知状态"

ROOT="https://www.pagerecorder.com"
class Recorder(object):
	def __init__(self,token):
		self.token = token

	def record(self,url,cb=''):
		"""
			作用:
				保存网页
			参数:
				url -> 需要保存的网页地址
				cb  -> 回调地址，一旦完成后。系统将回调这个地址通知保存已完成。
			返回:
				最终的jobid值
                jobid,int类型
		"""
		URL = "%s/api/v1/record/" % ROOT
		param = {
			'token' : self.token,
			'url'   : url
		}
		if cb:
			param['cb'] = cb
		p = urllib.urlencode(param)
		code,data = getpage("%s?%s" % (URL,p))
		if code == 200:
			obj = json.loads(data)
			if obj['ok']:
				return int(obj['jobid'])
			raise recordError(obj['msg'].encode('utf8'))
		raise recordError("Response code:%s \n%s" % (code,data))

	def query(self,jobid):
		"""
			查询任务的状态
			返回:
				ST_NO_EXIST : 任务不存在
				ST_RUNNING  : 还在处理中
				ST_DONE     : 已完成
		"""
		URL = "%s/api/v1/query/" % ROOT
		param = {
			'token' : self.token,
			'jobid' : jobid
		}
		p = urllib.urlencode(param)
		code,data = getpage('%s?%s'%(URL,p))
		if code == 200:
			obj = json.loads(data)
			if obj['ok']:
				st = obj['status']
				if st in [ST_NO_EXIST,ST_RUNNING,ST_DONE]: return st
				raise recordError("unknown job status:%s" % st)
			raise recordError(obj['msg'].encode('utf8'))
		raise recordError("Response code:%s \n%s" % (code,data))
	def isfinished(self,jobid):
		"""
			任务是否已经完成
		"""
		return self.query(jobid) == ST_DONE

	def get(self,jobid):
		"""
			获取网页数据.一个.zip文件
		"""
		URL = "%s/api/v1/get/" % ROOT

		param = {
			'token':self.token,
			'jobid':jobid
		}
		p = urllib.urlencode(param)
		code,data = getpage('%s?%s'%(URL,p))
		if code == 200:
			return data
		raise recordError("Response code:%s \n%s" % (code,data))

	def get2file(self,jobid,filename):
		"""
			获取结果到文件filename中
			必须是完成的任务,否则抛出异常
		"""
		data = self.get(jobid)
		open(filename,'w').write(data)
