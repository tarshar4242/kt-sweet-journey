# 課程筆記館・完整站台規格書（Site Map / Spec）

> **版本**：2026-07-24 快照（對應 main commit `92ba5fa`）｜本規格書由程式掃描 main 分支全站 HTML 自動彙整（標題／描述取自各頁 `<title>` 與 meta description，章節取自各頁實際小節標題），非人工推測。

- **入口網址**：https://tarshar4242.github.io/kt-sweet-journey/lessons.html
- **站台型態**：單一入口（`lessons.html`）＋ **7 大系列**；其中 **4 系列為兩層結構**（radio／plans／life／edm：第一層選系列→第二層列各集/作品卡），**3 系列為單頁或外站直達**（iPAS 單頁、論文研讀庫與 SKILL 技能包為外站）。
- **技術**：每頁皆為單檔 HTML（內含 CSS/JS）、繁體中文、手機優先、進度存 localStorage、GitHub Pages 發佈。
- **首頁呈現方式**：「▦ 卡片／☰ 目錄」切換，選擇存 localStorage `lessons_mode`。
- **頁面總數**：88 個 HTML 檔（含系統頁與範例頁）。

### 用途分類圖例（每頁條目開頭標記）
`逐幀筆記`＝EP 課堂筆記頁 ｜ `互動地圖`＝EP 互動技能地圖頁 ｜ `教案`＝對外教學設計 ｜ `作品`＝生活應用成品 ｜ `電子報`＝主題信 ｜ `單頁學習`＝iPAS ｜ `系統／範例`＝不在動線內

---

## 一、樹狀總覽

```
課程筆記館 lessons.html  ← 共同入口（首頁）  [1 頁]
│  呈現方式：▦ 卡片 / ☰ 目錄（存 localStorage lessons_mode）
│
├─ 📻 SERIES 01 直播電台   showSeries('radio')  →#radio   ── 27 集 / 54 頁
│    每集＝逐幀課堂筆記頁 ＋ 互動技能地圖頁（兩頁一組、互相連結）
│    EP46、EP45、EP44、EP43、EP42、EP41、EP41b、EP40、EP39、EP38、EP37、EP36、EP35、EP34、EP33、EP32、EP31、EP30、EP29、EP28、EP27、EP26、EP25、EP24、EP23、EP21、EP20
│
├─ 📚 SERIES 02 Tarshar 教案集  showSeries('plans')  →#plans  ── 20 份（每份＝單頁教案）
├─ 🧰 SERIES 03 生活應用    showSeries('life')   →#life   ── 5 件（每件＝獨立作品頁）
├─ 🎓 SERIES 04 iPAS 證照學習   單頁直達 → ipas-intermediate.html  [1 頁]
├─ 📖 SERIES 05 論文研讀庫      外站直達 → thesis-library/index.html（另一 repo，不在本站）
├─ 🛠️ SERIES 06 SKILL 技能包    外站直達 → thesis-library/skills.html（另一 repo，不在本站）
└─ 📮 SERIES 07 主題式電子報   showSeries('edm')    →#edm    ── 1 期（每期＝ edm-NNN.html）
```
> 節點頁數為本快照數字，新增內容後需同步更新。

> **共通導覽規則**：各內頁左上角固定「🏠 回筆記館入口」→ 連回 `lessons.html#<系列>`（radio／plans／life／edm 可直達第二層）。EP 的「筆記頁 ⇄ 地圖頁」互放對方連結。

---

## 二、SERIES 01 · 📻 直播電台
晨學講堂直播課。每集＝「逐幀筆記」＋「互動技能地圖」兩頁，互相連結。共 27 集，新到舊排列（編號缺 EP22；EP41b 為 EP41 同主題加課）。

### EP46
#### `ep46-notes.html`　`逐幀筆記`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep46-notes.html
- 標題：EP46 課堂筆記｜抽絲剝繭談 ChatGPT Work：從提問到完整交付（逐幀實錄）
- 內容簡述：晨學講堂 EP46 逐幀課堂筆記：ChatGPT Work 快速上手——Chat／Work／Codex 三模式、Work+Codex=Agent、目標式交付（新青安 3.0 動畫簡報 16 分鐘實作）、Sol／Terra／Luna 三模型、權限核准、Sites 建站、手機 Remote 遙控，含真實操作截圖、官方簡報原文與逐字稿佐證
- 內容物（章節）：0. 課程資訊與教材 ／ 1. 一頁看懂全課程 ／ 2. 逐幀時間軸（37 分鐘全程） ／ 3. 三種模式：Chat／Work／Codex ／ 4. Work 目標式交付（新青安 3.0 實戰） ／ 5. 選對模型：Sol／Terra／Luna ／ 6. 權限、Sites 與手機 Remote ／ 7. 專有名詞卡 ／ 8. 課後自我檢核（照本集實作） ／ 9. 資料來源與製作說明
- 連到其他頁：ep46-ai-skills.html

#### `ep46-ai-skills.html`　`互動地圖`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep46-ai-skills.html
- 標題：抽絲剝繭談 ChatGPT Work｜互動式學習地圖
- 內容簡述：EP46 晨學講堂：抽絲剝繭談 ChatGPT Work——Chat／Work／Codex 三模式、Work+Codex=Agent、目標式交付（新青安 3.0 動畫簡報 16 分鐘實作）、Sol／Terra／Luna 三模型、權限核准、Sites 建站、手機 Remote，互動式多層次學習地圖
- 內容物（章節）：三種模式 ／ 目標式交付 ／ 選對模型 ／ 權限與延伸
- 連到其他頁：ep45-notes.html, ep46-notes.html

### EP45
#### `ep45-notes.html`　`逐幀筆記`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep45-notes.html
- 標題：EP45 課堂筆記｜Google AI Studio 偷藏了這些 Agent！（逐幀實錄）
- 內容簡述：晨學講堂 EP45 逐幀課堂筆記：Google AI Studio 的隱藏 Agent——Codex 語音聽寫、模型 vs Agent、TTS 情境、Build with Agents、Antigravity、AI Talk Radio、多 Agent 團隊，含真實操作截圖、影片時間戳與逐字稿佐證
- 內容物（章節）：0. 課程資訊與教材 ／ 1. 一頁看懂全課程 ／ 2. 逐幀時間軸（37 分鐘全程） ／ 3. 輸入加速：Codex 語音聽寫 ／ 4. Google AI Studio：模型 vs Agent ／ 5. 官方 Agent 展示間 ／ 6. 進階：多 Agent 與實作 ／ 7. 專有名詞卡 ／ 8. 課後自我檢核（照本集實作） ／ 9. 資料來源與製作說明
- 連到其他頁：ep45-ai-skills.html

#### `ep45-ai-skills.html`　`互動地圖`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep45-ai-skills.html
- 標題：Google AI Studio 偷藏了這些 Agent！｜互動式學習地圖
- 內容簡述：EP45 晨學講堂：Google AI Studio 偷藏了這些 Agent！——Codex 語音聽寫、模型 vs Agent、TTS 情境、Build with Agents、Antigravity、AI Talk Radio、多 Agent 團隊，互動式多層次學習地圖
- 內容物（章節）：輸入加速 ／ AI Studio 基礎 ／ 官方 Agent ／ 進階實作
- 連到其他頁：ep44-notes.html, ep45-notes.html

### EP44
#### `ep44-notes.html`　`逐幀筆記`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep44-notes.html
- 標題：EP44 課堂筆記｜2026 上半年一定會的 AI 技能（逐幀實錄）
- 內容簡述：晨學講堂 EP44 逐幀課堂筆記：以「颱風」為貫穿案例，實錄文字篇、生圖篇、AI Agent 篇、自動化篇——含真實簡報截圖、影片時間戳與逐字稿佐證
- 內容物（章節）：0. 課程資訊與教材 ／ 1. 一頁看懂全課程 ／ 2. 逐幀時間軸（59 分鐘全程） ／ 3. 文字篇（實錄） ／ 4. 生圖篇（實錄） ／ 5. AI Agent 篇（實錄） ／ 6. 自動化篇（實錄） ／ 7. 課後自我檢核（照本集實作） ／ 8. 資料來源與製作說明
- 連到其他頁：ep44-ai-skills.html

#### `ep44-ai-skills.html`　`互動地圖`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep44-ai-skills.html
- 標題：2026 上半年一定會的 AI 技能｜互動式學習地圖
- 內容簡述：EP44 晨學講堂：2026 上半年一定會的 AI 技能 — 文字篇、生圖篇、AI Agent 篇、自動化篇，互動式多層次學習地圖
- 內容物（章節）：文字篇 ／ 生圖篇 ／ AI Agent 篇 ／ 自動化篇
- 連到其他頁：ep44-notes.html

### EP43
#### `ep43-notes.html`　`逐幀筆記`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep43-notes.html
- 標題：EP43 課堂筆記｜打通任督二脈學影片製作：Google Vids、Flow、Gemini Omni
- 內容簡述：晨學講堂 EP43 課堂筆記：Google 影片三工具——Vids（商務影片編輯室）、Flow（生成影片片場）、Gemini Omni（聊天中拍片改片）。含工具怎麼選、Omni 六核心能力、影片 Prompt 骨架、多輪編修心法、Avatar 流程與版權。依官方課程簡報與課堂筆記整理。
- 內容物（章節）：0. 課程資訊與教材 ／ 1. 一頁看懂全課程 ／ 2. 三工具怎麼選 ／ 3. Gemini Omni 是什麼、六核心能力 ／ 4. 第一支影片與 Prompt 骨架 ／ 5. 多輪編修心法與 App／Flow 分工 ／ 6. Avatar 正確流程 ／ 7. 學習順序、五個坑與版權 ／ 8. 資料來源與製作說明
- 連到其他頁：ep43-ai-skills.html

#### `ep43-ai-skills.html`　`互動地圖`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep43-ai-skills.html
- 標題：影片製作：Vids／Flow／Gemini Omni｜互動式學習地圖
- 內容簡述：EP43 晨學講堂：打通任督二脈學影片製作——Google Vids、Flow、Gemini Omni 三工具怎麼選、Omni 六核心能力、影片 Prompt 骨架、多輪編修、Avatar 流程與版權，互動式多層次學習地圖
- 內容物（章節）：三工具怎麼選 ／ Gemini Omni 六能力 ／ 第一支影片與 Prompt ／ 編修・Avatar・版權
- 連到其他頁：ep41-notes.html, ep43-notes.html

### EP42
#### `ep42-notes.html`　`逐幀筆記`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep42-notes.html
- 標題：EP42 課堂筆記｜各大主流大型語言模型（ChatGPT、Gemini、Claude）API 申請與應用
- 內容簡述：晨學講堂 EP42 課堂筆記：API 是什麼、如何取得 Key、用 Google Colab 最小測試、三類常見錯誤、Token 與費用、三項安全設定，以及 OpenRouter、OpenAI、Gemini、Claude 的申請與比較。依官方課程簡報與課堂筆記整理。
- 內容物（章節）：0. 課程資訊與教材 ／ 1. 一頁看懂全課程 ／ 2. API 到底在做什麼 ／ 3. OpenRouter：一把金鑰連多模型 ／ 4. OpenAI API 申請與 Colab 最小測試 ／ 5. 三類常見錯誤與除錯順序 ／ 6. Token 使用量與三項安全設定 ／ 7. Gemini／Claude 與怎麼選 ／ 8. 立即行動清單 ／ 9. 資料來源與製作說明
- 連到其他頁：ep42-ai-skills.html

