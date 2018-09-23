import requests
from urllib.parse import urlencode


phone = 'Phone number'
recipient = 'country code' + phone.lstrip('0')

body = '''Multi-line
message here
'''


url = "https://api.hubtel.com/v1/messages"

payload_dict = {
      "Content" : body,
      "From" : 'Sender Name',
      'To': recipient,
      'Direction': 'out',
    }

payload = urlencode(payload_dict)

headers = {

    'authorization': "Authorisation Code",
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

