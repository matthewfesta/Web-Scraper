import requests
from bs4 import BeautifulSoup

# Capture the URL as a result variable
result = requests.get("https://www.whitehouse.gov/briefings-statements/")
print(f'Status Code: \n {result.status_code}')  # Make sure page is accessible
# Get headers to verify correct page
for key, value in result.headers.items():
	print(key, ":", value)
print('\n')
src = result.content  # Extract the content and store it in a variable
# Create soup object to parse and process the source
soup = BeautifulSoup(src, "html.parser")
# Find all <a> tags to get the links:
links = soup.find_all("a")
# Print all links:
print('Links:')
for link in links:
	print(link.attrs['href'])
print('\n')

# Print links with an attribute:
for link in links:
	if "About" in link.text:
		print(link)
		print(link.attrs['href'])


