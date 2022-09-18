import requests
from bs4 import BeautifulSoup


def get_headers(url_result):
	"""
	Get headers to verify correct page
	:return:
	"""
	for key, value in url_result.headers.items():
		print(key, ":", value)


def get_structure(url_result):
	"""
	Retrieves the structure of the page
	:param url_result:
	:return:
	"""
	src = url_result.content  # Extract the content and store it in a variable
	# Create soup object to parse and process the source
	soup = BeautifulSoup(src, "html.parser")
	print(f'Page Structure: \n {soup.prettify()}')


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
	print(url_input)
	# Check status code to make sure it is accessible
	print(f'Status Code: \n {result.status_code}')
	quit = False
	while not quit:
		menu_input = input('Menu Options: \n'
		                   '1 - Get headers'
		                   '2 - Get Document Structure'
		                   '3 - Get Links'
		                   '4 - Get Email Addresses'
		                   '5 - Search by HTML Tag'
		                   '6 - Quit')
		try:
			menu_input = int(menu_input)
			if menu_input < 1 or menu_input > 6:
				print('Invalid Input')
		except:
			print('Invalid Input')
		else:
			if menu_input == 1:
				get_headers(result)
			elif menu_input == 2:
				get_structure()
			elif menu_input == 3:
				get_links()
			elif menu_input == 4:
				get_emails()
			elif menu_input == 5:
				get_tag()
			elif menu_input == 6:
				quit = True


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
