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
# 横長の7人組セット（全幅表示）
GOODS_WIDE = [
 ("goods_messagecard_hajimari.jpg","メッセージカード（全7種）","ハジマリCOLOR"),
 ("goods_photocard_pop.jpg","メンカラPOPフォトカード（全7種）","ハジマリCOLOR"),
 ("goods_photocard_kanji.jpg","漢字ネームフォトカード（全7種）","ハジマリCOLOR"),
 ("goods_collectcard_47plus1.jpg","コレクションカード（全7種）","青のはじまり 47+1"),
]
GOODS_OUT = ["フォトカード","トレカ","メッセージカード","アクスタ","アクリルキーホルダー","応援うちわ","フォト缶バッジ","Tシャツ","トートバッグ","ツアータオル","ゆらゆらチャーム","フォトカードバインダー","グリッター缶バッジ"]
GOODS_GAP = [
 ("公式ペンライト","K-POP系では必須なのに未確認＝最大の空白"),
 ("ヘビーアパレル（パーカー/スウェット/ジャケット）","Tシャツ止まり。日常着レンジが空いている"),
 ("ぬいぐるみ・マスコット","ファンダム定番だが未確認"),
 ("ステーショナリー（シール/メモ/付箋）","低単価で量が出る帯が空白"),
 ("コスメ・香水コラボ","世界観×日常の余地大"),
 ("フォトブック・スリーブ","未確認"),
]
# 提案：カテゴリごとに（アイデア名 / ねらい）の2列
PROPOSE = [
 {"cat":"🎴 推し活グッズ","sub":"アクスタ・缶バッジ等","tone":"#FF3186","rows":[
   ("絵文字アイコン缶バッジ 🐶🐬🐯🦢🐈‍⬛🦭🐰","各メンバーに絵文字がある稀有なグループ＝アイコン化が即できる"),
   ("メンカラ×名前ロゴ ホログラム/グリッタートレカ","既出のグリッター缶バッジと親和性◯"),
   ("全員集合アクスタ台座（青い炎モチーフ）","7色が揃うと虹になるコンセプトを立体で")]},
 {"cat":"👕 アパレル","sub":"T・パーカー等","tone":"#4CEDFF","rows":[
   ("パーカー/スウェット（未展開枠）","Tシャツしか出ていない＝空白の勝ち筋"),
   ("メンカラ刺繍ワンポイントのメンバー別アパレル","袖・裾に推し色を仕込む"),
   ("曲タイトル×青い炎グラフィックのツアー連動T","ライブ物販と連動")]},
 {"cat":"🧴 雑貨・日用品","sub":"タンブラー・ポーチ等","tone":"#0AFF00","rows":[
   ("メンカラ7色タンブラー/ボトル","日常使い×推し色・既出と被らない"),
   ("絵文字アイコンのポーチ/ミラー/ステーショナリー","未展開のシール・メモ帯を取りにいく"),
   ("青い炎世界観のブランケット/エコバッグ","物販の客単価アップ枠")]},
]
# ファクトチェック：検証済み / 要確認 の2分割（短文）
FC_OK = [
 "デビュー日・所属(JCONIC)・デビュー曲・ファンダム名(aoring)",
 "7人の生年月日・年齢・身長・出身（公式サイトと一致）",
 "HIKARU は「HAKU」から改名（2025/6/11・一次:Oricon）",
 "メンカラ7色・絵文字の割り当て（公式X @aoen_members 発表）",
 "メンバー写真・グッズ画像は公式から取得（各IP公式に帰属）",
]
FC_CHECK = [
 ("メンカラのHEX数値","二次ソース由来 → 実制作は公式ビジュアルからスポイト確認"),
 ("漢字の苗字・詳細ポジション","二次ソース確認ベース（公式プロフィール非掲載）"),
 ("SOTA・REO の苗字","事務所非公開"),
 ("デビュー追加メンバーの得票数","ソース間で桁が食い違い → 要一次確認"),
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
gw_imgs = [(load(f,(1100,1100),80), label, series) for f,label,series in GOODS_WIDE]
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
.sh .no{font-family:"Bebas Neue";font-size:30px;color:var(--blue)}
.sh h2{font-size:19px;font-weight:900}
.sh .typ{margin-left:auto;font-size:10px;font-weight:700;padding:3px 10px;border-radius:99px}
/* セクション型の色分け */
.t-data .no{color:#0a93c4}.t-data .typ{background:#e3f4fb;color:#0a6c93}.t-data>.card,.t-data .card{border-top:3px solid #4CEDFF}
.t-idea .no{color:#e84393}.t-idea .typ{background:#ffe3ee;color:#c2185b}.t-idea>.card,.t-idea .card{border-top:3px solid #FF3186}
.t-warn .no{color:#e1820a}.t-warn .typ{background:#fff1dd;color:#c2700a}.t-warn>.card,.t-warn .card{border-top:3px solid #ffb24d}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px;box-shadow:0 4px 18px rgba(10,60,107,.05)}
table{width:100%;border-collapse:collapse;font-size:14px}
th,td{text-align:left;padding:9px 8px;border-bottom:1px solid var(--line);vertical-align:top}
th{color:var(--mut);font-weight:700;width:30%;white-space:nowrap}
/* チップ */
.chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:6px}
.chip{font-size:11.5px;background:#eef3f7;border:1px solid var(--line);color:#3a4d5e;padding:3px 9px;border-radius:99px}
.chip.kw{background:#eaf7fc;border-color:#cce8f3;color:#0a6c93}
/* メンバーカード内ミニ表 */
.mc .mt{width:100%;font-size:11px;margin-top:2px}
.mc .mt td{padding:3px 0;border-bottom:1px solid #eef2f6;vertical-align:top}
.mc .mt td.k{color:var(--mut);width:42%;white-space:nowrap}
.mc .mt tr:last-child td{border-bottom:0}
/* 比較・提案テーブル */
.tbl{width:100%;border-collapse:collapse;font-size:13px;margin-top:8px}
.tbl th{background:#f1f6fa;color:#3a4d5e;font-weight:700;font-size:11.5px;width:auto;padding:7px 9px;border-bottom:2px solid var(--line)}
.tbl td{padding:8px 9px;border-bottom:1px solid var(--line)}
.tbl td.idea{font-weight:700;width:46%}
.tbl td.st{white-space:nowrap;width:1%;font-weight:700}
.tbl tr:nth-child(even) td{background:#fafcfe}
.ptab{margin-top:12px;border:1px solid var(--line);border-radius:14px;overflow:hidden}
.ptab .ph{display:flex;align-items:center;gap:8px;padding:10px 13px;font-weight:900;font-size:14px}
.ptab .ph .dot{width:11px;height:11px;border-radius:99px}
.ptab .ph .s{font-size:10px;color:var(--mut);font-weight:500}
/* ファクトチェック2分割 */
.fcwrap{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.fcbox{border-radius:12px;padding:13px 14px}
.fcbox.ok{background:#eefbf2;border:1px solid #bfe8cd}
.fcbox.ck{background:#fff7ea;border:1px solid #ffe0b0}
.fcbox h4{font-size:13px;margin-bottom:8px}
.fcbox ul{list-style:none}
.fcbox li{font-size:12px;padding:5px 0 5px 20px;position:relative;border-bottom:1px dashed rgba(0,0,0,.07);line-height:1.5}
.fcbox li:last-child{border:0}
.fcbox.ok li:before{content:"\\2705";position:absolute;left:0;font-size:11px}
.fcbox.ck li:before{content:"\\26A0\\FE0F";position:absolute;left:0;font-size:10px}
.fcbox li b{color:#0c1726}
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
.gcw{border:1px solid var(--line);border-radius:14px;overflow:hidden;background:#fff;margin-top:10px}
.gcw img{width:100%;height:auto;display:block;background:#f0f4f8}
.gcw .cap{padding:8px 12px}.gcw .cap b{font-size:12px}.gcw .cap span{font-size:10px;color:var(--mut);display:block}
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
@media(max-width:620px){.mgrid{grid-template-columns:repeat(2,1fr)}.ggrid{grid-template-columns:1fr 1fr}.hero h1{font-size:56px}.fcwrap{grid-template-columns:1fr}}
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

import re as _re
def hobby_chips(s):
    parts=[p for p in _re.split(r'[・／/]', s) if p.strip()]
    return ''.join('<span class="chip">'+esc(p.strip())+'</span>' for p in parts)

# 1 概要
H.append('<section class="t-data"><div class="sh"><span class="no">01</span><h2>🪪 IP概要</h2><span class="typ">DATA</span></div><div class="card"><table>')
for k,v in [("正式名称",GROUP["name_ja"]+" / "+GROUP["name_hangul"]),("名前の由来",GROUP["origin"]),("所属レーベル",GROUP["label"]),("デビュー",GROUP["debut"]),("発掘",GROUP["audition"]),("ファンダム名",GROUP["fandom"]),("メンバー数",GROUP["members"]),("コンセプト",GROUP["concept"])]:
    H.append('<tr><th>'+esc(k)+'</th><td>'+v+'</td></tr>')
H.append('<tr><th>ディスコグラフィー</th><td>'+''.join('<span class="chip">'+esc(d)+'</span>' for d in GROUP["disco"])+'</td></tr>')
H.append('<tr><th>公式SNS</th><td>'+" ・ ".join(['<a href="'+u+'" target="_blank">'+esc(n)+'</a>' for n,u in GROUP["sns"]])+'</td></tr>')
H.append('</table></div></section>')

# 2 members
H.append('<section class="t-data"><div class="sh"><span class="no">02</span><h2>👥 メンバー図鑑</h2><span class="typ">DATA</span></div><div class="mgrid">')
for m in MEMBERS:
    H.append('<div class="mc"><div class="ph"><img src="'+m_imgs[m["name"]]+'" alt="'+esc(m["name"])+'" loading="lazy">')
    H.append('<div class="strip"><span class="nm">'+esc(m["name"])+'</span><span class="emoji">'+m["emoji"]+'</span></div></div>')
    H.append('<div class="clrbar" style="background:'+m["hex"]+'"></div><div class="body">')
    H.append('<div class="ja">'+esc(m["ja"])+'</div><div class="pos">'+esc(m["pos"])+'</div>')
    H.append('<table class="mt">')
    H.append('<tr><td class="k">メンカラ</td><td><span style="display:inline-block;width:9px;height:9px;border-radius:2px;border:1px solid #ccc;background:'+m["hex"]+';vertical-align:middle"></span> '+esc(m["color"])+'</td></tr>')
    H.append('<tr><td class="k">誕生日</td><td>'+esc(m["birth"])+'（'+esc(m["age"])+'）</td></tr>')
    H.append('<tr><td class="k">身長</td><td>'+esc(m["height"])+'</td></tr>')
    H.append('<tr><td class="k">出身</td><td>'+esc(m["from"])+'</td></tr>')
    H.append('</table>')
    H.append('<div class="chips" style="margin-top:8px">'+hobby_chips(m["hobby"])+'</div>')
    H.append('</div></div>')
H.append('</div><p class="note">※ メンバー写真は aoen 公式（公式サイト profile / 公式 Weverse）から取得。各IP公式に帰属。</p></section>')

# 3 visual
H.append('<section class="t-data"><div class="sh"><span class="no">03</span><h2>🎨 ビジュアル & 世界観</h2><span class="typ">DATA</span></div><div class="card"><b>メンバーカラー パレット</b><div class="pal" style="margin-top:8px">')
for m in MEMBERS:
    H.append('<div class="sw"><div class="clr" style="background:'+m["hex"]+'"></div><div class="lab"><b>'+esc(m["color"])+'</b>'+m["hex"]+'<br>'+esc(m["name"])+' '+m["emoji"]+'</div></div>')
H.append('</div>')
H.append('<div style="margin-top:14px"><b style="font-size:13px">世界観キーワード</b><div class="chips" style="margin-top:6px">'+''.join('<span class="chip kw">'+esc(k)+'</span>' for k in ["青","炎","疾走","応援","情熱","輝き","新世代"])+'</div></div>')
H.append('<table class="tbl"><tr><th>アンカーカラー</th><td>ブルー '+GROUP["key_hex"]+'</td></tr><tr><th>MVトーン</th><td>Day版（清潔な青白）／ Night版（深い青）の2軸</td></tr><tr><th>カラー設計</th><td>7色が揃うと虹になる＝全員集合グッズと相性◯</td></tr></table>')
H.append('</div></section>')

# 4 goods
H.append('<section class="t-data"><div class="sh"><span class="no">04</span><h2>🛍 過去グッズ分析</h2><span class="typ">市場の答え合わせ</span></div><div class="card">')
H.append('<b>発売実物（公式 Weverse Shop）</b><div class="ggrid" style="margin-top:8px">')
for img,label,series in g_imgs:
    H.append('<div class="gc"><img src="'+img+'" alt="'+esc(label)+'" loading="lazy"><div class="cap"><b>'+esc(label)+'</b><span>'+esc(series)+'</span></div></div>')
H.append('</div>')
# 横長：フォトカード/トレカ展開
H.append('<p class="note" style="margin-top:16px"><b>📸 フォトカード・トレカ展開（リリース特典・全7種）</b></p>')
for img,label,series in gw_imgs:
    H.append('<div class="gcw"><img src="'+img+'" alt="'+esc(label)+'" loading="lazy"><div class="cap"><b>'+esc(label)+'</b><span>'+esc(series)+'（公式）</span></div></div>')
H.append('<p class="note" style="margin-top:14px"><b>出ているカテゴリ</b></p><div class="glist">')
for n in GOODS_OUT: H.append('<span class="gpill">✓ '+esc(n)+'</span>')
H.append('</div><p class="note" style="margin-top:10px">📌 デビュー約1年。グッズは<b>フォトカード/トレカ＋アクスタ中心</b>。立体・実用・本格アパレル系はまだ薄い＝伸びしろ大。</p>')
H.append('<p style="margin-top:14px;font-size:13px;font-weight:700;color:#d6336c">⬇ まだ出ていない ＝ KONNEKTEDの勝ち筋</p>')
H.append('<table class="tbl"><tr><th>未展開カテゴリ</th><th>なぜ空いてる</th></tr>')
for n,why in GOODS_GAP: H.append('<tr><td class="idea">⬜ '+esc(n)+'</td><td>'+esc(why)+'</td></tr>')
H.append('</table></div></section>')

# 5 propose
H.append('<section class="t-idea"><div class="sh"><span class="no">05</span><h2>🎯 KONNEKTED 提案ヒント</h2><span class="typ">IDEA</span></div>')
H.append('<div class="card" style="padding:14px"><p class="note" style="margin:0">3カテゴリ × このIPならではの具体アイデア（<b>過去グッズの空白と接続</b>）。※提案たたき台・要すり合わせ。</p>')
for p in PROPOSE:
    H.append('<div class="ptab"><div class="ph" style="background:'+p["tone"]+'18"><span class="dot" style="background:'+p["tone"]+'"></span>'+esc(p["cat"])+' <span class="s">'+esc(p["sub"])+'</span></div>')
    H.append('<table class="tbl" style="margin:0"><tr><th>アイデア</th><th>ねらい</th></tr>')
    for idea,aim in p["rows"]: H.append('<tr><td class="idea">'+esc(idea)+'</td><td>'+esc(aim)+'</td></tr>')
    H.append('</table></div>')
H.append('</div></section>')

# factcheck
H.append('<section class="t-warn"><div class="sh"><span class="no">!</span><h2>🔍 ファクトチェック</h2><span class="typ">CHECK</span></div><div class="card"><div class="fcwrap">')
H.append('<div class="fcbox ok"><h4>✅ 検証済み（一次照合）</h4><ul>')
for f in FC_OK: H.append('<li>'+f+'</li>')
H.append('</ul></div>')
H.append('<div class="fcbox ck"><h4>⚠️ 確定前に要確認</h4><ul>')
for item,note in FC_CHECK: H.append('<li><b>'+esc(item)+'</b>：'+esc(note)+'</li>')
H.append('</ul></div>')
H.append('</div></div></section>')

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
