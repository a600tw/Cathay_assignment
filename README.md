# Cathay_assignment

# Star War API 自動化測試

提供針對星際大戰 API (`https://swapi.dev/api/films/` 和 `https://swapi.dev/api/films/:id/`) 的自動化測試框架。測試基於 `pytest` 框架進行，並導入 Allure 報告以增加測試結果的可視化展示。

## 結構

為了保持測試邏輯與程式邏輯分離，本專案主要分為三個目錄，提升專案的維護性與擴展性：

- `/common`：包含配置文件與常數定義。
- `/api`：負責 FILM API 的請求設置。
- `/test`：包含測試案例及獨立的測試資料集。

## 專案目的

本專案旨在提供一個清晰的結構，將測試邏輯與程式邏輯分離，方便維護並提升擴充測試覆蓋率的靈活性。

## 前置作業

在執行測試之前，請確保已經安裝 `requirements.txt` 中所需的依賴組件：

```bash
pip install -r requirements.txt
```

## 執行測試
要執行 /test 目錄下的所有測試並生成 Allure 報告，可以執行以下命令：
```bash
pytest --alluredir=./allure-results
cp -r ./allure-report/history ./allure-results/
allure generate ./allure-results --clean -o ./allure-report
allure serve ./allure-results

```

## 流程：
1. 執行 /test 目錄下的所有測試案例。
2. 複製先前 Allure 報告中的歷史數據以便保留。
3. 生成網頁版的 Allure 報告。
4. 提供 Allure 報告的伺服器以便檢視結果。

## Note
- 強調測試資料與測試邏輯的分離，確保在更新測試案例或測試資料時更加靈活方便。
- Allure 報告提供了互動式且可視化的測試執行情況，有助於更有效地分析測試結果。



  <img width="1141" alt="截圖 2024-09-10 凌晨1 10 43" src="https://github.com/user-attachments/assets/277b4aa5-af52-4533-a586-dde0f15e9195">
<img width="1146" alt="截圖 2024-09-10 凌晨12 42 25" src="https://github.com/user-attachments/assets/70704ff9-7e82-46a2-ace9-1150dbaf8f9d">
