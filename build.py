#!/usr/bin/env python3
"""Osaka evening / night map (built 23.10.2026, v2 24.10.2026). Run: python3 build.py -> index.html"""
import json, html
from urllib.parse import quote

def gm(q):
    return "https://www.google.com/maps/search/?api=1&query=" + quote(q)

def gdir(dst, mode="walking", origin="Hotel Granvia Osaka"):
    return (f"https://www.google.com/maps/dir/?api=1&origin={quote(origin)}"
            f"&destination={quote(dst)}&travelmode={mode}")

def gimg(q):
    return "https://www.google.com/search?tbm=isch&q=" + quote(q)

def wja(t):
    return "https://ja.wikipedia.org/wiki/" + quote(t)

def tabelog(q):
    return "https://tabelog.com/rstLst/?sw=" + quote(q)

CC = json.load(open("credits.json"))
CC.update({
    "smoke-1.jpg": "Centara Grand Osaka, офиц. сайт",
    "nakaza-1.jpg": "GIRAFFE Japan, офиц. сайт",
    "giraffe-01.jpg": "GIRAFFE Japan, офиц. сайт",
    "giraffe-02.jpg": "GIRAFFE Japan, офиц. сайт",
    "giraffe-03.jpg": "GIRAFFE Japan, офиц. сайт",
    "giraffe-04.jpg": "GIRAFFE Japan, офиц. сайт",
    "canes-1.jpg": "Time Out Osaka",
    "sky40-1.jpg": "Conrad Osaka, TableCheck",
})

