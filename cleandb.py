# -*- encoding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def abstract(data):
	allowed = "q w e r t y u o p a s d f g h j k l i z x c v b n m ğ ş ü ç ö ı".split(" ")
	#print allowed
	""" abstracts the data """
	abst = ""
	for cur in str(data).lower():
		if cur in allowed and cur not in abst:
			abst += cur
	if abst == "":
		return ""
	else:
		return abst


black_arr = [i[:-1] for i in open("blklist_cln","r")]
black_abst = [abstract(i) for i in black_arr]

def chk(data):
	nums = "1 2 3 4 5 6 7 8 9 0"
	""" chks if it is eligible """
	data = str(data)
	abst = abstract(data)

	length = len(data)

	rtn = ""
	#1 if it is number
	for cur in data:
		if cur not in nums:
			rtn += cur

	#0 abstractions scan
	if abst in black_abst:
		return "#No! this is bad input"

	
	else: return data

#test
if __name__ == '__main__':
	
	#print abstract("!'asda gagag asd")
	print black_abst
	