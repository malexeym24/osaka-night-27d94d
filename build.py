#!/usr/bin/env python3
"""Osaka Friday night page (23.10.2026). Run: python3 build.py -> index.html"""
import json, html
from urllib.parse import quote

def gm(q):
    return "https://www.google.com/maps/search/?api=1&query=" + quote(q)

def gdir(dst, mode="walking", origin="Hotel Granvia Osaka"):
    return (f"https://www.google.com/maps/dir/?api=1&origin={quote(origin)}"
            f"&destination={quote(dst)}&travelmode={mode}")

CC = json.load(open("credits.json"))
CC.update({
    "smoke-1.jpg": "Centara Grand Osaka, офиц. сайт",
    "nakaza-1.jpg": "GIRAFFE Japan, офиц. сайт",
    "giraffe-02.jpg": "GIRAFFE Japan, офиц. сайт",
    "giraffe-03.jpg": "GIRAFFE Japan, офиц. сайт",
    "giraffe-04.jpg": "GIRAFFE Japan, офиц. сайт",
    "canes-1.jpg": "Time Out Osaka",
})

# kind: hotel / view / bar / club / walk
P = [
 # ---------- KITA / UMEDA ----------
 dict(n=0, zone="kita", kind="hotel", name="Hotel Granvia Osaka - ты здесь", ll=(34.701881, 135.496338),
      q="Hotel Granvia Osaka", photos=["osakast-1.jpg"],
      hours="", what="Отель в здании станции JR Osaka (Umeda). Отсюда всё в Umeda пешком 5-15 мин, до Minami 8 мин на метро.",
      dir=None),
 dict(n=1, zone="kita", kind="view", name="Umeda Sky Building - смотровая на крыше", ll=(34.70529, 135.49053),
      q="Umeda Sky Building Floating Garden Observatory", photos=["sky-2.jpg", "sky-1.jpg"],
      hours="9:30-22:30, вход до 22:00 · 2 000 ¥", walk="~15 мин пешком",
      what="Открытая круговая площадка на крыше 173 м между двумя башнями, ночная панорама всего города. Наверх через стеклянную трубу-эскалатор.",
      src="ANA travel planner, справочные сайты"),
 dict(n=2, zone="kita", kind="bar", name="Canes & Tales - бар Waldorf Astoria", ll=(34.70278, 135.49149),
      q="Canes & Tales Waldorf Astoria Osaka", photos=["canes-1.jpg"],
      hours="пт-сб 17:00-01:00 (последний заказ 00:30)", walk="~13 мин",
      what="Новый (2025) коктейльный бар-«спикизи» отеля Waldorf Astoria в стиле 1920-х, по входу без брони. Самый поздний из фэнси-баров рядом с отелем. Какая музыка - не проверял.",
      src="Hilton (офиц.), Time Out"),
 dict(n=3, zone="kita", kind="bar", name="ADEE - бар InterContinental, 20 этаж", ll=(34.70652, 135.49456),
      q="InterContinental Osaka adee Lounge & Bar", photos=[],
      hours="пт 17:00-23:30 (заказ до 23:00)", walk="~13 мин",
      what="Лаунж-бар с видом на Umeda с 20 этажа, Grand Front Osaka. Спокойный, для коктейля с видом.",
      src="icosaka.com (офиц.)"),
 dict(n=4, zone="kita", kind="view", name="Колесо обозрения HEP FIVE", ll=(34.70406, 135.50038),
      q="HEP FIVE Ferris Wheel", photos=["hep-2.jpg", "hep-1.jpg"],
      hours="11:00-23:00, посадка до 22:45 · ~1 000 ¥", walk="~8 мин",
      what="Красное колесо на крыше торгового центра в центре Umeda, круг ~15 мин. С октября 2025 по весну 2026 было на ремонте - что открылось, я не подтвердил, глянь на входе.",
      src="osaka-info.jp"),
 dict(n=5, zone="kita", kind="walk", name="Ohatsu Tenjin и переулки Urasando", ll=(34.69913, 135.50084),
      q="Ohatsutenjin Urasando Osaka", photos=["ohatsu-1.jpg", "ohatsu-2.jpg"],
      hours="izakaya обычно до ночи, часы у каждого свои", walk="~8 мин",
      what="Святилище посреди Umeda и улочки за ним: izakaya, стоячие бары, местные после работы. Самое живое место в Umeda, где проще разговориться.",
      src="гиды (magical-trip), не офиц."),
 dict(n=6, zone="kita", kind="bar", name="Kitashinchi - дорогой барный квартал", ll=(34.69839, 135.49727),
      q="Kitashinchi Osaka", photos=[],
      hours="бары до ночи", walk="~5 мин",
      what="«Гинза Осаки»: костюмы, каблуки, сотни баров в многоэтажках. Важно: вывески «club» и «lounge» здесь обычно = хостес-клубы (очень дорого, не для знакомств). Заходи только в коктейль-бары, зазывал игнорируй.",
      src="Osaka Tourism (Kitashinchi guide)"),
 dict(n=7, zone="kita", kind="bar", name="40 Sky Bar & Lounge - Conrad, 40 этаж", ll=(34.69359, 135.49547),
      q="40 Sky Bar & Lounge Conrad Osaka", photos=["conrad-1.jpg"],
      hours="ср-сб 11:00-24:00 · с 20:00 до 22:30 сбор 1 650 ¥", walk="~13 мин",
      what="Самый высокий бар с видом в Kita, Nakanoshima. Фэнси, иногда живая музыка; публика в основном за столиками.",
      src="Hilton (офиц.), TableCheck"),
 dict(n=8, zone="kita", kind="walk", name="Grand Green Osaka - новый парк у станции", ll=(34.70367, 135.49240),
      q="Grand Green Osaka Umekita Park", photos=["umekita-1.jpg"],
      hours="ночные часы парка не проверял", walk="~12 мин",
      what="Новый городской парк (2024-2025) сразу к северу от станции, между небоскрёбами. Тихая прогулка по пути к Umeda Sky.",
      src="Wikimedia"),
 # ---------- MINAMI ----------
 dict(n=9, zone="minami", kind="walk", name="Shinsaibashi-suji - крытая улица", ll=(34.67067, 135.50133),
      q="Shinsaibashi-suji Shopping Street", photos=["shinsaibashi-1.jpg", "shinsaibashi-2.jpg"],
      hours="улица открыта всегда, магазины до ~21:00", walk="от станции Shinsaibashi ~10 мин до моста",
      what="Длинная крытая пешеходная улица от станции Shinsaibashi прямо к мосту Ebisubashi. Вечером уже без магазинов, но людно.",
      src="Wikimedia"),
 dict(n=10, zone="minami", kind="walk", name="Ebisubashi, вывеска Glico и канал Dotonbori", ll=(34.66907, 135.50130),
      q="Ebisubashi Bridge Glico Sign Osaka", photos=["glico-1.jpg", "glico-2.jpg", "dotonbori-2.jpg", "dotonbori-1.jpg"],
      hours="всегда", walk="от станции Namba ~5 мин",
      what="Тот самый неон Осаки: мост, бегущий человек Glico, огни над каналом. По обоим берегам набережная, вдоль неё бары и рестораны до поздней ночи.",
      src="Wikimedia"),
 dict(n=11, zone="minami", kind="bar", name="NAKAZA SKY TERRACE - руфтоп над Dotonbori", ll=(34.66869, 135.502533),
      q="GIRAFFE Japan Nakaza Cuidaore Building Dotonbori 1-7-21", photos=["nakaza-1.jpg"],
      hours="ночные часы на сайте не указаны · по выходным вечером DJ", walk="~2 мин от Ebisubashi",
      what="Открытая терраса на крыше прямо над каналом: кальян, коктейли, по выходным DJ (по описанию на сайте). Под дождём неуютно - лучше до 23:00. Бронь через их LINE.",
      src="giraffe-japan.com (офиц.)"),
 dict(n=12, zone="minami", kind="club", name="GIRAFFE Japan - клуб, тот же дом, 5 этаж", ll=(34.66860, 135.50265),
      q="GIRAFFE Japan Nakaza Cuidaore Building Dotonbori 1-7-21", photos=["giraffe-04.jpg", "giraffe-02.jpg", "giraffe-03.jpg"],
      hours="22:00-04:00 · с 19:00 до 22:00 там шоу", walk="~2 мин от Ebisubashi",
      what="Большой коммерческий клуб, возрождённая легенда Minami (2025): звук d&b, дорогое шампанское, своя терраса. Музыка по гидам смешанная (EDM, хип-хоп, хаус). Туристы + местные - проще всего познакомиться. Билеты через Klook / GetYourGuide / Viator / Trip.com, цену не смотрел.",
      src="giraffe-japan.com (офиц.), Osaka Tourism"),
 dict(n=13, zone="minami", kind="walk", name="Hozenji Yokocho - переулок с фонарями", ll=(34.66818, 135.50267),
      q="Hozenji Yokocho Osaka", photos=["hozenji-1.jpg", "hozenji-2.jpg"],
      hours="всегда · бары до ночи", walk="~2 мин от Nakaza",
      what="Узкий каменный переулок старой Осаки: фонари, маленький храм со статуей во мху, крошечные бары и рестораны. Тихий контраст рядом с неоном.",
      src="Wikimedia"),
 dict(n=14, zone="minami", kind="bar", name="Smoke & Spin - руфтоп-лаунж Centara, 33 этаж", ll=(34.66015, 135.50224),
      q="Smoke & Spin Centara Grand Hotel Osaka", photos=["smoke-1.jpg"],
      hours="11:00-24:00 (напитки до 23:30) · smart casual", walk="~16 мин от Hozenji, на юг",
      what="Лаунж на 33 этаже (135 м) с видом на Namba, по сайту резидент-DJ каждый вечер. Под крышей - дождь не страшен.",
      src="centarahotelsresorts.com (офиц.)"),
 dict(n=15, zone="minami", kind="club", name="GHOST ultra lounge - Amerikamura", ll=(34.671082, 135.497574),
      q="GHOST ultra lounge 2-17-3 Nishishinsaibashi Osaka", photos=[],
      hours="22:00-05:00 (по гидам, офиц. сайта не нашёл)", walk="~8 мин от Ebisubashi",
      what="Лаунж-клуб в подвале, публика наряднее среднего; музыка по разным гидам от хип-хопа до хауса. Нужен паспорт (20+).",
      src="Agoda, Culture Trip, tablejourney - не офиц."),
 dict(n=16, zone="minami", kind="club", name="BAR Inc - DJ-бар (сегодня house / techno)", ll=(34.677105, 135.500626),
      q="BAR Inc 3-10-19 Minamisenba Osaka", photos=[],
      hours="сегодня 20:00-03:00 · WEEKEND SELECTERS", walk="~4 мин от станции Shinsaibashi",
      what="Небольшой музыкальный бар с хорошим звуком, сегодня Benedek, SFV Acid, Daisuke Kakimoto. Это андеграунд, не пафос - если хочется именно музыки.",
      src="Resident Advisor 23.10"),
]

