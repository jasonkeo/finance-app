import os
from celery import shared_task
import requests
from datetime import datetime
from openai import OpenAI
key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=str(key))

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

                 This are details you will use:
                **Today’s Date:** {todays_date}  
                **News:** {lst} (research more if needed)  
                **Market Data:** {market_data}  

                
                Here's some logic to help you with your analysis:

                ## **1. Unemployment Rate:**  
                - **Consumer Discretionary & Retail:**  
                - High unemployment → Lower disposable income → Retail, travel, and leisure decline  
                - Low unemployment → Higher consumer spending → Retail, travel, and hospitality growth  

                - **Utilities & Consumer Staples:**  
                - Less sensitive due to necessity-driven demand, but prolonged high unemployment → Decline  

                ---

                ## **2. Interest Rates:**  
                - **Real Estate & Utilities:**  
                - Rising rates → Higher mortgage and debt servicing costs → Decline  
                - Falling rates → Real estate boom → Construction sector rise  

                - **Financials:**  
                - Rising rates → Banks profit from lending → Financials up  
                - Falling rates → Narrower lending margins → Financials decline  

                ---

                ## **3. Inflation:**  
                - **Energy & Materials:**  
                - High inflation → Commodity prices rise → Oil, gas, metals sectors gain  
                - Low inflation → Reduced profit margins in commodities → Sector decline  

                - **Technology & Consumer Discretionary:**  
                - High inflation → Input costs rise → Margins shrink → Decline  
                - Low inflation → Lower production costs → Sector growth  

                ---

                ## **4. War & Geopolitical Tensions:**  
                - **Energy:**  
                - War in oil-producing regions → Supply disruptions → Oil prices spike → Energy sector gains  

                - **Industrials & Transportation:**  
                - High oil prices → Increased transportation and logistics costs → Sector decline  

                - **Defense & Aerospace:**  
                - War or geopolitical threats → Increased government defense spending → Sector growth  

                ---

                ## **5. Sanctions & Trade Wars:**  
                - **Technology & Manufacturing:**  
                - Supply chain disruptions → Tech hardware production slows → Decline  

                - **Agriculture & Food:**  
                - Import/export bans → Agriculture prices fluctuate → Sector volatility  

                ---

                ## **6. Earnings Reports:**  
                - **Tech & Consumer Discretionary:**  
                - Strong earnings → Tech, e-commerce, and luxury goods rally  
                - Weak earnings → Widespread sell-off in growth-driven sectors  

                ---

                ## **7. Mergers & Acquisitions (M&A):**  
                - **Healthcare & Pharma:**  
                - High-profile M&As → Increased investor confidence → Sector surge  

                - **Tech & Telecommunications:**  
                - Industry consolidation → Market leaders strengthen → Sector gains  

                ---

                ## **8. Stock Buybacks:**  
                - **Financials & Tech:**  
                - Frequent buybacks in these sectors → Share price growth  

                ---

                ## **9. Fiscal Policy (Taxes & Spending):**  
                - **Industrials & Construction:**  
                - Infrastructure spending → Sector boom  
                - Budget cuts → Reduced government contracts → Decline  

                - **Energy & Utilities:**  
                - Green energy incentives → Renewable energy sector gains  
                - Fossil fuel tax hikes → Oil & gas sector decline  

                ---

                ## **10. Monetary Policy (Federal Reserve Actions):**  
                - **Financials & Banks:**  
                - Tightening policy → Higher lending rates → Banks profit  
                - Loosening policy → Lower loan profits → Sector decline  

                ---

                ## **11. Consumer Confidence Index (CCI):**  
                - **Automotive & Travel:**  
                - High CCI → Increased car sales and travel bookings → Sector growth  
                - Low CCI → Automotive and travel sectors decline 

                ---
                
                Write your answer like the following example:
              **Market Indicator Predictions as of December 11, 2024:**\n\n- **Unemployment Rate:**  \n  - Prediction: **Decrease**  \n  - Reason: Current unemployment is stable around 4.2%, indicating a steady job market that supports consumer spending and corporate profits, likely benefiting the S&P 500.\n\n- **Interest Rates:**  \n  - Prediction: **Stay the Same**  \n  - Reason: With rates at 4.64%, a pause in further increases may support borrowing and investment, aiding corporate profits, thus positively impacting the S&P 500.\n\n- **Inflation:**  \n  - Prediction: **Stay the Same**  \n  - Reason: The CPI is stable, suggesting moderate inflation that indicates economic growth without eroding profit margins significantly, resulting in a neutral impact on the S&P 500.\n\n- **Geopolitical Tensions:**  \n  - Prediction: **Slight Decrease**  \n  - Reason: Ongoing tensions could disrupt markets and elevate oil prices, leading to higher inflation and decreased consumer spending, negatively affecting the S&P 500.\n\n- **Earnings Reports:**  \n  - Prediction: **Increase**  \n  - Reason: Expect strong earnings reports due to stable economic conditions, boosting investor confidence and likely lifting the S&P 500.\n\n- **Consumer Confidence Index (CCI):**  \n  - Prediction: **Increase**  \n  - Reason: With a reasonable unemployment rate and stable inflation, consumer confidence might rise, leading to increased spending and stronger corporate performance, benefiting the S&P 500.\n\nOverall, the market outlook is cautiously optimistic with factors supporting growth, although geopolitical risks could introduce volatility.

               

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

            res = completion.choices[0].message.content
            

            data = {
                'date': f"{todays_date}",
                'news': lst,
                'index': market_data,
                'analysis': res
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


