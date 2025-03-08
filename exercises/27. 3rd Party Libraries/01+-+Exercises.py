# Question 1
# Use the `pytz` and `dateutil` libraries to convert this string into a UTC naive `datetime` object.

from dateutil import parser
import pytz

# Input time string
time = "Feb 8, 2021 5:30pm (Denver Time)"

# Parse the time string
datetime_naive, _ = parser.parse(time, fuzzy_with_tokens=True)

# Localize to Denver time
timezone_denver = pytz.timezone('America/Denver')
datetime_aware = timezone_denver.localize(datetime_naive)

# Convert to UTC and remove timezone info to make it naive
datetime_utc = datetime_aware.astimezone(pytz.UTC)
datetime = datetime_utc.replace(tzinfo=None)

print(datetime)  # Output: datetime.datetime(2021, 2, 9, 0, 30)


# Question 2
# Use the `requests` library to load the following HTML page:

import requests

url = 'https://en.wikipedia.org/wiki/John_von_Neumann'
response = requests.get(url)

# Once you have loaded that page, extract the title of that page, which is the text located between the <title> and </title> tags

if response.status_code == 200:
    start = response.text.find('<title>')
    end = response.text.find('</title>')

    # Extract the title from the page content
    title = response.text[start+len('<title>'):end]
    print(title)  # Output: John von Neumann - Wikipedia
else:
    print(f'status_code: {response.status_code}')


# Question 3
# Use a `GET` request to this URL:

url = 'https://httpbin.org/json'
response = requests.get(url)

# Use the response from that request to:
# - Determine the response format
# - Extract the response into a Python object

content_type = response.headers.get('Content-Type')
data_json = response.json()
data_text = response.text

if response.status_code == 200:
    print(f'\ncontent_type: {content_type}\n')
    print(f'\ndata_json: {data_json}\n')
    print(f'\ndata_text: {data_text}\n')
else:
    print(f'Error: {response.status_code}')


# Question 4
# Use a `POST` request to call this URL:

url = 'https://httpbin.org/anything'
data = {
    'x': 100,
    'y': 200,
    'z': ['a', 'b', 'c']
}

# Make a POST request, passing query parameters a=1 and b=2
response = requests.post(url, params={'a': 1, 'b': 2}, data=data)

# Load the returned JSON into a Python object and print it out
if response.status_code == 200:
    print(f'json(): {response.json()}')
    print(f'text: {response.text}')
else:
    print(f'status_code: {response.status_code}')
