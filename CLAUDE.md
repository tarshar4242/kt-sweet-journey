# 專案工作規則（使用者指定，必須遵守）

## 觸發語「ADHD模式」（2026-08-03 起，所有專案通用）

使用者說「**ADHD模式**」＝照 `.claude/skills/i-have-adhd/SKILL.md` 切換 ADHD 友善輸出
（答案與下一步放第一行、多步驟編號、每回合報進度、時間估計講具體），整個對話持續生效；
說「停止ADHD模式」「一般模式」才關閉。規則正本在 tarshar-vault/skills/i-have-adhd/。

## 安裝新 Skill 前必先安全審查（2026-08-04 起，所有專案通用）

任何要新裝進本 repo `.claude/skills/` 的 Skill，安裝前必先照
`tarshar-vault/sop/新技能安裝前安全審查清單.md` 跑完審查（逐檔看完整個資料夾、
找連外回傳與可疑指令、紅黃綠燈回報）：🔴 有回傳統計／叫 AI 隱瞞的一律不裝；
🟡 功能必要的連外先讓使用者拍板；🟢 才能裝。審完要在該清單的「審查紀錄」補一行。
（2026-08-04 已對本 repo 現有 2 份技能總盤點，全數安全。）
（2026-08-09 新裝 2 份技能，來源為 GitHub msitarzewski/agency-agents（MIT 授權）：
`proposal-strategist`（改作自 sales-proposal-strategist＋grant-writer，工作提案／公部門投案）、
`essay-structure-coach`（改作自 academic-narratologist，散文／心得長文結構診斷，預設只診斷不代筆）。
三份原檔逐檔審查完畢全數 🟢：純提示詞、無連外回傳、無隱瞞指令；原檔與 MIT 授權存於各技能 `references/`。
正本清單「審查紀錄」在 tarshar-vault，本環境搆不到，請使用者見到此行後自行補記一行。）

## 觸發語「訪談彙整／研究彙整／演講彙整」（2026-08-05 起）

使用者說「**訪談彙整**」「**研究彙整**」「**演講彙整**」「交叉拆解」，或丟出兩位以上人物的
訪談連結／截圖要求整理觀點時，走 `.claude/skills/research-digest/SKILL.md` 全流程：
查證 → 論者重整（含利益位置）→ 六種思維鏈 → 兩張 SVG 圖 → 接回她的隱性知識外化研究主軸
→ 產出「研究彙整頁」（收 🧰 生活應用）＋「電子報」（收 📮 主題式電子報）→ 上架 ＋ 附純文字校對檔。
⚠️ 該技能第一鐵則：人名／模型名／數字一律要兩個獨立來源對得上才寫，對不上就說查不到，不可猜。
（2026-08-05 由 Claude 從零撰寫，無連外回傳、無隱瞞指令，內容已交使用者過目，判定 🟢。）

## 觸發語「AI協作日誌」（2026-08-16 起，所有專案通用）

使用者說「**AI協作日誌**」「協作日誌」「更新協作日誌」「這個專案的日誌」時：

1. **先用她既有的技能**：`ai-coevolution-journal`（工作進行中保存決策、修正與分支）與
   `create-ai-collaboration-journal`（把一段重要協作整理成完整的繁中 AI 協作日誌）。
   兩者已以**實體檔案**版控於 `.claude/skills/`（不是 symlink）；雲端 session 開啟此 repo 時應直接載入。
2. **無論用哪個技能，動手前一律先讀 `docs/` 裡既有的日誌當範本**：
   `docs/小熊健康小屋-AI協作日誌.html`（01，格式正本）、`docs/AI咒語師護照-AI協作日誌.html`（02）。
3. 格式固定：單檔 HTML、第一人稱她的口吻、封面＋內容目錄＋導讀四節（為什麼做／協作主線／各方角色／
   資料界線）＋九部（完整紀錄×2、偏航與修正、決策帳、關鍵字辭典、研究素材、文件狀態、仍待確認、下一步），
   存到 `docs/`，並在第七部附上所有相關文件的可點連結。
⚠️ **這條的由來：她說「AI協作日誌」時，Claude 已經有好幾次交出錯誤產物——自創了索引式交接文件
（檔案清單＋定案總表＋時間軸）。那是 `project-handover-doc` 的東西，不是協作日誌。**
根因是她的技能只在 Mac 上、沒進 repo，雲端 Claude 看不到；因此**先讀 docs/ 範本**這一步是必要的保險。
與 thesis-journal（給教授的研究日誌）、chat-checkpoint（給下一個 Claude 的接力棒）也完全不同，不可互相取代。

## 通則：專案裡已有先例的產出物，動手前先找上一份長什麼樣（2026-08-16 起）

