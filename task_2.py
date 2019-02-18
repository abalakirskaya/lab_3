import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl
'''
This module saves information about entered user in 'data.json' file.
'''
# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
f = open('data.json', 'a')
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input('Enter Twitter Account:')
    f.write(acct)
    f.write('\n')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'})
    f.write('Retrieving')
    f.write(url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    f.write(json.dumps(js, indent=2))
    headers = dict(connection.getheaders())
    f.write('Remaining')
    f.write(headers['x-rate-limit-remaining'])
    for u in js['users']:
        f.write(u['screen_name'])
        if 'status' not in u:
            f.write('   * No status found')
            continue
        s = u['status']['text']
        try:
            f.write('   ')
            f.write(s[:50])
        except:
            pass
