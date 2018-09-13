from textblob import TextBlob
import tweepy
import statistics
import matplotlib.pyplot as plt

consumer_key = 'jNxKs0R8pMu7DRy9HeQXOTt2M'
consumer_secret = 'PYse46jTjsFVSfCZ1YnpdyE6Jom3fo7UFM1u3NiYh6lnuJl5z6'

access_token = '4417041925-zhs7YufBdGuzK0x9wFgdXGeT08B2fdzxHRyySgZ'
access_token_secret = 'xpKtUdknor6qkI2TNKjuiN03XH1BLAGBoP8oA4wqpdspl'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

keyword = input('Please enter a keyword: ')
num_tweets = input('Please enter the number of tweets you want to mine: ')
is_int = False
while is_int == False:
    if num_tweets.isnumeric():
        is_int = True
    else:
        num_tweets = input('Please enter an integer value for the number of tweets you want to mine: ')
        if num_tweets.isnumeric():
            is_int = True

works = True
tweets_mined = tweepy.Cursor(api.search, q = keyword, lang = 'en').items(int(num_tweets))
tweets_list = list()
try:
    for tweet in tweets_mined:
        analysis = TextBlob(tweet.text)
        tweets_list.append(analysis.sentiment.polarity)
except:
    print("Please try again in 15 minutes.")
    works = False

def standard_dev(lst):
    std = statistics.stdev(tweets_list)
    print("Standard Deviation: " + str(std))

def mean(lst):
    mn = statistics.mean(lst)
    print("Mean: " + str(mn))

def median(lst):
    md = statistics.median(lst)
    print("Median: " + str(md))

def pos(lst):
    count = 0
    for num in lst:
        if num > 0:
            count += 1
    percentage = (float(count)/float(len(lst)))*100
    print("The number of positive tweets are: " + str(count))
    print("The percentage of positive tweets is: " + str(percentage) + '%')
    return count

def neg(lst):
    count = 0
    for num in lst:
        if num < 0:
            count += 1
    percent = (float(count)/float(len(lst)))*100
    print("The number of negative tweets are: " + str(count))
    print("The percentage of negative tweets is: " + str(percent) + '%')
    return count

def neutral(lst):
     count = 0
     for num in lst:
         if float(num) == 0.0:
             count += 1
     percentage = (float(count)/float(len(lst)))*100
     print("The number of neutral tweets are: " + str(count))
     print("The percentage of neutral tweets is: " + str(percentage) + '%')
     return count

def pie_chart(lst):
    labels = ['Positive Tweets', 'Negative Tweets','Neutral Tweets']
    sizes = [pos(lst),neg(lst),neutral(lst)]
    colors = ['#99ff99','#f76767','#66b3ff']
    plt.axis('equal')
    plt.pie(sizes, labels = labels, autopct = '%0.1f%%', radius = 1, shadow = False, startangle = 180)
    plt.show()

if works:
    standard_dev(tweets_list)
    mean(tweets_list)
    median(tweets_list)
    pos(tweets_list)
    neg(tweets_list)
    neutral(tweets_list)
    pie_chart(tweets_list)