#### `ep42-ai-skills.html`　`互動地圖`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep42-ai-skills.html
- 標題：各大模型 API 申請與應用｜互動式學習地圖
- 內容簡述：EP42 晨學講堂：ChatGPT／Gemini／Claude／OpenRouter API 申請與應用——API 是什麼、OpenRouter 一把金鑰連多模型、OpenAI 與 Colab 最小測試、三類錯誤、Token 與安全設定，互動式多層次學習地圖
- 內容物（章節）：API 是什麼 ／ OpenRouter ／ OpenAI 與 Colab ／ 錯誤・Token・選型
- 連到其他頁：ep40-notes.html, ep42-notes.html

### EP41
#### `ep41-notes.html`　`逐幀筆記`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep41-notes.html
- 標題：EP41 課堂筆記｜AI 生圖篇：不只給漁獲，也不只給釣竿，AI 直接給你智慧漁網
- 內容簡述：晨學講堂 EP41 課堂筆記：AI 生圖進階——Guidance／CFG 服從程度旋鈕、Seed 種子碼與重現、可重現紀錄表、從生圖延伸到影片、推薦實驗流程與易錯點。依官方課程簡報與課堂筆記整理。
- 內容物（章節）：0. 課程資訊與教材 ／ 1. 一頁看懂全課程 ／ 2. Guidance／CFG 是什麼 ／ 3. CFG 實驗方式：一次只改一個變數 ／ 4. Seed 種子碼與「重現」 ／ 5. 建立可重現紀錄表 ／ 6. 從生圖延伸到影片 ／ 7. 推薦實驗流程與易錯點 ／ 8. 資料來源與製作說明
- 連到其他頁：ep41-ai-skills.html

#### `ep41-ai-skills.html`　`互動地圖`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep41-ai-skills.html
- 標題：AI 生圖篇：智慧漁網｜互動式學習地圖
- 內容簡述：EP41 晨學講堂：AI 生圖篇 智慧漁網——Guidance／CFG 服從旋鈕、Seed 種子碼與重現、可重現紀錄表、從生圖延伸到影片，互動式多層次學習地圖
- 內容物（章節）：CFG 服從旋鈕 ／ Seed 與重現 ／ 可重現紀錄表 ／ 影片延伸與流程
- 連到其他頁：ep41-notes.html, ep43-notes.html

### EP41b
#### `ep41b-notes.html`　`逐幀筆記`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep41b-notes.html
- 標題：EP41｜視覺化簡報技巧課堂筆記：與 AI 共行，用布林邏輯（交集、聯集）做圖
- 內容簡述：晨學講堂 EP41 視覺化簡報技巧 課堂筆記：把 PowerPoint「合併圖案」當布林邏輯——聯集、合併、分割、交集、減去五種 Merge Shapes，應用在圖示、鏡頭遮罩與文字填圖。依官方 11 頁簡報與課堂筆記逐頁整理（本集無錄影回放）。
- 內容物（章節）：0. 課程資訊與教材 ／ 1. 一頁看懂全課程 ／ 2. 把圖形當作集合 ／ 3. 五個 Merge Shapes 按鈕（逐一詳解） ／ 4. 圖片裁切與文字穿透字 ／ 5. 易錯點與立即練習 ／ 6. 資料來源與製作說明
- 連到其他頁：ep41-notes.html, ep41b-ai-skills.html

#### `ep41b-ai-skills.html`　`互動地圖`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep41b-ai-skills.html
- 標題：視覺化簡報技巧：布林邏輯做圖｜互動式學習地圖
- 內容簡述：EP41 晨學講堂：視覺化簡報技巧——用 PowerPoint 合併圖案（聯集、合併、分割、交集、減去）做圖示、鏡頭遮罩與文字穿透字，互動式多層次學習地圖
- 內容物（章節）：把圖形當集合 ／ 五個 Merge Shapes ／ 圖片裁切與穿透字 ／ 易錯點與練習
- 連到其他頁：ep40-notes.html, ep41-notes.html, ep41b-notes.html

### EP40
#### `ep40-notes.html`　`逐幀筆記`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep40-notes.html
- 標題：EP40 課堂筆記｜ChatGPT for Excel & PowerPoint 六種實際應用（含 Codex 入門）
- 內容簡述：晨學講堂 EP40 課堂筆記：把 ChatGPT 放進 Excel 與 PowerPoint 的工作流程——三種產品釐清、安裝與側邊欄、背景+任務+輸出下指令公式、Excel 四應用、PowerPoint 四應用、整合一條龍與五個安全提醒。依官方課程簡報與課堂筆記整理。
- 內容物（章節）：0. 課程資訊與教材 ／ 1. 一頁看懂全課程 ／ 2. 先分清三種產品（別被名字搞混） ／ 3. 安裝增益集與側邊欄導覽 ／ 4. 下指令黃金公式：背景＋任務＋輸出 ／ 5. Excel 四應用 ／ 6. PowerPoint 四應用 ／ 7. 整合一條龍與五個安全提醒 ／ 8. 立即練習與名詞表 ／ 9. 資料來源與製作說明
- 連到其他頁：ep40-ai-skills.html

#### `ep40-ai-skills.html`　`互動地圖`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep40-ai-skills.html
- 標題：ChatGPT for Excel &amp; PowerPoint｜互動式學習地圖
- 內容簡述：EP40 晨學講堂：ChatGPT for Excel & PowerPoint 六種實際應用——三種產品釐清、安裝與側邊欄、背景+任務+輸出、Excel 四應用、PowerPoint 四應用，互動式多層次學習地圖
- 內容物（章節）：認識與安裝 ／ 下指令心法 ／ Excel 四應用 ／ PowerPoint 四應用
- 連到其他頁：ep40-notes.html, ep42-notes.html

### EP39
#### `ep39-notes.html`　`逐幀筆記`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep39-notes.html
- 標題：EP39 課堂筆記｜NotebookLM 與 Markdown 格式交互應用
- 內容簡述：晨學講堂 EP39 課堂筆記：讓 NotebookLM 產出「排版不跑掉」的報告——自然語言的坑（退格、表格會不見）、改用 Markdown／YAML 指令、用工作室預覽複製保留格式、目錄與頁碼三做法、Google Docs＋Apps Script 收尾（頁碼／目錄／統一標楷體）。依官方課程簡報與 GAS 程式碼整理。
- 內容物（章節）：0. 課程資訊與教材 ／ 1. 一頁看懂全課程 ／ 2. 自然語言的坑：退格與表格會不見 ／ 3. 用 Markdown／YAML 把格式「規格化」 ／ 4. 工作室預覽：複製最能保真 ／ 5. 目錄與頁碼：三種做法 ／ 6. Google Docs＋Apps Script 收尾 ／ 7. 名詞卡與立即練習 ／ 8. 資料來源與製作說明
- 連到其他頁：ep39-ai-skills.html

#### `ep39-ai-skills.html`　`互動地圖`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep39-ai-skills.html
- 標題：NotebookLM 與 Markdown 格式交互應用｜互動式學習地圖
- 內容簡述：EP39 晨學講堂：NotebookLM 與 Markdown——自然語言的坑、Markdown／YAML 格式化指令、工作室預覽保真、目錄與頁碼三做法、Google Docs＋Apps Script 收尾，互動式多層次學習地圖
- 內容物（章節）：自然語言的坑 ／ Markdown／YAML ／ 預覽保真與目錄頁碼 ／ Apps Script 收尾
- 連到其他頁：ep39-notes.html, ep46-notes.html

### EP38
#### `ep38-notes.html`　`逐幀筆記`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep38-notes.html
- 標題：EP38 課堂筆記｜Gemini Avatar：從概念到應用（虛擬人、虛擬分身與數字人）
- 內容簡述：晨學講堂 EP38 課堂筆記：Gemini Avatar——什麼是 AI 驅動的虛擬互動角色、核心四要素（文字／語音／形象／知識）、運作流程五步、主要特色、應用情境、製作步驟、優勢與限制、使用注意事項。含每一頁課程簡報原圖。
- 內容物（章節）：0. 課程資訊與教材 ／ 1. 什麼是 Gemini Avatar ／ 2. 核心組成：四大要素 ／ 3. 運作流程：從輸入到輸出五步 ／ 4. 主要特色：Gemini Avatar 的亮點 ／ 5. 應用情境：哪些場景最實用 ／ 6. 製作步驟：打造 Gemini Avatar 五步 ／ 7. 優勢與限制：使用前要知道的兩面向 ／ 8. 使用注意事項：安全、倫理與品質 ／ 9. 重點整理：快速回顧 Gemini Avatar ／ 10. 資料來源與製作說明
- 連到其他頁：ep38-ai-skills.html

#### `ep38-ai-skills.html`　`互動地圖`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep38-ai-skills.html
- 標題：Gemini Avatar：從概念到應用｜互動式學習地圖
- 內容簡述：EP38 晨學講堂：Gemini Avatar——什麼是虛擬互動角色、核心四要素、運作流程、主要特色、應用情境、製作步驟、優勢限制與使用注意事項，互動式多層次學習地圖
- 內容物（章節）：是什麼＋核心組成 ／ 運作流程＋製作步驟 ／ 主要特色＋應用情境 ／ 優勢限制＋注意事項
- 連到其他頁：ep38-notes.html, ep43-notes.html, ep46-notes.html

### EP37
#### `ep37-notes.html`　`逐幀筆記`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep37-notes.html
- 標題：EP37 課堂筆記｜與 AI 共行：RAG 訓練不用從頭開始
- 內容簡述：晨學講堂 EP37 課堂筆記：與 AI 共行・RAG——生成式 AI 概念紮根、ChatGPT 客製化與個人化、RAG 檢索增強生成是什麼、ChatGPT 專案功能＝免費 RAG、兩個實作（建立專案上傳檔案／設定專案指令）、Gemini Gem 免費 RAG、NotebookLM 個人知識庫、AI 生圖與印製注意事項。
- 內容物（章節）：0. 課程資訊與教材 ／ 1. 概念紮根：先站穩地基 ／ 2. ChatGPT 客製化與個人化 ／ 3. RAG 是什麼（本集核心） ／ 4. ChatGPT 專案功能 ＝ 免費 RAG ／ 5. 實作一：建立專案 ＋ 上傳檔案（RAG 建置） ／ 6. 實作二：設定專案自訂指令（角色＋語氣＋格式＋任務） ／ 7. Gemini 篇：Gem ＝免費 RAG，打通 Google 生態 ／ 8. NotebookLM ＝個人知識庫 ／ 9. 延伸：AI 生圖與印製注意事項 ／ 10. 重點整理（帶走這幾句） ／ 11. 資料來源與製作說明
- 連到其他頁：ep36-notes.html, ep37-ai-skills.html, ep39-notes.html