# kind: hotel / view / bar / club / walk ; subs = bars inside an area card (no own pin)
P = [
 # ---------- KITA / UMEDA ----------
 dict(n=0, zone="kita", kind="hotel", name="Hotel Granvia Osaka - ты здесь", ll=(34.701881, 135.496338),
      q="Hotel Granvia Osaka", photos=["osakast-1.jpg", "toki-1.jpg"],
      what="Отель в здании станции JR Osaka (Umeda). Отсюда всё в Umeda пешком 5-15 мин, до Minami 8 мин на метро.",
      links=[("Сайт отеля", "https://www.granvia-osaka.jp/"), ("Wikipedia (ja)", wja("ホテルグランヴィア大阪"))]),
 dict(n=17, zone="kita", kind="view", name="Toki no Hiroba - площадь над путями", ll=(34.702383, 135.495897),
      q="Toki no Hiroba Osaka Station City", photos=["toki-1.jpg", "toki-2.jpg"],
      hours="8:00-23:30 (по справочным сайтам)", walk="~1 мин, 5 этаж станции",
      what="Площадь с большими часами на 5 этаже станции Osaka, прямо над платформами: сверху видно поезда и стеклянную крышу. Выше на 11 и 14 этажах - сады на крыше станции.",
      src="справочные сайты (iko-yo, happyell)",
      links=[("Osaka Station City", "https://osakastationcity.com/"), ("Wikipedia (ja)", wja("大阪ステーションシティ"))]),
 dict(n=18, zone="kita", kind="walk", name="Shin-Umeda Shokudogai - бары под путями", ll=(34.703907, 135.49791),
      q="Shin-Umeda Shokudogai", photos=["shokudo-1.jpg", "shokudo-2.jpg", "shokudo-3.jpg"],
      hours="обычно 11:00-23:00, у каждого места свои", walk="~3-7 мин",
      what="Старый (с 1950 года) проход под железной дорогой у восточного выхода станции: около 100 крошечных izakaya, стоячих баров, кушикацу и окономияки.",
      src="Walkerplus, Wikipedia (ja)",
      links=[("Wikipedia (ja)", wja("新梅田食道街")), ("Walkerplus", "https://summer.walkerplus.com/odekake/detail/ar0727s559244/")]),
 dict(n=1, zone="kita", kind="view", name="Umeda Sky Building - смотровая на крыше", ll=(34.70529, 135.49053),
      q="Umeda Sky Building Floating Garden Observatory", photos=["sky-3.jpg", "sky-4.jpg", "sky-5.jpg", "sky-2.jpg", "sky-1.jpg"],
      hours="9:30-22:30, вход до 22:00 · 2 000 ¥", walk="~15 мин пешком",
      what="Открытая круговая площадка на крыше 173 м между двумя башнями, ночная панорама всего города. Наверх через стеклянную трубу-эскалатор. С 30.10 там коллаборация с аниме My Hero Academia.",
      src="ANA travel planner, справочные сайты",
      links=[("Osaka Info", "https://osaka-info.jp/en/spot/umeda-sky-building-kuchu-teien-observatory/"), ("Wikipedia", "https://en.wikipedia.org/wiki/Umeda_Sky_Building")]),
 dict(n=2, zone="kita", kind="bar", name="Canes & Tales - бар Waldorf Astoria", ll=(34.70278, 135.49149),
      q="Canes & Tales Waldorf Astoria Osaka", photos=["canes-1.jpg"],
      hours="пт-сб 17:00-01:00 (заказ до 00:30), вс-чт до 24:00", walk="~13 мин",
      what="Коктейльный бар-«спикизи» отеля Waldorf Astoria в стиле 1920-х, открыт с 2025, по входу без брони. Самый поздний из фэнси-баров рядом с отелем. Какая музыка - не проверял.",
      src="Hilton (офиц.), Time Out",
      links=[("Сайт бара (Hilton)", "https://www.hilton.com/en/hotels/osawawa-waldorf-astoria-osaka/dining/canes-tales"), ("Time Out", "https://www.timeout.com/osaka/bars-and-pubs/canes-tales"), ("TableCheck", "https://www.tablecheck.com/en/shops/waldorf-astoria-osaka-canesandtales/reserve")]),
 dict(n=3, zone="kita", kind="bar", name="ADEE - бар InterContinental, 20 этаж", ll=(34.70652, 135.49456),
      q="InterContinental Osaka adee Lounge & Bar", photos=["gfo-1.jpg"],
      hours="пн-чт 17:00-23:00 · пт 17:00-23:30 · сб 14:00-23:30 · вс 14:00-23:00", walk="~13 мин",
      what="Лаунж-бар с видом на Umeda с 20 этажа башни Grand Front Osaka (на фото). Спокойный, для коктейля с видом.",
      src="icosaka.com (офиц.)",
      links=[("Сайт бара", "https://icosaka.com/en/restaurant/adee"), ("TableCheck", "https://www.tablecheck.com/en/shops/intercontinental-osaka-adee/reserve")]),
 dict(n=4, zone="kita", kind="view", name="Колесо обозрения HEP FIVE", ll=(34.70406, 135.50038),
      q="HEP FIVE Ferris Wheel", photos=["hep-2.jpg", "hep-3.jpg", "hep-1.jpg"],
      hours="11:00-23:00, посадка до 22:45 · ~1 000 ¥", walk="~8 мин",
      what="Красное колесо на крыше торгового центра в центре Umeda, круг ~15 мин. С октября 2025 по весну 2026 было на ремонте - что открылось, я не подтвердил, глянь на входе.",
      src="osaka-info.jp",
      links=[("Сайт HEP FIVE", "https://www.hepfive.jp/"), ("Osaka Info", "https://osaka-info.jp/en/spot/hep-five-ferris-wheel"), ("Wikipedia", "https://en.wikipedia.org/wiki/HEP_Five")]),
 dict(n=19, zone="kita", kind="walk", name="Hankyu Higashi-dori - главная улица баров Umeda", ll=(34.70233, 135.50058),
      q="Hankyu Higashi-dori Shopping Street Osaka", photos=["higashi-1.jpg", "higashi-2.jpg", "higashi-3.jpg"],
      hours="до ночи, у каждого места свои", walk="~8 мин",
      what="Крытая улица баров, izakaya, караоке и игровых залов. По официальному туристическому сайту Осаки - крупнейший квартал развлечений Kita. Молодёжь и офисные после работы. Зазывал игнорируй.",
      src="osaka-info.jp (офиц.)",
      links=[("Osaka Info", "https://osaka-info.jp/special/coolosaka/en/cool-night/719/"), ("Wikipedia (ja)", wja("阪急東通商店街"))]),
 dict(n=5, zone="kita", kind="walk", name="Ohatsu Tenjin и переулки Urasando", ll=(34.69913, 135.50084),
      q="Ohatsutenjin Urasando Osaka", photos=["ohatsu-1.jpg", "ohatsu-3.jpg", "ohatsu-4.jpg", "ohatsu-2.jpg"],
      hours="izakaya обычно до ночи", walk="~8 мин",
      what="Святилище Tsuyu no Tenjin (Ohatsu Tenjin) посреди Umeda, за ним улочки Urasando с маленькими барами и izakaya. Местные, легко разговориться.",
      src="гиды (magical-trip), офиц. сайт святилища",
      links=[("Сайт святилища", "https://www.tuyutenjin.com/"), ("Wikipedia (ja)", wja("露天神社"))]),
 dict(n=6, zone="kita", kind="bar", name="Kitashinchi - дорогой барный квартал", ll=(34.69839, 135.49727),
      q="Kitashinchi Osaka", photos=["shinchi-1.jpg"],
      hours="бары до ночи", walk="~5 мин",
      what="«Гинза Осаки»: костюмы, каблуки, сотни баров в многоэтажках. Вывески «club» и «lounge» здесь обычно = хостес-клубы (очень дорого, не для знакомств). Заходи в коктейль-бары, зазывал игнорируй.",
      src="Osaka Tourism (Kitashinchi guide)",
      links=[("Гид по Kitashinchi", "https://www.osakatourism.org/kitashinchi-guide/"), ("Wikipedia (ja)", wja("北新地"))]),
 dict(n=7, zone="kita", kind="bar", name="40 Sky Bar & Lounge - Conrad, 40 этаж", ll=(34.69359, 135.49547),
      q="40 Sky Bar & Lounge Conrad Osaka", photos=["nakanoshima-1.jpg", "nakanoshima-2.jpg", "sky40-1.jpg", "conrad-1.jpg"],
      hours="ср-сб 11:00-24:00 · с 20:00 до 22:30 сбор 1 650 ¥", walk="~13 мин",
      what="Самый высокий бар с видом в Kita, остров Nakanoshima (на фото - вид на реку и башню отеля). Фэнси, иногда живая музыка; публика в основном за столиками.",
      src="Hilton (офиц.), TableCheck",
      links=[("Сайт бара (Hilton)", "https://www.hilton.com/en/hotels/osacici-conrad-osaka/dining/40-sky-bar-and-lounge"), ("TableCheck", "https://www.tablecheck.com/en/shops/conradosaka-40skybar/reserve")]),
 dict(n=8, zone="kita", kind="walk", name="Grand Green Osaka - новый парк у станции", ll=(34.70367, 135.49240),
      q="Grand Green Osaka Umekita Park", photos=["umekita-2.jpg", "umekita-3.jpg", "umekita-1.jpg"],
      hours="ночные часы парка не проверял", walk="~12 мин",
      what="Новый городской парк (2024-2025) сразу к северу от станции, между небоскрёбами. Тихая прогулка по пути к Umeda Sky.",
      src="Wikimedia",
      links=[("Сайт Grand Green", "https://umekita.com/"), ("Wikipedia", "https://en.wikipedia.org/wiki/Grand_Green_Osaka")]),
 # ---------- NEAR: FUKUSHIMA / TENMA ----------
 dict(n=20, zone="near", kind="bar", name="Fukushima - бары для местных", ll=(34.696893, 135.487218),
      q="JR Fukushima Station Osaka", photos=["fukushima-1.jpg"],
      hours="бары до 24:00-03:00", walk="~15 мин пешком на запад или 1 ост. JR",
      what="Район в одной остановке к западу от станции Osaka. Не неон и не клубы: стоячие бары, винные бары, izakaya, публика в основном местная. Шумная крытая улица Shoten-dori идёт на север от станции.",
      subs=[("Tachinomi Jack to Matilda", "立ち呑み ジャックとマチルダ 福島 大阪", "стильный стоячий бар, хвалят еду, сакэ и хайболы, легко зайти одному; 15:00-24:00 (заказ до 23:00), 1-2 мин от станции", "https://retty.me/restaurant/100001286966/"),
            ("Roji-ura Avant-garde", "路地裏アバンギャルド 福島 大阪", "стоячий бар в стиле Showa в переулке, оден и сэндвич с дасимаки; пн-пт 18:00-02:00, сб-вс 16:00-02:00, 1 мин от станции", None),
            ("Macelleria di Takeuchi", "マチェレリーアディタケウチ 福島 大阪", "мясной бар с вином, сомелье подбирает под вкус; вт-сб 18:00-03:00, вс 17:00-24:00, 1 мин от станции", None)],
      src="Retty (часы баров), National Geographic (район). Не официальные сайты",
      links=[("National Geographic: районы Осаки", "https://www.nationalgeographic.com/travel/article/guide-to-osaka-bars-vintage-shopping"), ("Wikipedia", "https://en.wikipedia.org/wiki/Fukushima-ku,_Osaka")]),
 dict(n=21, zone="near", kind="walk", name="Tenma - народный квартал izakaya", ll=(34.704925, 135.512317),
      q="Tenma Station Osaka", photos=["tenma-1.jpg", "tenma-2.jpg"],
      hours="izakaya до ночи", walk="1 ост. JR Loop Line или ~25 мин пешком",
      what="Квартал стоячих баров и дешёвых izakaya вокруг станции Tenma, рядом самая длинная торговая улица Японии Tenjinbashisuji (~2,6 км). Шумно, просто, очень по-осакски.",
      src="mapple, Wikipedia (ja)",
      links=[("Wikipedia (ja): Tenma", wja("天満 (大阪市)")), ("Wikipedia (ja): Tenjinbashisuji", wja("天神橋筋商店街"))]),
 # ---------- MINAMI ----------
 dict(n=9, zone="minami", kind="walk", name="Shinsaibashi-suji - крытая улица", ll=(34.67067, 135.50133),
      q="Shinsaibashi-suji Shopping Street", photos=["shinsaibashi-1.jpg", "shinsaibashi-2.jpg"],
      hours="улица открыта всегда, магазины до ~21:00", walk="от станции Shinsaibashi ~10 мин до моста",
      what="Длинная крытая пешеходная улица от станции Shinsaibashi прямо к мосту Ebisubashi. Вечером уже без магазинов, но людно.",
      src="Wikimedia",
      links=[("Wikipedia", "https://en.wikipedia.org/wiki/Shinsaibashi"), ("Wikipedia (ja)", wja("心斎橋筋商店街"))]),
 dict(n=10, zone="minami", kind="walk", name="Ebisubashi, вывеска Glico и канал Dotonbori", ll=(34.66907, 135.50130),
      q="Ebisubashi Bridge Glico Sign Osaka", photos=["glico-1.jpg", "glico-3.jpg", "glico-2.jpg", "glico-4.jpg", "dotonbori-2.jpg", "dotonbori-1.jpg"],
      hours="всегда", walk="от станции Namba ~5 мин",
      what="Тот самый неон Осаки: мост, бегущий человек Glico (с 1935 года), огни над каналом. По обоим берегам набережная, вдоль неё бары и рестораны до поздней ночи.",
      src="Wikimedia",
      links=[("Osaka Info", "https://osaka-info.jp/en/spot/dotonbori/"), ("Wikipedia: Dotonbori", "https://en.wikipedia.org/wiki/D%C5%8Dtonbori"), ("Wikipedia: Glico Man", "https://en.wikipedia.org/wiki/Glico_Man")]),
 dict(n=11, zone="minami", kind="bar", name="NAKAZA SKY TERRACE - руфтоп над Dotonbori", ll=(34.66869, 135.502533),
      q="GIRAFFE Japan Nakaza Cuidaore Building Dotonbori 1-7-21", photos=["nakaza-1.jpg"],
      hours="ночные часы на сайте не указаны · по выходным вечером DJ", walk="~2 мин от Ebisubashi",
      what="Открытая терраса на крыше прямо над каналом: кальян, коктейли, по выходным DJ (по описанию на сайте). Бронь через их LINE.",
      src="giraffe-japan.com (офиц.)",
      links=[("Сайт террасы", "https://giraffe-japan.com/nakazaskyterrace_202607/"), ("Instagram", "https://www.instagram.com/giraffejapan/")]),
 dict(n=12, zone="minami", kind="club", name="GIRAFFE Japan - клуб, тот же дом, 5 этаж", ll=(34.66860, 135.50265),
      q="GIRAFFE Japan Nakaza Cuidaore Building Dotonbori 1-7-21", photos=["giraffe-04.jpg", "giraffe-02.jpg", "giraffe-03.jpg", "giraffe-01.jpg"],
      hours="22:00-04:00 · с 19:00 до 22:00 там шоу", walk="~2 мин от Ebisubashi",
      what="Большой коммерческий клуб, возрождённая легенда Minami (2025): звук d&b, шампанское, своя терраса. Музыка по гидам смешанная (EDM, хип-хоп, хаус). Туристы + местные - проще всего познакомиться. Билеты через Klook / GetYourGuide / Viator / Trip.com, цену не смотрел.",
      src="giraffe-japan.com (офиц.), Osaka Tourism",
      links=[("Сайт клуба", "https://giraffe-japan.com/nightclub"), ("Instagram", "https://www.instagram.com/giraffejapan/"), ("Гид по клубам Осаки", "https://www.osakatourism.org/best-nightclubs-in-osaka/")]),
 dict(n=13, zone="minami", kind="walk", name="Hozenji Yokocho - переулок с фонарями", ll=(34.66818, 135.50267),
      q="Hozenji Yokocho Osaka", photos=["hozenji-1.jpg", "hozenji-3.jpg", "hozenji-4.jpg", "hozenji-2.jpg"],
      hours="всегда · бары до ночи", walk="~2 мин от Nakaza",
      what="Узкий каменный переулок старой Осаки: фонари, маленький храм с покрытой мхом статуей Mizukake Fudo (её поливают водой), крошечные бары и рестораны. Тихий контраст рядом с неоном.",
      src="Wikimedia, Osaka Info",
      links=[("Osaka Info", "https://osaka-info.jp/en/spot/hozenji-yokocho/"), ("Wikipedia: Hōzen-ji", "https://en.wikipedia.org/wiki/Hozen-ji"), ("Wikipedia (ja)", wja("法善寺横丁"))]),
 dict(n=14, zone="minami", kind="bar", name="Smoke & Spin - руфтоп-лаунж Centara, 33 этаж", ll=(34.66015, 135.50224),
      q="Smoke & Spin Centara Grand Hotel Osaka", photos=["smoke-1.jpg", "namba-1.jpg"],
      hours="11:00-24:00 (напитки до 23:30) · smart casual", walk="~16 мин от Hozenji, на юг",
      what="Лаунж на 33 этаже (135 м) с видом на Namba, по сайту резидент-DJ каждый вечер. Под крышей. Второе фото - Namba Parks внизу рядом с отелем.",
      src="centarahotelsresorts.com (офиц.)",
      links=[("Сайт бара", "https://www.centarahotelsresorts.com/centaragrand/cgoj/smoke-and-spin"), ("TableCheck", "https://www.tablecheck.com/en/shops/centaragrand-osaka-smokeandspin/reserve")]),
 dict(n=15, zone="minami", kind="club", name="GHOST ultra lounge - Amerikamura", ll=(34.671082, 135.497574),
      q="GHOST ultra lounge 2-17-3 Nishishinsaibashi Osaka", photos=["amemura-1.jpg", "amemura-2.jpg"],
      hours="22:00-05:00 (по гидам, офиц. сайта не нашёл)", walk="~8 мин от Ebisubashi",
      what="Лаунж-клуб в подвале в квартале Amerikamura (на фото - сам квартал), публика наряднее среднего; музыка по разным гидам от хип-хопа до хауса. Нужен паспорт (20+).",
      src="Agoda, Culture Trip, tablejourney - не офиц.",
      links=[("Culture Trip: клубы Осаки", "https://theculturetrip.com/asia/japan/articles/the-best-clubs-in-osaka"), ("Wikipedia: Amerikamura", "https://en.wikipedia.org/wiki/Amerikamura")]),
 dict(n=16, zone="minami", kind="club", name="BAR Inc - DJ-бар (house / techno)", ll=(34.677105, 135.500626),
      q="BAR Inc 3-10-19 Minamisenba Osaka", photos=[],
      hours="пт 23.10: 20:00-03:00 (WEEKEND SELECTERS); обычно пт-сб 20:00-04:00", walk="~4 мин от станции Shinsaibashi",
      what="Небольшой музыкальный бар с хорошим звуком. Андеграунд, не пафос - если хочется именно музыки. Расписание - в Instagram.",
      src="Resident Advisor, листинг бара",
      links=[("Instagram", "https://www.instagram.com/bar_inc_osaka/"), ("Resident Advisor: 23.10", "https://ra.co/events/2538833")]),
]

