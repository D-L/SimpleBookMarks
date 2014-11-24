#coding: utf8

from bottle import response,request,redirect
import gzip,hashlib,os.path,urlparse,datetime,time,threading

from database import DB
from copycat import CopyCat

from config import DATA_DIR

try:
    import cStringIO as StringIO
except:
    import StringIO

def utf8(unimsg):
    if unimsg:
        return unimsg.encode("utf8")
    return ""

def now():
	return int(time.time()*1000)

CFG=threading.local()
def getcfg():
	CFG.host=''
	CFG.domain=''
	CFG.port=0
	for line in open("config.txt","rb"):
		content = line.strip().lower()
		if content.find('host=') >=0:
			CFG.host=content.replace('host=','').strip()
		elif content.find('port=') >=0:
			CFG.port =int(content.replace('port=','').strip())
		elif content.find('domain=') >=0:
			CFG.domain=content.replace('domain=','').strip()
getcfg() #run this config

def wait(timeout):
	import select
	n = now()+timeout
	while True:
		try:
			select.select([],[],[],5.0)
		except:
			pass
		if now() > n: break

def nt():
	a = datetime.date.today()
	return '%s-%02d-%02d' % (a.year,a.month,a.day)

def md5sum(msg):
	return hashlib.md5(msg).hexdigest()

def getDB():
	dbfile = os.path.join(DATA_DIR,'db.dat')
	if not os.path.exists(dbfile):
		raise Exception("Database db.dat No Existed!")
	return DB(dbfile)

def getCC(db):
	"""得到CopyCat的对象"""
	db.execute('SELECT APP_ID,SECURITY_KEY,ROOT_URL FROM API WHERE VALID=1')
	v = db.getone()
	if not v:
		return None
	appid,key,rooturl = v
	return CopyCat(int(appid),key,rooturl)
	

def normaliseurl(url):
	#规范化一个URL
	#1. 去除#
	#2. 检查/和没有/的
	v = urlparse.urlparse(url)
	if v.path == '/':
		u = (v.scheme,v.netloc,'',v.params,v.query,'') #去除了fragment
	else:
		u = (v.scheme,v.netloc,v.path,v.params,v.query,'') #去除了fragment
	return urlparse.urlunparse(u)

def getshorturlid(url):
	"""得到一个URL的ShortID这样能快速查找用户是否已经保存过这个URL了"""
	u = normaliseurl(url)
	return int(md5sum(u)[:7],16)

def refineTag(tag):
	"""将全角逗号替换,去除重复的,全部为小写"""
	if not tag: return tag
	tag = tag.replace('，',',').lower()
	return ','.join([x.strip() for x in set(tag.split(',')) if x.strip()])

def isdeny(url):
	url = url.lower()
	if not url.startswith('http://') and not url.startswith('https://'): return True
	return False

def html_escape(string):
    ''' Escape HTML special characters ``&<>`` and quotes ``'"``. '''
    return string.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('"','&quot;').replace("'",'&#039;')

def ulen(utf8str):
	return len(utf8str.decode('utf8','ignore'))

def ulenget(utf8str,size):
	return utf8str.decode('utf8','ignore')[:size].encode('utf8')

db = getDB()
def wrapdb(func):
	def func_i(*args,**kw):
		v=list(args)
		v.append(db)
		try:
			return func(*tuple(v),**kw)
		except:
			raise
		finally:
			db.commit()
	return func_i

def islogined():
	session_value = request.get_cookie('token','')
	if not session_value:
		return False
	db.execute('SELECT TOKEN FROM COOKIE')
	for token, in db.getall():
		if token == session_value:
			return True
	return False

def login(func):
	"""
		需要登陆的
	"""
	def login_i(*args,**kws):
		if islogined():
			return func(*args,**kws)
		redirect("/login.html") #返回登陆页面
	return login_i

if __name__=="__main__":
	pass
