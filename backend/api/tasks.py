import os
from celery import shared_task
import requests
from datetime import datetime
from openai import OpenAI
client = OpenAI()

@shared_task
def my_periodic_task():
    todays_date = datetime.now().strftime('%Y-%m-%d')
    api_key = os.getenv('NEWS_API')
    market_key = os.getenv('AlPHA_API')
    client.api_key = os.getenv('OPENAI_API_KEY')
    
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
                    market_data[key] = [closing_prices[:-1], dates[:-1]]

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
            msg = f"""Given the current news or news you research, analyze the market indicators below, give predictions on whether they will increase, decrease, 
                stay the same, and more importantly, explain why you think that.

                - **Unemployment Rate:**  
                - High unemployment → Lower consumer spending → Reduced corporate profits → S&P 500 decline  
                - Low unemployment → Higher consumer spending → Increased corporate profits → S&P 500 rise  

                - **Interest Rates:**  
                - Rising interest rates → Higher borrowing costs → Reduced business investments & consumer spending → S&P 500 decline  
                - Falling interest rates → Cheaper borrowing → Business expansion & increased consumer spending → S&P 500 rise  

                - **Inflation:**  
                - High inflation → Increased input costs → Lower corporate profit margins → S&P 500 decline  
                - Moderate inflation → Indicates economic growth → Potential S&P 500 gains  

                - **War and Geopolitical Tensions:**  
                - Increased oil prices due to supply disruptions → Higher inflation → Lower consumer spending & corporate profits → S&P 500 decline  
                - Peace agreements → Market stability → S&P 500 recovery  

                - **Sanctions and Trade Wars:**  
                - Sanctions on major economies → Supply chain disruptions & trade slowdown → Corporate revenue decline → S&P 500 drop  
                - Trade agreements → Reduced tariffs → Increased trade and profitability → S&P 500 rise  

                - **Earnings Reports:**  
                - Strong earnings → Investor confidence → Higher S&P 500  
                - Weak earnings → Investor sell-off → Lower S&P 500  

                - **Mergers & Acquisitions:**  
                - Significant M&A activity → Market confidence in growth prospects → S&P 500 rise  

                - **Stock Buybacks:**  
                - Corporate stock buybacks → Reduced supply of shares → Higher stock prices → S&P 500 boost  

                - **Fiscal Policy (Taxes & Spending):**  
                - Tax cuts → Increased disposable income & corporate profits → S&P 500 rise  
                - Tax hikes → Reduced consumer & business spending → S&P 500 decline  

                - **Monetary Policy (Federal Reserve Actions):**  
                - Quantitative easing → Increased liquidity → S&P 500 rise  
                - Tightening monetary policy → Reduced liquidity → S&P 500 decline  

                - **Consumer Confidence Index (CCI):**  
                - High CCI → More spending → Stronger corporate performance → S&P 500 rise  
                - Low CCI → Reduced spending → Weaker corporate profits → S&P 500 decline  

                Write your answer in dot points and make sure it's short but efficient:  
                **Today’s Date:** {todays_date}  
                **News:** {lst} (research more if needed)  
                **Market Data:** {market_data}  
                """

                        
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "user",
                        "content": msg
                    }
                ]
            )

            res = completion.choices[0].message
            

            data = {
                'date': f"{todays_date}",
                'news': lst,
                'index': market_data,
                'analysis': str(res)
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


