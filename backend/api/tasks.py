import os
from celery import shared_task
import requests
from datetime import datetime

@shared_task
def my_periodic_task():
    todays_date = datetime.now().strftime('%Y-%m-%d')
    api_key = os.getenv('NEWS_API')
    market_key = os.getenv('AlPHA_API')
    
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
            lst = []
            temp = []
            while len(titles) > 0:
                temp.append(titles.pop())
                if len(temp) == 5:
                    lst.append(temp)
                    temp = []
            # Prepare data for the API endpoint

            market_data = {}

            urls = {
                        'VOO' : f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=VOO&apikey={market_key}',
                        'VTI' : f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=VTI&apikey={market_key}',
    }

            
            
            try:
                for key, url in urls.items():
                    response = requests.get(url)
                    response.raise_for_status()  # Will raise an HTTPError for bad responses
                    temp = response.json()
                    # print(temp)
                    recent = temp["Time Series (Daily)"]
                    
                    closing_prices = [float(entry["4. close"]) for entry in list(recent.values())[:8]]
                    dates = [entry for entry in list(recent.keys())[:8]]
                    market_data[key] = [closing_prices[-1], dates[-1]]

            except requests.RequestException as e:
                print(f"Failed to fetch market data: {e}")

            new_urls =   {#                  "data": [
        # {
        #     "date": "2024-11-01",
        #     "value": "4.2"
        # },
        # {
        #     "date": "2024-10-01",
        #     "value": "4.1"
        # },
        # {
        #     "date": "2024-09-01",
        #     "value": "4.1"
                        'gdp' : f'https://www.alphavantage.co/query?function=REAL_GDP&interval=annual&apikey={market_key}',
                       'unemployment' : f'https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={market_key}',
                      'cpi' : f'https://www.alphavantage.co/query?function=CPI&apikey={market_key}',
                         'interest_rate' : f'https://www.alphavantage.co/query?function=FEDERAL_FUNDS_RATE&apikey={market_key}',
            }
            try:
                for key, new_urls in new_urls.items():
                    response = requests.get(new_urls)
                    response.raise_for_status()  # Will raise an HTTPError for bad responses
                    temp = response.json()
                    # print(temp)
                    recent = temp["data"]
                    
                    closing_prices = [float(entry["value"]) for entry in recent[:8]]
                    
                    dates = [(entry["date"]) for entry in recent[:8]]
                    market_data[key] = [closing_prices[:-1], dates[:-1]]

            except requests.RequestException as e:
                print(f"Failed to fetch market data: {e}")


            data = {
                'date': f"{todays_date}",
                'news': lst,
                'index': market_data
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


