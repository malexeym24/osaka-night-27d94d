#!/usr/bin/env python3
"""Minami Saturday-evening plans (24.10.2026). Run: python3 plan_build.py -> plan.html"""
import json, html
from urllib.parse import quote

def gm(q): return "https://www.google.com/maps/search/?api=1&query=" + quote(q)
def gimg(q): return "https://www.google.com/search?tbm=isch&q=" + quote(q)
def gdir(dst, mode="transit", origin="Hotel Granvia Osaka"):
    return f"https://www.google.com/maps/dir/?api=1&origin={quote(origin)}&destination={quote(dst)}&travelmode={mode}"

CC = json.load(open("credits.json"))
CC.update({
    "bar36-1.jpg": "Swissôtel Nankai Osaka, офиц. сайт", "bar36-2.jpg": "Swissôtel Nankai Osaka, офиц. сайт (днём)",
    "joule-1.jpg": "clubJOULE, офиц. сайт", "joule-2.jpg": "clubJOULE, терраса 4F, офиц. сайт", "joule-3.jpg": "clubJOULE, офиц. сайт",
    "ev-barinc.jpg": "Флаер 24.10, Resident Advisor", "ev-teranoma.jpg": "Флаер 24.10, Resident Advisor",
    "ev-teranoma2.jpg": "Тайминг 24.10, Resident Advisor", "ev-rake.jpg": "Флаер 24.10, Resident Advisor",
    "smoke-1.jpg": "Centara Grand Osaka, офиц. сайт", "nakaza-1.jpg": "GIRAFFE Japan, офиц. сайт",
    "giraffe-02.jpg": "GIRAFFE Japan, офиц. сайт", "giraffe-03.jpg": "GIRAFFE Japan, офиц. сайт", "giraffe-04.jpg": "GIRAFFE Japan, офиц. сайт",
})
R = json.load(open("plan_routes.json"))
PT = R["pts"]

