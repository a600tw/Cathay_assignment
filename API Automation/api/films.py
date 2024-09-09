from common.configurations import SWAPI
import requests


# BASE_URL = "https://swapi.dev/api/films/"
class FilmsAPI():

    BASE_URL = SWAPI.API_Path + "/films/"

    # def __init__(self, response_time=None):
    #     self.request = Request(response_time)

    def get_films(self, append:str=None):
        '''
        '''
        if append != None:
            URL = self.BASE_URL + append
        else:
            URL = self.BASE_URL
        response = requests.get(URL)
        print(f"Status: {response.status_code}")
        print(f"Response Body: {response.json()}")
        return response
    
    def patch_films(self, append:str=None):
        '''
        '''
        if append != None:
            URL = self.BASE_URL + append
        else:
            URL = self.BASE_URL
        response = requests.patch(URL)
        print(f"Status: {response.status_code}")
        print(f"Response Body: {response.json()}")
        return response

    def get_films_by_id(self, id: int):
        '''
        '''
        ID_URL = self.BASE_URL+f"{id}/"
        response = requests.get(ID_URL)
        print(f"Status: {response.status_code}")
        print(f"Response Body: {response.json()}")
        return response
    
    def delete_films_by_id(self, id: int):
        '''
        '''
        ID_URL = self.BASE_URL+f"{id}/"
        response = requests.delete(ID_URL)
        print(f"Status: {response.status_code}")
        print(f"Response Body: {response.json()}")
        return response