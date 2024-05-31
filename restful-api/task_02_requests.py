import requests
import csv


def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print('title:{}'.format(post['title']))


def fetch_and_save_posts():

    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        post = response.json()
        data = [{'id': posts['id'], 'title': posts['title'],
                'body': posts['body']} for posts in post]

    with open('post.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
        writer.writeheader()
        writer.writerows(data)
