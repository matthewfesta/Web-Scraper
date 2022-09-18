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


def get_links(url_result):
	src = url_result.content  # Extract the content and store it in a variable
	# Create soup object to parse and process the source
	soup = BeautifulSoup(src, "html.parser")
	links = soup.find_all("a")
	print('Links:')
	for link in links:
		print(link.attrs['href'])


def get_emails():
	pass


def get_tag(url_result):
	src = url_result.content  # Extract the content and store it in a variable
	# Create soup object to parse and process the source
	soup = BeautifulSoup(src, "html.parser")
	# Find all occurrences of a tag:
	tag_input = input('Enter tag: ')
	print(soup.find_all(tag_input))


def main():


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
					get_structure(result)
				elif menu_input == 3:
					get_links(result)
				elif menu_input == 4:
					get_emails()
				elif menu_input == 5:
					get_tag()
				elif menu_input == 6:
					quit = True