#### `ep37-ai-skills.html`　`互動地圖`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep37-ai-skills.html
- 標題：與 AI 共行：RAG 訓練不用從頭開始｜互動式學習地圖
- 內容簡述：EP37 晨學講堂：與 AI 共行・RAG——概念紮根、ChatGPT 客製化、RAG 檢索增強生成、專案功能免費 RAG、兩個實作、Gemini Gem、NotebookLM 個人知識庫，互動式多層次學習地圖
- 內容物（章節）：概念紮根＋客製化 ／ RAG＋專案免費 RAG ／ 兩個實作 ／ Gem／NotebookLM／生圖
- 連到其他頁：ep36-notes.html, ep37-notes.html, ep39-notes.html

### EP36
#### `ep36-notes.html`　`逐幀筆記`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep36-notes.html
- 標題：EP36 課堂筆記｜Gemini Notebooks 5 種稀鬆平常的用法
- 內容簡述：晨學講堂 EP36 課堂筆記：Gemini Notebooks（Gemini 筆記本）——認識 Notebooks、六大環境設定（角色/任務/資料/工作/輸出/限制）、五種實用用法：簡報模板資料庫、學習教練機器人、專案管理機器人、跨筆記本對話、Gemini×ChatGPT 共享來源。含完整範例 Prompt。
- 內容物（章節）：0. 課程資訊與教材 ／ 1. 認識 Gemini Notebooks ／ 2. 六大環境設定（開口前先調教） ／ 3. 打造「簡報模板資料庫」 ／ 4. 打造「學習教練機器人」 ／ 5. 打造「專案管理機器人」 ／ 6. 跨筆記本對話功能 ／ 7. 共享來源：讓 Gemini 與 ChatGPT 不用從頭打造 ／ 8. 範例 Prompt 全集（可直接複製） ／ 9. 重點整理（帶走這幾句） ／ 10. 資料來源與製作說明
- 連到其他頁：ep36-ai-skills.html

#### `ep36-ai-skills.html`　`互動地圖`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep36-ai-skills.html
- 標題：Gemini Notebooks 5 種用法｜互動式學習地圖
- 內容簡述：EP36 晨學講堂：Gemini Notebooks——認識筆記本、六大環境設定、五種實用用法（簡報模板資料庫、學習教練、專案管理、跨筆記本對話、共享來源），互動式多層次學習地圖
- 內容物（章節）：認識筆記本＋六大設定 ／ 用法①②：簡報＋學習 ／ 用法③④：專案＋跨本 ／ 用法⑤＋Prompt 全集
- 連到其他頁：ep36-notes.html, ep37-notes.html, ep39-notes.html

### EP35
#### `ep35-notes.html`　`逐幀筆記`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep35-notes.html
- 標題：EP35 課堂筆記｜從 Prompt 到 Harness：打造可控 AI 系統
- 內容簡述：晨學講堂 EP35 課堂筆記：Harness Engineering（駕馭工程）——大模型的先天缺陷、AI 工程三次遷徙、Agent−Model=Harness、成熟 Harness 六層架構、OpenAI/Anthropic 真實做法，以及用 Gemini Gem＋NotebookLM 實作「每日 AI 新鮮事產生器」的完整六層落地手冊與 Prompt。
- 內容物（章節）：0. 課程資訊與教材 ／ 1. 為什麼需要 Harness：大模型的先天缺陷 ／ 2. AI 工程的三次遷徙 ／ 3. Harness 的定義：Agent − Model = Harness ／ 4. 成熟 Harness 的六層架構（本集核心） ／ 5. OpenAI／Anthropic 的真實做法 ／ 6. 實作：每日 AI 新鮮事產生器 ／ 7. 每日操作 SOP（約 15 分鐘） ／ 8. 重點整理（帶走這幾句） ／ 9. 資料來源與製作說明
- 連到其他頁：ep35-ai-skills.html, ep36-notes.html, ep37-notes.html, ep39-notes.html

#### `ep35-ai-skills.html`　`互動地圖`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep35-ai-skills.html
- 標題：從 Prompt 到 Harness：打造可控 AI 系統｜互動式學習地圖
- 內容簡述：EP35 晨學講堂：Harness Engineering 駕馭工程——大模型缺陷、三次遷徙、Agent−Model=Harness、六層架構、OpenAI/Anthropic 做法、每日 AI 新鮮事產生器實作，互動式多層次學習地圖
- 內容物（章節）：為什麼需要 Harness ／ 前三層架構 ／ 後三層架構 ／ 實作：每日新鮮事
- 連到其他頁：ep35-notes.html, ep36-notes.html, ep37-notes.html

### EP34
#### `ep34-notes.html`　`逐幀筆記`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep34-notes.html
- 標題：EP34 課堂筆記｜打通生成式 AI 任督二脈・Canva 動畫篇
- 內容簡述：晨學講堂 EP34 課堂筆記：ChatGPT Image 2.0（代號 Duct Tape）五大升級、免費限制、長輩圖與做簡報範例、YouMind 提示詞集散地、AI 生圖著作權三重點、Canva Magic Layers 圖層概念、彈出動畫與 VBA 動畫腳本。
- 內容物（章節）：0. 課程資訊與教材 ／ 1. ChatGPT Image 2.0（代號 Duct Tape） ／ 2. 升級對照與免費限制 ／ 3. 實用範例 ／ 4. YouMind：Image 2.0 提示詞集散地 ／ 5. AI 生圖著作權三重點 ／ 6. Canva Magic Layers：圖層概念 ／ 7. 動畫：設計流程＋VBA 動畫腳本 ／ 8. 重點整理（帶走這幾句） ／ 9. 資料來源與製作說明
- 連到其他頁：ep34-ai-skills.html, ep37-notes.html, ep41-notes.html, ep43-notes.html

#### `ep34-ai-skills.html`　`互動地圖`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep34-ai-skills.html
- 標題：打通生成式 AI 任督二脈・Canva 動畫篇｜互動式學習地圖
- 內容簡述：EP34 晨學講堂：ChatGPT Image 2.0 五大升級、免費限制、長輩圖與做簡報、YouMind 提示詞集散地、AI 生圖著作權、Canva Magic Layers 圖層、VBA 動畫，互動式多層次學習地圖
- 內容物（章節）：ChatGPT Image 2.0 ／ 實用範例＋YouMind ／ 生圖著作權 ／ Magic Layers＋動畫
- 連到其他頁：ep34-notes.html, ep41-notes.html, ep43-notes.html

### EP33
#### `ep33-notes.html`　`逐幀筆記`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep33-notes.html
- 標題：EP33 課堂筆記｜一起來讓簡報、資訊圖表改起來及動起來（NotebookLM x Canva Magic Layers x Gamma x PowerPoint）
- 內容簡述：晨學講堂 EP33（Drive 原始標示 EP32+1）課堂筆記：NotebookLM 產出資訊圖表 → Canva Magic Layers 免費編輯 → Gamma 生成動態簡報 → ChatGPT 轉 GIF → PowerPoint VBA 巨集自動動畫，逐段實錄真實截圖與可直接使用的 VBA 程式碼、ChatGPT 提示詞。
- 內容物（章節）：0. 課程資訊與教材 ／ 1. 一頁看懂全課程 ／ 2. Canva Magic Layers：把資訊圖表拆成可編輯圖層 ／ 3. Gamma：讓簡報內容動起來 ／ 4. ChatGPT Gif 轉檔功能：把靜態圖變成會飄的花瓣 ／ 5. PPT 的自動動畫功能：請 ChatGPT 寫一段 VBA 巨集 ／ 6. 課後自我檢核（照本集實作） ／ 7. 資料來源與製作說明
- 連到其他頁：ep33-ai-skills.html

#### `ep33-ai-skills.html`　`互動地圖`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep33-ai-skills.html
- 標題：讓簡報、資訊圖表動起來｜互動式學習地圖
- 內容簡述：EP33 晨學講堂：一起來讓簡報、資訊圖表改起來及動起來——NotebookLM 產內容、Canva Magic Layers 拆圖層、Gamma 一句話生成動態簡報、ChatGPT 轉 GIF、PowerPoint VBA 巨集自動動畫，互動式多層次學習地圖，含完整 VBA 程式碼與提示詞範本
- 內容物（章節）：Canva Magic Layers ／ Gamma 動態簡報 ／ ChatGPT Gif 轉檔 ／ PPT 自動動畫（VBA）
- 連到其他頁：ep33-notes.html, ep34-notes.html

### EP32
#### `ep32-notes.html`　`逐幀筆記`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep32-notes.html
- 標題：EP32 課堂筆記｜打通生成式 AI 任督二脈：Claude Code 篇（逐幀實錄）
- 內容簡述：晨學講堂 EP32 逐幀課堂筆記：Claude Code 從零安裝到上手——Chat／Cowork／Code 三分頁、Windows 安裝實戰（CMD vs PowerShell、Git for Windows）、settings.json 與 additionalDirectories、CCC 快速啟動別名、/model 切換模型、Plan Mode 計劃模式。本集資料夾無簡報檔，全部內容依錄影
- 內容物（章節）：0. 課程資訊與教材 ／ 1. 一頁看懂全課程 ／ 2. 逐幀時間軸（68 分鐘全程） ／ 3. Claude 桌面版：三分頁與能力清單 ／ 4. Windows 安裝實戰（含真實踩雷） ／ 5. 邊查邊做：ChatGPT／NotebookLM 陪你設定專案 ／ 6. 用自然語言改設定：settings.json 與內建 Skill ／ 7. 上手操作：模型、計劃模式與網路搜尋 ／ 8. 專有名詞卡 ／ 9. 課後自我檢核（照本集實作） ／ 10. 資料來源與製作說明
- 連到其他頁：ep32-ai-skills.html

#### `ep32-ai-skills.html`　`互動地圖`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep32-ai-skills.html
- 標題：打通生成式 AI 任督二脈：Claude Code 篇｜互動式學習地圖
- 內容簡述：EP32 晨學講堂：Claude Code 從零安裝到上手——桌面版三分頁、Windows 終端機安裝實戰（CMD／PowerShell 踩雷）、邊查邊做設定專案、用自然語言改 settings.json、/model 與 Plan Mode，互動式多層次學習地圖
- 內容物（章節）：桌面版三分頁 ／ 終端機安裝實戰 ／ 邊查邊做設定專案 ／ 自然語言改設定 ／ 上手操作
- 連到其他頁：ep32-notes.html

### EP31
#### `ep31-notes.html`　`逐幀筆記`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep31-notes.html
- 標題：EP31 課堂筆記｜Gemini X Google Workspace應用
- 內容簡述：晨學講堂 EP31 課堂筆記：Gemini 如何整合進 Google Maps、Docs、Sheet、Slide。Maps 五大能力與比較表、Docs／Sheet 各 8 類應用與完整 prompt 範本、Slide 簡報應用，依官方課程簡報原文逐節整理，內含大量可直接套用的 prompt。
- 內容物（章節）：0. 課程資訊與教材 ／ 1. 一頁看懂全課程 ／ 2. Google Maps x Gemini ／ 3. Google Docs x Gemini ／ 4. Google Sheet x Gemini ／ 5. Google Slide x Gemini ／ 6. 跨工具比較與選擇心法 ／ 7. 實戰心法與常見誤區 ／ 8. 課後自我檢核表 ／ 9. 資料來源與製作說明
- 連到其他頁：ep31-ai-skills.html

