import requests

def get_country_data_from_api(country_name):
    url = f'https://restcountries.com/v2/name/{country_name}'
    res = requests.get(url)

    if res.status_code != 200:
        return "API data not found" 
    else:
        api_data = res.json()
        return api_data