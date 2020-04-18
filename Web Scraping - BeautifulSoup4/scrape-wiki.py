import requests
from bs4 import BeautifulSoup
import json
import time

links = []
links_uncleaned = []
web_pages = {}

r = requests.get("https://en.wikipedia.org/wiki/Apple_Inc.")
parsed_content = BeautifulSoup(r.text, 'html.parser')

# Loop to get all the links the single requested page
for each_link in parsed_content.find_all('a'):
	inside_link = str(each_link.get('href'))

	links_uncleaned.append(inside_link)

	# Data sanitisation (cleaning process)
	if 'http' in inside_link:
		links.append(inside_link)

#Checking the difference between uncleaned (without http) and cleaned links (with http)
print(len(links), len(links_uncleaned))

# Getting contents of all urls in the list
for link in links:
	# Requests the url to get the page contents
	r = requests.get(link)

	# To avoid websites denying access to the bot we making
	sleep(1.5)

	# Convert the page to DOM structure (tree structure in simple words)
	parsed = BeautifulSoup(r.text, 'html.parser')
	if parsed:
		text = parsed.get_text()
		if parsed.title:
			# Get the page topic or heading
			topic = parsed.title.string
		else:
			topic = "undefined"

		web_pages[topic] = text

#Export the dictionary created from the above loop into .json file
with open('pages.json', 'w') as pg:
	json.dump(web_pages, pg)