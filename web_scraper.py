import requests
import re
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
	"""
	Retrieves the links on the page
	:param url_result:
	:return:
	"""
	src = url_result.content  # Extract the content and store it in a variable
	# Create soup object to parse and process the source
	soup = BeautifulSoup(src, "html.parser")
	try:
		links = soup.find_all("a")
	except:
		print('Sorry. I can\'t find any links on the page')
	else:
		print('Links:')
		for link in links:
			print(link.attrs['href'])


def get_emails(url_result):
	"""
	Retrieves tne emails on the page
	:param url_result:
	:return:
	"""
	EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
	# for Javascript rendered websites:
	url_result.html.render()
	for re_match in re.finditer(EMAIL_REGEX, url_result.html.raw_html.decode()):
		try:
			print(re_match.group())
		except:
			print('Sorry, I can\'t find any emails')


def get_tag(url_result):
	src = url_result.content  # Extract the content and store it in a variable
	# Create soup object to parse and process the source
	soup = BeautifulSoup(src, "html.parser")
	# Find all occurrences of a tag:
	tag_input = input('Enter tag: ')
	try:
		print(soup.find_all(tag_input))
	except:
		print(f'Sorry. I can\'t find {tag_input}')


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
		                    '1 - Get headers \n'
		                    '2 - Get Document Structure \n'
		                    '3 - Get Links \n'
		                    '4 - Get Email Addresses \n'
		                    '5 - Search by HTML Tag \n'
		                    '6 - Quit \n')
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
					get_emails(result)
				elif menu_input == 5:
					get_tag(result)
				elif menu_input == 6:
					quit = True


if __name__ == '__main__':
	main()