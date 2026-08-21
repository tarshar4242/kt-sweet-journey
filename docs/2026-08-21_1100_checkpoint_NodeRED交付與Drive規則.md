# 對話檢查點｜2026-08-21 11:00｜Node-RED 交付結案：系列不用搬、PDF 已交、Drive 規則補進 SKILL.md

> 🔄 **本文件是對話接力棒**
> 產出時間：2026-08-21 11:00
> 對話主題：接手 08-20 那份 Node-RED 接力棒的兩件未完成事項
> 進度狀態：**兩件都結案**，Tarshar 說「完工」。目前沒有未完成的接手任務。
> ⚠️ **接手第一件事：08-20 那份接力棒的「未完成二」已經作廢，不要照著做**（見第 2 節）

---

## 1. Tarshar 的原始問題與需求

**第 1 輪**
> 照接力棒繼續

（當下 repo 裡最新的接力棒是 `docs/接力棒-2026-08-19b.md`，但它已結案。追問後她說「有新的接力棒還沒給你」。）

**第 2 輪**
上傳 `20260820_0730_checkpoint_NodeRED_______.md`，即 08-20 那份接力棒，內容是兩件未完成事項：
Drive 沒上傳、系列放錯。

**第 3 輪**（回答三個確認題，見第 3 節）

**第 4 輪**
> 完工

---

## 2. Tarshar 的思考與顧慮

**⚠️ 最重要的一條：「直播筆記」是誤判，系列不用搬**

08-20 那份接力棒把她說的「他要幫我放在我的網站的直播筆記裡面」判讀成
「要從 📦 訂閱制課程搬到 📻 直播電台」，並列為「未完成二」，交代接手的 Claude 去搬四個 HTML
的內文、回入口連結與卡片前綴。

**這次直接問她，她選了「📦 訂閱制課程（維持現狀）」。** 所以：
- 四個 HTML 一個字都不用改，`lessons.html` 的卡片位置本來就是對的
- 那份接力棒第 5 節的「未完成二」整段作廢
- 教訓延續前一棒的觀察：**她口語講的系列名稱不等於網站上的系列 key，一定要問過才動**

**她要的交付格式是 PDF**：問她時我先講明「HTML 原檔放 Drive 不能線上瀏覽、點了只會下載，
而且筆記裡的圖片是 GitHub 相對路徑、離開網站會破圖」，她據此選 PDF（不是 PDF＋HTML 兩份，
也不是只放連結清單）。

**她同意把漏掉的步驟寫進規則**：她記得「SKILL 有說要存到我指定的資料夾」，但 SKILL.md 全文確實沒有。
這次她拍板「補進去」，所以規則與實作的落差已經補平。

---

## 3. 關鍵決策與理由

| 決策項目 | 選了什麼 | 為什麼 | 現況 |
|---|---|---|---|
| 系列歸屬 | **維持 📦 訂閱制課程** | 她直接拍板；上一棒的「搬去直播電台」是誤判 | ✅ 網站不用動 |
| Drive 交付格式 | **PDF** | HTML 放 Drive 不能線上看、圖片會破 | ✅ 四份已產出 |
| PDF 怎麼進 Drive | **SendUserFile 傳給她，她自己拖進資料夾** | MCP `create_file` 塞不下幾 MB 的 base64，且會跳核准 | ✅ 已交檔 |
| 補規則 | **補進 SKILL.md＋CLAUDE.md** | 她記得有這條但檔案沒寫，下次才不會再漏 | ✅ 已上 main |
| 互動地圖列印 | 注入 CSS 攤平後才印 | 直接印只印得到首頁五張章節卡 | ✅ 17／19 頁完整 |
| `.topic` 是否 `break-inside:avoid` | **不設** | 設了會變成一個技能佔一頁、下半頁全空 | ✅ 第一版印壞、已修正 |

---

## 4. 已完成的工作

**四份 PDF（已用 SendUserFile 交給她）**

| 檔名 | 頁數 | 來源 |
|---|---|---|
| `Node-RED研習營(I)｜課堂筆記.pdf` | 16 頁 | `nodered1-notes.html` |
| `Node-RED研習營(I)｜互動學習地圖.pdf` | 17 頁 | `nodered1-ai-skills.html` |
| `Node-RED研習營(II)｜課堂筆記.pdf` | 20 頁 | `nodered2-notes.html` |
| `Node-RED研習營(II)｜互動學習地圖.pdf` | 19 頁 | `nodered2-ai-skills.html` |

