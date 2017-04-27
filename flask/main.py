from flask import Flask
import twitter
import re
import keys

app = Flask(__name__)

api = twitter.Api(consumer_key=keys.consumer_key,
                  consumer_secret=keys.consumer_secret,
                  access_token_key=keys.access_token_key,
                  access_token_secret=keys.access_token_secret)


def isSuspended(str):
    if not 'uspended' in str:
        return []
    return re.findall(r'\w*.?\s\d\d*', str)


@app.route('/')
def index():
    statuses = api.GetUserTimeline(screen_name='NYCASP')
    output = ''
    for status in statuses:
        dates = isSuspended(status.text)
        suffix = ','.join(dates) if dates else '(Not Suspended)'
        output = output + status.text + '    ' + suffix + '<br/>'
    return output


if __name__ == "__main__":
    app.run()