KIND = {"hotel": ("#ffffff", "Отель"), "view": ("#6fc3ff", "Вид"), "bar": ("#e8b86b", "Бар / руфтоп"),
        "club": ("#ff6fae", "Клуб / DJ"), "walk": ("#7be08a", "Прогулка")}

def card(p):
    col, lab = KIND[p["kind"]]
    pics = "".join(
        f'<figure><img src="img/{f}" loading="lazy" alt="{html.escape(p["name"])}"><figcaption>{html.escape(CC.get(f, ""))}</figcaption></figure>'
        for f in p["photos"])
    gal = f'<div class="gal">{pics}</div>' if pics else '<div class="nophoto">фото не нашёл в открытых источниках</div>'
    kv = ""
    if p.get("hours"): kv += f'<div class="k">Часы</div><div><b>{html.escape(p["hours"])}</b></div>'
    if p.get("walk"): kv += f'<div class="k">Как далеко</div><div>{html.escape(p["walk"])}</div>'
    if p.get("src"): kv += f'<div class="k">Источник</div><div class="small">{html.escape(p["src"])}</div>'
    btns = f'<a class="btn pri" href="{gm(p["q"])}" target="_blank" rel="noopener">📍 Google Maps</a>'
    if p["zone"] == "kita" and p["kind"] != "hotel":
        btns += f'<a class="btn" href="{gdir(p["q"])}" target="_blank" rel="noopener">🚶 Пешком от отеля</a>'
    elif p["zone"] == "minami":
        btns += f'<a class="btn" href="{gdir(p["q"], "transit")}" target="_blank" rel="noopener">🚇 Маршрут от отеля</a>'
    return f'''<div class="card" id="p{p["n"]}">{gal}<div class="bd">
<div class="hd"><span class="num" style="background:{col}">{p["n"] if p["n"] else "★"}</span><h2>{html.escape(p["name"])}</h2></div>
<div class="tag" style="color:{col}">{lab}</div>
<p class="why">{html.escape(p["what"])}</p><div class="kv">{kv}</div><div class="btns">{btns}</div></div></div>'''

