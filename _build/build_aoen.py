# -*- coding: utf-8 -*-
import os, io, base64, json
from PIL import Image

ROOT = "/Users/yuriko/Documents/konnekted-ip"
SRC  = os.path.join(ROOT, "aoen", "_src")
TODAY = "2026-06-16"

def b64(path, size, quality=82):
    img = Image.open(path).convert("RGB")
    img.thumbnail(size, Image.LANCZOS)
    out = io.BytesIO()
    img.save(out, "JPEG", quality=quality, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(out.getvalue()).decode()

def load(name, size, q=82):
    p = os.path.join(SRC, name)
    return b64(p, size, q) if os.path.exists(p) else ""

# ---- data ----
GROUP = {
    "name_ja":"aoen（アオエン）","name_hangul":"아오엔",
    "origin":"ao（青＝最も熱い炎の色）＋ en（炎＝情熱の疾走）。「応援（エール）」の音も重ねた造語。意味は「青い炎で世界を満たす」",
    "label":"JCONIC（旧 YX LABELS / HYBE LABELS JAPAN・2026/1 移管）",
    "debut":"2025年6月11日 デビュー曲「The Blue Sun」",
    "audition":"オーディション番組「応援-HIGH 〜夢のスタートライン〜（Oen-HIGH）」発",
    "fandom":"aoring（アオリン）","members":"7名",
    "concept":"次世代J-POPボーイズ。「青い炎」＝情熱・スピード・応援。MV/ビジュアルは Day版 / Night版 の2軸展開",
    "key_hex":"#4CEDFF",
    "sns":[("公式サイト","https://aoen-official.jp/"),("X","https://x.com/aoen_official"),
           ("Instagram","https://www.instagram.com/aoen.official/"),("YouTube","https://www.youtube.com/@aoen_official"),
           ("Weverse","https://weverse.io/aoen")],
    "disco":["1st Single「The Blue Sun」(2025/6/11)","Digital Single「青春インクレディブル」(2025/10/15)",
             "2nd Single「秒で落ちた」(2026/3/18)","3rd Single「ハジマリCOLOR」(2026/7/22)"],
}
MEMBERS = [
 {"name":"YUJU","ja":"蒼井 優樹","emoji":"🐶","color":"ライトブルー","hex":"#4CEDFF","img":"member_yuju.jpg","birth":"2002/12/20","age":"23","height":"178cm","from":"埼玉県","blood":"A","pos":"リーダー","hobby":"サッカー・料理・音楽鑑賞・アニメ・リフティング"},
 {"name":"RUKA","ja":"山倉 琉楓","emoji":"🐬","color":"グリーン","hex":"#0AFF00","img":"member_ruka.jpg","birth":"2003/11/01","age":"22","height":"174cm","from":"宮崎県","blood":"A","pos":"サブリーダー","hobby":"4歳からダンス・振付習得が速い・ヨーヨー・衣類リメイク"},
 {"name":"GAKU","ja":"藤野 雅久","emoji":"🐯","color":"レッド","hex":"#FE0B00","img":"member_gaku.jpg","birth":"2004/04/25","age":"22","height":"176cm","from":"長野県","blood":"O","pos":"メインダンサー","hobby":"HIPHOPダンス・バスケ・スケボー・短距離走・撮影"},
 {"name":"HIKARU","ja":"白濱 輝","emoji":"🦢","color":"ホワイト","hex":"#E6EEF5","img":"member_hikaru.jpg","birth":"2005/03/28","age":"21","height":"182cm","from":"群馬県","blood":"B","pos":"ビジュアル・ダンサー","hobby":"3歳からクラシックバレエ・空手・アニメ・高い柔軟性"},
 {"name":"SOTA","ja":"颯太","emoji":"🐈‍⬛","color":"ピンク","hex":"#FF3186","img":"member_sota.jpg","birth":"2005/08/15","age":"20","height":"176cm","from":"東京都","blood":"O","pos":"ボーカル","hobby":"水泳・ゲーム・バスケ／早稲田大在学中"},
 {"name":"KYOSUKE","ja":"芹澤 京助","emoji":"🦭","color":"オレンジ","hex":"#FF7A00","img":"member_kyosuke.jpg","birth":"2005/09/25","age":"20","height":"176cm","from":"神奈川県","blood":"B","pos":"メインボーカル・ダンサー","hobby":"5歳からダンス・全国大会1位・自然鑑賞"},
 {"name":"REO","ja":"礼央","emoji":"🐰","color":"パープル","hex":"#CE33FF","img":"member_reo.jpg","birth":"2007/07/09","age":"18","height":"173cm","from":"宮城県仙台市","blood":"A","pos":"ボーカル・最年少","hobby":"4歳からダンス・作詞作曲・韓国語・映画・買い物"},
]
GOODS = [
 ("goods_acrylicstand_pcset.jpg","アクスタ＆フォトカードセット","1st Anniversary"),
 ("goods_canbadge_glitter.jpg","グリッターフォト缶バッジ","1st Anniversary"),
 ("goods_keyring_acrylic.jpg","アクリルキーリング","1st Anniversary"),
 ("goods_acrylicstand_seishun.jpg","アクリルスタンド","青春インクレディブル"),
 ("goods_photocard_seishun.jpg","フォトカード","青春インクレディブル"),
 ("goods_tshirt_black.jpg","Tシャツ（ブラック）","青のはじまり 47+1"),
]
GOODS_OUT = ["フォトカード","アクスタ","アクリルキーホルダー","応援うちわ","フォト缶バッジ","Tシャツ","トートバッグ","ツアータオル","ゆらゆらチャーム","フォトカードバインダー","グリッター缶バッジ"]
GOODS_GAP = [
 ("公式ペンライト","K-POP系では必須なのに未確認＝最大の空白"),
 ("ヘビーアパレル（パーカー/スウェット/ジャケット）","Tシャツ止まり。日常着レンジが空いている"),
 ("ぬいぐるみ・マスコット","ファンダム定番だが未確認"),
 ("ステーショナリー（シール/メモ/付箋）","低単価で量が出る帯が空白"),
 ("コスメ・香水コラボ","世界観×日常の余地大"),
 ("フォトブック・スリーブ","未確認"),
]
PROPOSE = [
 {"cat":"🎴 推し活グッズ（アクスタ・缶バッジ等）","tone":"#FF3186","ideas":[
   "メンカラ7色＋<b>絵文字アイコン缶バッジ</b>（🐶🐬🐯🦢🐈‍⬛🦭🐰）— 各メンバーの絵文字がそのままアイコン化できる稀有なグループ",
   "メンカラ×名前ロゴの<b>ホログラム/グリッタートレカ</b>（既出グリッター缶バッジの流れで親和性◯）",
   "「青い炎」モチーフの<b>全員集合アクスタ台座</b>（7色が揃うと虹になるコンセプトを立体で）"]},
 {"cat":"👕 アパレル（T・パーカー等）","tone":"#4CEDFF","ideas":[
   "<b>未展開のパーカー/スウェット</b>を狙う ← Tシャツしか出ていない＝KONNEKTEDの空白勝ち筋",
   "メンカラ刺繍ワンポイント（袖・裾）の<b>メンバー別カラー展開アパレル</b>",
   "曲タイトル×青い炎グラフィックの<b>ツアー連動T</b>"]},
 {"cat":"🧴 雑貨・日用品（タンブラー・ポーチ等）","tone":"#0AFF00","ideas":[
   "メンカラ7色の<b>タンブラー/ボトル</b>（日常使い×推し色・既出と被らない）",
   "絵文字アイコンを散らした<b>ポーチ/ミラー/ステーショナリー</b>（未展開のシール・メモ帯を取りに行く）",
   "「青い炎」世界観の<b>ブランケット/エコバッグ</b>（物販客単価アップ枠）"]},
]
FACTCHECK = [
 "<b>検証済み（2026/6/16・一次ソース照合）</b>：デビュー日・所属レーベル(JCONIC)・デビュー曲・ファンダム名(aoring)・7人の生年月日/年齢/身長/出身は公式サイトと一致。",
 "HIKARU（輝）は番組内は「HAKU」名義。<b>2025/6/11デビュー当日に本名HIKARUへ改名</b>（一次：Oricon）。",
 "メンカラ7色・絵文字の<b>割り当て</b>は公式X（@aoen_members）発表ベースで一致。ただし<b>HEX数値は二次ソース由来</b>＝実制作は公式ビジュアルからスポイト確認推奨。",
 "漢字の苗字（蒼井/山倉/藤野/白濱/芹澤）・詳細ポジションは<b>公式プロフィール非掲載の項目を含み二次ソース確認ベース</b>＝確定前に要確認。SOTA・REO の苗字は事務所非公開。",
 "デビュー追加メンバーの得票数はソース間で桁が食い違う＝<b>Oricon一次ソースで要確認</b>。",
 "メンバー写真・グッズ画像は<b>公式（公式サイト profile / 公式 Weverse Shop）から取得</b>。各IP公式に帰属。",
]
REFS = [
 ("公式・一次ソース",[
   ("aoen 公式サイト — プロフィール","https://aoen-official.jp/profile"),
   ("aoen 公式サイト","https://aoen-official.jp/"),
   ("aoen 公式 Weverse / Weverse Shop","https://weverse.io/aoen"),
   ("aoen 公式X（@aoen_official／@aoen_members：メンカラ・絵文字発表）","https://x.com/aoen_official"),
   ("aoen 公式Instagram","https://www.instagram.com/aoen.official/"),
   ("Universal Music Japan — aoen","https://www.universal-music.co.jp/aoen/"),
 ]),
 ("報道・レーベル発表",[
   ("Oricon News — デビューメンバー7名確定","https://www.oricon.co.jp/news/2381064/full/"),
   ("Oricon News — HAKU→HIKARU 改名","https://www.oricon.co.jp/news/2390102/full/"),
   ("Real Sound —「ハジマリCOLOR」発売（2026/7/22）","https://realsound.jp/2026/05/post-2405099.html"),
   ("HYBE JAPAN「JCONIC」レーベル新設発表","https://neotokyo2099.com/2026/01/05/hybe-japan-launches-new-label-jconic-with-the-aim-of-creating-an-icon-that-symbolizes-the-era-from-japan/"),
 ]),
 ("二次・ファンサイト（補助確認）",[
   ("Wikipedia — Aoen","https://en.wikipedia.org/wiki/Aoen"),
   ("kprofiles — aoen Members Profile","https://kprofiles.com/aoen-members-profile/"),
   ("kpoptune — aoen","https://kpoptune.jp/artist/1837"),
   ("UtaTen — aoen メンバー","https://utaten.com/specialArticle/index/9586"),
   ("aoringnote — メンカラ・絵文字／年齢順","https://ayaso810.com/aoenemoji/"),
   ("satsutabi — aoen ポジション/プロフィール","https://satsutabi.com/aoen-position/"),
 ]),
]

def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

# ---- load images ----
print("compressing images...")
m_imgs = {m["name"]: load(m["img"], (560,720), 80) for m in MEMBERS}
g_imgs = [(load(f,(760,760),80), label, series) for f,label,series in GOODS]
hero_img = load("group_01.jpg",(1100,1100),80)

CSS = '''*{margin:0;padding:0;box-sizing:border-box}
:root{--blue:#4CEDFF;--ink:#0c1726;--paper:#f4f8fc;--card:#fff;--line:#e2ebf3;--mut:#65788c}
body{font-family:"Noto Sans JP",sans-serif;background:var(--paper);color:var(--ink);line-height:1.7;-webkit-text-size-adjust:100%}
.wrap{max-width:980px;margin:0 auto;padding:0 16px 64px}
a{color:#0a93c4;word-break:break-all}
.hero{position:relative;color:#fff;padding:54px 22px 44px;border-radius:0 0 26px 26px;overflow:hidden;background:#08406b}
.hero .bg{position:absolute;inset:0;background-size:cover;background-position:center 22%;opacity:.42}
.hero .ov{position:absolute;inset:0;background:linear-gradient(135deg,rgba(8,42,64,.92),rgba(10,147,196,.55))}
.hero .in{position:relative}
.kic{font-size:12px;letter-spacing:.18em;color:var(--blue);font-weight:700}
.hero h1{font-family:"Bebas Neue";font-size:72px;letter-spacing:.04em;line-height:.95;margin:6px 0 2px}
.hero .sub{font-size:14px}
.hero .tag{display:inline-block;margin-top:14px;font-size:11px;background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.3);padding:5px 12px;border-radius:99px}
.back{display:inline-block;margin:18px 0 -6px;font-size:12px;color:#0a93c4;text-decoration:none}
section{margin-top:30px}
.sh{display:flex;align-items:center;gap:10px;margin-bottom:14px}
.sh .no{font-family:"Bebas Neue";font-size:30px;color:var(--blue);-webkit-text-stroke:1px #0a93c4}
.sh h2{font-size:19px;font-weight:900}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px;box-shadow:0 4px 18px rgba(10,60,107,.05)}
table{width:100%;border-collapse:collapse;font-size:14px}
th,td{text-align:left;padding:9px 8px;border-bottom:1px solid var(--line);vertical-align:top}
th{color:var(--mut);font-weight:700;width:30%;white-space:nowrap}
.mgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:13px}
.mc{background:var(--card);border:1px solid var(--line);border-radius:16px;overflow:hidden;box-shadow:0 4px 18px rgba(10,60,107,.06)}
.mc .ph{position:relative;aspect-ratio:3/4;background:#dde8f0;overflow:hidden}
.mc .ph img{width:100%;height:100%;object-fit:cover;object-position:top}
.mc .ph .strip{position:absolute;left:0;bottom:0;width:100%;padding:18px 12px 9px;background:linear-gradient(transparent,rgba(6,16,28,.82));display:flex;align-items:flex-end;justify-content:space-between}
.mc .nm{font-family:"Bebas Neue";font-size:27px;color:#fff;letter-spacing:.03em;line-height:1}
.mc .emoji{font-size:25px}
.mc .clrbar{height:5px}
.mc .body{padding:11px 13px}
.mc .ja{font-weight:700;font-size:13.5px}
.mc .pos{display:inline-block;font-size:10px;background:var(--paper);border:1px solid var(--line);padding:2px 8px;border-radius:99px;margin:5px 0}
.mc .meta{font-size:11.5px;color:var(--mut)}
.mc .hob{font-size:11.5px;margin-top:6px;border-top:1px dashed var(--line);padding-top:6px}
.pal{display:flex;flex-wrap:wrap;gap:10px}
.sw{flex:1 1 12%;min-width:88px;border-radius:12px;overflow:hidden;border:1px solid var(--line)}
.sw .clr{height:50px}.sw .lab{font-size:10px;padding:5px 7px;background:#fff}.sw .lab b{font-family:"Bebas Neue";font-size:14px;display:block}
.ggrid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.gc{border:1px solid var(--line);border-radius:14px;overflow:hidden;background:#fff}
.gc img{width:100%;aspect-ratio:1;object-fit:cover;display:block;background:#eef3f7}
.gc .cap{padding:8px 10px}.gc .cap b{font-size:12px}.gc .cap span{font-size:10px;color:var(--mut);display:block}
.glist{display:flex;flex-wrap:wrap;gap:7px;margin:6px 0 2px}
.gpill{font-size:12px;background:#eef6fb;border:1px solid #d4e8f3;color:#0a6c93;padding:5px 10px;border-radius:8px}
.gap{background:#fff5f8;border:1px solid #ffd0e0;border-radius:12px;padding:11px 13px;margin-top:8px}
.gap b{color:#d6336c}.gap .why{font-size:12px;color:var(--mut);display:block;margin-top:2px}
.pcat{border-radius:16px;padding:16px;margin-top:12px;border:1px solid var(--line);background:#fff}
.pcat h3{font-size:15px;margin-bottom:8px;display:flex;align-items:center;gap:8px}
.pcat .dot{width:12px;height:12px;border-radius:99px;display:inline-block}
.pcat ul{list-style:none}.pcat li{font-size:13.5px;padding:7px 0 7px 22px;position:relative;border-bottom:1px dashed var(--line)}
.pcat li:last-child{border:0}.pcat li:before{content:"\\2192";position:absolute;left:0;color:#0a93c4;font-weight:700}
.fc li{font-size:13px;margin-left:18px;margin-bottom:6px}
.note{font-size:12px;color:var(--mut);margin-top:8px}
.srcgrid{display:flex;flex-wrap:wrap;gap:8px}
.srcgrid a{font-size:12px;background:#eef3f7;border:1px solid var(--line);padding:6px 11px;border-radius:8px;text-decoration:none}
footer{margin-top:36px;padding:18px;background:#0c1726;color:#9fb3c6;border-radius:16px;font-size:11.5px;text-align:center;line-height:1.8}
footer b{color:#ffd43b}
@media(max-width:880px){.mgrid{grid-template-columns:repeat(3,1fr)}}
@media(max-width:620px){.mgrid{grid-template-columns:repeat(2,1fr)}.ggrid{grid-template-columns:1fr 1fr}.hero h1{font-size:56px}}
'''

H=['<!DOCTYPE html><html lang="ja"><head><meta charset="utf-8">',
 '<meta name="viewport" content="width=device-width,initial-scale=1">',
 '<meta name="robots" content="noindex,nofollow"><title>aoen｜KONNEKTED IP提案ブリーフ</title>',
 '<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Noto+Sans+JP:wght@400;500;700;900&display=swap" rel="stylesheet">',
 '<style>'+CSS+'</style></head><body>']
# hero
H.append('<div class="hero"><div class="bg" style="background-image:url('+hero_img+')"></div><div class="ov"></div>')
H.append('<div class="wrap"><div class="in">')
H.append('<div class="kic">KONNEKTED ＿ IP PROPOSAL BRIEF</div><h1>aoen</h1>')
H.append('<div class="sub">'+esc(GROUP["name_hangul"])+' ・ 7人組 次世代J-POPボーイズ ・ '+esc(GROUP["label"])+'</div>')
H.append('<div class="tag">社内提案検討用 ／ '+TODAY+' 作成</div></div></div></div>')
H.append('<div class="wrap"><a class="back" href="../">← 目次（IP一覧）にもどる</a>')

# 1 概要
H.append('<section><div class="sh"><span class="no">01</span><h2>🪪 IP概要</h2></div><div class="card"><table>')
for k,v in [("正式名称",GROUP["name_ja"]+" / "+GROUP["name_hangul"]),("名前の由来",GROUP["origin"]),("所属レーベル",GROUP["label"]),("デビュー",GROUP["debut"]),("発掘",GROUP["audition"]),("ファンダム名",GROUP["fandom"]),("メンバー数",GROUP["members"]),("コンセプト",GROUP["concept"]),("ディスコグラフィー"," ／ ".join(GROUP["disco"]))]:
    H.append('<tr><th>'+esc(k)+'</th><td>'+v+'</td></tr>')
H.append('<tr><th>公式SNS</th><td>'+" ・ ".join(['<a href="'+u+'" target="_blank">'+esc(n)+'</a>' for n,u in GROUP["sns"]])+'</td></tr>')
H.append('</table></div></section>')

# 2 members
H.append('<section><div class="sh"><span class="no">02</span><h2>👥 メンバー図鑑</h2></div><div class="mgrid">')
for m in MEMBERS:
    H.append('<div class="mc"><div class="ph"><img src="'+m_imgs[m["name"]]+'" alt="'+esc(m["name"])+'" loading="lazy">')
    H.append('<div class="strip"><span class="nm">'+esc(m["name"])+'</span><span class="emoji">'+m["emoji"]+'</span></div></div>')
    H.append('<div class="clrbar" style="background:'+m["hex"]+'"></div><div class="body">')
    H.append('<div class="ja">'+esc(m["ja"])+'</div><div class="pos">'+esc(m["pos"])+'</div>')
    H.append('<div class="meta">'+esc(m["color"])+' '+m["hex"]+'<br>🎂 '+esc(m["birth"])+'（'+esc(m["age"])+'歳）<br>'+esc(m["height"])+'・'+esc(m["from"])+'</div>')
    H.append('<div class="hob">🎯 '+esc(m["hobby"])+'</div></div></div>')
H.append('</div><p class="note">※ メンバー写真は aoen 公式（公式サイト profile / 公式 Weverse）から取得。各IP公式に帰属。</p></section>')

# 3 visual
H.append('<section><div class="sh"><span class="no">03</span><h2>🎨 ビジュアル & 世界観</h2></div><div class="card"><b>メンバーカラー パレット</b><div class="pal" style="margin-top:8px">')
for m in MEMBERS:
    H.append('<div class="sw"><div class="clr" style="background:'+m["hex"]+'"></div><div class="lab"><b>'+esc(m["color"])+'</b>'+m["hex"]+'<br>'+esc(m["name"])+' '+m["emoji"]+'</div></div>')
H.append('</div><p class="note" style="margin-top:14px"><b>世界観キーワード</b>：青・炎・疾走・応援・情熱・輝き・新世代 ／ アンカー = ブルー '+GROUP["key_hex"]+' ／ MVは Day版（清潔な青白）と Night版（深い青）の2軸 ／ <b>7色が揃うと虹になる</b>コンセプト＝全員集合グッズと相性◯</p></div></section>')

# 4 goods
H.append('<section><div class="sh"><span class="no">04</span><h2>🛍 過去グッズ分析（市場の答え合わせ）</h2></div><div class="card">')
H.append('<b>発売実物（公式 Weverse Shop）</b><div class="ggrid" style="margin-top:8px">')
for img,label,series in g_imgs:
    H.append('<div class="gc"><img src="'+img+'" alt="'+esc(label)+'" loading="lazy"><div class="cap"><b>'+esc(label)+'</b><span>'+esc(series)+'</span></div></div>')
H.append('</div>')
H.append('<p class="note" style="margin-top:14px"><b>出ているカテゴリ</b></p><div class="glist">')
for n in GOODS_OUT: H.append('<span class="gpill">'+esc(n)+'</span>')
H.append('</div><p class="note" style="margin-top:14px"><b style="color:#d6336c">⬇ まだ出ていない＝KONNEKTEDの勝ち筋</b></p>')
for n,why in GOODS_GAP: H.append('<div class="gap"><b>'+esc(n)+'</b><span class="why">'+esc(why)+'</span></div>')
H.append('</div></section>')

# 5 propose
H.append('<section><div class="sh"><span class="no">05</span><h2>🎯 KONNEKTED 提案ヒント</h2></div>')
H.append('<div class="card" style="padding:14px"><p class="note" style="margin:0 0 4px">3カテゴリ × このIPならではの具体アイデア。<b>過去グッズの空白</b>と接続。※アイデアは提案たたき台（要すり合わせ）。</p>')
for p in PROPOSE:
    H.append('<div class="pcat"><h3><span class="dot" style="background:'+p["tone"]+'"></span>'+esc(p["cat"])+'</h3><ul>')
    for i in p["ideas"]: H.append('<li>'+i+'</li>')
    H.append('</ul></div>')
H.append('</div></section>')

# factcheck
H.append('<section><div class="sh"><span class="no">!</span><h2>🔍 ファクトチェック注記</h2></div><div class="card"><ul class="fc">')
for f in FACTCHECK: H.append('<li>'+f+'</li>')
H.append('</ul></div></section>')

# 参考文献
H.append('<section><div class="sh"><span class="no">📚</span><h2>参考文献</h2></div><div class="card refs">')
n=1
for grp,items in REFS:
    H.append('<h4 style="font-size:13px;margin:10px 0 4px;color:#0a6c93">'+esc(grp)+'</h4><ol style="margin:0 0 4px 22px">')
    for title,u in items:
        H.append('<li style="font-size:12.5px;margin-bottom:5px;line-height:1.5">'+esc(title)+'<br><a href="'+u+'" target="_blank" style="font-size:11px">'+esc(u)+'</a></li>')
        n+=1
    H.append('</ol>')
H.append('<p class="note" style="margin-top:12px">最終確認：2026-06-16。情報は上記を二重照合し、公式・一次を優先。メンバー写真／グッズ画像は公式サイト profile ページ及び公式 Weverse Shop から取得。</p></div></section>')

H.append('<footer><b>社内提案検討用 / 対外配布禁止</b><br>画像・情報は aoen 各公式に帰属します。提案検討のための社内リサーチであり、確定情報ではありません。<br>generated '+TODAY+' by KONNEKT ＿ /ip-brief</footer>')
H.append('</div></body></html>')

out = os.path.join(ROOT,"aoen","index.html")
with open(out,"w",encoding="utf-8") as f: f.write("".join(H))
print("aoen size:", round(os.path.getsize(out)/1024/1024,2),"MB")

# thumb for index card (group banner small)
thumb = load("group_01.jpg",(640,640),78)
with open(os.path.join(ROOT,"aoen","_thumb.txt"),"w") as f: f.write(thumb)
print("thumb saved")
