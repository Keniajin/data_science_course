# tweet_sentiment.py: computes the sentiment of each tweet in a given file
# using the "AFINN-111.txt" dictionary of sentiment words.
# Author: Gani Simsek

import sys
import json


def create_sentiment_dict(sentiment_file):
    """ (file) -> (dict)
    Reads the AFINN-111.txt file and creates a sentiment dictionary
    """
    scores = {}
    with open(sentiment_file) as afinnfile:
        for line in afinnfile:
            term, score  = line.split("\t")  # The file is tab-delimited.
            scores[term] = int(score) # Store each term with its integer value
        afinnfile.close()
    return scores

def create_tweet_list(twitter_stream_file):
    """ (file) -> (list) of tweets
    Reads a Twitter stream file and returns a list that
    contains only the text part of each tweet
    """
    tweetlist = []
    with open(twitter_stream_file) as tweetfile:
        for line in tweetfile:
            text = ""
            tweet = json.loads(line) #Convert each tweet from JSON to Dict
            if "text" in tweet.keys():
                text = tweet["text"] #Get the text of tweet, if any
            tweetlist.append(text)
    return tweetlist

def compute_tweet_scores(sentiment_dict, tweet_list):
    """ (dict, list) -> (list)
    Given a sentiment dict and a list of tweets, this method computes
    the sentiment value of each tweet
    """
    tweet_scores = []
    for tweet in tweet_list:
        total_score = 0.0
        words = tweet.split()
        for word in words:
            if word.encode('utf-8') in sentiment_dict.keys():
                total_score += float(sentiment_dict[word])
        tweet_scores.append(total_score)
    return tweet_scores
    

def main():
    sf = sys.argv[1] #Sentiment File
    tf = sys.argv[2] #Twitter File
    sent_dict = create_sentiment_dict(sf)
    tweet_lst = create_tweet_list(tf)
    computed_scores = compute_tweet_scores(sent_dict, tweet_lst)
    for item in computed_scores:
        print item

if __name__ == '__main__':
    main()
