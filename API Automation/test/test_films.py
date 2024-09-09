import pytest
import sys
import os
import allure
from testdata import TestData  

# 加項目根目錄到 sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api.films import FilmsAPI


@allure.feature('SW API Tests')
class TestCase_Films():

    swapi = FilmsAPI()

    # 測試1: 驗證 status code 為 200    
    @allure.title("Check Status Code is 200")
    @allure.description("Verify the status code returned by the SWAPI films endpoint is 200")
    @allure.story("/api/films")
    def test_status_code_200(self):
        res = self.swapi.get_films()
        res_status = res.status_code
        assert res_status == 200
    
    # 測試2: 驗證回應時間在逾時之前
    @allure.title("驗證回應時間在逾時之前")
    @allure.description("驗證回應時間在3秒之內")
    @allure.story("/api/films")
    def test_response_time(self):
        # response = requests.get(BASE_URL)
        res = self.swapi.get_films()
        assert res.elapsed.total_seconds() < TestData.Wait_Time  # 設定逾時限制

    # 測試3: 驗證回應內容 Header 包含正確json格式
    @allure.title("驗證 Header 中的 Content-Type")
    @allure.description("驗證 Header 中的 Content-Type 為 application/json")
    @allure.story("/api/films")    
    def test_json_header(self):
        res = self.swapi.get_films()
        assert res.headers['Content-Type'] == "application/json"

    # 測試4: 驗證回應內容之欄位格式為預期格式
    @allure.title("驗證回應內容之欄位格式為預期格式")
    @allure.description("抽部分回應內容欄位驗證格式為預期格式")
    @allure.story("/api/films")    
    def test_field_format(self):
        # response = requests.get(BASE_URL)
        res = self.swapi.get_films()
        body = res.json()
        for film in body['results']:
            assert isinstance(film['title'], str)
            assert isinstance(film['episode_id'], int)
            assert isinstance(film['release_date'], str)

    # 測試5: 驗證回應內容影片數量與count符合
    @allure.title("驗證回應內容影片數量與count符合")
    @allure.description("驗證回應內容影片數量與count符合")
    @allure.story("/api/films")  
    def test_film_count(self):
        res = self.swapi.get_films()
        body = res.json()
        assert body['count'] == len(body['results'])

    # 測試6: 驗證回應內容所有星戰六部曲片名
    @allure.title("驗證回應內容所有星戰六部曲片名")
    @allure.description("驗證回應內容所有星戰六部曲片名符合預期列表內片名")
    @allure.story("/api/films")  
    def test_star_wars_titles(self):
        
        res = self.swapi.get_films()
        body = res.json()
        titles = [film['title'] for film in body['results']]
        assert set(TestData.Expected_Title_List) == set(titles)

    # 測試7: 驗證 錯誤路徑(/api/films566) 會得到 status code 為 404 NOT FOUND
    @allure.title("驗證得到 status code 為 404")
    @allure.description("驗證 錯誤路徑(/api/films566) 會得到 status code 為 404 NOT FOUND")
    @allure.story("/api/films")  
    def test_invalid_path(self):
        res = self.swapi.get_films("566")
        assert res.status_code == 404

    # 測試8: 驗證 不支援的METHOD (PATCH) 會得到 status code 為 405 與錯誤訊息
    @allure.title("驗證不支援的METHOD得到 status code 為 405 與錯誤訊息")
    @allure.description("驗證不支援的METHOD (PATCH) 會得到 status code 為 405 與錯誤訊息")
    @allure.story("/api/films")  
    def test_unsupported_method(self):
        # response = requests.patch(BASE_URL)
        res = self.swapi.patch_films()
        assert res.status_code == 405
        assert res.json()['detail'] == TestData.Invalid_Method_Detail_PATCH

    # 測試9: 驗證重複發送 API 請求後回應內容仍正確
    @allure.title("驗證重複發送 API 請求後回應內容仍正確")
    @allure.description("驗證重複發送 API 3次後請求後回應內容仍正確")
    @allure.story("/api/films")  
    @pytest.mark.parametrize("repeat", range(3))  # 重複發送3次
    def test_repeated_requests(self, repeat):
        res = self.swapi.get_films()
        status = res.status_code
        body = res.json()

        if repeat == 0:
            pytest.first_status = status
            pytest.first_body = body
        
        else:
            assert body == pytest.first_body
            assert status == pytest.first_status

