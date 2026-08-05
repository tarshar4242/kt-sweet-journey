---
name: lecture-notes-site
description: 把 Google Drive 的課程資料夾（講義簡報＋錄影回放）做成「逐幀詳細課堂筆記 HTML」＋「akira 風格多層次互動學習地圖 HTML」。當使用者貼出 Drive 課程資料夾連結、提到晨學講堂 EP 集數、或要求「課堂筆記／學習地圖／逐幀記錄」時使用。
---

# 課堂筆記＋互動學習地圖 產生器

把一個課程 Drive 資料夾變成兩個單檔 HTML 交付物，推上 GitHub 並發佈 Artifact 預覽。
**鐵則（見 repo CLAUDE.md）：資料來源不可自行跳過或降級。拿不到內容就解套，解套不了就 AskUserQuestion，絕不默默用推測內容交差。**

## 輸入

1. Drive 資料夾連結或 EP 集數（必要）
2. 參考 UI 網站（預設 akira.ipas-ai.com 風格：深色霓虹、卡片多層導覽、搜尋、遊戲化進度）

## 流程

### 第 1 步：定位與取得檔案

1. 從連結取出 folderId → `get_file_metadata` 確認標題。
2. `search_files` 用 `parentId = '<folderId>'` 列內容；**共享資料夾常搜不到子項**，
   改用 `sharedWithMe = true and title contains '<關鍵字>'` 與 `fullText contains '<EP編號>'` 交叉找。
3. 找不到就請使用者把檔案「建立副本」到自己的雲端硬碟（歷史有效解法），副本會出現在搜尋。
4. `read_file_content` 讀簡報文字。若簡報是滿版圖片型（抽出文字極少），文字內容要靠影片＋簡報原圖。

### 第 2 步：拿到影片與簡報原圖（逐幀的關鍵）

- Drive MCP 的 `download_file_content` 是 base64 回傳，**大檔不可用**。
- 需要網域 `drive.google.com`、`drive.usercontent.google.com`、`googleusercontent.com`、
  `huggingface.co`、`cdn-lfs.huggingface.co`。先 `curl -sS -o /dev/null -w "%{http_code}" --cacert /root/.ccr/ca-bundle.crt https://drive.usercontent.google.com/` 測（`000`=被擋）。
- 被擋 → AskUserQuestion 給三選項：①開通環境 Network access（claude.ai/code → Environments → Unrestricted）②使用者用 NotebookLM 產逐字稿存成 Google 文件給我讀 ③兩者都做。等待時用背景迴圈每 60s 監測，通了自動開跑。
- 下載（處理大檔確認頁）：
  ```bash
  url="https://drive.usercontent.google.com/download?id=${ID}&export=download&confirm=t"
  curl -sSL --cacert /root/.ccr/ca-bundle.crt -o out.bin "$url"
  # 若 file out.bin 是 HTML：抽 name="uuid" value 再帶 &uuid= 重打一次
  ```
- 簡報 pptx 下載後 `unzip -o ep.pptx 'ppt/media/*'` 取原圖，挑代表圖嵌入筆記。
- 影片抽格（2026-08-03 升級：借鑑 drpwchen/lecture-to-notes 的「去重＋接地」做法，
  取代舊的固定每 15 秒抽格，可少看六～七成重複幀）：
  ```bash
  FF=$(ls /opt/pw-browsers/ffmpeg-*/ffmpeg 2>/dev/null | head -1); FF=${FF:-ffmpeg}
  mkdir -p frames
  # 第一遍：場景變化偵測——畫面有變（換頁/切示範）才留一張，showinfo 記下每張秒數
  "$FF" -i ep.mp4 -vf "select='gt(scene,0.08)',showinfo,scale=1280:-2" \
        -vsync vfr -q:v 3 frames/sc_%04d.jpg 2> frames/showinfo.log
  grep -o 'pts_time:[0-9.]*' frames/showinfo.log | cut -d: -f2 > frames/timestamps.txt
  # 第 N 張 sc_ 圖 ＝ timestamps.txt 第 N 行的秒數
  # 保底：長時間不換頁的講解/示範段落，每 60 秒補抽一張，避免漏掉畫面內的漸進變化
  "$FF" -i ep.mp4 -vf "fps=1/60,scale=1280:-2" -q:v 3 frames/bk_%04d.jpg
  ```
  閾值自 0.08 起調：一小時課 sc_ 圖 <40 張＝偵測太鈍（降到 0.05）、>300 張＝雜訊太多（升到 0.12）。
- 看圖前先零成本預篩（便宜的先篩，貴的才看）：檔案特小的圖幾乎必是純黑／純色分隔頁／轉場，
  挑掉不看：`mkdir -p frames/skip && find frames -maxdepth 1 -name '*.jpg' -size -12k -exec mv {} frames/skip/ \;`
  （1280 寬 jpg 的經驗門檻約 12KB；不確定就從 skip/ 抽兩張開來確認再調。**只准跳空白頁**——
  純影像無文字的頁面檔案大、不會被此門檻誤殺）。
  剩下的用 Read 工具**親眼逐張看**並記錄每頁簡報／示範畫面（鐵則不變，這就是「一幀一幀」）。
