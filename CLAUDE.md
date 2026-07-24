# 專案工作規則（使用者指定，必須遵守）

## 資料來源處理原則（最重要）

1. **不可以自行跳過或降級使用者指定的資料來源。**
   使用者要求「逐幀（每一幀）記錄影片／簡報內容」時，必須實際取得並讀完內容才能寫筆記。
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

## 【進行中】EP44 逐幀課堂筆記——新工作階段接手指南

使用者要求把 EP44 錄影「每一幀」記錄成課堂筆記（不可跳過）。已完成：
`ep44-notes.html`（筆記骨架，含 Drive 內嵌與 SVG 圖解）、`ep44-ai-skills.html`（akira 風格多層次互動地圖）。
待辦（需網路開通後執行）：

1. 檔案 ID：錄影（原始連結共享，可匿名下載）`1JN_7ioqD19TkDEeb26vauFZVm47a2FXu`；
   使用者硬碟副本影片 `1qpIe2YcVoOew7REmSrv8qHhrekWD-ZVz`、簡報 pptx `10MbFHlGMs_1ISJXDcX9vFdMFlI6JgyWj`。
2. 下載（drive.usercontent.google.com 開通後）：
   `curl -L --cacert /root/.ccr/ca-bundle.crt -o ep44.mp4 "https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t"`
   （大檔會回確認頁，抽 `name="uuid"` 再帶上 `&uuid=` 重打；流水線腳本樣板見 scratchpad/fetch_ep44.sh 的寫法）。
3. 抽格：ffmpeg 每 15 秒抽 1 格 →「親眼」逐格閱讀（Read 工具看圖），記錄每頁簡報與示範畫面；
   簡報 pptx 下載後 unzip 取 `ppt/media/` 原圖，嵌入筆記。
4. 逐字稿：pip 裝 faster-whisper（模型自 huggingface.co 下載），16kHz 單聲道 wav 轉寫。
5. 將逐幀內容增補進 `ep44-notes.html`（保留現有結構，逐節替換為實錄內容＋真實截圖），
   並同步更新 `ep44-ai-skills.html` 的技能細節，commit + push 到分支
   `claude/lecture-notes-html-page-r3m77v`。

## 常設授權與觸發語（使用者已明確同意）

- 使用者丟出「課程 Drive 資料夾連結」（或說「做 EP<NN> 筆記」「做成筆記並上架」）時，
  直接執行 `/lecture-notes-site` 全流程：逐幀筆記＋互動地圖 → 上架 `lessons.html` 總覽頁
  → **合併回 main 並 push，讓 GitHub Pages 立即上線**（此動作已獲常設授權，無須再問）。
- `lessons.html` 是課程筆記館的**共同入口，採兩層結構**：
  第一層選「系列」，目前有四個：「📻 直播電台」＝晨學講堂直播課（showSeries('radio')＋#view-radio）、
  「📚 Tarshar 教案集」＝對外授課教案（公部門／機關工作坊，如蘆洲監理所 AI 開機日；showSeries('plans')＋#view-plans）、
  「🎓 iPAS 證照學習」＝直接連到單頁 `ipas-intermediate.html`（onclick location.href，無第二層）、
  「🧰 生活應用」＝旅程手冊／口譯機／參訪日誌／生圖指令包等實作成品（showSeries('life')＋#view-life）。
  第二層才是該系列的各集/各作品（卡片標題前綴系列名，如「直播電台 EP44」，最新在前，
  課程卡連到逐幀筆記頁與互動地圖頁；教案卡連到單頁教案 HTML）。
  新增集數→插入 `#view-radio` 最前；新增教案→插入 `#view-plans` 最前；新增作品→插入 `#view-life` 最前。
  新系列（有第二層）則在 `#view-home` 加系列卡＋`#view-<key>` 區塊，並在 JS 的 `SERIES_META` 補標題與計數；
  單頁直達型系列（如 iPAS）用 `onclick="location.href='<page>.html'"`，不需第二層。
  各頁「回入口」連結用 `lessons.html#radio`／`#plans`／`#life`（直達系列頁）；
  獨立作品頁左下角有固定「🏠 回筆記館入口」浮動鈕。
  （2026-07-23 新增）「📮 主題式電子報」系列（showSeries('edm')＋#view-edm）：
  每期一頁 `edm-NNN.html`，卡片前綴「電子報 NNN」，編號「電子報 NNN｜YYYY.MM.DD」，最新在最前；
  回入口用 `lessons.html#edm`。首頁另有「呈現方式」切換鈕（▦ 卡片／☰ 目錄）：
  目錄模式左側是自動從各 `#view-*` 卡片生成的系列目錄，選擇存 localStorage `lessons_mode`；
  新增系列/卡片時目錄會自動更新，但單頁直達型系列要在 JS 的 `TOC_SERIES` 補一列。
  ⚠️ 多人可能同時改 `lessons.html`／CLAUDE.md：push main 前先 `git fetch origin main`，
  若 origin 已前進就 rebase 並保留他人新增的系列/卡片（別覆蓋），衝突時兩邊內容都留。
  ⚠️ **`index.html` 必須與 `lessons.html` 內容完全一致**（根網址 `…/kt-sweet-journey/` 直接就是課程館，
  不再用轉址頁，避免「先閃舊頁再跳轉」）。**每次改完 `lessons.html` 後，一律 `cp lessons.html index.html` 再一起 commit。**

## 網頁慣例

- 單檔 HTML（內含 CSS/JS）、繁體中文、手機優先、進度存 localStorage，
  以 GitHub Pages 發佈（https://tarshar4242.github.io/kt-sweet-journey/<檔名>.html）。
