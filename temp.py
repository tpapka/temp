import requests

main_dict = []

def hacker_news():
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    r = requests.get(url)
    submission_ids = r.json()
    hn_dict = []

    for sid in submission_ids[:30]:
        url = ('https://hacker-news.firebaseio.com/v0/item/' + str(sid) + '.json')
        submission_r = requests.get(url)
        response_dict = submission_r.json()
        hn_dict = {'title': response_dict['title'], 'link': response_dict['url']}
        main_dict.append(hn_dict)


if __name__ == "__main__":
    hacker_news()
    for sd in main_dict:
        print(sd['title'])

        
        "http://api.nytimes.com/svc/topstories/v2/home.json?api-key="