- 簡報接地（自動對時間戳）：timestamps.txt 第 N 張的秒數＝該頁開始講的時間；
  逐字稿 segment 的時間落在第 N 張與第 N+1 張之間者歸入該頁。
  筆記各節的 `[mm:ss]` 一律由此換算，不靠人工對時間、也不憑印象填。
- 逐字稿：`pip install faster-whisper` → 16kHz 單聲道 wav → small/int8 模型轉寫（4 核約 30–60 分鐘），
  **保留 segment 級 start/end 秒數**供接地使用；轉寫可背景跑，與看幀並行。

### 第 3 步：產出兩個 HTML（單檔、繁中、手機優先）

命名：`ep<NN>-notes.html`（筆記）與 `ep<NN>-<主題slug>.html`（互動地圖）。

**筆記頁**（米白紙感、側欄目錄、可列印）依序含：
0 課程資訊表＋內嵌 Drive 預覽（`https://drive.google.com/file/d/<ID>/preview` iframe：簡報翻頁＋錄影播放）
1 一頁全景 SVG 圖解 → 各章逐節（重點清單/操作步驟/指令範例框/比較表/金句卡/真實簡報截圖）
→ 課後自我檢核表 → 資料來源與整理說明（誠實標註哪些是實錄、哪些是重構）。

**嵌圖三級規則（2026-08-03，借鑑 lecture-to-notes 的實戰教訓）**——決定每張截圖／簡報原圖
放不放進筆記時，先問兩題：「這張圖的內容，文字筆記是否已經講完？」
「扣掉文字，圖裡還剩多少資訊（箭頭、影像、版面關係）？」然後套三級：
- **必嵌**：流程圖、決策路徑、架構圖——資訊在線與箭頭裡，寫成文字會失真。
- **保底必嵌**：示範操作畫面、表格、統計圖、介面/工具截圖——就算講者只帶過一句，
  也不可掉出筆記（原作者教訓：11 張流程圖被判不重要整批消失）。
- **強制不嵌**：純條列文字頁——內容已寫成筆記條列，再貼圖是同一件事講兩次、還拖慢載入。
某張畫面內容判斷不了（模糊、被遮）→ 寧可不嵌，不嵌一張不知道裡面是什麼的圖。

**互動地圖頁**（akira 風格）：深色 `#0a0e1a` 底＋青紫霓虹漸層＋星點背景；
首頁章節卡片 → 章節頁（麵包屑）→ 技能手風琴 → 細節區塊，共四層；
全站關鍵字搜尋（點結果跳到該技能並展開）；技能打勾進度存 localStorage
（key 格式 `ep<NN>-skills-v1`）＋總進度條＋各章小進度條＋重置鈕；
內容一律放在 JS 的 `DATA` 物件（章→技能→blocks：ul/steps/prompt/table/tip/warn），由 JS 渲染。

### 第 4 步：驗證、上架網站與交付

1. 無頭 Chromium 截圖驗版面：`/opt/pw-browsers/chromium-*/chrome-linux/chrome --headless --no-sandbox --screenshot=x.png file:///...`；`--dump-dom` 確認 JS 有渲染出內容。
2. **上架共同入口 `lessons.html`（兩層結構）**：第一層是「系列」卡（如「📻 直播電台」）、
   第二層是該系列各集。晨學講堂直播課 → 在 `#view-radio` 卡片區「最前面」插入新課程卡
   （沿用既有 `.course` 卡片結構：`.ep` 標籤寫「直播電台 EP<NN>」、課名、一句簡介、tags、日期、
   兩顆連結鈕 `ep<NN>-notes.html`／`ep<NN>-<slug>.html`；`--c` 輪換 cyan/blue/purple/green）。
   若是新的課程系列：在 `#view-home` 加系列卡＋新增 `#view-<key>` 區塊。
   各集頁面「回入口」連結用 `lessons.html#radio`（直達系列頁）。
3. commit（繁中訊息）→ push 工作分支 → **合併回 main 並 push（使用者已常設授權：
   「一次一個課程放上我的網頁」，見 CLAUDE.md）**，讓 GitHub Pages 生效。
4. 兩檔各發佈 Artifact（favicon 固定：地圖🧠、筆記📝；重發用同檔名同路徑保 URL）。
5. 回覆使用者三組網址：GitHub Pages 正式網址
   （`https://tarshar4242.github.io/kt-sweet-journey/lessons.html` 起點）、
   Artifact 預覽連結、raw.githack 備用連結
   （`https://raw.githack.com/<owner>/<repo>/<branch>/<file>`，Drive iframe 在此可正常內嵌）。

## 品質守則

- 筆記的每一條內容都要能對到來源（簡報頁／影片時間點／逐字稿段落）；對不到的標「系列課程脈絡補充」。
- 逐字稿完成後回頭把筆記逐節替換成實錄內容，附影片時間戳（格式 `[mm:ss]`，
  由「簡報接地」的 timestamps.txt 換算，不憑印象填）。
- **簡報文字以 pptx 原始檔與 `ppt/media/` 原圖為準**；影片截圖只負責「這頁何時講到、
  講者在畫面上示範／指了什麼」。截圖裡的小字看不清就對照 pptx 原圖確認，
  對不到就標「畫面不清」，不硬讀不硬寫（看模糊字硬讀會編造出圖上沒有的文字）。
- SVG 圖解至少 3 張（全景、核心觀念、流程）；表格一律包 `overflow-x:auto` 容器。
