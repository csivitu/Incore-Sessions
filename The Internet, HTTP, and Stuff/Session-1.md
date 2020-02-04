# Session 1

- Date: 03.02.2020

# Overview

- Introduction and brief overview of how the internet works
- Basics about Routing, IP Addressing and DNS
- HTTP and how it works, request and response structure
- Sample HTTP requests and response formats portrayed with the help of netcat
- Using the Network tab in a Chrome browser
- Python hands on session to make a script to login to a website
- Cookies and why they are needed

# The Internet

- The internet is a network of networks
- When you get an internet connection, you basically join this network
- Computers are identified using IP Addresses
- Servers are just computers on this network which you can communicate with
- There are some special servers called DNS Servers, they are responsible for mapping domain names like `csivit.com` to the IP Addresses of the respective servers.
- The internet is analogous to sending letters, the domain name is like the name of the recipient and the IP is like the address of the recipient
- Routers are basically mailboxes which are responsible for transferring the letters from one place to another

# HTTP

- Hypertext Transfer Protocol (Protocol - a set of rules or guidelines)
- All the information transferred is in the form of plain text
- Just like a letter has a format (e.g. formal letter), HTTP specifies a format of the message to be used for communication between computers over the internet
- Requests are messages sent to the server, the most commonly used `methods` (types) are:
    * GET: to get information from the server, like a webpage or a file
    * POST: to submit information to the server, like usernames and passwords (in the request body)
- Request structure
```
RequestMethod / HTTP/1.1
HTTP Headers

HTTP Body
```
- Headers consist of additional information about the object sent in the body, like the type of content (html file or jpeg file etc.)
- Body consists of the actual content to be shown
- Sample GET request
```
GET / HTTP/1.1
Host: localhost:8000
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36
Sec-Fetch-User: ?1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9,hi;q=0.8,de-DE;q=0.7,de;q=0.6,bn;q=0.5,la;q=0.4
```

- Response structure
```
HTTP/1.1 STATUSCODE
HTTP Headers

HTTP Body
```

- Sample response
```
HTTP/1.1 200 OK
Content-Type: text/html

<h1>Sample HTTP Response</h1>
```

# Python Hands On

## Requirements
- Python 3.5+
- `requests` library (present by default, if not, can be installed by executing `pip install requests`)

## Content
- Template code for sending a GET request

```python
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

- Template for sending post request

```python
import requests

req_url = "Enter request URL here"

payload = {
    "username": "Enter username",
    "password": "Enter password"
} # A dictionary to store the form data to be sent in the request body

post_response = requests.post(req_url, data=payload)

print("Response Content")
print(post_response.content)

print("Response Headers")
print(post_response.headers)

print("Response Cookies (object)")
print(post_response.cookies)
```
- HTTP is a stateless protocol; a stateless protocol is a communications protocol in which no session information is retained by the receiver, usually a server.
- The server identifies it's clients with the help of cookies
- When you log in to a website, the server sends back a cookie to the client (browser), and the client saves the cookie in it's storage. When the client sends the next request, it sends the cookie along with it. The server checks this cookie and verifies if it is valid. If you have actually logged in to the website, you would have a valid cookie, hence it will allow you to access the protected pages, otherwise it will ask you to log in.
- Sample requests with cookies

```python
import requests

req_url = "Enter the URL of a login page here"
req_url_protected = "Enter a URL which is protected, i.e, can not be accessed without logging in"

payload = {
    "username": "Your Username",
    "password": "Your Password"
}

# First attempt - request the protected URL without passing any cookies

r = requests.get(req_url_protected)
print(r.content) # Does not allow you to access the URL, probably asks you to login


# Second attempt - login through req_url first and use the cookie received to access the protected URL

login_response = requests.post(req_url, data=payload)

my_cookies = login_response.cookies

r = requests.get(req_url_protected, cookies=my_cookies)
print(r.content) # Returns the requested page, since login is successful
```

# Mini Project - 1

- Write a Python script using the `requests` library to log in to VIT Wifi.