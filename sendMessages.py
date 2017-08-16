import os,time,sqlite3
from slackclient import SlackClient
from config import BOT_TOKEN
slack = SlackClient(BOT_TOKEN)

def sendConfirmation(text, opponentId):
	slack.api_call(
		"chat.postMessage",
		channel=opponentId,
		as_user = True,
		text=text
	)

if __name__ == "__main__":
	if slack.rtm_connect():
		BOT_ID = slack.api_call("auth.test").get('user_id')
		print('PongPal - Connected and Ready To Go!')
		while(True):
			print('Sending Message');
			sendConfirmation("Test message","U5N89N3K2")
			time.sleep(5)
	else:
		print("Connection failed. Invalid Slack token or bot ID?")
