import requests

base_url = "http://makeup-api.herokuapp.com/api/v1/products.json"
querystring = {"brand"}
response = requests.get(base_url)
data = response.json()


brands = [item['brand'] for item in data]


with open('brand.txt', 'w+') as f:
    for items in list(set(brands)):
        f.write('%s\n' % items)