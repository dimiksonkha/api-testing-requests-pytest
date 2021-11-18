from clients.places.base_client import BaseClient
from config import BASE_URI,COUNTRY,ZIP_CODE
from utils.request import APIRequest

class PlaceClient(BaseClient):
    
    def __init__(self):
        super().__init__()

        self.base_uri = BASE_URI
        self.country = COUNTRY
        self.zipcode = ZIP_CODE
        self.request = APIRequest()

    def read_all_places_by_zipcode_and_country(self):
        
        return self.request.get(self.base_uri,self.country,self.zipcode)
