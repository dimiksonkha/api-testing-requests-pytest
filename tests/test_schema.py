import json
import requests
from assertpy import assert_that
from cerberus import Validator
from config import BASE_URI, COUNTRY, ZIP_CODE

schema = { "country": {'type':'string'},
  "country abbreviation": {'type':'string'},
  "places": [ { "latitude": {'type':'float'},
                "longitude": {'type':'float'},
                "place name": {'type':'string'},
                "state": {'type':'string'},
                "state abbreviation": {'type':'string'}
             }
            ],
  "post code": {'type':'number'}
  }

def test_schema_has_expected_schema():
    response = requests.get(BASE_URI+'/'+COUNTRY+'/'+ZIP_CODE)
    response_text = json.loads(response.text)

    validator = Validator(schema, require_all=True)
    is_valid = validator.validate(response_text)

    assert_that(is_valid,description=validator.errors).is_true()
