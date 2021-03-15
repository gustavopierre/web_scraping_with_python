import requests

files = {'uploadFile': open('python.jpg', 'rb')}
r = requests.post('http://pythonscraping.com/pages/processing2.php', files=files)

print(r.text)
