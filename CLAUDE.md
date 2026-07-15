# 專案工作規則（使用者指定，必須遵守）

## 資料來源處理原則（最重要）

1. **不可以自行跳過或降級使用者指定的資料來源。**
   使用者要求「逐針（每一針）記錄影片／簡報內容」時，必須實際取得並讀完內容才能寫筆記。
2. 遇到檔案抓不到、網路被擋、格式讀不了時，**依序這樣做**：
   - 先嘗試所有解套辦法（例：請使用者把捷徑/檔案複製到他自己的雲端硬碟再由 Drive 工具讀取、
     換網域下載、轉檔後再讀、把影片抽格成圖片逐張看、環境網路政策開通後直接下載等）。
   - 解套都不行時，**必須用 AskUserQuestion 詢問使用者**要怎麼處理，
     並附上具體可選方案（含需要使用者做的操作步驟）。
   - **絕對不可以**默默改用「重構／推測」的內容交差，然後只在文末註記限制。
3. 曾經用過且有效的解套方法：把共享連結的檔案「建立副本」到使用者自己的雲端硬碟，
   再用 Google Drive MCP 從使用者硬碟讀取。

## 環境備忘

- 此遠端環境的外連網路走 egress proxy，`drive.google.com`、`drive.usercontent.google.com`、
  `huggingface.co` 等網域預設被政策擋（CONNECT 403）。要下載大型 Drive 檔案需請使用者
  到 claude.ai/code 的環境設定把 Network access 改為不受限或加入上述網域。
- Google Drive MCP 的 `download_file_content` 以 base64 回傳，僅適合小檔（< 1MB）；
  大檔不可用此工具下載。`read_file_content` 支援文件/簡報/PDF/圖片，不支援影片。
- 本機有 Chromium 與 ffmpeg（/opt/pw-browsers/），可做網頁截圖與影音抽格。

## 網頁慣例

- 單檔 HTML（內含 CSS/JS）、繁體中文、手機優先、進度存 localStorage，
  以 GitHub Pages 發佈（https://tarshar4242.github.io/kt-sweet-journey/<檔名>.html）。