# venue library
V = {
 "ebisu": dict(name="Ebisubashi и вывеска Glico", kind="walk", q="Ebisubashi Bridge Glico Sign Osaka",
   photos=["glico-1.jpg", "glico-3.jpg", "namba-2.jpg", "glico-4.jpg"],
   what="Центр неона: мост через канал Dotonbori, бегущий человек Glico (с 1935 года). Отсюда во все стороны улицы с огнями.",
   facts=[("Часы", "всегда")], links=[("Osaka Info", "https://osaka-info.jp/en/spot/dotonbori/")]),
 "mizuno": dict(name="Mizuno (美津の) - окономияки", kind="food", q="美津の 道頓堀 Mizuno okonomiyaki",
   photos=["okono-1.jpg", "okono-2.jpg"],
   what="Давняя (老舗) окономияки-лавка Dotonbori, по гидам 6 лет подряд в Michelin Bib Gourmand. Фирменное - yamaimo-yaki на тесте из горного ямса, готовят на плите-теппане. Часто очередь - лучше прийти к 19:00. Фото - окономияки в Осаке вообще, не сам Mizuno.",
   facts=[("Часы", "11:00-22:00, последний заказ 21:00, вых. чт"), ("Цены", "yamaimo-yaki 1 830 ¥, Mizuno-yaki 1 600 ¥ (данные 2024)")],
   links=[("Retty", "https://retty.me/restaurant/100000014901/"), ("Tabelog", "https://tabelog.com/rstLst/?sw=" + quote("美津の"))]),
 "hozenji": dict(name="Hozenji Yokocho", kind="walk", q="Hozenji Yokocho Osaka",
   photos=["hozenji-1.jpg", "hozenji-3.jpg", "hozenji-4.jpg", "hozenji-2.jpg"],
   what="Каменный переулок с фонарями в минуте от неона: маленький храм со статуей во мху (Mizukake Fudo, её поливают водой на удачу), крошечные бары.",
   facts=[("Часы", "всегда")], links=[("Osaka Info", "https://osaka-info.jp/en/spot/hozenji-yokocho/")]),
 "bar36": dict(name="Bar36 - Swissôtel Nankai, 36 этаж", kind="bar", q="Bar36 Swissotel Nankai Osaka",
   photos=["bar36-1.jpg", "bar36-2.jpg", "swiss-1.jpg"],
   what="Бар на самом верхнем этаже отеля над станцией Namba, 147 м, панорама на весь город. В соседнем зале Table36 по субботам 20:00-22:30 играет живая группа (Chroma Band). Самый поздний бар с видом в Minami.",
   facts=[("Часы", "сб 15:00-24:30, последний заказ 23:45"), ("Цены", "в ценах уже 13% сервис и налог; сбора за вход на сайте нет"), ("Тел.", "+81 6 6646 5125")],
   links=[("Сайт бара", "https://swissotelnankaiosaka.com/restaurants-bars/tavola36/")]),
 "smoke": dict(name="Smoke & Spin - Centara, 33 этаж (запасной)", kind="bar", q="Smoke & Spin Centara Grand Hotel Osaka",
   photos=["smoke-1.jpg"],
   what="Лаунж на 33 этаже с резидент-DJ каждый вечер, smart casual. Если в Bar36 нет мест - сюда, ~10 мин пешком на юг.",
   facts=[("Часы", "11:00-24:00, напитки до 23:30")],
   links=[("Сайт бара", "https://www.centarahotelsresorts.com/centaragrand/cgoj/smoke-and-spin"), ("TableCheck", "https://www.tablecheck.com/en/shops/centaragrand-osaka-smokeandspin/reserve")]),
 "giraffe": dict(name="GIRAFFE Japan - клуб с террасой над Dotonbori", kind="club", q="GIRAFFE Japan Nakaza Cuidaore Building Dotonbori 1-7-21",
   photos=["giraffe-04.jpg", "giraffe-02.jpg", "giraffe-03.jpg", "nakaza-1.jpg"],
   what="Большой клуб в доме Nakaza Cuidaore, 5 этаж, прямо у моста. Музыка по гидам смешанная (диско, хаус, поп, EDM), туристы и местные - проще всего познакомиться. На крыше руфтоп NAKAZA SKY TERRACE.",
   facts=[("Часы", "клуб 22:00-04:00 (до 22:00 там шоу)"), ("Вход", "билеты через Klook / GetYourGuide / Viator / Trip.com, цену не смотрел")],
   links=[("Сайт клуба", "https://giraffe-japan.com/nightclub"), ("Instagram", "https://www.instagram.com/giraffejapan/")]),
 "joule": dict(name="clubJOULE - MISHMASH Halloween B2B (вместо GIRAFFE)", kind="club", q="club JOULE Osaka 西心斎橋2-11-7",
   photos=["joule-1.jpg", "joule-2.jpg", "joule-3.jpg"],
   what="Один из главных клубов Осаки (с 1999), свой руфтоп-терраса на 4 этаже. Сегодня вечеринка MISHMASH: диджеи парами (B2B), хэллоуинская, жанр в анонсе не указан. Дресс-код smart casual, в выходные без шорт.",
   facts=[("Сегодня", "23:00-05:00"), ("Вход", "2 500 ¥; иностранцам 1 500 ¥; до 23 лет 2 000 ¥ с Jägermeister (офиц. сайт)")],
   links=[("Событие на сайте", "https://club-joule.com/events/mishmash-all-b2b-party-hallowen-edition/"), ("Гид по клубам", "https://www.osakatourism.org/best-nightclubs-in-osaka/")]),
 "barinc": dict(name="BAR Inc - Gonno (house / techno)", kind="club", q="BAR Inc 3-10-19 Minamisenba Osaka",
   photos=["ev-barinc.jpg"],
   what="Музыкальный бар с хорошим звуком. Сегодня WEEKEND SELECTERS: Gonno - один из главных японских диджеев house и techno, выходил на Ostgut Ton (лейбл Berghain), International Feel, Beats In Space. Андеграунд, не пафос.",
   facts=[("Сегодня", "20:00-03:00"), ("Вход", "2 000 ¥ (Resident Advisor)")],
   links=[("Resident Advisor", "https://ra.co/events/2538837"), ("Instagram", "https://www.instagram.com/bar_inc_osaka/")]),
 "teranoma": dict(name="MMIXUP × WAVE - deep house и визуалы", kind="club", q="大阪市中央区難波千日前4-19",
   photos=["ev-teranoma.jpg", "ev-teranoma2.jpg"],
   what="Вечеринка deep house с видеоартом в маленьком клубе Teranoma Tidepool (Ikeume Bldg, 4 этаж). Гость из Кореи Ruud в 01:00. О самой площадке в сети почти ничего - формат маленький, локальный.",
   facts=[("Сегодня", "21:00-05:00"), ("Вход", "1 500 ¥: до 22:00 с напитком, после + 1 напиток"),
          ("Тайминг", "21:00 KONDO Mitsuo · 22:20 Junki Akutagawa · 23:40 Curumayoi · 01:00 Ruud · 02:20 Sugar Do · 03:40 yu-more")],
   links=[("Resident Advisor", "https://ra.co/events/2561243")]),
 "rake": dict(name="AfterLife - progressive house (запасной)", kind="club", q="大阪市中央区宗右衛門町6-2-8",
   photos=["ev-rake.jpg"],
   what="Вечеринка progressive house и techno в баре rake?raka? в Soemoncho, у канала. Маленькое место.",
   facts=[("Сегодня", "22:00-05:00"), ("Вход", "2 000 ¥ (Resident Advisor)")],
   links=[("Resident Advisor", "https://ra.co/events/2529384")]),
 "arcade": dict(name="Shinsaibashi-suji - крытая улица", kind="walk", q="Shinsaibashi-suji Shopping Street",
   photos=["shinsaibashi-1.jpg", "shinsaibashi-2.jpg"],
   what="Длинная крытая пешеходная улица от станции Shinsaibashi прямо к мосту Ebisubashi, вечером людно.",
   facts=[("Часы", "улица всегда, магазины до ~21:00")], links=[]),
 "tombori": dict(name="Tombori River Walk - набережная канала", kind="walk", q="Tombori River Walk Osaka",
   photos=["tombori-1.jpg", "dotonbori-2.jpg", "dotonbori-1.jpg"],
   what="Пешеходная набережная вдоль канала Dotonbori ниже уровня улицы: огни отражаются в воде, тише, чем наверху.",
   facts=[("Часы", "всегда")], links=[("Osaka Info", "https://osaka-info.jp/en/spot/dotonbori/")]),
 "hidezou": dict(name="Ura-Namba: Sakanaya Hidezou (рыбный стоячий бар)", kind="food", q="魚屋ひでぞう 立ち呑み店 難波千日前",
   photos=["sennichi-1.jpg"],
   what="Ura-Namba - переулки за Namba, где пьют местные. Hidezou держит оптовый рыбный поставщик: стоя, свежая рыба, сакэ. По гидам легко зайти одному. Фото - улицы Sennichimae рядом.",
   facts=[("Часы", "не нашёл, смотри в Google Maps")],
   links=[("Tabelog: Ura-Namba", "https://tabelog.com/matome/5600/")]),
 "ajito": dict(name="Ura-Namba: Stand Ajito (стоячий бар-бистро)", kind="food", q="スタンドあじと 難波千日前",
   photos=[],
   what="Стоячая версия популярного бистро Dining Ajito: европейская еда и вино недорого. В 2 мин от Hidezou - можно зайти в оба.",
   facts=[("Часы", "не нашёл, смотри в Google Maps")], links=[]),
}

