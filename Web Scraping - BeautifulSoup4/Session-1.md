# Session 1

- Date: 05.02.20

# Overview

- Revise requests
- What is HTML DOM structure (HTML Tree)
- What is BeautifulSoup (bs4)
- Use bs4 to parse the webpage contents
- Getting page information using bs4
- Build a crawler to loop over all URLs.
- Adding a timeout to avoid getting blocked (DOS protection by sites)

# PIP packages INSTALLATION needed

- If you get a package not found. Then install the package using pip (Python packages repository)
- Use python3.6 or greater (You will have this installed most probably, don't worry)
- For BeautifulSoup4 (mandatory)
  - `pip install beautifulsoup4`
- For requests (mandatory)
  - `pip install requests`

- Template: Requests to get the url info

```Python
import requests

req_url = "Enter request URL here"
get_response = requests.get(req_url) # The requests.get() function returns the response obtained, it's stored in get_response

print("Response Content:")
print(get_response.content) # to print the body of the response

print("Response Headers:")
print(get_response.headers) # to get response HTTP headers

print("Response Status Code")
print(get_response.status_code) # to get the status code of the response: 200 -> Success, 404 -> Not found, etc.
```

- Template: BeautifulSoup to parse the page contents

```Python
from bs4 import BeautifulSoup

parsed = BeautifulSoup(get_response.text, 'html.parser')

# Getting only text from the page (no tags)
text = parsed.get_text()

# Get the title tag info
title = parsed.title.string

# Get only the url from the page
url_only = parsed.find_all('a').get('href').string
```


# Mini Project - 2

- Write a Python script using the `requests` and `beautifulSoup4` library to scrape the stack overflow website for answers.
- The flow
- * Get the query (question to be asked) from input()
- * Add this to search parameter to get the stack overflow page.
  - * URL to be passed to requests: (`stackoverflow_url + search?q= + "python not installing"`)
  - * Additional: How it will be encoded on browser as url(`https://stackoverflow.com/search?q=python+not+installing`)
- * Parse this using beautifulSoup (`parsed = BeautifulSoup(get_response.text, 'html.parser')`)
- * Get the first link from the answers list (Select right div)
- * Print out the answer contents (Selecting right nesting of divs)