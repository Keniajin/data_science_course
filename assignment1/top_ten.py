# top_ten.py: computes the top ten hashtags in the given sentiment file
# Author: Gani Simsek

import sys
import json

def compute_hashtag_freq(twitter_stream_file):
    """ (file) -> (list)
    Reads a Twitter stream file and returns the top ten hashtags
    """
    hashtags = {}
    with open(twitter_stream_file) as tweetfile:
        for line in tweetfile:
            hashtag_list = []
            tweet = json.loads(line) #Convert each tweet from JSON to Dict
            if "entities" in tweet.keys() and "hashtags" in tweet["entities"]:
                hashtag_list = tweet["entities"]["hashtags"]
                for item in hashtag_list:
                    hashtag = item["text"]
                    if hashtag in hashtags.keys():
                        hashtags[hashtag] += 1.0 #Increase by 1 if found
                    else:
                        hashtags[hashtag] = 1.0 #Insert hashtag if not found
                    
    top_hashtags = sorted(hashtags.items(), key=lambda item: item[1],
                          reverse=True)
    top_ten = 10
    if len(top_hashtags) >= top_ten:
        return top_hashtags[:top_ten]
    else:
        return top_hashtags


def main():
    tf = sys.argv[1] #Twitter File
    top_ten_hashtags = compute_hashtag_freq(tf)
    for item in top_ten_hashtags:
        hashtag, count = item
        print hashtag.encode('utf-8'), count

if __name__ == '__main__':
    main()
