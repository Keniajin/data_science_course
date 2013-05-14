import urllib
import json
import codecs

def get_tweets(query_string, num_of_pages=10):
    """ (str) --> (list)

    Perform a Twitter search with the provided search string
    and return the list of texts in the resulting tweets
    
    >>> get_tweets("microsoft", 10)
    [list of tweets]
    """
    url = "http://search.twitter.com/search.json?q="
    result = []
    for page in range(1, num_of_pages+1):
        search_url = url + query_string + "&page=" + str(page)
        response = urllib.urlopen(search_url)
        data = json.load(response)
        tweets = data["results"]
        for tweet in tweets:
            result.append(tweet["text"])
    return result

my_tweets = get_tweets("microsoft", 2)
loc = "D:/Dropbox/Documents/GitHub/datasci_course_materials/assignment1/w.txt" 
f = codecs.open(loc, "a", "utf-8")
for mt in my_tweets:
    f.write(mt)
    f.write("\n")
f.close()
