# Encoding: UTF-8
#message = str(sys.argv[1])
# database addition etc..
#import cPickle as pickle

arr = [i.decode("utf-8")[:-1] for i in open("kufurler","r")]
#pickle.dump( arr, open( "aqarrayi.pkl", "wb" ) )
whitelist = [i.decode("utf-8")[:-1] for i in open("whitelist","r")]
		
def abstraction(meme):
	""" create a little abstraction arr """
	abstract = []
	ret = ""
	for elems in meme:
		if elems not in abstract:
			abstract.append(elems)
			ret += elems
	return ret

abstracts = [abstraction(i) for i in arr]

def chk(bulk):
	abstr = abstraction(bulk)
	
	if bulk in whitelist:
		return bulk

	elif abstr in abstracts:
		return "***"

	else:
		return bulk


def strip(phrase):
	ret_data	= ""
	ret_arr 	= []
	msg = []
	#arr = ["!","'","^","+","%","&","/","(",")","=","*","-","|","_","?","}","]","[","{","¾","½","$","#","£",">","<","~","`","'",":","."]
	arr = [" ","q","w","e","r","t","y","u","ı","o","p","ğ","ü","a","s","d","f","g","h","j","k","l","k","l","ş","i","z","x","c","v","b","n","m","ö","ç"]

	for i in str(phrase).split(" "):
		ret = ""
		cur = i.lower()
		for lel in cur:
			if lel in arr:
				ret += lel
		ret_arr.append(ret)


	for elems in ret_arr:
		resp = chk(elems)
		msg.append(resp)
		if resp == "***":
			return 0
	return 1

if __name__ == '__main__':
	
	try:
		asd = sys.argv[1]
		print strip(asd)
	except: pass
