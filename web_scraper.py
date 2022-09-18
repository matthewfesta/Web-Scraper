import requests
from bs4 import BeautifulSoup

# Capture the URL as a result variable
result = requests.get("https://www.google.com/")
print(f'Status Code: \n {result.status_code}')  # Make sure page is accessible
print(f'Headers: \n {result.headers}')  # Get headers to verify correct page
print('\n')
src = result.content  # Extract the content and store it in a variable
# Create soup object to parse and process the source
soup = BeautifulSoup(src, "html.parser")
# Find all <a> tags to get the links:
links = soup.find_all("a")
print('Links:')
for link in links:
	print(link)
print('\n')

