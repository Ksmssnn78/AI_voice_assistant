import requests
from bs4 import BeautifulSoup


def query(request):
    user_query = request

    url = "https://www.google.com/search?q="+user_query

    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }

    page = requests.get(url, headers=header)
    print(page)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find(class_='Z0LcW').get_text()
    return result

