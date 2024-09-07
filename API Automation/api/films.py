from ..common.configurations import SWAPI


class FilmsAPI(BaseAPI):

    BASE_URL = urljoin(SWAPI.API_Path, "films/")

    # LIST = "List"

    def get_films(self):
        '''
        '''
    

    def get_films_by_id(self, id: int):
        '''
        '''


    def ad_list(self, authenticate: str, placement_id: list):
        """4.15廣告版位內容

        Args:
            Authenticate (str):  JKOS Token
            PlacementID (str): 廣告 ID, Null or 空陣列全部回傳
        """
        headers = {
            'Authenticate': authenticate
        }
        body = {
            'PlacementID': placement_id
        }
        return self._send_request(
            method='POST',
            url=urljoin(self.BASE_URL, self.LIST),
            headers=headers,
            json=body
        )