#### `ep31-ai-skills.html`　`互動地圖`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep31-ai-skills.html
- 標題：Gemini X Google Workspace應用｜互動式學習地圖
- 內容簡述：EP31 晨學講堂：Gemini X Google Workspace應用——Maps 五大能力、Docs／Sheet／Slide 各 8 類應用與完整 prompt 範本，互動式多層次學習地圖，含全站搜尋與打勾進度。
- 內容物（章節）：Google Maps x Gemini ／ Google Docs x Gemini ／ Google Sheet x Gemini ／ Google Slide x Gemini
- 連到其他頁：ep31-notes.html

### EP30
#### `ep30-notes.html`　`逐幀筆記`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep30-notes.html
- 標題：EP30 課堂筆記｜AnythingLLM（NotebookLM 平替版）逐節實錄
- 內容簡述：晨學講堂 EP30 課堂筆記：AnythingLLM（NotebookLM 平替版）——NotebookLM 簡報上傳新功能、AnythingLLM 是什麼與核心功能、安裝七步驟、與 NotebookLM 比較、應用情境、直播聊天室真實問答精華
- 內容物（章節）：0. 課程資訊與教材 ／ 1. 一頁看懂全課程 ／ 2. NotebookLM 簡報上傳新功能 ／ 3. AnythingLLM 是什麼＋核心功能 ／ 4. 安裝七步驟 ／ 5. AnythingLLM vs NotebookLM 比較 ／ 6. 應用情境 ／ 7. 課堂問答精華（直播聊天室真實留言整理） ／ 8. 課後自我檢核 ／ 9. 資料來源與製作說明
- 連到其他頁：ep30-ai-skills.html

#### `ep30-ai-skills.html`　`互動地圖`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep30-ai-skills.html
- 標題：AnythingLLM（NotebookLM 平替版）｜互動式學習地圖
- 內容簡述：EP30 晨學講堂：AnythingLLM（NotebookLM 平替版）——NotebookLM 簡報上傳新功能、AnythingLLM 是什麼與核心功能、安裝與設定、與 NotebookLM 怎麼選、應用情境，互動式多層次學習地圖
- 內容物（章節）：NotebookLM 新功能 ／ AnythingLLM 是什麼 ／ 安裝與設定 ／ 與 NotebookLM 怎麼選 ／ 應用情境
- 連到其他頁：ep29-notes.html, ep30-notes.html

### EP29
#### `ep29-notes.html`　`逐幀筆記`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep29-notes.html
- 標題：EP29 課堂筆記｜會議紀錄字幕工作流：從逐字稿到結構化 YAML 指令
- 內容簡述：晨學講堂 EP29 逐節課堂筆記：語音轉文字工具比較（Gemini／NotebookLM／Google AI Studio／雅婷／Word／Otter.ai）、逐字稿加時間戳、整理成問題與決策、會議紀錄生成、VTT 字幕製作（每段不超過3秒）、YouTube 字幕流程、NotebookLM 會議分析，以及後半段從一句提示詞升級到結構化 YAML 指令的五大應用，含官方簡報原圖與課堂逐字稿逐句佐證
- 內容物（章節）：0. 課程資訊與教材 ／ 1. 一頁看懂全課程 ／ 2. 語音轉文字工具比較 ／ 3. 錄音轉逐字稿＋時間戳 ／ 4. 逐字稿整理與會議紀錄生成 ／ 5. 字幕（VTT）生成與 YouTube 流程 ／ 6. NotebookLM 會議分析與自動化系統 ／ 7. 進階：從一句提示詞到結構化 YAML 指令 ／ 8. 課後自我檢核（照本集實際教學內容） ／ 9. 資料來源與製作說明
- 連到其他頁：ep29-ai-skills.html

#### `ep29-ai-skills.html`　`互動地圖`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep29-ai-skills.html
- 標題：會議紀錄字幕工作流｜互動式學習地圖
- 內容簡述：EP29 晨學講堂：會議紀錄字幕工作流——語音轉文字工具選擇、逐字稿產出與整理、會議紀錄生成、字幕(VTT)製作、NotebookLM 自動化工作流、結構化 YAML 指令五大應用，互動式多層次學習地圖
- 內容物（章節）：語音轉文字工具選擇 ／ 逐字稿產出與整理 ／ 會議紀錄生成 ／ 字幕（VTT）製作 ／ NotebookLM 與自動化工作流 ／ 結構化 YAML 指令
- 連到其他頁：ep29-notes.html

### EP28
#### `ep28-notes.html`　`逐幀筆記`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep28-notes.html
- 標題：EP28 課堂筆記｜文獻耙梳工具 AnswerThis
- 內容簡述：晨學講堂 EP28 課堂筆記：AnswerThis——以學術研究流程為核心的 AI 研究助理平台。核心特色、Tools（文獻回顧／學術搜尋／Chat with PDF／引用地圖）與 Agents（論文寫手／研究缺口發現器／改寫／同理心審稿）、Library 與 Citation Map，以及用 YAML 讓 AI 搜尋更精準。
- 內容物（章節）：0. 課程資訊與教材 ／ 1. AnswerThis 是什麼 ／ 2. 核心特色四項 ／ 3. 功能架構：Tools ／ Agents ／ 4. Tools 工具詳解 ／ 5. Agents 智能代理 ／ 6. Library 與 Citation Map ／ 7. 延伸：用 YAML 讓 AI 搜尋更精準 ／ 8. 重點整理（帶走這幾句） ／ 9. 資料來源與製作說明
- 連到其他頁：ep28-ai-skills.html, ep29-notes.html, ep39-notes.html

#### `ep28-ai-skills.html`　`互動地圖`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep28-ai-skills.html
- 標題：文獻耙梳工具 AnswerThis｜互動式學習地圖
- 內容簡述：EP28 晨學講堂：AnswerThis——AI 學術研究助理平台。核心特色、Tools（文獻回顧／學術搜尋／Chat with PDF／引用地圖）與 Agents（論文寫手／研究缺口發現器／改寫／同理心審稿）、Library 與 YAML 精準搜尋，互動式多層次學習地圖。
- 內容物（章節）：是什麼＋核心特色 ／ Tools 工具 ／ Agents 智能代理 ／ Library＋精準搜尋
- 連到其他頁：ep28-notes.html, ep29-notes.html, ep39-notes.html

### EP27
#### `ep27-notes.html`　`逐幀筆記`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep27-notes.html
- 標題：EP27 課堂筆記｜用 Prezi AI 做出動態簡報
- 內容簡述：晨學講堂 EP27 課堂筆記：Prezi——以縮放式視覺地圖為核心的非線性簡報工具。核心特色與適合情境、三大產品（Present／Video／Design）、Prezi vs PowerPoint、Prezi AI 信用點數、中文字體與關鍵功能（主題路徑、故事/動畫/星球主題、縮放技巧）。
- 內容物（章節）：0. 課程資訊與教材 ／ 1. Prezi 是什麼 ／ 2. 核心特色與適合情境 ／ 3. 三大產品 ／ 4. Prezi vs PowerPoint ／ 5. Prezi AI 需要多少信用點數 ／ 6. 中文字體與關鍵功能 ／ 7. 重點整理（帶走這幾句） ／ 8. 資料來源與製作說明
- 連到其他頁：ep27-ai-skills.html, ep34-notes.html, ep43-notes.html

#### `ep27-ai-skills.html`　`互動地圖`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep27-ai-skills.html
- 標題：用 Prezi AI 做出動態簡報｜互動式學習地圖
- 內容簡述：EP27 晨學講堂：Prezi——縮放式非線性簡報工具。是什麼＋核心特色、三大產品（Present／Video／Design）、Prezi vs PowerPoint＋AI 信用點數、中文字體與關鍵功能（主題路徑／內建主題／縮放技巧），互動式多層次學習地圖。
- 內容物（章節）：是什麼＋核心特色 ／ 三大產品 ／ vs PowerPoint＋AI 點數 ／ 中文字體與關鍵功能
- 連到其他頁：ep27-notes.html, ep34-notes.html, ep43-notes.html

### EP26
#### `ep26-notes.html`　`逐幀筆記`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep26-notes.html
- 標題：EP26 課堂筆記｜知行合一 Manus AI：Skill 與 Manus Agents
- 內容簡述：晨學講堂 EP26 課堂筆記：Manus AI 基礎操作與應用。Skill 技能包的元素與製作流程、Manus vs Claude Code 比較、用 skill-creator 實作「資訊圖表 Prompt 產生器」、官方技能庫與應用篇（Remotion／Manim）、Manus Agents 個人代理、傳統 Chatbot vs Agents、Telegram 用法與九大功能。
- 內容物（章節）：0. 課程資訊與教材 ／ 1. Skill 是什麼與元素 ／ 2. 剖析 Skill 製作流程 ／ 3. Manus vs Claude Code ／ 4. 實作：用 skill-creator 做「資訊圖表 Prompt 產生器」 ／ 5. 官方技能庫與應用篇 ／ 6. Manus Agents 個人代理 ／ 7. 傳統 Chatbot vs Manus Agents ／ 8. Manus Agents 的 Telegram 用法與九大功能 ／ 9. 重點整理（帶走這幾句） ／ 10. 資料來源與製作說明
- 連到其他頁：ep26-ai-skills.html, ep28-notes.html, ep39-notes.html

#### `ep26-ai-skills.html`　`互動地圖`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep26-ai-skills.html
- 標題：知行合一 Manus AI：Skill 與 Agents｜互動式學習地圖
- 內容簡述：EP26 晨學講堂：Manus AI 的 Skill 技能包與 Manus Agents 個人代理。Skill 元素與製作流程、Manus vs Claude Code、skill-creator 實作資訊圖表 Prompt 產生器、官方技能庫與應用篇、Manus Agents 與 Telegram 九大功能，互動式多層次學習地圖。
- 內容物（章節）：Skill 是什麼與元素 ／ 製作流程＋Manus vs Claude Code ／ 實作：資訊圖表 Prompt 產生器 ／ 官方技能庫與應用篇 ／ Manus Agents 與 Telegram
- 連到其他頁：ep26-notes.html, ep28-notes.html, ep39-notes.html

