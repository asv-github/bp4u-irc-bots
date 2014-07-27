#!/usr/bin/python
import socket, re

crlf = '\r\n'
class Bot:
	def __init__(self, host='127.0.0.1', port=6667, nick="Robot", user="Robot", longuser="I am a robot!", join="#yolo"):
		self.s = socket.socket()
		self.s.connect((host,port))
		self.f = self.s.makefile()
		
		self.write = lambda x : self.s.send(x + crlf)
		self.read = self.f.readline
		
		self.nick = nick
		self.write('NICK ' + nick)
		self.write('USER ' + user + ' * * :' + longuser)
		if join != "":
			self.write('JOIN ' + join)

	def say(self, what, whom): #say something to a person or channel
		self.write('PRIVMSG ' + whom + ' :' + what)

	def me(self, what, whom): # e.g. "/me does stuff"
		self.write('PRIVMSG ' + whom + ' :ACTION ' + what + '')

	def announce(self, what, whom): # It's actually basically the same as "say", sadly.
		self.write('NOTICE ' + whom + ' :' + what)

	def op(self, user, chan):
		self.write('MODE ' + chan + ' +o ' + user)

	def hop(self, user, chan): # hop = half-op
		self.write('MODE ' + chan + ' +h ' + user)

	def kick(self, user, chan, reason=''):
		self.write('KICK ' + chan + ' ' + user + ' :' + reason)

	def join(self, chan):
		self.write('JOIN ' + chan)

	def part(self, chan):
		self.write('PART ' + chan)

	def nick(self, newnick):
		self.write('NICK ' + newnick) # In case there's an error, we update self.nick when the server actually responds that the nick was updated

	def handle_msg(self, what, fromwhom, towhom):
		pass

	def handle_pm(self, what, fromwhom): # PM = private message
		pass

	def handle_join(self, who, where):
		pass

	def handle_part(self, who, where):
		pass

	def handle_quit(self, who, why):
		pass
	
	def handle_nickchange(self, oldnick, newnick): # Called when other people change their nicknames
		pass

	def process(self):
		line = self.read();
		if re.match("PING :.*", line):
			self.write("PONG :" + line[6:])
			
		msg = re.match(r":(\w+)!\S* PRIVMSG (\S+) :(.*)", line)
		if (msg):
			fromwhom = msg.group(1).strip()
			towhom = msg.group(2).strip()
			what = msg.group(3).strip()
			if towhom == self.nick:
				self.handle_pm(what, fromwhom)
			else:
				self.handle_msg(what, fromwhom, towhom)
				
		join = re.match(r":(\w+)!\S* JOIN :(.*)", line)
		if (join):
			who = join.group(1).strip()
			where = join.group(2).strip()
			self.handle_join(who, where)

		part = re.match(r":(\w+)!\S* PART :(.*)", line)
		if (part):
			who = join.group(1).strip()
			where = join.group(2).strip()
			self.handle_part(who, where)

		quit = re.match(r":(\w+)!\S* QUIT :(.*)", line)
		if (part):
			who = join.group(1).strip()
			why = join.group(2).strip()
			self.handle_quit(who, why)

		nick = re.match(r":(\w+)!\S* NICK :(.*)", line)
		if (part):
			oldnick = join.group(1).strip()
			newnick = join.group(2).strip()
			if oldnick == self.nick:
				self.nick = newnick
			else:
				self.handle_nickchange(oldnick, newnick)

class SimpleOpBot(Bot):
	def handle_pm(self, what, fromwhom):
		self.say("I am a robot. Beep boop.", fromwhom)
	def handle_join(self,who,where):
		self.hop(who,where)
