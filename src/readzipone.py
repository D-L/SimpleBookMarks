#coding: utf8
"""
	从.zip文件中读取数据
"""
import zipfile,os.path,mimetypes

from bottle import abort,HTTPResponse

from cfg import Config

DATADIR=Config["datadir"]

Names = {} #taskid => set()
MAX_NAMES = 1024

def readone(taskid,name):
	"""
		返回zip文件中的name文件
	"""
	filename = os.path.join(DATADIR,"%s.zip" % taskid)
	if not os.path.exists(filename):
		abort(404,"NO FOUND")

	if taskid not in Names:
		if len(Names) >= MAX_NAMES:
			Names.clear()

		z = zipfile.ZipFile(filename,'r')
		Names[taskid] = set(z.namelist())
		z.close()
	
	if name not in Names[taskid]:
		abort(404,"NO FOUND")

	headers = {}
	mimetype, encoding = mimetypes.guess_type(name)
	if encoding:
		headers['Content-Encoding'] = encoding

	if mimetype:
		if mimetype[:5] == 'text/' and 'charset' not in mimetype:
			mimetype += '; charset=%s' % 'UTF-8'
		headers['Content-Type'] = mimetype

	z = zipfile.ZipFile(filename,'r')
	content = z.read(name)
	z.close()

	return HTTPResponse(content, **headers)
