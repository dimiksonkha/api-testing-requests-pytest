import requests
from assertpy.assertpy import assert_that
from utils.print_helpers import pretty_print
from config import BASE_URI,COUNTRY,ZIP_CODE


def test_zipcode():
    response = requests.get(BASE_URI+'/'+COUNTRY+'/'+ZIP_CODE)
    response_text = response.json()
    pretty_print(response_text)

     # Extract data from json response
    country = response_text ['country']
    country_abbr = response_text ['country abbreviation']
    latitude = response_text['places'][0]['latitude']
    longitude = response_text['places'][0]['longitude']
    place_name = response_text['places'][0]['place name']
    state = response_text['places'][0]['state']
    state_abbr = response_text['places'][0]['state abbreviation']
    post_code = response_text['post code']
    
    #Header assertion
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    
    # Response body assertion
    assert_that(country).is_equal_to('United States')
    assert_that(country_abbr).is_equal_to('US')
    assert_that(latitude).is_equal_to('34.0901')
    assert_that(longitude).is_equal_to('-118.4065')
    assert_that(place_name).is_equal_to('Beverly Hills')
    assert_that(state).is_equal_to('California')
    assert_that(state_abbr).is_equal_to('CA')
    assert_that(post_code).is_equal_to(ZIP_CODE)