PLANS = [
 dict(id="A", title="Фэнси: ужин → вид с 36 этажа → клуб", tag="Рекомендую",
   intro="Классика пятницы-субботы в Minami: окономияки, неон, бокал над городом под живую музыку, потом клуб у канала. Около 2,7 км пешком за вечер.",
   start="Метро до Namba (8 мин), выход к Dotonbori, 5 мин до моста.",
   steps=[("18:45", "ebisu"), ("19:00", "mizuno"), ("20:30", "hozenji"), ("21:00", "bar36"), ("", "smoke"), ("23:00", "giraffe"), ("", "joule")],
   end="Домой: такси ~4 км до отеля, или метро из Namba до 00:10."),
 dict(id="B", title="House-музыка: от Gonno к deep house до утра", tag="Для музыки",
   intro="Если хочется именно хорошей электроники, а не пафоса. Места маленькие, андеграундные; публика пришла за музыкой.",
   start="Метро до Shinsaibashi (7 мин), 4 мин пешком до BAR Inc. Поесть заранее (например, в Shin-Umeda Shokudogai у отеля).",
   steps=[("20:00", "barinc"), ("22:00", "arcade"), ("22:30", "teranoma"), ("", "rake"), ("", "joule")],
   end="Домой: такси (метро после 00:10 не ходит)."),
 dict(id="C", title="Спокойно: прогулка, ужин, местные бары, бокал с видом", tag="Без клубов",
   intro="Посмотреть неон без спешки: крытая улица, мост, набережная, фонари Hozenji, ужин и стоячие бары Ura-Namba, в конце - вид с 36 этажа. Около 3 км пешком.",
   start="Метро до Shinsaibashi (7 мин) и пешком на юг по крытой улице.",
   steps=[("18:30", "arcade"), ("18:45", "ebisu"), ("19:00", "tombori"), ("19:20", "hozenji"), ("19:30", "mizuno"), ("21:00", "hidezou"), ("", "ajito"), ("22:30", "bar36")],
   end="Домой: последний поезд из Namba 00:10 → Umeda 00:19."),
]
COL = {"walk": "#7be08a", "food": "#ffb36b", "bar": "#e8b86b", "club": "#ff6fae"}
LAB = {"walk": "Прогулка", "food": "Еда / стоячий бар", "bar": "Бар с видом", "club": "Клуб / DJ"}