### EP25
#### `ep25-notes.html`　`逐幀筆記`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep25-notes.html
- 標題：EP25 課堂筆記｜用 YAML 讓簡報乖乖聽話：從規格到產出一次搞定
- 內容簡述：晨學講堂 EP25 課堂筆記：從手工挑模板到規格化控制模板、黃金公式（架構模組＋風格模組）、在 NotebookLM 建立自己的 YAML 資料庫、跨工具實測比較、素材蒐集小撇步。含真實影片截圖與逐字稿重點整理。
- 內容物（章節）：0. 課程資訊與教材 ／ 1. 開場：這堂課要練什麼 ／ 2. 從「手工挑模板」到「規格化控制模板」 ／ 3. 核心方法：黃金公式——架構模組與風格模組 ／ 4. 打造你自己的 YAML 資料庫（在 NotebookLM 建立筆記本） ／ 5. 把 YAML 規格拿到不同工具做測試比較 ／ 6. 素材蒐集小撇步＆整體邏輯總複習 ／ 7. 結語與社群資訊 ／ 8. 重點整理：快速回顧 EP25 ／ 9. 資料來源與製作說明
- 連到其他頁：ep25-ai-skills.html

#### `ep25-ai-skills.html`　`互動地圖`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep25-ai-skills.html
- 標題：用 YAML 讓簡報乖乖聽話：從規格到產出一次搞定｜互動式學習地圖
- 內容簡述：EP25 晨學講堂：從手工挑模板到規格化控制模板、黃金公式（架構模組＋風格模組）、在 NotebookLM 建立自己的 YAML 資料庫、跨工具實測比較、素材蒐集小撇步，互動式多層次學習地圖
- 內容物（章節）：手工挑模板 → 規格化控制 ／ 核心方法：黃金公式 ／ 打造你的 YAML 資料庫 ／ 跨工具實測＋素材蒐集
- 連到其他頁：ep25-notes.html

### EP24
#### `ep24-notes.html`　`逐幀筆記`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep24-notes.html
- 標題：EP24 課堂筆記｜從亂試到有策略：Meta AI 圖像生成這樣學最快
- 內容簡述：晨學講堂 EP24 課堂筆記：Meta AI 圖像生成——跨平台進入途徑、文字回應特色、與 Midjourney/Flux 的技術結合、結構化提示詞五法則、常見失敗診斷、六個生圖實戰案例。取材自課程筆記 Google Doc 與簡報 PDF，文字版完整整理。
- 內容物（章節）：0. 課程資訊與教材 ／ 1. Meta AI 是什麼：跨平台入口與三大核心功能 ／ 2. 怎麼開始使用：手機版與電腦版 ／ 3. 文字回應特色：來自社群大數據的「生活化視角」 ／ 4. 生圖引擎解密：與 Midjourney、Flux 的技術結合 ／ 5. 定位與適用情境：能做什麼、不能做什麼 ／ 6. 提示詞法則：結構與順序 ／ 7. 提示詞法則：失敗診斷 ／ 8. 可複用的方法：把生圖變成一套系統 ／ 9. 兩種 Prompt 模式：教學結構法 × 借力 Midjourney 生態 ／ 10. 影音能力延伸：向 Sora、即夢等生成式影片工具靠攏 ／ 11. 六個生圖案例實戰拆解 ／ 12. 重點整理：快速回顧 Meta AI 圖像生成 ／ 13. 資料來源與製作說明
- 連到其他頁：ep24-ai-skills.html

#### `ep24-ai-skills.html`　`互動地圖`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep24-ai-skills.html
- 標題：從亂試到有策略：Meta AI 圖像生成｜互動式學習地圖
- 內容簡述：EP24 晨學講堂：Meta AI 圖像生成——跨平台進入途徑、文字回應特色、與 Midjourney/Flux 技術結合、提示詞結構與順序法則、失敗診斷、可複用方法、兩種 Prompt 模式、影音延伸與六大案例，互動式多層次學習地圖
- 內容物（章節）：認識與進入 ／ 文字與生圖引擎 ／ 提示詞心法 ／ 影音延伸＋實戰案例
- 連到其他頁：ep24-notes.html

### EP23
#### `ep23-notes.html`　`逐幀筆記`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep23-notes.html
- 標題：EP23 課堂筆記｜用YAML讓您的NotebookLM資訊圖表乖乖聽話（含十個資訊圖表工具介紹）
- 內容簡述：晨學講堂 EP23 課堂筆記：用YAML讓NotebookLM等資訊圖表工具乖乖聽話——YAML核心概念、三大規則、標準製作流程與視覺規格、十個資訊圖表工具介紹（NotebookLM／AI Studio／Felo AI／Manus／Napkin AI／Dreamina AI等）、兩大生圖流派、常見痛點解法與老師的Pro Tips。內容取自課程筆記Google Doc與簡報PDF，文字整理，本集無簡
- 內容物（章節）：0. 課程資訊與教材 ／ 1. 為什麼資訊圖表要用 YAML：AI 的「資訊規格書」 ／ 2. YAML 只需要懂的三個規則 ／ 3. 標準製作流程與視覺規格 ／ 4. 十個資訊圖表工具詳解 ／ 5. AI 視覺化圖表的兩大流派 ／ 6. 解決 AI 生圖常見痛點：中文字與畫質 ／ 7. 老師的專家建議（Pro Tips） ／ 8. 重點整理：快速回顧 EP23 ／ 9. 資料來源與製作說明
- 連到其他頁：ep23-ai-skills.html

#### `ep23-ai-skills.html`　`互動地圖`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep23-ai-skills.html
- 標題：用YAML讓NotebookLM資訊圖表乖乖聽話｜互動式學習地圖
- 內容簡述：EP23 晨學講堂：用YAML讓資訊圖表乖乖聽話——YAML核心概念、三大規則、標準製作流程與視覺規格、十個資訊圖表工具介紹、兩大生圖流派、常見痛點解法與Pro Tips，互動式多層次學習地圖
- 內容物（章節）：核心概念：為什麼要用 YAML ／ YAML 只需要懂的三個規則 ／ 標準製作流程＋視覺規格 ／ 十個資訊圖表工具詳解 ／ 兩大生圖流派 ／ 痛點修正＋老師 Pro Tips
- 連到其他頁：ep23-notes.html

### EP21
#### `ep21-notes.html`　`逐幀筆記`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep21-notes.html
- 標題：EP21 課堂筆記｜讓數據會說話：AI 賦能的 Power BI × Looker Studio 視覺化實戰
- 內容簡述：晨學講堂 EP21 課堂筆記：從懶人一鍵生成到可互動儀表板；Power BI 與 Looker Studio 比較；模擬彩券資料的資料型態判讀；手把手拖曳做圖基本功；用 AI 技能自動化 Looker Studio 操作；Power BI 可寫程式的 AI 整合優勢。含真實課程截圖三張。
- 內容物（章節）：0. 課程資訊與教材 ／ 1. 開場：為什麼要做視覺化，不只是做表格 ／ 2. 兩大主流視覺化工具比較：Power BI vs Looker Studio ／ 3. 練習資料：模擬版全台頭獎投注彩券資料 ／ 4. 手把手基本功：先自己拖一次，再交給 AI ／ 5. 進階自動化：把「操作 Looker Studio」寫成一個 AI 技能（Skill） ／ 6. Power BI 與 AI 整合的優勢：可以直接寫程式 ／ 7. 結語與社群資訊 ／ 8. 資料來源與製作說明
- 連到其他頁：ep21-ai-skills.html

#### `ep21-ai-skills.html`　`互動地圖`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep21-ai-skills.html
- 標題：讓數據會說話：Power BI × Looker Studio｜互動式學習地圖
- 內容簡述：EP21 晨學講堂：為什麼要做視覺化、Power BI vs Looker Studio 比較、模擬彩券練習資料與型態判讀、手把手拖曳基本功、用 AI 技能自動化 Looker Studio、Power BI 可寫程式的優勢，互動式多層次學習地圖
- 內容物（章節）：為什麼要視覺化＋工具比較 ／ 練習資料＋拖曳基本功 ／ AI 技能自動化 ／ Power BI 進階＋結語
- 連到其他頁：ep21-notes.html

### EP20
#### `ep20-notes.html`　`逐幀筆記`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep20-notes.html
- 標題：EP20 課堂筆記｜打通 Anthropic 任督二脈：Claude 篇（含 Cowork 介紹及應用）
- 內容簡述：晨學講堂 EP20 課堂筆記：Claude 全功能整理——額度與隱私設定、深度思考與寫作風格、Artifacts／SVG、Connectors 連接器、Projects 與 Research、桌面版與 Chrome 擴充、Excel 與數據分析、官方 Skills 一覽。
- 內容物（章節）：0. 課程資訊與教材 ／ 1. 基礎設置與使用策略 ／ 2. 隱私與個人化配置 ／ 3. 深度思考與寫作風格 ／ 4. Claude Artifacts：視覺化與 SVG 生成 ／ 5. Connectors：把 Claude 連到你的資料與工具 ／ 6. Projects 專案功能與 Research 研究功能 ／ 7. 多端工具與瀏覽器擴充 ／ 8. Excel 與數據分析應用 ／ 9. 其他介面設定與官方 Skills 一覽 ／ 10. 重點整理：快速回顧 EP20 ／ 11. 資料來源與製作說明
- 連到其他頁：ep20-ai-skills.html

#### `ep20-ai-skills.html`　`互動地圖`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ep20-ai-skills.html
- 標題：打通 Anthropic 任督二脈：Claude 篇｜互動式學習地圖
- 內容簡述：EP20 晨學講堂：Claude 全功能整理——額度與隱私、深度思考與寫作風格、Artifacts／SVG、Connectors 連接器、Projects 與 Research、桌面版與 Chrome 擴充、Excel 與數據分析、官方 Skills 一覽，互動式多層次學習地圖
- 內容物（章節）：基礎設置與隱私 ／ 深度思考與寫作風格 ／ Artifacts：視覺化與 SVG ／ Connectors／Projects／Research ／ 多端工具與數據分析
- 連到其他頁：ep20-notes.html

---

## 三、SERIES 02 · 📚 Tarshar 教案集
對外授課的完整教案，每份為單頁 HTML。共 20 份（method 編號缺 06、14；06 對應 `build-knowledge-library.html`）。

#### `method-01-paper-translation.html`　`教案`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/method-01-paper-translation.html
- 標題：用 AI 把一篇英文論文變成你的研讀包｜Tarshar 教案集
- 內容簡述：Tarshar 教案集方法教案第一號：不是英文很好才能讀懂原文論文，是拆對三件事。記錄小D 用 AI 把一篇英文學術論文轉譯成研讀簡報、逐句中英對照、口語小抄三件套的完整做法，給零基礎研究生的方法教學
- 內容物（章節）：為什麼要做研讀包 ／ 三件套是什麼：一篇論文，三種用法 ／ 怎麼派 AI 逐段翻譯：不是整篇丟過去 ／ 中英對照的排版邏輯：眼睛要能一秒對上 ／ 口語小抄：跟教授報告用 ／ 驗收：抽段比對、術語一致 ／ 給你的三步驟行動建議：下一篇論文就能開始
- 外部連結：https://tarshar4242.github.io/thesis-library/

