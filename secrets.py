
# Don't put your secrets in this file. Instead, make a file named secrets_local.py and put your secrets there.

try:
	from secrets_local import *
except ImportError:
	print "WARNING: You are using the default secrets file!"
	print "You should create a file named secrets_local.py with your own secrets."
	# Default secrets follow.
	privesc_password = "su"
	announce_password = "\(clears throat\)"
	god_user = "ircop_user"
	god_pass = "ircop_pass"