日誌、教案、圖卡、電子報、簡報、交接文件——凡是這個 repo 裡已經做過同類型的東西，
**先在 repo 裡搜尋既有檔案、照既有格式做**，沒有先例才自己設計。
不要憑自己的想法排一份新格式再交給她挑錯；她要的一致性是「跟上一份長得一樣」。

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
  （2026-07-25 新增）「🔧 TARSHAR 工具集」系列＝單頁直達型（onclick location.href='tools.html'，
  TOC_SERIES 已補列）：`tools.html` 是仿 tool.lifehacker.tw 風格的免費線上工具箱總覽頁
  （搜尋＋分類篩選＋深淺色切換，工具資料在頁內 JS 的 `TOOLS` 陣列）。
  ⚠️ **收錄定義很嚴格（使用者 2026-07-25 明確指定）**：只收「單一用途、點進來就能直接
  完成一件事」的線上小工具（參考 tool.lifehacker.tw 的換行轉換器、抽獎轉盤那種）；
  行程手冊、參訪日誌、心得分享、教學頁、目錄導覽頁**都不算工具，不可以放進去**。
  工具會由使用者指定、一個一個設計加入 → 在 `TOOLS` 陣列加一筆（icon／name／cat／desc／tags／href／cost），
  分類晶片只顯示有工具的分類（CATS 補 key 即可），並同步更新入口卡與此處的「收錄 N 樣」數字。
  **算力分級規則（使用者 2026-07-25 指定，設計每個新工具前先判斷）**：
  cost:'free'＝不用算力或免費公開資料源就能做到（純前端文字處理、canvas、亂數、
  瀏覽器內建語音、免金鑰的免費 API）→ 優先做這種；cost:'device'＝要在使用者裝置跑
  AI 模型（免費但速度看設備）；cost:'key'＝要使用者自備 AI 金鑰。
  凡 device／key：(1) 卡片會自動顯示 ⚡／🔑 標示（免費即用則顯示 ✅）；
  (2) **工具頁內開始使用前必須先用白話提示**：要準備什麼、去哪申請、會不會花錢、資料會不會離開瀏覽器；
  (3) 動工前先把「算力誰出」的建議帶給使用者拍板。
  （2026-07-23 新增）「📮 主題式電子報」系列（showSeries('edm')＋#view-edm）：
  每期一頁 `edm-NNN.html`，卡片前綴「電子報 NNN」，編號「電子報 NNN｜YYYY.MM.DD」，最新在最前；
  回入口用 `lessons.html#edm`。
  ⚠️ **內容利基：每期都要引用真實他人視角並給出自己的立場（2026-08-05 使用者指定）**：
  單純的「我做了什麼」過程紀錄容易流於日記，缺乏可被讀者帶走的亮點。從電子報 007 起，
  每期固定一個「🔭 別人怎麼看」區塊（`.cite` 樣式，琥珀色，跟她自己判斷用的綠色 `.pull` 區分開）：
  引用至少一則**查證過的真實**訪談／文章原句＋來源連結，再附一到兩句她自己的回應
  （同意、反對，或補一個對方沒講到的角度）——連結要真的查證過，不可捏造。
  結構也優先「先講立場（金句/判斷），再用案例佐證」，而不是「先敘事、最後才悟出道理」，
  讓文章一開始就有鉤子。舊期數（001-006）不用回頭改，新規格從 007 開始套用即可。
  ⚠️ **不可以自己標註自己的語氣**（2026-07-31 使用者指定，範圍含標籤與所有文案）：不要出現
  「✍️ 本人口吻」這類卡片標籤，也不要在系列說明、卡片簡介、SERIES_META 的 `sub` 裡寫「用我自己的
  口吻寫」「親筆」「原汁原味」之類的字。網站是她自己的，用她的口吻寫是理所當然，特地標出來反而
  一看就是 AI 代筆。標籤與文案只講這一期實際做了什麼、用了什麼工具（如 🎬 簡報變影片、🎙️ 語音合成）。
  ⚠️ **品牌名一律寫成「🍀Learn AI with Tarshar」**（2026-07-31 使用者指定）：電子報內頁的頁尾與
  「關於我」段落都要帶 🍀，不可以只寫 Learn AI with Tarshar。首頁另有「呈現方式」切換鈕（▦ 卡片／☰ 目錄）：
  目錄模式左側是自動從各 `#view-*` 卡片生成的系列目錄，選擇存 localStorage `lessons_mode`；
  新增系列/卡片時目錄會自動更新，但單頁直達型系列要在 JS 的 `TOC_SERIES` 補一列。
  ⚠️ 多人可能同時改 `lessons.html`／CLAUDE.md：push main 前先 `git fetch origin main`，
  若 origin 已前進就 rebase 並保留他人新增的系列/卡片（別覆蓋），衝突時兩邊內容都留。
  ⚠️ **`index.html` 必須與 `lessons.html` 內容完全一致**（根網址 `…/kt-sweet-journey/` 直接就是課程館，
  不再用轉址頁，避免「先閃舊頁再跳轉」）。**每次改完 `lessons.html` 後，一律 `cp lessons.html index.html` 再一起 commit。**

## 電子報交付慣例（2026-08-05 使用者指定，所有專案通用）

電子報（`edm-NNN.html`）上架、給使用者網址連結的**同一則訊息**，一律**同時附上一份純文字檔**
（用 SendUserFile 傳送，不是貼在對話裡），讓她來得及在文字層面挑錯字、改用詞，不用進 HTML 找。
文字檔內容＝這一期的純文字版本（標題、各段小標、內文，去掉 HTML 標籤），檔名比照
`edm-NNN.txt`。之後每次發電子報都要照這個流程，不用她每次再提醒。

## 網頁慣例

- 單檔 HTML（內含 CSS/JS）、繁體中文、手機優先、進度存 localStorage，
  以 GitHub Pages 發佈（https://tarshar4242.github.io/kt-sweet-journey/<檔名>.html）。
- **講「做好了／已上線」時，同一則訊息就要附上可以直接點的連結**（2026-07-31 使用者指定）：
  不可以只講檔案名稱或路徑，不可以要她自己去網站或 GitHub 找。網頁給下面那條統一入口；
  產出的檔案（影片、簡報、文件）直接把檔案傳給她；GitHub 檔案給 blob 連結。
- **跟使用者報網址一律給統一入口 `https://tarshar4242.github.io/`**（2026-07-25 使用者指定）：
  個別頁面的長網址在 Pages 重建期間會先 404、又有轉址，對她很麻煩；
  根網址永遠有效並自動帶到課程館，新內容請她從入口點進去即可。
