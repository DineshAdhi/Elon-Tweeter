
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import json

class StdOutListener(StreamListener):

    def on_data(self, data):
        try:
            res = json.loads(data);

            print res.get('user')['screen_name']
            print res.get('text')
            print ('\n\n');

            if "@" in res.get('text'):
                return True;
            else:
                print res
                print res.get('id');
                api.update_status("Love you @"+res.get('user')['screen_name'], in_reply_to_status_id = res.get('id'));
                return True;
        except:
            print ("error try again")

    def on_error(self, status):
        print status


consumer_key ='jfTyB9zBpzK2wnIfw7NMTLe7O'
consumer_secret='NtKc6TaVS5hQkyuGjnAgcKI9XsuRLnyOxJ8T49HnyZ7xUkazoY'
access_token='833854925495029760-nOrThzBIi2lPQZeUV8DQIYPDES0m0h0'
access_token_secret='Ckwe2OR40AeOAoXlgsySB6tqH8dvxeZu6ZECLoV3WxHCo'

l = StdOutListener()
auth = OAuthHandler(consumer_key,consumer_secret);
auth.set_access_token(access_token,access_token_secret);

api = tweepy.API(auth);

stream = Stream(auth, l);
stream.filter(follow=['833681812039811073','44196397'])
