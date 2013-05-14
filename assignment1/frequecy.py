# frequency.py: computes the frequency of terms in a twitter stream file
# Author: Gani Simsek
import sys
import json

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


def compute_frequency(list_of_tweets):
    """ (list) -> (dict {word:count} )
    Calculates the frequency of individual tokens in the given list
    """
    word_counts = {}
    all_tokens = []
    for tweet in list_of_tweets:
        for token in tweet.split():
            all_tokens.append(token)

    for word in all_tokens:
        word_counts[word] = all_tokens.count(word)

    return word_counts


def main():
    tf = sys.argv[1] #Twitter File
    tweet_list = create_tweet_list(tf)
    counts = compute_frequency(tweet_list)
    sorted_counts = sorted(counts.items(), key = lambda item: item[1],
                           reverse = True)
    for item in sorted_counts:
        x,y = item
        print x.encode('utf8'), y

if __name__ == '__main__':
    main()
