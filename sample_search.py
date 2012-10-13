from pprint import pprint
from urllib import quote
import requests

TWITTER_SEARCH = 'http://search.twitter.com/search.json?q='
SEARCH_TERM = '#python'

response = requests.get(TWITTER_SEARCH + quote(SEARCH_TERM))
if response.ok:
    pprint(response.json)
else:
    response.raise_for_status()

