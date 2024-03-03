import requests
import json
import urllib.parse

posts = ['死ね', 'おはよう', 'ふざけんな', 'カス']

for i in range(len(posts)):
    encoded_text = urllib.parse.quote(posts[i])

    api_url = 'http://api1.webpurify.com/services/rest/?'
    api_url += ('api_key=' + 'e14f316dddf4dcb90d175f094bb6c090&')
    api_url += 'method=webpurify.live.check&'
    api_url += f'text={encoded_text}&'
    api_url += 'lang=jp&'
    api_url += 'format=json'

    response = requests.get(api_url)
    json_response = json.loads(response.text)

    if json_response['rsp']['found'] == '0':
        print(posts[i] + ': This post is not offensive.')
    else:
        print(posts[i] + ': This post is offensive.')