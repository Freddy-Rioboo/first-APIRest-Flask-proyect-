import requests

url6 ='http://127.0.0.1:5000/products/delete/1'
response6 = requests.delete(url6)
print(response6.content.decode())  
