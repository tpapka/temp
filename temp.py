import requests

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'

r = requests.get(url)

submission_ids = r.json()
submission_dicts = []

for sid in submission_ids[:30]:
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(sid) + '.json')
    submission_r = requests.get(url)
    response_dict = submission_r.json()
    submission_dict = {'title': response_dict['title'], 'link': response_dict['url']}
    submission_dicts.append(submission_dict)

for sd in submission_dicts:
    print(sd['title'])


    
    http://api.nytimes.com/svc/topstories/v2/home.json?api-key=94a90c94d7154c3eb02c0462f5441ced
