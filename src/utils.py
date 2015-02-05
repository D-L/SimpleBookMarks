#coding:utf-8

import hashlib

def utf8(u):
	if isinstance(u,unicode):
		return u.encode('utf8')
	return u

def md5sum(msg):
	return hashlib.md5(msg).hexdigest()

def urlkey(url):
	return int(md5sum(url)[:6],16)
