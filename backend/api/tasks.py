import os
from celery import shared_task
from .models import News
from .serializer import NewsSerializer
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
            
           
                # Prepare data for the serializer
            data = {
                'date': f"{todays_date}",
                'news': titles
            }
            print(data)
            
            # Create or update the news item
            serializer = NewsSerializer(data=data)
            
            if serializer.is_valid():
                serializer.save()  # This will create a new entry or update if needed
            else:
                print(f"Serializer validation failed: {serializer.errors}")
            
            print("News fetched and processed successfully!")
        else:
            print("Unexpected response format: No articles found.")
        
    except requests.RequestException as e:
        print(f"Failed to fetch news: {e}")
