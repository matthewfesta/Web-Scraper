import requests
from bs4 import BeautifulSoup

def menu_options():
	print('Menu Options: \n'
	      '1 - Get headers'
	      '2 - Get Document Structure'
	      '3 - Get Links'
	      '4 - Get Email Addresses'
	      '5 - Search by HTML Tag'
	      '6 - Quit')
	pass
def get_headers():
	pass
def get_structure():
	pass
def get_links():
	pass
def get_emails():
	pass
def get_tag():
	pass


# Capture the URL as a result variable

url_input = input('Enter URL: \n')
try:
	result = requests.get(url_input)
except:
	print('Invalid URL', url_input)
else:
	quit = False
	while not quit:
	print(f'Status Code: \n {result.status_code}')  # Make sure page is accessible
	# Get headers to verify correct page
	for key, value in result.headers.items():
		print(key, ":", value)
print('\n')
src = result.content  # Extract the content and store it in a variable
# Create soup object to parse and process the source
soup = BeautifulSoup(src, "html.parser")
print(f'Page Structure: \n {soup.prettify()}')
print('\n')
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


# Find all occurrences of a tag:
tag_input = input('Enter tag: ')
print(soup.find_all(tag_input))

# Find first occurrence of a tag:
tag_input = input('Enter tag: ')
print(soup.tag_input)