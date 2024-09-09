import pytest
import sys
import os
import allure
import re
from testdata import TestData  

# 加項目根目錄到 sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api.films import FilmsAPI

@allure.feature('SW API by ID Tests')
class TestCase_Films_by_ID():
    
    swapi = FilmsAPI()

    # 測試1: 驗證 id=1時 status code 為 200    
    @allure.title("驗證 id=1時 status code 為 200   ")
    @allure.description("驗證 id=1時 status code 為 200   ")
    @allure.story("/api/films/:id")
    @pytest.mark.parametrize("id", [1])  # 設定ID為1
    def test_id_1_status_code(self, id):
        res = self.swapi.get_films_by_id(id)
        res_status = res.status_code
        assert res_status == 200

    # 測試2: 驗證 id=a時 status code 為 404    
    @allure.title("驗證 id=a時 status code 為 404   ")
    @allure.description("驗證 id=a時 status code 為 404 且detail為 Not found")
    @allure.story("/api/films/:id")
    @pytest.mark.parametrize("id", ['a'])  # 設定ID為a
    def test_id_a(self, id):
        res = self.swapi.get_films_by_id(id)
        res_status = res.status_code
        res_body = res.json()
        assert res_status == 404
        assert res_body["detail"] == TestData.Not_Found

    # 測試3: 驗證 id=0時 status code 為 404    
    @allure.title("驗證 id=0 時 status code 為 404   ")
    @allure.description("驗證 id=0 時 status code 為 404 且detail為 Not found")
    @allure.story("/api/films/:id")
    @pytest.mark.parametrize("id", [0])  # 設定ID為0
    def test_id_0(self, id):
        res = self.swapi.get_films_by_id(id)
        res_status = res.status_code
        res_body = res.json()
        assert res_status == 404
        assert res_body["detail"] == TestData.Not_Found

    # 測試4: 驗證 id=3時回應時間在3秒內   
    @allure.title("驗證 id=3 時回應時間在3秒內")
    @allure.description("驗證 id=3 時回應時間在 TO 設定的3秒內")
    @allure.story("/api/films/:id")
    @pytest.mark.parametrize("id", [3])  # 設定ID為3
    def test_id_3_response_time(self, id):
        res = self.swapi.get_films_by_id(id)
        assert res.elapsed.total_seconds() < TestData.Wait_Time  # 設定逾時限制

    # 測試5: 驗證 id=2 時回應中的 episode_id
    @allure.title("驗證 id=2 時回應中的episode_id")
    @allure.description("驗證 id=2 時回應中的 episode_id 應為5")
    @allure.story("/api/films/:id")
    @pytest.mark.parametrize("id", [2])  # 設定ID為2
    def test_id_2_episode_id(self, id):
        res = self.swapi.get_films_by_id(id)
        res_status = res.status_code
        res_body = res.json()
        assert res_status == 200
        assert res_body["episode_id"] == TestData.Episode_ID_2

    # 測試6: 驗證 id=2 時回應中的 opening_crawl
    @allure.title("驗證 id=2 時回應中的 opening_crawl")
    @allure.description("驗證 id=2 時回應中的 opening_crawl 不為空")
    @allure.story("/api/films/:id")
    @pytest.mark.parametrize("id", [2])  # 設定ID為2
    def test_id_2_opening_crawl(self, id):
        res = self.swapi.get_films_by_id(id)
        res_status = res.status_code
        res_body = res.json()
        assert res_status == 200
        assert res_body["opening_crawl"] != ""

    # 測試7: 驗證 id=3 時回應中的 release_date 格式
    @allure.title("驗證 id=3 時回應中的 release_date 格式")
    @allure.description("驗證 id=3 時回應中的 release_date 格式為 YYYY-MM-DD")
    @allure.story("/api/films/:id")
    @pytest.mark.parametrize("id", [3])  # 設定ID為3
    def test_id_3_date_format(self, id):
        res = self.swapi.get_films_by_id(id)
        res_status = res.status_code
        res_body = res.json()
        assert res_status == 200
        assert re.match(TestData.Date_Regex, res_body['release_date'])

    # 測試8: 驗證 id=3 時不支援的METHOD (Delete) 會得到 status code 為 405 與錯誤訊息
    @allure.title("驗證 不支援的METHOD")
    @allure.description("驗證 id=3 時不支援的METHOD (Delete) 會得到 status code 為 405 與錯誤訊息")
    @allure.story("/api/films/:id")
    @pytest.mark.parametrize("id", [3])  # 設定ID為3
    def test_id_3_unsupported_method(self, id):
        res = self.swapi.delete_films_by_id(id)
        res_status = res.status_code
        res_body = res.json()
        assert res_status == 405
        assert res.json()['detail'] == TestData.Invalid_Method_Detail_DELETE