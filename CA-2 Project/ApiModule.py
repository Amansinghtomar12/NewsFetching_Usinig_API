import requests

API_KEY = '9cea89daf5c3427f8d8d4f38a4e4907c'

def FetchNews(country):
    url = 'https://newsapi.org/v2/everything'
    parameters = {
        'q': country,
        'sortBy': 'publishedAt',
        'apiKey': API_KEY,
        'pageSize': 10
    }
    try:
        response = requests.get(url, params=parameters)
        response.raise_for_status()
        data = response.json()
        
        articles = data.get('articles', [])
        
        if articles:
            for i, article in enumerate(articles):
                title = article.get('title', 'No title available')
                source = article.get('source', {}).get('name', 'Unknown source')
                description = article.get('description', 'No description available')
                url = article.get('url', 'No link available')
                published_at = article.get('publishedAt', 'No publication date available')
                
                print(f"Article {i + 1}:")
                print(f"Title: {title}")
                print(f"Source: {source}")
                print(f"Description: {description}")
                print(f"Published At: {published_at}")
                print(f"Read more: {url}")
                print('-' * 205)
        else:
            print("No news articles found for this country.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