轉檔腳本在 scratchpad 的 `topdf.js`（容器回收就沒了，做法已寫進 SKILL.md，照著寫得回來）。
產出後有實際把 PDF 轉成 PNG 逐頁看過再交件，不是只看檔案大小。

**規則更新（commit `82ce984`，已合併 main）**
- `.claude/skills/lecture-notes-site/SKILL.md` 第 4 步新增第 5 點：交付到指定 Drive 資料夾，
  含格式（PDF）、轉檔要注入哪些 CSS、檔名慣例、以及 MCP 傳不動大檔的實測限制
- `CLAUDE.md` 常設授權段新增對應的觸發層規則

---

## 5. 進行中 / 未完成的工作

📍 **沒有未完成的接手任務。**

唯一還在她手上的動作：把四份 PDF 拖進「第三季」資料夾
（`1LSPX3vXbJ3oCscttTpsQacClbcSNL1f4`）。這件事機器做不到，不是卡住，是分工。

---

## 6. 待確認的問題

- ❓ **四個頁面的內容她還沒驗收過。** 她從頭到尾只處理「放哪裡」與「交付格式」，
  節點觀念、三層變數、Codex 把 HTML 變成節點、`find is not a function` 除錯那幾段，
  她都還沒說看過。這次問她要不要挑一節先看，她回「完工」，等於暫時不看。→ **未答，可日後再提**

---

## 7. 已建立的規則與約定

- ✅ **逐幀筆記做完要轉 PDF 交付到指定 Drive 資料夾**（正本 SKILL.md 第 4 步第 5 點，
  觸發層在 CLAUDE.md）。上架網站不等於交付完成。
- ✅ **互動地圖轉 PDF 前必須注入 CSS 攤平**：`.view{display:block!important}`、
  `.topic-body{max-height:none!important;overflow:visible!important}`，並補 `open`／`active` class；
  隱藏 `.topbar,nav.toc,.crumbs,.chapnav,.searchbox,.iframe-wrap`。不做這步只印得到首頁。
- ✅ **`.topic` 不要設 `break-inside:avoid`**：會讓每個技能各佔一頁、下半頁全空。
- ✅ **Drive MCP 傳不動幾 MB 的檔案**：`create_file` 只吃行內 base64／文字，一份 4MB 的 PDF
  編碼後約 5.5MB，遠超過單次工具呼叫塞得下的量；寫入還會跳 `requires approval`。
  這是工具限制，不是網路被擋，硬試不會成功 → 走 SendUserFile。
- ✅ **接力棒裡的判讀不等於事實**：上一棒把「直播筆記」寫成待辦的搬遷任務，實際問過才知道不用搬。
  接手時對「上一棒推測、未經她確認」的項目要先問，別直接執行。

---

## 8. 給下一個 Claude 的提醒

**先看清楚 08-20 那份接力棒哪些還有效。** 它的素材處理、決策表、規則那幾節都是準的，
但第 5 節「未完成二：系列歸屬改成直播筆記」**已經被她否決**，照做會把四個正確的頁面改壞。
Drive 那件（未完成一）則是做完了。

**這次問問題的方式可以延用。** 上一棒的教訓是「AskUserQuestion 的題幹不能夾帶未確認的前提」，
這次照做：把「系列歸屬」「Drive 格式」「要不要補規則」三題一次問完，題幹只陳述事實
（含查到的資料夾真名叫「第三季」），不預設答案。她一次全答完，沒有來回。

**查證比推測有用。** 這次先用 `get_file_metadata` 查出那個資料夾 ID 的真名是「第三季」、
上層是「+ECF_2026」，這個事實直接進了問題的題幹，讓她判斷系列歸屬時有依據。

**她的驗收習慣沒變**：會實際點開看。所以 PDF 產出後有逐頁轉圖檢查，第一版發現版面有問題
（每個技能佔一頁）就重印，不是印完就交。

**關鍵位置速查**
- repo：`/home/user/kt-sweet-journey/`（分支 `claude/relay-baton-continuation-nlwx3o`，已與 main 同步）
- 技能正本：`.claude/skills/lecture-notes-site/SKILL.md`
- 四個頁面：`nodered1-notes.html`／`nodered1-ai-skills.html`／`nodered2-notes.html`／`nodered2-ai-skills.html`
- 她的收檔資料夾：「第三季」`1LSPX3vXbJ3oCscttTpsQacClbcSNL1f4`
- 網站入口：https://tarshar4242.github.io/
