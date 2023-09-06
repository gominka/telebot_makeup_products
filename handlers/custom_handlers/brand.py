import requests
import json


base_url = "http://makeup-api.herokuapp.com/api/v1/products.json"
querystring = {"brand"}

response = requests.get(base_url)
data = response.json()


def find_values(id, json_repr):
    results = []

    def _decode_dict(a_dict):
        try:
            results.append(a_dict[id])
        except KeyError:
            pass
        return a_dict

    json.loads(json_repr, object_hook=_decode_dict)  # Return value ignored.
    return results


json_repr = response.json()[0]
print(find_values('brand', json_repr))