KIND = {"hotel": ("#ffffff", "Отель"), "view": ("#6fc3ff", "Вид"), "bar": ("#e8b86b", "Бар / руфтоп"),
        "club": ("#ff6fae", "Клуб / DJ"), "walk": ("#7be08a", "Прогулка")}

def a(label, url, cls="lnk"):
    return f'<a class="{cls}" href="{html.escape(url)}" target="_blank" rel="noopener">{html.escape(label)}</a>'

def card(p):
    col, lab = KIND[p["kind"]]
    pics = "".join(
        f'<figure><img src="img/{f}" loading="lazy" alt="{html.escape(p["name"])}"><figcaption>{html.escape(CC.get(f, ""))}</figcaption></figure>'
        for f in p["photos"])
    cnt = f'<span class="cnt">{len(p["photos"])} фото →</span>' if len(p["photos"]) > 1 else ""
    gal = f'<div class="galw"><div class="gal">{pics}</div>{cnt}</div>' if pics else '<div class="nophoto">своих фото нет - смотри «Ещё фото» ниже</div>'
    kv = ""
    if p.get("hours"): kv += f'<div class="k">Часы</div><div><b>{html.escape(p["hours"])}</b></div>'
    if p.get("walk"): kv += f'<div class="k">Как далеко</div><div>{html.escape(p["walk"])}</div>'
    if p.get("src"): kv += f'<div class="k">Источник</div><div class="small">{html.escape(p["src"])}</div>'
    subs = ""
    for nm, q, desc, url in p.get("subs", []):
        extra = (" · " + a("Retty", url)) if url else ""
        subs += (f'<li><b>{html.escape(nm)}</b> - {html.escape(desc)}<br>{a("📍 Google Maps", gm(q))} · '
                 f'{a("📷 фото", gimg(q))} · {a("Tabelog", tabelog(q.split(" 福島")[0]))}{extra}</li>')
    if subs:
        subs = f'<div class="subs"><div class="k">Куда зайти</div><ul>{subs}</ul></div>'
    links = [a("📷 Ещё фото (Google)", gimg(p["q"]))] + [a(l, u) for l, u in p.get("links", [])]
    btns = f'<a class="btn pri" href="{gm(p["q"])}" target="_blank" rel="noopener">📍 Google Maps</a>'
    if p["zone"] in ("kita", "near") and p["kind"] != "hotel":
        btns += f'<a class="btn" href="{gdir(p["q"])}" target="_blank" rel="noopener">🚶 Пешком от отеля</a>'
    elif p["zone"] == "minami":
        btns += f'<a class="btn" href="{gdir(p["q"], "transit")}" target="_blank" rel="noopener">🚇 Маршрут от отеля</a>'
    return f'''<div class="card" id="p{p["n"]}">{gal}<div class="bd">
<div class="hd"><span class="num" style="background:{col}">{p["n"] if p["n"] else "★"}</span><h2>{html.escape(p["name"])}</h2></div>
<div class="tag" style="color:{col}">{lab}</div>
<p class="why">{html.escape(p["what"])}</p>{subs}<div class="kv">{kv}</div>
<div class="links">{" ".join(links)}</div><div class="btns">{btns}</div></div></div>'''

