import os
from celery import shared_task
import requests
from datetime import datetime

@shared_task
def my_periodic_task():
    todays_date = datetime.now().strftime('%Y-%m-%d')
    api_key = os.getenv('NEWS_API')
    
    if not api_key:
        print("API key is not set.")
        return

    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'us',
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Will raise an HTTPError for bad responses
        news = response.json()
        
        if 'articles' in news:
            # Extract titles from articles
            titles = [article['title'] for article in news['articles']]
            
            # Prepare data for the API endpoint
            data = {
                'date': f"{todays_date}",
                'news': titles
            }
            
            # Send data to the Django API endpoint
            api_url = 'http://web:8000/api/news/'  # Replace with your API endpoint URL
            api_headers = {
                'Content-Type': 'application/json'
            }

            try:
                api_response = requests.post(api_url, json=data, headers=api_headers)
                api_response.raise_for_status()  # Will raise an HTTPError for bad responses
                print("Data successfully sent to the API endpoint.")
            except requests.RequestException as api_e:
                print(f"Failed to send data to the API: {api_e}")
            
        else:
            print("Unexpected response format: No articles found.")
        
    except requests.RequestException as e:
        print(f"Failed to fetch news: {e}")
