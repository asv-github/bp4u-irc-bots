bp4u-irc-bots
=============

We have you cover for very low ruble!

To make a new bot, subclass the Bot class. Override handle\_pm to do stuff when your bot gets private messaged, handle\_msg to do stuff when a message goes out to a channel your bot is on, handle\_join when someone joins a channel your bot is on, etc. 
To start the bot running, instantiate it and then call "yourbot.process()" in a while True loop. Thats's it

Currently the Bot superclass has no SSL support. If the IRC server you're using doesn't allow external non-SSL connections, you may need to convince the server operator to let you run the bot on their server. SSL support is (hopefully) coming soon.
