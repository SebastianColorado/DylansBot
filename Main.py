"""Tweets out a random city name + the phrase."""
import csv
import twitter
import os
import random
import time

numRows = 15633
cities = []

with open('cities.csv', 'rt') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        cities.append(row[0])

# Authenticate the twitter bot by passing the twitter api keys retrieved from
# environment variables
twitterApi = twitter.Api(consumer_key=os.environ['CONSUMER_KEY'],
                         consumer_secret=os.environ['CONSUMER_SECRET'],
                         access_token_key=os.environ['ACCESS_TOKEN'],
                         access_token_secret=os.environ['ACCESS_TOKEN_SECRET'])


def postTweet(city):
    """Post tweet with given parameters."""
    try:
        status = twitterApi.PostUpdate(city + " niggas? They trained to go.")

    except twitter.error.TwitterError as e:
        print('There was an error: ' + e.message[0]['message'])

    else:
        print("%s just posted: %s" % (status.user.name, status.text))

    return


def getCity():
    """Get a random city from the array."""
    return cities[random.randrange(numRows)]


while True:
    currentCity = getCity()

    postTweet(currentCity)

    time.sleep(17280)
