import requests

# Testing requests links.
url = 'http://127.0.0.1:5000/products'
response = requests.get(url)
print(response.content.decode())

print('________________________________')

url1 = 'http://127.0.0.1:5000/products/2'
response1 = requests.get(url1)
print(response1.content.decode())

print('________________________________')

url2 ='http://127.0.0.1:5000/products/model/Les-Paul'
response2 = requests.get(url2)  
print(response2.content.decode())

print('________________________________')

url3 = 'http://127.0.0.1:5000/products/color/Red'
response3 = requests.get(url3)
print(response3.content.decode())

print('________________________________')

# Testing POST method request.
new_product={
    
    "model": "Super_strat",
    "brand": "Ibanez",
    "color": "Purple"
}

url4 = 'http://127.0.0.1:5000/products/insert-new'
response4 = requests.post(url4, json=new_product)
print(response4.content.decode())

print('_____________________________________')