#### `method-02-frame-notes.html`　`教案`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/method-02-frame-notes.html
- 標題：一堂直播課，變成一座可以逛的互動筆記館｜Tarshar 教案集
- 內容簡述：Tarshar 教案集：逐幀課堂筆記法。記錄小D 怎麼用 AI 把一集直播課的錄影、簡報、逐字稿，變成一頁逐幀筆記＋一張互動節點地圖，再上架成一座隨時能逛的筆記館。給零基礎學員的方法教學
- 內容物（章節）：為什麼上完課，筆記還是散的 ／ 什麼叫「逐幀」：不是聽一遍抓重點 ／ 素材怎麼收：三樣東西缺一不可 ／ AI 怎麼把畫面變成一頁筆記 ／ 互動地圖是什麼：不是塞更多，是拆更細 ／ 上架與分享：改一個入口頁，全世界都看得到 ／ 給你的三步驟行動建議：下一堂課就能開始
- 外部連結：https://tarshar4242.github.io/kt-sweet-journey/ep45-notes.html, https://tarshar4242.github.io/kt-sweet-journey/lessons.html

#### `method-03-knowledge-cards.html`　`教案`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/method-03-knowledge-cards.html
- 標題：一個主題，怎麼變成一套圖卡，再變成一座網站｜Tarshar 教案集
- 內容簡述：Tarshar 教案集：記錄小D 怎麼把一個主題拆成一套知識圖卡，再把圖卡整理成一頁式線上展示館。從念頭拆解、卡片骨架、風格描述、命名版本、圖卡到網頁、歸檔分享六個章節，給零基礎學員的方法教學
- 內容物（章節）：為什麼是圖卡：一張卡一個念頭 ／ 一套圖卡的骨架：封面、內容卡、結尾卡 ／ 怎麼跟 AI 描述風格 ／ 命名與版本管理 ／ 從圖卡到展示館網頁 ／ 歸檔與分享：雲端資料夾怎麼放 ／ 給你的三步驟行動建議：明天就能開始
- 外部連結：https://tarshar4242.github.io/tar-webcard/

#### `method-04-doc-makeover.html`　`教案`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/method-04-doc-makeover.html
- 標題：樸素文件變身手帳風筆記，我怎麼做的｜Tarshar 教案集
- 內容簡述：Tarshar 教案集：規格書、Google 文件這些純文字稿，怎麼一步步變成牛皮紙配和紙膠帶的手帳風視覺版。記錄小D 盤點文件、先改一份當示範、確認風格再量產的完整做法，給零基礎學員的方法教學
- 內容物（章節）：為什麼文件需要視覺化 ／ 先定義你的視覺標準 ／ 盤點診斷：哪些文件不符合標準 ／ 先改一份當示範，不要一次全改 ／ 確認風格再量產 ／ 版本管理：改造版另存，不覆蓋原稿 ／ 量產階段：還在路上 ／ 給你的三步驟行動建議：明天就能開始

#### `method-05-ai-visuals.html`　`教案`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/method-05-ai-visuals.html
- 標題：用 AI 生成影片與視覺素材：從參考圖到提示詞的完整流程｜Tarshar 教案集
- 內容簡述：Tarshar 教案集：記錄小D 怎麼準備參考素材、寫生成提示詞，讓 AI 產出風格一致的影片與圖像。從缺參考錨點的問題、素材分類收集、原始影片抽格、提示詞結構、角色一致性到驗收挑選六個章節，給零基礎學員的方法教學
- 內容物（章節）：為什麼 AI 生圖總是不像你要的 ／ 參考素材怎麼準備：臉部、服飾、動作分開收 ／ 原始影片抽格，當你的動作字典 ／ 提示詞怎麼寫：描述＋參考＋禁止事項 ／ 角色一致性：固定設定檔的做法 ／ 產出驗收與挑選 ／ 給你的三步驟行動建議：明天就能開始

#### `build-knowledge-library.html`　`教案`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/build-knowledge-library.html
- 標題：我用 AI 幫論文蓋了一座圖書館｜Tarshar 教案集
- 內容簡述：Tarshar 教案集：不會寫程式，也能用 AI 蓋出自己的知識庫網站。記錄小D 零程式基礎，用 AI 蓋出論文研讀庫網站的完整做法，起點、架構、視覺設計、踩坑、搜尋功能、部署、工作流程七個章節，給零基礎學員的方法教學
- 內容物（章節）：起點：先有需求，才有工具 ／ 架構：資料夾就是你的設計圖 ／ 視覺設計：我說「淺綠文青風」，它真的懂 ／ 踩坑：白色區塊是怎麼來的？ ／ 搜尋功能：15 行程式碼 ／ 部署：從本機到全世界，只要三行指令 ／ 工作流程：我是怎麼跟 AI 協作的 ／ 給你的三步驟行動建議：明天就能開始
- 外部連結：https://tarshar4242.github.io/thesis-library/

#### `method-07-workshop-hub.html`　`教案`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/method-07-workshop-hub.html
- 標題：我用 AI 幫實體工作坊蓋了一個線上導覽台，還做了一個總站串起所有專案｜Tarshar 教案集
- 內容簡述：Tarshar 教案集：不會寫程式，也能用 AI 幫實體課蓋一個線上導覽台，再用總站把所有專案串起來。記錄小D 幫機關工作坊做導覽站、以及總站加子站架構的完整做法，給零基礎學員的方法教學
- 內容物（章節）：為什麼實體課需要一個線上導覽台 ／ 導覽台裡放什麼 ／ 怎麼請 AI 蓋出來 ／ 總站與子站的分工：一個專案一個站 ／ 新專案怎麼掛上去：持續累積的做法 ／ 維護與更新：改一個站，不影響其他站 ／ 給你的三步驟行動建議：明天就能開始
- 外部連結：https://tarshar4242.github.io/ai-kaiji-luzhou/, https://tarshar4242.github.io/tarshar-2026/

#### `method-08-browser-tools.html`　`教案`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/method-08-browser-tools.html
- 標題：不用後端、不用資料庫：用 AI 做一個跑在瀏覽器裡的小工具｜Tarshar 教案集
- 內容簡述：Tarshar 教案集：不會寫程式，也能用 AI 做出跑在瀏覽器裡的純前端小工具。記錄小D 做台股回測工具、QR code 產生器的完整做法，什麼是純前端、怎麼跟 AI 描述需求、怎麼串公開資料、怎麼部署分享，給零基礎學員的方法教學
- 內容物（章節）：什麼叫「純前端」小工具 ／ 什麼需求適合做成小工具 ／ 怎麼跟 AI 開口要一個工具 ／ 串公開資料：API 是什麼的白話版，台股回測實例 ／ 借現成的功能，不用自己重寫 ／ 部署分享：丟上 GitHub Pages 就是網址 ／ 工具箱思維：不是每個都能純前端到底 ／ 給你的三步驟行動建議：明天就能開始
- 外部連結：https://tarshar4242.github.io/give-me-money/, https://tarshar4242.github.io/renmei-qrcode-generator/

#### `method-09-pwa-app.html`　`教案`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/method-09-pwa-app.html
- 標題：我用 AI 做了一個裝在手機桌面的個人 App｜Tarshar 教案集
- 內容簡述：Tarshar 教案集：不會寫程式，也能用 AI 做出一個裝在手機桌面、離線可用、雲端同步的個人 App。記錄小D 從一個學英文的困擾開始，做出自己的英文學習 App 的完整過程，六個章節加行動建議，給零基礎學員的方法教學
- 內容物（章節）：為什麼要自己做一個 App ／ 什麼是「加到手機桌面」的網頁 ／ 需求怎麼講給 AI 聽 ／ 離線優先：沒網路也要能用 ／ 雲端同步：換手機、換裝置，進度不會不見 ／ 老實說，這關比前幾篇難一點 ／ 給你的三步驟行動建議：明天就能開始
- 外部連結：https://tarshar4242.github.io/lingua-buddy/

#### `method-10-worksys-courage.html`　`教案`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/method-10-worksys-courage.html
- 標題：我不是工程師，但我最懂這條流程｜Tarshar 教案集
- 內容簡述：Tarshar 教案集：非工程師也能用 AI 把自己最熟的工作流程做成系統雛形。記錄小D 在製造業繞了一圈的經歷，怎麼用六個資料夾、一次次重來，把進料、品檢、報工這些日常流程做成看得見的網頁雛形。不教技術，教方法與敢重來的勇氣。
- 內容物（章節）：我最懂的不是程式，是這條流程 ／ 第一版很醜，沒關係 ／ 怎麼把流程講給 AI 聽 ／ 六個資料夾，不是每次重來都成功 ／ 雛形能幹嘛：讓別人看到你腦子裡在想什麼 ／ 界線：雛形不是正式系統 ／ 給你的三步驟行動建議：明天就能開始

#### `method-11-report-to-web.html`　`教案`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/method-11-report-to-web.html
- 標題：工具吐出來的分析報告，我讓它變成手機一頁看完的網頁｜Tarshar 教案集
- 內容簡述：Tarshar 教案集：非工程師也能把工具自動產出的分析報告，變成一頁手機能滑完、還能分享出去的網頁。記錄小D 把 Claude Code 的使用洞察報告，翻成中文、重新編排、部署成網址的完整做法，方法教案 #11。
- 內容物（章節）：痛點：報告是給工程師看的 ／ 報告裡其實藏著故事 ／ 怎麼請 AI 重新編排 ／ 手機可讀的排版原則 ／ 部署成可分享網址 ／ 這招用在哪些報告都行 ／ 我沒有全部照單全收 ／ 給你的三步驟行動建議：明天就能開始
- 外部連結：https://tarshar4242-rgb.github.io/claude-code-insights/

#### `method-12-digital-staff.html`　`教案`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/method-12-digital-staff.html
- 標題：幫自己請一個 AI 數位員工，甚至一整支團隊｜Tarshar 教案集
- 內容簡述：Tarshar 教案集：不是多請一個人，是把你的做法寫成一個人。記錄小D 打造 AI 數位員工的完整做法，從定義角色、交辦任務、自動循環到驗證交付，附兩個真實案例：一位自動整理直播資料的數位員工，和一支一位總管帶四位專員的 AI 行銷團隊。
- 內容物（章節）：什麼是數位員工：不是聊天機器人，是有職務說明書的 AI ／ 先定義員工，不是先丟工具：寫一份職務說明書 ／ 一則公告，就是它的工作單：怎麼交辦任務 ／ 只補新增，舊檔永遠保留：讓它自動完成整個循環 ／ 做完不算完成，驗證才算交付 ／ 從一個人到一支團隊：一位總管，分工協作 ／ 給你的三步驟行動建議：明天就能開始

#### `method-13-content-pipeline.html`　`教案`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/method-13-content-pipeline.html
- 標題：從 0 到 1 架一條自動化內容生產線：以我的電子報為例｜Tarshar 教案集
- 內容簡述：Tarshar 教案集：從 0 到 1 架一條自動化內容生產線，以我的電子報為例。記錄小D 零程式基礎，怎麼選工具、開刊、發創刊號、設定每週自動產草稿，自己只做最後過目與發布。教的不是寫一篇內容，是搭一條會自己跑的生產線。
- 內容物（章節）：為什麼內容經營總是斷更：靠意志力必輸 ／ 選工具的判準：免費、簡單、名單握在自己手上 ／ 創刊號怎麼生：標題給選項，草稿 AI 先寫，我做最後定稿 ／ 封面圖的品牌一致性：固定風格範本，不用每次重新想 ／ 排程自動化：每週自動產草稿，我只做過目 ／ 人的位置：AI 產，人審，絕不全自動發布 ／ 給你的三步驟行動建議：明天就能開始

