# -*- encoding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import random

taunts ="""ahahaha bu kadar mı?
naber lan tüpçü?
ananem bile daha çok küfür biliyor
ehehe bebe yaa
yuh aq öyle mi denir
vay aq samet neler olmuş
bu dediğine eşşekler bile inanmaz
naber lan muhallebi çocuğu
bu ağızla anneni nasıl öpüyorsun?
küfretsene oç
sus sikerim
popo ye
pipi suyu iç
bu kadar mı aq
amk mı aq mu?
pipiş
aq liselisi
iq kaç?
küçük primat
embesilce sövme zekice söv
:(""".split("\n")

def taunt():
	l = len(taunts)
	asd = taunts[random.randrange(0,l)]
	return asd


if __name__ == '__main__':
	print taunt()