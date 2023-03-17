import requests
import webbrowser

url = input("enter the website address: ")
weblink = 'http://web.archive.org/web/20051129021746/http://' + url + '/'
request = requests.get(weblink)

webbrowser.open(weblink)
print(request.text)

weblink = 'http://web.archive.org/web/20140125235112/http://' + url + '/'
request = requests.get(weblink)

webbrowser.open(weblink)
print(request.text)

weblink = 'http://web.archive.org/web/20191207235926/https://' + url + '/'
request = requests.get(weblink)

webbrowser.open(weblink)
print(request.text)
