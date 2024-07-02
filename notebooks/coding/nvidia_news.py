# filename: nvidia_news.py

import requests
from bs4 import BeautifulSoup

# Define url to scrape news from
url = "https://www.google.com/search?q=nvidia+stock+news&rlz=1C1GCEU_enUS832US832&source=lnt&tbs=qdr:m&sa=X&ved=0ahUKEwjO4brW5J_iAhWJct8KHdZ5A2wQpwUIKg&biw=1366&bih=657&dpr=1"

# Send request
response = requests.get(url)

# Parse the html content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all news headlines
headlines = soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd')

# Print the news headlines
for headline in headlines:
    print(headline.text)