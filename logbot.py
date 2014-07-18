#!/usr/bin/python
from bot import *
import os
class LogBot:
	def __init__(self, loglocation, host=127.0.0.1, port=6667, nick="LogBot", user="LogBot", longuser="IRC-logging Robot", join="#yolo"):
		super(self, host=host, port=port, nick=nick, user=user, longuser=longuser, join="#yolo")
		self.loglocation = loglocation
	
	def handle_msg(self, what, fromwhom, towhom):
		self.log("%s: %s" % (fromwhom, what)) 

	def handle_pm(self, what, fromwhom):
		pass

	def handle_join(self, who, where):
		self.log("* %s entered %s" % (who,where))

	def handle_part(self, who, where):
		self.log("* %s left %s." % (who,where))

	def handle_quit(self, who, why):
		self.log("* %s quit. (%s)" % (who,why))

	def log(string):
		print time.strftime("%Y %b %d %H:%M:%S") + ": " + string
