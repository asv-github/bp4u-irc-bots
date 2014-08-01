#!/usr/bin/python
from bot import *
import re, random, threading
class FrayBot(Bot):
	initdefaults = {"join": "", "nick": "FrayBot", "user": "fraybot", "longuser": "H. Fraybot"}
	def __init__(self,  chans=["#yolo"], **kwargs):
		for k, v in self.initdefaults.items():
			if k not in kwargs:
				kwargs[k] = v
		Bot.__init__(self,**kwargs)
		self.chans = chans
		print("Loading booklist into memory....")
		with open("books","r", encoding="UTF-8") as booklistfile:
			self.booklist = list(filter(lambda s : not s.startswith("#"), booklistfile.readlines()))
		print ("Loaded %d books." % len(self.booklist))
	def handle_pm(self, what, fromwhom):
		if what == "books plz":
			self.spam_reuse()
		else:
			self.say("Sorry, the item has been claimed.",fromwhom)
	def spam_reuse(self):
		# Construct a spammy reuse message
		numbooks = int(random.triangular(3.5, 9.5, 6.5)) # Number of books: Let's try 6, plus or minus 3. (.5 corrects for rounding down)
		books = random.sample(self.booklist,numbooks)
		message = ["Reuse: Books (will send ONLY if you send interoffice address):"] + [str(i+1) + ". " + books[i] for i in range(numbooks)]
		for chan in self.chans:
			for line in message:
				self.say(line, chan)
	def repeatedly_spam_reuse(self, avgperiod=3600):
		self.spam_reuse();
		self.spamtimer = threading.Timer(random.expovariate(1.0 / avgperiod), self.repeatedly_spam_reuse, kwargs={'avgperiod':avgperiod}) # Poisson process with average time between spams of avgperiod
		self.spamtimer.start()
		
if __name__ == "__main__":
	fraybot = FrayBot(chans=['#tetazoo','#nanometer'])
	fraybot.repeatedly_spam_reuse(avgperiod=24*7*3600)
	while True:
		fraybot.process()
