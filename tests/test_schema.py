import json
import requests
from assertpy import assert_that
from cerberus import Validator
from config import BASE_URI, COUNTRY, ZIP_CODE

schema = { "country": {'type':'string'},
  "country abbreviation": {'type':'string'},
  "places": {'type':'list',
              'items': [{'type':'dict',
                        'keysrules':
                          {'type':'number','type':'number','type':'string',
                          'type':'string','type':'string'}
                          
                        }]
                       },
  "post code": {'type':'string'}
  }

def test_zipcode_has_expected_schema():
    response = requests.get(BASE_URI+'/'+COUNTRY+'/'+ZIP_CODE)
    response_text = json.loads(response.text)

    validator = Validator(schema, require_all=True)
    is_valid = validator.validate(response_text)

    assert_that(is_valid,description=validator.errors).is_true()