#### `method-15-second-brain.html`　`教案`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/method-15-second-brain.html
- 標題：幫自己搭一個 AI 第二大腦：任務總帳＋個人知識庫｜Tarshar 教案集
- 內容簡述：Tarshar 教案集：記錄小D 怎麼用一個任務總帳資料庫當單一事實來源，讓 AI 自動登記與更新任務，再建一座個人知識庫存放脈絡，並定期稽核排程抓重複整併。給非工程師的方法教學。
- 內容物（章節）：任務派出去就追不到，是我最痛的地方 ／ 單一事實來源：一個總帳，不要五個清單 ／ 讓 AI 自己記帳，不等我開口 ／ 知識庫怎麼分區：我的圖書館長什麼樣子 ／ 定期稽核抓重複：排程整併的真實案例 ／ 誠實談維護成本：不整理就長成垃圾山 ／ 給你的三步驟行動建議：明天就能開始

#### `method-16-decision-brake.html`　`教案`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/method-16-decision-brake.html
- 標題：想做一個大系統之前，先讓 AI 幫你踩剎車｜Tarshar 教案集
- 內容簡述：Tarshar 教案集方法教案第16篇：記錄小D 曾經想蓋一個大系統、規格書都寫好了，最後請 AI 先評估再動工的真實過程。從規格書的衝動、痛點與解法分開看、把成本攤在陽光下、問 AI 那個關鍵問題，到最後改走輕量方案照樣解決痛點，六個章節加行動三步。
- 內容物（章節）：規格書寫得越漂亮，越危險 ／ 先確認痛點是不是真的 ／ 把成本攤在陽光下 ／ 問 AI 那個關鍵問題 ／ 輕量方案長什麼樣 ／ 什麼時候該做重的 ／ 給你的三步驟行動建議：下次動工前先做這件事

#### `method-17-job-application.html`　`教案`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/method-17-job-application.html
- 標題：AI 陪跑求職：把真的你，講給公部門聽｜Tarshar 教案集
- 內容簡述：Tarshar 教案集：用 AI 陪跑準備一次公部門職缺應徵資料的完整做法，從急件清單、自傳草稿、履歷補強、官方表格對照到送件前核對，六段真實走過的路，特別適合中高齡、二度就業、要投公部門或培訓案的人
- 內容物（章節）：投遞公部門最怕漏東西 ／ 先列急件清單：AI 幫你從公告揪出要交什麼、缺什麼 ／ 自傳不是自誇文：讓 AI 訪談你，把經歷變成故事 ／ 履歷補強：把新技能寫進去的方法 ／ 官方表格對照：AI 幫你逐欄核對格式 ／ 送件前核對清單：防漏的三次檢查 ／ 給你的三步驟行動建議：明天就能開始

#### `method-18-batch-screening.html`　`教案`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/method-18-batch-screening.html
- 標題：一百多篇論文，AI 幫你一天篩完：批次文獻篩選法｜Tarshar 教案集
- 內容簡述：Tarshar 教案集：不是讀得快，是先知道哪些不用讀。記錄小D 用 AI 一天篩完一整場學術研討會 164 篇論文的做法，從定義相關性標準、批次處理、總表產出到人的把關位置，給非工程師的文獻初篩方法
- 內容物（章節）：一百多篇論文的絕望感 ／ 先講清楚什麼叫「相關」 ／ 分批餵、逐篇判：批次處理怎麼跑 ／ 總表：一張表看到全部 ／ 人在哪裡：AI 初篩，人把關 ／ 這招不是只能篩論文 ／ 給你的三步驟行動建議：明天就能開始

#### `claim-companion.html`　`教案`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/claim-companion.html
- 標題：理賠陪跑主題館｜Learn AI with Tarshar
- 內容簡述：一位陪你一步一步做的教練。從查醫療紀錄、找保單、遮個資，到用 AI 整理、正式申請理賠，手機拿在手上跟著做就好。本平台不儲存、不經手任何個人資料。
- 內容物（章節）：🌿 先給你一個安心承諾 ／ 你想問的，這裡先回答

#### `voice-to-notes.html`　`教案`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/voice-to-notes.html
- 標題：地端 AI 語音轉紀錄 · 教案
- 內容簡述：一份音檔，自動變成你要的紀錄。全程在自己電腦上離線運算、免費、資料不外流——會議記錄、課堂筆記、論文Meeting、演講摘要一鍵完成。教學用教案。
- 內容物（章節）：1它解決什麼問題？ ／ 2它怎麼運作？三步驟 ／ 3不只會議記錄——五大分群、16 種紀錄 ／ 4看實際成品 ／ 5怎麼開始用？ ／ 6給講師的教學重點
- 連到其他頁：sample-lecture.html, sample-project.html, sample-talk.html, sample-thesis.html

#### `luzhou-ai-startup.html`　`教案`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/luzhou-ai-startup.html
- 標題：AI 開機日．蘆洲監理所｜教案
- 內容簡述：Tarshar 教案集：AI 開機日．蘆洲監理所——兩小時公部門 AI 體驗工作坊，起承轉合教學流程、四大秘訣、進階帶回家 11 招，含完整簡報與學員講義
- 內容物（章節）：0. 教案資訊與教材 ／ 1. 一頁看懂這堂課 ／ 2. 教學流程（起承轉合） ／ 3. 四大秘訣心法（小美用的就是這四招） ／ 4. 進階帶回家 11 招（P27–41） ／ 5. 金句與收尾 ／ 6. 完整簡報與學員講義

---

## 四、SERIES 03 · 🧰 生活應用
課堂之外的實作成品，每件為獨立作品頁。共 5 件。

#### `admin-assistant.html`　`作品`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/admin-assistant.html
- 標題：行政助手｜LINE 訊息自動變行程
- 內容簡述：LINE 訊息（連截圖）丟給它，AI 自動讀懂、寫進試算表、排進 Google 日曆、時間到主動提醒——含完整程式碼與小白安裝教學，全部免費工具。
- 內容物（章節）：在 LINE 傳訊息 ／ 連客戶的截圖都能讀 ／ 它自動讀懂你的話 ／ 自動建到 Google 日曆 ／ 它回你一張確認卡 ／ 🧺 要準備的材料 ／ 🔧 動手做（約 30 分鐘） ／ 📜 完整程式碼 ／ 💬 可以這樣跟它說 ／ 🙋 卡住了？先看這裡

#### `graduate-daily-thinking.html`　`作品`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/graduate-daily-thinking.html
- 標題：研究生的日常思維・生圖指令包 | 🍀 Learn AI with Tarshar
- 內容簡述：研究生的日常思維・生圖指令包：文獻閱讀、筆記與知識管理、寫作與輸出、心態與節奏四大類，共 32 組 YAML 結構化生圖咒語，點擊即可複製貼給 AI 生圖。
- 內容物（章節）：A📖 文獻閱讀思維 ／ B🗂️ 筆記與知識管理思維 ／ C✍️ 寫作與輸出思維 ／ D🧘 心態與節奏思維

#### `kt-sweet-journey.html`　`作品`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/kt-sweet-journey.html
- 標題：K&T 甜蜜日之旅 🌸 箱根・鎌倉・東京 2026
- 內容物（章節）：🚦 交通接駁執行清單 ／ 💰 已確認基本旅費明細
- 連到其他頁：interpreter.html

#### `interpreter.html`　`作品`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/interpreter.html
- 標題：隨身口譯機 🎙 K&T 甜蜜日之旅
- 內容物（章節）：⚙️ 設定

#### `suntory-visit-report.html`　`作品`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/suntory-visit-report.html
- 標題：泡沫上的科技，水裡的匠心｜三得利武蔵野啤酒工場參訪學習日誌
- 內容物（章節）：清晨，從府中市場走來 ／ 水と生きる：先講水，再講酒 ／ 從天然水，到一杯神泡 ／ 我看見的，不是啤酒 ／ 把永續，落到很具體的地方 ／ 隱性知識外顯化的兩種命運 ／ 我看的是啤酒，想的是研究

---

## 五、SERIES 04–06 · 單頁／外站直達

#### `ipas-intermediate.html`　`單頁學習`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/ipas-intermediate.html
- 標題：iPAS AI 應用規劃師中級｜Learn AI with Tarshar
- 內容簡述：iPAS AI 應用規劃師中級：三科 34 個能力單元、30 天讀書路線、白話比喻與本機學習進度。
- 內容物（章節）：自然語言處理技術與應用 ／ 三科學習地圖 ／ Obsidian 式知識節點圖 ／ 30 天每日陪跑 ／ 最適合你的四步學習法
- 外部連結：https://ipas-intermediate-learning.tarshar4242.chatgpt.site
- 備註：SERIES 04：首頁卡片以 location.href 直接進入，無第二層

**SERIES 05 論文研讀庫**（外站，另一 repo `thesis-library`）：https://tarshar4242.github.io/thesis-library/index.html#library

**SERIES 06 SKILL 技能包**（外站，另一 repo `thesis-library`）：https://tarshar4242.github.io/thesis-library/skills.html

---

## 六、SERIES 07 · 📮 主題式電子報
每期一頁 edm-NNN.html，最新在前。共 1 期。

#### `edm-001.html`　`電子報`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/edm-001.html
- 標題：電子報 001｜會議記錄我不聽打了
- 內容簡述：主題式電子報第一期：把散會後那一小時外包給自己家的電腦。地端 AI 語音轉紀錄，離線、免費、資料不外流。
- 內容物（章節）：😮‍💨先講一個我很討厭的時刻 ／ 🔒我要的不只是「能轉錄」 ／ ✋我只做一個動作 ／ 🗝️我在這裡藏了一個原理 ／ 📚現在它能跑出什麼 ／ ⚖️我做過的兩個取捨 ／ 🚀下一步 ／ 💬想跟你說的一句話 ／ 🍀關於我
- 連到其他頁：voice-to-notes.html

---

## 七、系統頁／未掛入系列動線的頁面
以下頁面存在於 repo，但不在首頁系列卡的點擊動線內（系統頁、範例頁），列出供完整性參考。

#### `404.html`　`系統／範例`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/404.html
- 標題：找不到頁面｜Learn AI with Tarshar
- 連到其他頁：/kt-sweet-journey/lessons.html

#### `index.html`　`系統／範例`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/index.html
- 標題：Learn AI with Tarshar｜課程筆記館
- 連到其他頁：interpreter.html, kt-sweet-journey.html

#### `sample-lecture.html`　`系統／範例`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/sample-lecture.html
- 標題：金融科技課程：股票與期貨交易實務
- 內容物（章節）：⚡一句話總覽 ／ 🧠知識地圖 ／ •核心觀念 ／ 📚完整課堂實錄（整理版） ／ 💬老師金句 ／ 📖名詞白話對照 ／ ☑️課後延伸與待複習

#### `sample-project.html`　`系統／範例`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/sample-project.html
- 標題：官網改版專案　週會
- 內容物（章節）：📊專案儀表板 ／ ✅行動項 Action Items ／ 📚完整會議實錄（整理版） ／ •本次進度更新 ／ 📈里程碑時程 ／ 🎯風險與議題

