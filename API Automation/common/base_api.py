import requests
from .configurations import Configs

class BaseAPI:

    def __init__(self, waiting_time=None):
        self.waiting_time = waiting_time or Configs.DEFAULT_WAITING_TIME
        self._session = requests.Session()