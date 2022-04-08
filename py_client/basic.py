import requests

endpoint = "http://httpbin.org/status/200/"
# endpoint = "http://httpbin.org/anything"

get_response = requests.get(endpoint, data={"query":"Hello query"})
print(get_response.json()) # in text format