def a(label, url, cls="lnk"):
    return f'<a class="{cls}" href="{html.escape(url)}" target="_blank" rel="noopener">{html.escape(label)}</a>'

legs = {k: {(l[0], l[1]): (l[2], l[3]) for l in R["routes"][k]["legs"]} for k in R["routes"]}

def step_card(plan, i, t, key, nxt):
    v = V[key]; col = COL[v["kind"]]
    pics = "".join(f'<figure><img src="img/{f}" loading="lazy" alt="{html.escape(v["name"])}"><figcaption>{html.escape(CC.get(f, ""))}</figcaption></figure>' for f in v["photos"])
    cnt = f'<span class="cnt">{len(v["photos"])} фото →</span>' if len(v["photos"]) > 1 else ""
    gal = f'<div class="galw"><div class="gal">{pics}</div>{cnt}</div>' if pics else '<div class="nophoto">своих фото нет - кнопка «Ещё фото» ниже</div>'
    kv = "".join(f'<div class="k">{html.escape(k)}</div><div>{html.escape(x)}</div>' for k, x in v["facts"])
    links = [a("📍 Google Maps", gm(v["q"]), "lnk pri"), a("📷 Ещё фото", gimg(v["name"].split(" - ")[0].split(" (")[0] + " Osaka"))] + [a(l, u) for l, u in v["links"]]
    alt = '<span class="alt">или</span>' if not t else f'<span class="time">{t}</span>'
    nx = ""
    if nxt and (key, nxt) in legs[plan]:
        m, mins = legs[plan][(key, nxt)]
        nx = f'<div class="next">↓ дальше {mins} мин пешком ({m} м) · {a("маршрут", "https://www.google.com/maps/dir/?api=1&origin=" + quote(v["q"]) + "&destination=" + quote(V[nxt]["q"]) + "&travelmode=walking")}</div>'
    return f'''<div class="card"><div class="bd top"><div class="hd"><span class="num" style="background:{col}">{i}</span>{alt}<h2>{html.escape(v["name"])}</h2></div>
<div class="tag" style="color:{col}">{LAB[v["kind"]]}</div></div>{gal}<div class="bd">
<p class="why">{html.escape(v["what"])}</p><div class="kv">{kv}</div><div class="links">{" ".join(links)}</div></div></div>{nx}'''

secs = ""; js_plans = {}
for p in PLANS:
    cards = ""; pins = []
    seq = [k for _, k in p["steps"]]
    rseq = R["routes"][p["id"]]
    for i, (t, key) in enumerate(p["steps"], 1):
        nxt = seq[i] if i < len(seq) else None
        cards += step_card(p["id"], i, t, key, nxt)
        lat, lng = PT[key]
        pins.append(dict(n=i, lat=lat, lng=lng, name=V[key]["name"], col=COL[V[key]["kind"]]))
    js_plans[p["id"]] = dict(pins=pins, line=rseq["geom"])
    secs += f'''<section class="plan" id="plan{p["id"]}"><div class="ph"><span class="pid">{p["id"]}</span><div><div class="ptag">{p["tag"]}</div><h3>{html.escape(p["title"])}</h3></div></div>
<p class="intro">{html.escape(p["intro"])}</p><div class="box small2">🚇 <b>Старт:</b> {html.escape(p["start"])}</div>
{cards}<div class="box small2">🏨 {html.escape(p["end"])}</div></section>'''

