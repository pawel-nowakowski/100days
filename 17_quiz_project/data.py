# import urllib library
from urllib.request import urlopen

# import json
import json

# store the URL in url as
# parameter for urlopen
url = "https://opentdb.com/api.php?amount=20&type=boolean"

# store the response of URL
response = urlopen(url)

# storing the JSON response
# from url in data
data_json = json.loads(response.read())

question_data = data_json['results']