sec = {z: "".join(card(p) for p in P if p["zone"] == z) for z in ("kita", "near", "minami")}
markers = json.dumps([dict(n=p["n"], lat=p["ll"][0], lng=p["ll"][1], name=p["name"], z=p["zone"],
                           col=KIND[p["kind"]][0]) for p in P], ensure_ascii=False)
nphotos = sum(len(p["photos"]) for p in P)

PAGE = f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex,nofollow"><meta name="theme-color" content="#0b0d12"><title>Osaka · вечер и ночь</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css">
<style>
:root{{--bg:#0b0d12;--card:#171b25;--card2:#1e2330;--ink:#eef0f5;--mute:#9aa2b4;--line:#2a3040;--acc:#e8b86b;--warn:#ff8a7a}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}}
.wrap{{max-width:720px;margin:0 auto;padding:14px 16px 40px}}h1{{font-size:24px;margin:6px 0 2px}}.sub{{color:var(--mute);font-size:13px}}
a{{color:#7cc4ff}}.box{{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:12px 14px;margin:12px 0}}
.box h3{{margin:0 0 6px;font-size:16px;color:var(--acc)}}ul,ol{{margin:0;padding-left:20px}}li{{margin:4px 0}}
#map{{height:460px;border-radius:16px;border:1px solid var(--line);margin:12px 0}}
.zbtn{{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin-top:-4px}}.zbtn button{{min-height:40px;border-radius:12px;border:1px solid var(--line);background:var(--card2);color:var(--ink);font-weight:600;font-size:13px;padding:0 4px}}
.legend{{display:flex;flex-wrap:wrap;gap:6px 12px;font-size:13px;color:var(--mute);margin:8px 0}}.legend i{{display:inline-block;width:11px;height:11px;border-radius:50%;margin-right:5px;vertical-align:-1px}}
.pin{{width:28px;height:28px;border-radius:50%;color:#111;font:800 13px/28px -apple-system,sans-serif;text-align:center;border:2px solid #111;box-shadow:0 1px 4px rgba(0,0,0,.6)}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:18px;overflow:hidden;margin:16px 0}}
.galw{{position:relative}}.cnt{{position:absolute;right:8px;top:8px;background:rgba(0,0,0,.6);color:#fff;font-size:12px;padding:3px 8px;border-radius:999px;pointer-events:none}}
.gal{{display:flex;gap:4px;overflow-x:auto;scroll-snap-type:x mandatory;background:var(--card2)}}
.gal figure{{margin:0;flex:0 0 86%;scroll-snap-align:start;position:relative}}.gal figure:only-child{{flex-basis:100%}}
.gal img{{width:100%;height:230px;object-fit:cover;display:block}}.gal figcaption{{position:absolute;left:0;right:0;bottom:0;font-size:10px;color:#ddd;background:linear-gradient(transparent,rgba(0,0,0,.7));padding:10px 8px 4px}}
.nophoto{{padding:10px 14px;color:var(--mute);font-size:12px;background:var(--card2)}}
.bd{{padding:12px 14px 14px}}.hd{{display:flex;gap:10px;align-items:center}}h2{{margin:0;font-size:19px}}
.num{{flex:0 0 30px;height:30px;border-radius:50%;color:#111;font-weight:800;display:flex;align-items:center;justify-content:center}}
.tag{{font-size:12px;font-weight:700;margin:4px 0 0 40px;text-transform:uppercase;letter-spacing:.04em}}
.why{{margin:8px 0;font-size:15px}}.kv{{display:grid;grid-template-columns:96px 1fr;gap:6px 10px;font-size:14px;margin-top:10px}}.k{{color:var(--mute)}}
.subs{{background:var(--card2);border-radius:12px;padding:8px 10px;margin:8px 0;font-size:14px}}.subs .k{{font-size:13px;margin-bottom:4px}}.subs li{{margin:8px 0}}
.links{{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px}}.lnk{{display:inline-block;padding:6px 10px;border-radius:999px;border:1px solid var(--line);background:var(--card2);font-size:13px;text-decoration:none}}
.subs .lnk{{padding:2px 8px;font-size:12px}}
.btns{{display:flex;gap:8px;margin-top:12px}}.btn{{flex:1;display:flex;align-items:center;justify-content:center;min-height:46px;border-radius:12px;border:1px solid var(--line);background:var(--card2);color:var(--ink);text-decoration:none;font-weight:600;font-size:14px;text-align:center}}
.btn.pri{{background:var(--acc);border-color:var(--acc);color:#1a1205}}
.sech{{font-size:21px;margin:28px 0 2px;color:var(--acc)}}.small{{font-size:12px;color:var(--mute)}}
.warn{{border-left:3px solid var(--warn);background:var(--card2);padding:8px 10px;border-radius:8px;font-size:14px;margin-top:10px}}
table{{width:100%;border-collapse:collapse;font-size:14px}}td{{padding:6px 4px;border-bottom:1px solid var(--line);vertical-align:top}}td.t{{color:var(--acc);font-weight:700;white-space:nowrap}}
</style></head><body><div class="wrap">
<h1>Osaka · вечер и ночь</h1>
<div class="sub">Где ты и куда пойти: бары с видом, клубы, прогулки · {len(P)} мест, {nphotos} фото · обновлено 24.10.2026 ~03:00 JST</div>

<div class="warn">🌦 Погода (Open-Meteo, 24.10 ночью): <b>сб 24.10 вечер сухо</b> (18:00 - 18%, 22:00 - 7%, ~21°). <b>вс 25.10 дождь весь день</b>, сильнее всего ~18:00.</div>

<div id="map"></div>
<div class="zbtn"><button data-z="all">Вся Осака</button><button data-z="kita">Umeda</button><button data-z="near">Fukushima · Tenma</button><button data-z="minami">Minami (неон)</button></div>
<div class="legend"><span><i style="background:#fff"></i>отель</span><span><i style="background:#e8b86b"></i>бар / руфтоп</span><span><i style="background:#ff6fae"></i>клуб / DJ</span><span><i style="background:#6fc3ff"></i>вид</span><span><i style="background:#7be08a"></i>прогулка</span></div>

<div class="box"><h3>⏰ До скольки работает Осака</h3>
<table>
<tr><td class="t">до 22:30-23:00</td><td>Смотровые: Umeda Sky (вход до 22:00), колесо HEP FIVE (посадка до 22:45)</td></tr>
<tr><td class="t">до 23:00-24:00</td><td>Бары отелей с видом: ADEE (23:00-23:30), Smoke & Spin и 40 Sky Bar (24:00)</td></tr>
<tr><td class="t">до 01:00</td><td>Canes & Tales, Waldorf Astoria (пт-сб)</td></tr>
<tr><td class="t">до 02:00-05:00</td><td>Клубы и DJ-бары: GIRAFFE 22-04, GHOST 22-05, BAR Inc до 03-04; в Fukushima бары до 02:00-03:00</td></tr>
<tr><td class="t">00:10</td><td><b>Последнее метро</b> Namba → Umeda (в 00:19 у отеля) - одинаково пт, сб и вс. Позже - такси, ~4 км</td></tr>
</table>
<div class="small" style="margin-top:6px">Как в Токио: всё красивое с видом закрывается к 23-24. Дальше до утра живут клубы и DJ-бары (в основном Minami) и маленькие бары Fukushima.</div></div>

<div class="box"><h3>🚇 Как доехать до неона (Minami)</h3><ol>
<li>От отеля ~5 мин пешком до станции <b>Umeda</b>, линия <b>Midosuji (красная)</b>, платформа 1, поезд на <b>Nakamozu</b>. <a href="{gm("Umeda Station Osaka Metro Midosuji Line")}" target="_blank" rel="noopener">📍 станция</a></li>
<li>Остановки: Yodoyabashi → Hommachi → <b>Shinsaibashi</b> (~7 мин) или дальше до <b>Namba</b> (8 мин). Поезда каждые несколько минут. <a href="{gdir("Namba Station Osaka Metro Midosuji Line", "transit")}" target="_blank" rel="noopener">🚇 маршрут</a></li>
<li>Из Shinsaibashi - 10 мин пешком по крытой улице Shinsaibashi-suji до моста Ebisubashi. Из Namba - 5 мин.</li>
<li><b>Обратно:</b> Namba, платформа 2, поезд на Shin-Osaka или Minoh-kayano. Последний 00:10 → Umeda 00:19. Позже - <a href="{gdir("Hotel Granvia Osaka", "driving", "Ebisubashi Bridge Osaka")}" target="_blank" rel="noopener">🚕 такси до отеля</a>, без пробок ~7 мин. Водителю: ホテルグランヴィア大阪.</li>
</ol></div>

<div class="sech">Мой район · Umeda и Kitashinchi (пешком)</div>
<div class="sub">Второй центр Осаки: бары отелей с видом, улицы izakaya, вечером людно. Клубы с расписанием, которые я нашёл, - в Minami.</div>
{sec["kita"]}
<div class="sech">Рядом · Fukushima и Tenma (15-25 мин пешком)</div>
<div class="sub">Где пьют местные: маленькие бары и izakaya, без туристов и без неона.</div>
{sec["near"]}
<div class="sech">Minami · Dotonbori, Shinsaibashi, Namba (8 мин на метро)</div>
<div class="sub">Главная ночная Осака: неон, канал, переулки, руфтопы и клубы рядом друг с другом.</div>
{sec["minami"]}
<div class="box small">Не вошло: clubJOULE - на 23-24.10 подходящих событий не было. По Resident Advisor в эти дни в основном техно (Circus, Blvck Water). Фото: Wikimedia Commons (авторы и лицензии на фото) и официальные сайты мест. «Ещё фото» открывает поиск картинок Google по месту.</div>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script>
<script>
var M={markers};
var map=L.map('map',{{zoomControl:true}});
L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{{z}}/{{y}}/{{x}}',{{attribution:'Tiles © Esri',maxZoom:18}}).addTo(map);
var Z={{all:[],kita:[],near:[],minami:[]}};
M.forEach(function(p){{
  var ic=L.divIcon({{className:'',html:'<div class="pin" style="background:'+p.col+'">'+(p.n||'★')+'</div>',iconSize:[28,28],iconAnchor:[14,14]}});
  var m=L.marker([p.lat,p.lng],{{icon:ic,zIndexOffset:p.n?0:1000}}).addTo(map);
  m.bindPopup('<b>'+(p.n||'★')+'. '+p.name+'</b><br><a href="#p'+p.n+'">подробнее ↓</a>');
  Z.all.push([p.lat,p.lng]); Z[p.z].push([p.lat,p.lng]);
  if(p.n===0){{Z.kita.push([p.lat,p.lng]);Z.near.push([p.lat,p.lng]);}}
}});
map.fitBounds(Z.all,{{padding:[20,20]}});
document.querySelectorAll('.zbtn button').forEach(function(b){{b.onclick=function(){{map.fitBounds(Z[b.dataset.z],{{padding:[24,24]}});}};}});
</script>
<script src="lightbox.js?v=4" defer></script>
</body></html>'''
open("index.html", "w").write(PAGE)
print("ok", len(PAGE), "places", len(P), "photos", nphotos)
