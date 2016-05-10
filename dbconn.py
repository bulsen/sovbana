# -*- unicode: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import pymongo, time, random
import cleandb as cln

con = pymongo.MongoClient(connect=False)
db	= con.Dabates
kuf = db.treatmelikeabadserver
kim = db.kimlersovmus


def now():
	return time.strftime("%H:%M:%S - %d/%m/%y")

def cleaner(bulk):
	bulk = str(bulk)
	arr = [",","'","\"","-","&","%","<",">","(",")","[","]","{","}","?","|","-"]
	rtn = ""
	for i in bulk:
		if i not in arr:
			rtn += i
		else: pass
	return rtn

def totalentry():
	cnt = 0
	for i in kuf.find():
		cnt +=1

	return cnt

def sovmeaq():
	return kuf.find().limit(-1).skip(random.randrange(0,totalentry())).next()["kufur"]

def push(kufur,ip):
	y_kufur = cleaner(kufur)
	n_ip	= cleaner(ip)
	zaman 	= now()

	n_kufur = cln.chk(y_kufur)

	if len([i for i in kuf.find({"kufur":n_kufur})]) ==0:
		# globallesmenin amina koyayim
		kuf.insert({"kufur":n_kufur,"ip":n_ip,"zaman":zaman})
		kim.insert({"ip":n_ip, "zaman":zaman})
	
	else:
		return "bu var kardes almiyim"

def listele():
	return [i["kufur"] for i in kuf.find()]

	
if __name__ == '__main__':
	#push("popo","ip")
	#print totalentry()
	#print sovmeaq()
	print listele()
