#!/usr/bin/python3

import requests
import csv

url = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        
        # Structurer les données
        structured_posts = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]
        
        # Écrire dans un fichier CSV
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for post in structured_posts:
                writer.writerow(post)        