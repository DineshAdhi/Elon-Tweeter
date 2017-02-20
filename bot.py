
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

            if "@harish31245" in res.get('text'):
                return True;
            elif "@elonmusk" in res.get('text'):
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


consumer_key ='jMb4DSemFf0FALmpohLxenNh5'
consumer_secret='AE58yVAS1VhEkGiDSUGpOdTufhym5Q8y1vjgTXfuMXkLkFaqtQ'
access_token='422310522-b5VfIIbj1R6c3rHzi1GjBXMgwpHGqWxuui2brI5s'
access_token_secret='srtvlv04oJYMSXQY24sJsqDfufqCbFZBrcaCmV6VMgxcF'

l = StdOutListener()
auth = OAuthHandler(consumer_key,consumer_secret);
auth.set_access_token(access_token,access_token_secret);

api = tweepy.API(auth);

stream = Stream(auth, l);
stream.filter(follow=['833681812039811073','44196397'])
