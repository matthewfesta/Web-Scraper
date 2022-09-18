import requests
from bs4 import BeautifulSoup

# Capture the URL as a result variable
result = requests.get("https://www.google.com/")
print(result.status_code)  # Make sure page is accessible
print(result.headers)  # Get headers