#### `sample-talk.html`　`系統／範例`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/sample-talk.html
- 標題：AI 時代的個人品牌經營
- 內容物（章節）：⚡三句話重點 ／ •核心論點 ／ •我可以怎麼用（行動建議） ／ 📚完整演講實錄（整理版） ／ 💬金句摘錄 ／ ⏱️章節時間軸

#### `sample-thesis.html`　`系統／範例`
- 網址：https://tarshar4242.github.io/kt-sweet-journey/sample-thesis.html
- 標題：論文第三章　研究方法討論
- 內容物（章節）：•教授回饋與指正 ／ ☑️待修改清單 ／ •下次進度目標 ／ 📚完整討論實錄（整理版） ／ •本次討論重點 ／ •文獻與方法建議 ／ •要向教授拍板的問題

---

## 八、命名規則與編號缺口
- `epNN-notes.html` / `epNN-ai-skills.html`：直播電台第 NN 集的「筆記頁 / 地圖頁」；`epNNb`＝同集加課（目前僅 EP41b）。
- `method-NN-<slug>.html`：教案集方法教案第 NN 號。
- `edm-NNN.html`：主題式電子報第 NNN 期。
- `<slug>.html`（無數字前綴）：獨立作品／單頁（如 kt-sweet-journey、interpreter、ipas-intermediate）。
- **編號缺口（非遺漏，本就跳號）**：直播電台缺 **EP22**；教案 method 缺 **06**（其位置由 `build-knowledge-library.html` 承接）、**14**。

## 九、維護規則（新增內容時怎麼改）
- **新增一集直播**：`#view-radio` 最前插入 course 卡（連 `epNN-notes.html`＋`epNN-ai-skills.html`）；兩頁互放連結。
- **新增教案／作品／電子報**：分別插入 `#view-plans`／`#view-life`／`#view-edm` 最前。
- **新增『兩層』系列**：`#view-home` 加系列卡＋新增 `#view-<key>` 區塊，並在 JS `SERIES_META` 補標題與副標。
- **新增『單頁直達』系列**（如 iPAS）：系列卡用 `onclick="location.href='<page>.html'"`，不需第二層；但**目錄模式**要在 JS `TOC_SERIES` 補一列。
- **首頁計數（badge / count）由 JS 自動計算**（掃 `.course:not(.soon)` 數量）；HTML 內寫死的「收錄 N 集」為佔位字，**不需手改**。
- **各頁回入口**用 `lessons.html#radio`／`#plans`／`#life`／`#edm`（直達系列）。
- **推 main 前**先 `git fetch origin main`；若 origin 已前進就 rebase 並保留他人新增的系列/卡片（勿覆蓋）。

## 十、反向索引（檔名 → 用途 → 所屬系列）

| 檔名 | 用途 | 所屬系列 |
|---|---|---|
| `404.html` | 系統／範例 | （未掛入動線） |
| `admin-assistant.html` | 作品 | SERIES 03 生活應用 |
| `build-knowledge-library.html` | 教案 | SERIES 02 教案集 |
| `claim-companion.html` | 教案 | SERIES 02 教案集 |
| `edm-001.html` | 電子報 | SERIES 07 電子報 |
| `ep20-ai-skills.html` | 互動地圖 | SERIES 01 直播電台 |
| `ep20-notes.html` | 逐幀筆記 | SERIES 01 直播電台 |
| `ep21-ai-skills.html` | 互動地圖 | SERIES 01 直播電台 |
| `ep21-notes.html` | 逐幀筆記 | SERIES 01 直播電台 |
| `ep23-ai-skills.html` | 互動地圖 | SERIES 01 直播電台 |
| `ep23-notes.html` | 逐幀筆記 | SERIES 01 直播電台 |
| `ep24-ai-skills.html` | 互動地圖 | SERIES 01 直播電台 |
| `ep24-notes.html` | 逐幀筆記 | SERIES 01 直播電台 |
| `ep25-ai-skills.html` | 互動地圖 | SERIES 01 直播電台 |
| `ep25-notes.html` | 逐幀筆記 | SERIES 01 直播電台 |
| `ep26-ai-skills.html` | 互動地圖 | SERIES 01 直播電台 |
| `ep26-notes.html` | 逐幀筆記 | SERIES 01 直播電台 |
| `ep27-ai-skills.html` | 互動地圖 | SERIES 01 直播電台 |
| `ep27-notes.html` | 逐幀筆記 | SERIES 01 直播電台 |
| `ep28-ai-skills.html` | 互動地圖 | SERIES 01 直播電台 |
| `ep28-notes.html` | 逐幀筆記 | SERIES 01 直播電台 |
| `ep29-ai-skills.html` | 互動地圖 | SERIES 01 直播電台 |
| `ep29-notes.html` | 逐幀筆記 | SERIES 01 直播電台 |
| `ep30-ai-skills.html` | 互動地圖 | SERIES 01 直播電台 |
| `ep30-notes.html` | 逐幀筆記 | SERIES 01 直播電台 |
| `ep31-ai-skills.html` | 互動地圖 | SERIES 01 直播電台 |
| `ep31-notes.html` | 逐幀筆記 | SERIES 01 直播電台 |
| `ep32-ai-skills.html` | 互動地圖 | SERIES 01 直播電台 |
| `ep32-notes.html` | 逐幀筆記 | SERIES 01 直播電台 |
| `ep33-ai-skills.html` | 互動地圖 | SERIES 01 直播電台 |
| `ep33-notes.html` | 逐幀筆記 | SERIES 01 直播電台 |
| `ep34-ai-skills.html` | 互動地圖 | SERIES 01 直播電台 |
| `ep34-notes.html` | 逐幀筆記 | SERIES 01 直播電台 |
| `ep35-ai-skills.html` | 互動地圖 | SERIES 01 直播電台 |
| `ep35-notes.html` | 逐幀筆記 | SERIES 01 直播電台 |
| `ep36-ai-skills.html` | 互動地圖 | SERIES 01 直播電台 |
| `ep36-notes.html` | 逐幀筆記 | SERIES 01 直播電台 |
| `ep37-ai-skills.html` | 互動地圖 | SERIES 01 直播電台 |
| `ep37-notes.html` | 逐幀筆記 | SERIES 01 直播電台 |
| `ep38-ai-skills.html` | 互動地圖 | SERIES 01 直播電台 |
| `ep38-notes.html` | 逐幀筆記 | SERIES 01 直播電台 |
| `ep39-ai-skills.html` | 互動地圖 | SERIES 01 直播電台 |
| `ep39-notes.html` | 逐幀筆記 | SERIES 01 直播電台 |
| `ep40-ai-skills.html` | 互動地圖 | SERIES 01 直播電台 |
| `ep40-notes.html` | 逐幀筆記 | SERIES 01 直播電台 |
| `ep41-ai-skills.html` | 互動地圖 | SERIES 01 直播電台 |
| `ep41-notes.html` | 逐幀筆記 | SERIES 01 直播電台 |
| `ep41b-ai-skills.html` | 互動地圖 | SERIES 01 直播電台 |
| `ep41b-notes.html` | 逐幀筆記 | SERIES 01 直播電台 |
| `ep42-ai-skills.html` | 互動地圖 | SERIES 01 直播電台 |
| `ep42-notes.html` | 逐幀筆記 | SERIES 01 直播電台 |
| `ep43-ai-skills.html` | 互動地圖 | SERIES 01 直播電台 |
| `ep43-notes.html` | 逐幀筆記 | SERIES 01 直播電台 |
| `ep44-ai-skills.html` | 互動地圖 | SERIES 01 直播電台 |
| `ep44-notes.html` | 逐幀筆記 | SERIES 01 直播電台 |
| `ep45-ai-skills.html` | 互動地圖 | SERIES 01 直播電台 |
| `ep45-notes.html` | 逐幀筆記 | SERIES 01 直播電台 |
| `ep46-ai-skills.html` | 互動地圖 | SERIES 01 直播電台 |
| `ep46-notes.html` | 逐幀筆記 | SERIES 01 直播電台 |
| `graduate-daily-thinking.html` | 作品 | SERIES 03 生活應用 |
| `index.html` | 系統／範例 | （未掛入動線） |
| `interpreter.html` | 作品 | SERIES 03 生活應用 |
| `ipas-intermediate.html` | 單頁學習 | SERIES 04 iPAS |
| `kt-sweet-journey.html` | 作品 | SERIES 03 生活應用 |
| `lessons.html` | 入口首頁 | — |
| `luzhou-ai-startup.html` | 教案 | SERIES 02 教案集 |
| `method-01-paper-translation.html` | 教案 | SERIES 02 教案集 |
| `method-02-frame-notes.html` | 教案 | SERIES 02 教案集 |
| `method-03-knowledge-cards.html` | 教案 | SERIES 02 教案集 |
| `method-04-doc-makeover.html` | 教案 | SERIES 02 教案集 |
| `method-05-ai-visuals.html` | 教案 | SERIES 02 教案集 |
| `method-07-workshop-hub.html` | 教案 | SERIES 02 教案集 |
| `method-08-browser-tools.html` | 教案 | SERIES 02 教案集 |
| `method-09-pwa-app.html` | 教案 | SERIES 02 教案集 |
| `method-10-worksys-courage.html` | 教案 | SERIES 02 教案集 |
| `method-11-report-to-web.html` | 教案 | SERIES 02 教案集 |
| `method-12-digital-staff.html` | 教案 | SERIES 02 教案集 |
| `method-13-content-pipeline.html` | 教案 | SERIES 02 教案集 |
| `method-15-second-brain.html` | 教案 | SERIES 02 教案集 |
| `method-16-decision-brake.html` | 教案 | SERIES 02 教案集 |
| `method-17-job-application.html` | 教案 | SERIES 02 教案集 |
| `method-18-batch-screening.html` | 教案 | SERIES 02 教案集 |
| `sample-lecture.html` | 系統／範例 | （未掛入動線） |
| `sample-project.html` | 系統／範例 | （未掛入動線） |
| `sample-talk.html` | 系統／範例 | （未掛入動線） |
| `sample-thesis.html` | 系統／範例 | （未掛入動線） |
| `suntory-visit-report.html` | 作品 | SERIES 03 生活應用 |
| `voice-to-notes.html` | 教案 | SERIES 02 教案集 |

---

## 十一、統計（本快照）
- 入口頁 `lessons.html`：**1 頁**
- 直播電台：27 集 × 2 頁 = **54 頁**
- 教案集：**20 頁** ／ 生活應用：**5 頁** ／ 電子報：**1 頁** ／ iPAS 單頁：**1 頁**
- 系統／範例頁：**6 頁**（404.html, index.html, sample-lecture.html, sample-project.html, sample-talk.html, sample-thesis.html）
- **分項加總：1＋54＋20＋5＋1＋1＋6 = 88 頁**（＝ repo 實際 88 頁 ✓）
- 外站系列（不計入本站頁數）：論文研讀庫、SKILL 技能包（`thesis-library` repo）