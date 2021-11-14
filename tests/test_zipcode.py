import requests
import pytest
from json import dumps
from utils.print_helpers import pretty_print


BASE_URI = 'http://api.zippopotam.us/us/90210'

def test_zipcode():
    response = requests.get(BASE_URI)
    response_text = response.json()
    pretty_print(response_text)
    
    assert response.status_code == 200
    
    country = response_text ['country']
    country_abbr = response_text ['country abbreviation']
    latitude = response_text['places'][0]['latitude']
    longitude = response_text['places'][0]['longitude']
    place_name = response_text['places'][0]['place name']
    state = response_text['places'][0]['state']
    state_abbr = response_text['places'][0]['state abbreviation']
    post_code = response_text['post code']

    assert country == 'United States'
    assert country_abbr == 'US'
    assert latitude == '34.0901'
    assert longitude == '-118.4065'
    assert place_name == 'Beverly Hills'
    assert state == 'California'
    assert state_abbr == 'CA'
    assert post_code == '90210' 


