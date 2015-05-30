#!/usr/bin/python
from bot import *
import re, random
import secrets
class GodBot(Bot):
	initdefaults = {"chans": {}, "nick": "God", "user": "God", "longuser": "God"}
	def __init__(self, **kwargs):
		for k, v in self.initdefaults.items():
			if k not in kwargs:
				kwargs[k] = v
		Bot.__init__(self,**kwargs)
		self.write("OPER %s %s" % (secrets.god_user, secrets.god_pass))
	def handle_pm(self, what, fromwhom):
		if fromwhom in ["OpBot", "RichardStallbot", "SmartBot", "MetaBot", "MzBot"]:
			kickedprayer = re.match("Help! (.*) kicked me from #(.*)!" ,what)
			if kickedprayer:
				evildoer = kickedprayer.group(1)
				chan = "#" + kickedprayer.group(2)
				reason = random.choice(["FEEL MY WRATH!","Fudge off, you fuck!","Don't fucking kick the bots!","What the fuck is wrong with you?!","Why did you kick poor %s?"%fromwhom])
				self.join(chan)
				self.op(self.nick, chan)
				self.kick(evildoer, chan, reason)
				self.op(fromwhom, chan)
				self.part(chan)
				print "Kicked %s from %s for kicking %s." % (evildoer, chan, fromwhom)
		else:
			self.me("isn't real.",fromwhom) # God isn't real
god = GodBot()
while True:
	god.process()
