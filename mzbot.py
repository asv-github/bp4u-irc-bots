#!/usr/bin/python
import re, urllib, urllib2, json
from bot import *

class MusicazooBot(Bot):
	def send_to_musicazoo(self, what, who_to_tell):
		mz = re.match("mz (.*)", what)
		if mz:
			query = mz.group(1).strip()
			try:
				# This is the mz script, courtesy ervanalb
				json_req={"cmd":"do","args":{"message":query}}
				req = urllib2.Request("http://musicazoo.mit.edu/nlp")
				req.add_header('Content-type', 'text/json')
				req.data=json.dumps(json_req)
				handler = urllib2.urlopen(req)
				result=json.loads(handler.read())
				if result['success']:
					f = result['result'].split('\n')
					for line in f:
						self.say(line,who_to_tell)
				else: #Error!
					self.report_error(query,result['error'],who_to_tell)
			except urllib2.HTTPError as e:
				self.report_error(query,e,who_to_tell)
			except urllib2.URLError as e:
				self.report_error(query,e,who_to_tell)
			except:
				self.report_error(query,"Unknown error! :-/",who_to_tell)
	def report_error(self,query,e,who_to_tell):
		print("Error!\nQuery = \"%s\"\nError: %s" % (query, str(e)))
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

m = MusicazooBot(nick="MzBot", chans={"#tetazoo"}, user="mzbot", longuser="Musicazoo Bot")
while True:
	m.process()