nph = sum(len(V[k]["photos"]) for k in V)
PAGE = f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex,nofollow"><meta name="theme-color" content="#0b0d12"><title>Minami · план на субботу</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css">
<style>
:root{{--bg:#0b0d12;--card:#171b25;--card2:#1e2330;--ink:#eef0f5;--mute:#9aa2b4;--line:#2a3040;--acc:#e8b86b}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}}
.wrap{{max-width:720px;margin:0 auto;padding:14px 16px 40px}}h1{{font-size:24px;margin:6px 0 2px}}.sub{{color:var(--mute);font-size:13px}}a{{color:#7cc4ff}}
.box{{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:12px 14px;margin:12px 0}}.box h3{{margin:0 0 6px;font-size:16px;color:var(--acc)}}
ol{{margin:0;padding-left:20px}}li{{margin:4px 0}}.small2{{font-size:14px}}
.sticky{{position:sticky;top:0;z-index:500;background:var(--bg);padding:8px 0 6px}}
.pbtn{{display:grid;grid-template-columns:repeat(3,1fr);gap:6px}}.pbtn button{{min-height:44px;border-radius:12px;border:1px solid var(--line);background:var(--card2);color:var(--ink);font-weight:700;font-size:14px}}
.pbtn button.on{{background:var(--acc);color:#1a1205;border-color:var(--acc)}}
#map{{height:380px;border-radius:16px;border:1px solid var(--line);margin:10px 0}}
.pin{{width:28px;height:28px;border-radius:50%;color:#111;font:800 13px/28px -apple-system,sans-serif;text-align:center;border:2px solid #111;box-shadow:0 1px 4px rgba(0,0,0,.6)}}
.plan{{margin-top:18px;display:none}}.plan.on{{display:block}}.ph{{display:flex;gap:12px;align-items:center}}.pid{{flex:0 0 44px;height:44px;border-radius:12px;background:var(--acc);color:#1a1205;font:800 22px/44px -apple-system,sans-serif;text-align:center}}
.ph h3{{margin:0;font-size:20px}}.ptag{{font-size:12px;color:var(--acc);font-weight:700;text-transform:uppercase;letter-spacing:.05em}}.intro{{margin:8px 0;font-size:15px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:18px;overflow:hidden;margin:12px 0 4px}}
.galw{{position:relative}}.cnt{{position:absolute;right:8px;top:8px;background:rgba(0,0,0,.6);color:#fff;font-size:12px;padding:3px 8px;border-radius:999px;pointer-events:none}}
.gal{{display:flex;gap:4px;overflow-x:auto;scroll-snap-type:x mandatory;background:var(--card2)}}.gal figure{{margin:0;flex:0 0 86%;scroll-snap-align:start;position:relative}}.gal figure:only-child{{flex-basis:100%}}
.gal img{{width:100%;height:230px;object-fit:cover;display:block}}.gal figcaption{{position:absolute;left:0;right:0;bottom:0;font-size:10px;color:#ddd;background:linear-gradient(transparent,rgba(0,0,0,.7));padding:10px 8px 4px}}
.nophoto{{padding:10px 14px;color:var(--mute);font-size:12px;background:var(--card2)}}
.bd{{padding:12px 14px 14px}}.bd.top{{padding-bottom:8px}}.hd{{display:flex;gap:8px;align-items:center;flex-wrap:wrap}}h2{{margin:0;font-size:18px;flex:1 1 60%}}
.num{{flex:0 0 30px;height:30px;border-radius:50%;color:#111;font-weight:800;display:flex;align-items:center;justify-content:center}}
.time{{font-weight:800;color:var(--acc);font-size:15px}}.alt{{font-size:12px;color:var(--mute);border:1px solid var(--line);border-radius:999px;padding:1px 8px}}
.tag{{font-size:12px;font-weight:700;margin:2px 0 0 38px;text-transform:uppercase;letter-spacing:.04em}}
.why{{margin:0 0 8px;font-size:15px}}.kv{{display:grid;grid-template-columns:78px 1fr;gap:6px 10px;font-size:14px}}.k{{color:var(--mute)}}
.links{{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px}}.lnk{{display:inline-block;padding:7px 11px;border-radius:999px;border:1px solid var(--line);background:var(--card2);font-size:13px;text-decoration:none}}
.lnk.pri{{background:var(--acc);border-color:var(--acc);color:#1a1205;font-weight:700}}
.next{{font-size:13px;color:var(--mute);margin:2px 0 4px 14px}}
</style></head><body><div class="wrap">
<h1>Minami · суббота 24.10 вечером</h1>
<div class="sub">3 готовых плана по району неона: Dotonbori, Hozenji, Ura-Namba, Shinsaibashi · {nph} фото · проверено 24.10.2026 ~14:00 JST · <a href="./">все места Осаки</a></div>
<div class="box small2">🌤 <b>Погода:</b> вечером сухо, ~21°, дождь 7-18% (Open-Meteo). 🚇 <b>Туда:</b> от отеля 5 мин до станции Umeda, линия Midosuji (красная), платформа 1, на Nakamozu → Shinsaibashi 7 мин / Namba 8 мин. 🚇 <b>Обратно:</b> последний поезд Namba 00:10 → Umeda 00:19 (Shinsaibashi 00:12), платформа 2, на Shin-Osaka (Yahoo, сб 24.10). Позже - такси, ~4 км, водителю: ホテルグランヴィア大阪. <a href="{gdir("Namba Station Osaka Metro Midosuji Line")}" target="_blank" rel="noopener">маршрут до Namba</a></div>
<div class="sticky"><div class="pbtn"><button data-p="A" class="on">A · Фэнси</button><button data-p="B">B · House</button><button data-p="C">C · Спокойно</button></div></div>
<div id="map"></div>
{secs}
<div class="box sub">Источники: офиц. сайты Swissôtel, clubJOULE, Centara, GIRAFFE; Resident Advisor (события 24.10); Retty, mapple, Tabelog (Mizuno, Ura-Namba); Osaka Tourism (дресс-код, клубы). Фото: Wikimedia Commons (авторы на фото), сайты мест, флаеры RA. Маршруты пешком - OSRM, время ориентировочное.</div>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script>
<script>
var P={json.dumps(js_plans, ensure_ascii=False)};
var map=L.map('map');
L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{{z}}/{{y}}/{{x}}',{{attribution:'Tiles © Esri',maxZoom:18}}).addTo(map);
var layer=L.layerGroup().addTo(map);
function show(id){{
  layer.clearLayers(); var p=P[id], b=[];
  L.polyline(p.line,{{color:'#e8b86b',weight:4,opacity:.85,dashArray:'6 6'}}).addTo(layer);
  p.pins.forEach(function(x){{
    var ic=L.divIcon({{className:'',html:'<div class="pin" style="background:'+x.col+'">'+x.n+'</div>',iconSize:[28,28],iconAnchor:[14,14]}});
    L.marker([x.lat,x.lng],{{icon:ic}}).addTo(layer).bindPopup('<b>'+x.n+'. '+x.name+'</b>'); b.push([x.lat,x.lng]);
  }});
  map.fitBounds(b,{{padding:[28,28]}});
  document.querySelectorAll('.pbtn button').forEach(function(x){{x.classList.toggle('on',x.dataset.p===id);}});
  document.querySelectorAll('.plan').forEach(function(s){{s.classList.toggle('on',s.id==='plan'+id);}});
}}
document.querySelectorAll('.pbtn button').forEach(function(btn){{btn.onclick=function(){{show(btn.dataset.p); document.getElementById('map').scrollIntoView({{behavior:'smooth',block:'center'}});}};}});
show('A');
</script>
<script src="lightbox.js?v=4" defer></script>
</body></html>'''
open("plan.html", "w").write(PAGE)
print("ok", len(PAGE), "photos", nph)
