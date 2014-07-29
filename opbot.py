#!/usr/bin/python
import socket, time, re, random
from bot import *
import secrets

class OpBot(Bot):
	nicelist = dict()
	listeningto = ''

	def handle_pm(self, what, fromwhom):
		"""
			Handles PMs to the bot.
			In general, says a silly message depending on what you say to it.
			There's also a password that can lead to it giving you full op bits,
			and a password to have the bot make an announcement for you.
		"""
		if re.match(secrets.privesc_password, what.lower()): # Prepare to escalate privileges
			try:
				self.nicelist[fromwhom] = random.randint(2,10)
				self.say(";)", fromwhom)
			except e:
				print e
				self.say(":o", fromwhom) 
		elif re.match(secrets.announce_password + " (#\w*): (.*)", what): # Have it make an anouncment
			announce = re.match(secrets.announce_password + " (#\w*): (.*)", what)
			self.announce(announce.group(2),announce.group(1))
		elif re.match(r"beep (boop beep|beep boop) boop.*", what.lower()): # Silly message
			self.me("climaxes", fromwhom)
		else: # Default silly messages
			messages = [
				"Greetings, human.",
				"I am a robot. Beep boop.",
				"RESISTANCE IS FUTILE. YOU WILL BE ASSIMILATED.",
				"Beep boop beep boop... climax!",
				"OpBot 3000 at your service!"
			]
			self.say(random.choice(messages), fromwhom)
	

	def handle_msg(self, what, fromwhom, where):
		"""
			Handles a message in a channel.
			This has a lot of goop in it. Here's what's going on:
			Someone can get the bot's attention by saying "Hey OpBot" or "@OpBot".
			To escalate privileges, say "op me plz".
			For hilarity's sake, it will say "No.", and you'll have to keep saying "plz" a random number of times until it gives in and ops you.
			This will only work if you've already PM'ed it the password.
			Hopefully this will lead to people who don't know about the password asking it for op bits and saying "plz" repeatedly.
			:)
		"""
		atme = re.match("(hey |@)%s" % self.nick.lower(), what.lower());
		if atme:
			self.say("Beep boop?", where)
			self.listeningto = fromwhom
		elif fromwhom == self.listeningto:
			if re.match("op me plz", what) or re.match("plz",what):
				if self.nicelist and fromwhom in self.nicelist:
					self.nicelist[fromwhom] -= 1
					if self.nicelist[fromwhom] == 0:
						self.say("Fine.",where)
						self.op(fromwhom, where)
						del self.nicelist[fromwhom]
					else:
						self.say("No.",where)
				else:
					if random.random() < .2:
						self.kick(fromwhom,where,"Fudge off, you fuck!") # Kick people about 1 in 5 times
					else:
						self.say("No.",where)
		#sillies
		if re.match("beep (boop beep|beep boop) boop.*", what.lower()):
			self.me("climaxes",where)

	def handle_join(self, who, where):
		self.op(who, where)




Oppy = OpBot(join="#tetazoo", nick="OpBot", user="OpBot", longuser="I am a robot!")
while True:
	Oppy.process()