kita = "".join(card(p) for p in P if p["zone"] == "kita")
minami = "".join(card(p) for p in P if p["zone"] == "minami")
markers = json.dumps([dict(n=p["n"], lat=p["ll"][0], lng=p["ll"][1], name=p["name"],
                           col=KIND[p["kind"]][0]) for p in P], ensure_ascii=False)

T = "https://www.google.com/maps/dir/?api=1&origin=" + quote("Hotel Granvia Osaka")
PAGE = f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex,nofollow"><meta name="theme-color" content="#0b0d12"><title>Osaka · пятница вечером</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css">
<style>
:root{{--bg:#0b0d12;--card:#171b25;--card2:#1e2330;--ink:#eef0f5;--mute:#9aa2b4;--line:#2a3040;--acc:#e8b86b;--warn:#ff8a7a}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}}
.wrap{{max-width:720px;margin:0 auto;padding:14px 16px 40px}}h1{{font-size:24px;margin:6px 0 2px}}.sub{{color:var(--mute);font-size:13px}}
a{{color:#7cc4ff}}.box{{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:12px 14px;margin:12px 0}}
.box h3{{margin:0 0 6px;font-size:16px;color:var(--acc)}}ul,ol{{margin:0;padding-left:20px}}li{{margin:4px 0}}
#map{{height:460px;border-radius:16px;border:1px solid var(--line);margin:12px 0}}
.zbtn{{display:flex;gap:8px;margin-top:-4px}}.zbtn button{{flex:1;min-height:40px;border-radius:12px;border:1px solid var(--line);background:var(--card2);color:var(--ink);font-weight:600;font-size:14px}}
.legend{{display:flex;flex-wrap:wrap;gap:6px 12px;font-size:13px;color:var(--mute);margin:8px 0}}.legend i{{display:inline-block;width:11px;height:11px;border-radius:50%;margin-right:5px;vertical-align:-1px}}
.pin{{width:28px;height:28px;border-radius:50%;color:#111;font:800 13px/28px -apple-system,sans-serif;text-align:center;border:2px solid #111;box-shadow:0 1px 4px rgba(0,0,0,.6)}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:18px;overflow:hidden;margin:16px 0}}
.gal{{display:flex;gap:4px;overflow-x:auto;scroll-snap-type:x mandatory;background:var(--card2)}}
.gal figure{{margin:0;flex:0 0 88%;scroll-snap-align:start;position:relative}}.gal figure:only-child{{flex-basis:100%}}
.gal img{{width:100%;height:220px;object-fit:cover;display:block}}.gal figcaption{{position:absolute;left:0;right:0;bottom:0;font-size:10px;color:#ddd;background:linear-gradient(transparent,rgba(0,0,0,.7));padding:10px 8px 4px}}
.nophoto{{padding:10px 14px;color:var(--mute);font-size:12px;background:var(--card2)}}
.bd{{padding:12px 14px 14px}}.hd{{display:flex;gap:10px;align-items:center}}h2{{margin:0;font-size:19px}}
.num{{flex:0 0 30px;height:30px;border-radius:50%;color:#111;font-weight:800;display:flex;align-items:center;justify-content:center}}
.tag{{font-size:12px;font-weight:700;margin:4px 0 0 40px;text-transform:uppercase;letter-spacing:.04em}}
.why{{margin:8px 0;font-size:15px}}.kv{{display:grid;grid-template-columns:96px 1fr;gap:6px 10px;font-size:14px;margin-top:10px}}.k{{color:var(--mute)}}
.btns{{display:flex;gap:8px;margin-top:12px}}.btn{{flex:1;display:flex;align-items:center;justify-content:center;min-height:46px;border-radius:12px;border:1px solid var(--line);background:var(--card2);color:var(--ink);text-decoration:none;font-weight:600;font-size:14px;text-align:center}}
.btn.pri{{background:var(--acc);border-color:var(--acc);color:#1a1205}}
.sech{{font-size:21px;margin:28px 0 2px;color:var(--acc)}}.small{{font-size:12px;color:var(--mute)}}
.warn{{border-left:3px solid var(--warn);background:var(--card2);padding:8px 10px;border-radius:8px;font-size:14px;margin-top:10px}}
table{{width:100%;border-collapse:collapse;font-size:14px}}td{{padding:6px 4px;border-bottom:1px solid var(--line);vertical-align:top}}td.t{{color:var(--acc);font-weight:700;white-space:nowrap}}
</style></head><body><div class="wrap">
<h1>Osaka · пятница 23.10 вечером</h1>
<div class="sub">Где ты и куда пойти: бары с видом, клубы, прогулки · проверено 23.10.2026 ~21:10 JST</div>

<div class="warn">☔ Дождь с ~23:00 (84%), сильный после 01:00 (Open-Meteo). Открытые крыши - до 23:00, зонт с собой.</div>

<div id="map"></div>
<div class="zbtn"><button data-z="all">Вся Осака</button><button data-z="kita">Мой район (Umeda)</button><button data-z="minami">Minami (неон)</button></div>
<div class="legend"><span><i style="background:#fff"></i>отель</span><span><i style="background:#e8b86b"></i>бар / руфтоп</span><span><i style="background:#ff6fae"></i>клуб / DJ</span><span><i style="background:#6fc3ff"></i>вид</span><span><i style="background:#7be08a"></i>прогулка</span></div>

<div class="box"><h3>⏰ До скольки работает Осака</h3>
<table>
<tr><td class="t">до 22:30-23:00</td><td>Смотровые: Umeda Sky (вход до 22:00), колесо HEP FIVE (посадка до 22:45)</td></tr>
<tr><td class="t">до 23:30-24:00</td><td>Бары отелей с видом: ADEE (23:30), Smoke & Spin и 40 Sky Bar (24:00)</td></tr>
<tr><td class="t">до 01:00</td><td>Canes & Tales, Waldorf Astoria (пт-сб)</td></tr>
<tr><td class="t">до 03:00-05:00</td><td>Клубы и DJ-бары: GIRAFFE 22-04, GHOST 22-05, BAR Inc сегодня 20-03</td></tr>
<tr><td class="t">00:10</td><td><b>Последнее метро</b> Namba → Umeda (в 00:19 у отеля). Позже - такси, ~4 км</td></tr>
</table>
<div class="small" style="margin-top:6px">Как в Токио: всё красивое с видом закрывается к 23-24. Дальше до утра живут клубы и DJ-бары, в основном в Minami.</div></div>

<div class="box"><h3>🚇 Как доехать до неона (Minami)</h3><ol>
<li>От отеля ~5 мин пешком до станции <b>Umeda</b>, линия <b>Midosuji (красная)</b>, платформа 1, поезд на <b>Nakamozu</b>. <a href="{gm("Umeda Station Osaka Metro Midosuji Line")}" target="_blank" rel="noopener">📍 станция</a></li>
<li>Остановки: Yodoyabashi → Hommachi → <b>Shinsaibashi</b> (~7 мин) или дальше до <b>Namba</b> (8 мин). Поезда каждые несколько минут. <a href="{gdir("Namba Station Osaka Metro Midosuji Line", "transit")}" target="_blank" rel="noopener">🚇 маршрут</a></li>
<li>Из Shinsaibashi - 10 мин пешком по крытой улице Shinsaibashi-suji до моста Ebisubashi. Из Namba - 5 мин.</li>
<li><b>Обратно:</b> последний поезд Namba 00:10 → Umeda 00:19 (платформа 2, на Shin-Osaka). Позже - <a href="{gdir("Hotel Granvia Osaka", "driving", "Ebisubashi Bridge Osaka")}" target="_blank" rel="noopener">🚕 такси до отеля</a>, без пробок ~7 мин, цену не проверял.</li>
</ol></div>

<div class="sech">Мой район · Umeda и Kitashinchi (пешком)</div>
<div class="sub">Вечером здесь больше бары отелей с видом и izakaya; клубы с расписанием на сегодня, которые я нашёл, все в Minami.</div>
{kita}
<div class="sech">Minami · Dotonbori, Shinsaibashi, Namba (8 мин на метро)</div>
<div class="sub">Главная пятничная Осака: неон, канал, переулки, руфтопы и клубы рядом друг с другом.</div>
{minami}
<div class="box small">Не на сегодня: clubJOULE (большой клуб с руфтопом) - событий на 23.10 на сайте нет, ближайшее 24.10. По Resident Advisor сегодня ещё в основном техно (Circus, Blvck Water). Фото: Wikimedia Commons (авторы на фото) и официальные сайты мест.</div>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script>
<script>
var M={markers};
var map=L.map('map',{{zoomControl:true}});
L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{{z}}/{{y}}/{{x}}',{{attribution:'Tiles © Esri',maxZoom:18}}).addTo(map);
var all=[],kita=[],minami=[];
M.forEach(function(p){{
  var ic=L.divIcon({{className:'',html:'<div class="pin" style="background:'+p.col+'">'+(p.n||'★')+'</div>',iconSize:[28,28],iconAnchor:[14,14]}});
  var m=L.marker([p.lat,p.lng],{{icon:ic,zIndexOffset:p.n?0:1000}}).addTo(map);
  m.bindPopup('<b>'+(p.n||'★')+'. '+p.name+'</b><br><a href="#p'+p.n+'">подробнее ↓</a>');
  all.push([p.lat,p.lng]); (p.lat>34.685?kita:minami).push([p.lat,p.lng]);
}});
var Z={{all:all,kita:kita,minami:minami}};
map.fitBounds(all,{{padding:[20,20]}});
document.querySelectorAll('.zbtn button').forEach(function(b){{b.onclick=function(){{map.fitBounds(Z[b.dataset.z],{{padding:[24,24]}});}};}});
</script>
<script src="lightbox.js?v=4" defer></script>
</body></html>'''
open("index.html", "w").write(PAGE)
print("ok", len(PAGE))
