#!/usr/bin/python
import re, urllib, urllib2
from bot import *

class MusicazooBot(Bot):
	def send_to_musicazoo(self, what, who_to_tell):
		mz = re.match("mz (.*)", what)
		if mz:
			query = mz.group(1).strip()
			try:
				f = urllib2.urlopen("http://musicazoo.mit.edu/nlp", urllib.urlencode([('q',query)]))
				for line in f:
					self.say(line,who_to_tell)
			except urllib2.HTTPError as e:
				print("Error!\nQuery = \"%s\"\nError: %s" % (what, query, str(e)))
				self.say("OH SHIT!!!",who_to_tell)
				self.say("There was an error talking to musicazoo.",who_to_tell)
				self.say(":(",who_to_tell)

	def handle_msg(self, what, fromwhom, where):
		self.send_to_musicazoo(what, where)
		
	def handle_pm(self, what, fromwhom):
		self.send_to_musicazoo(what, fromwhom)
	
	def handle_getting_kicked(self, kicker, where, why):
		# Immediately rejoin, and cry to GodBot	
		self.join(where)
		self.say("Help! %s kicked me from %s!" % (kicker, where),"God")

m = MusicazooBot(nick="MzBot", join="#tetazoo", user="mzbot", longuser="Musicazoo Bot")
while True:
	m.process()
