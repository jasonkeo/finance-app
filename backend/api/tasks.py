# myapp/tasks.py
import os
from celery import shared_task
import requests
from datetime import datetime
@shared_task
def my_periodic_task():
    todays_date = datetime.now().strftime('%Y-%m-%d') 
    print("ye")
    api_key = os.getenv('NEWS_API')
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    response = requests.get('https://newsapi.org/v2/top-headlines?country=us&totalresults=5', headers=headers)
    
    if response.status_code == 200:
        news = response.json()
        print("News fetched successfully!")
        temp = []
        for i in news['articles']:
            temp.append(i['title'])

        post_data = {
            'date': todays_date,
            'news': temp
        }
        add = requests.post(
            'http://127.0.0.1:8000/api/news/',
            json=post_data,  # Ensure that the data is sent as JSON
            headers={'Content-Type': 'application/json'}
        )

    else:
        print(f"Failed to fetch news. Status code: {response.status_code}")