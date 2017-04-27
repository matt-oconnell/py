import twitter
import keys
import re

api = twitter.Api(consumer_key=keys.consumer_key,
                  consumer_secret=keys.consumer_secret,
                  access_token_key=keys.access_token_key,
                  access_token_secret=keys.access_token_secret)


def getSuspendedDates(str):
    if not 'uspended' in str:
        return []
    return re.findall(r'\w*.?\s\d\d*', str)


def getParkingTweets():
    statuses = api.GetUserTimeline(screen_name='NYCASP')
    output = []
    for status in statuses:
        output.append({
            'text': status.text,
            'suspended_dates': getSuspendedDates(status.text)
        })
    return output