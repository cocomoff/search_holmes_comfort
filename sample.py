import requests
import lxml.html

URL = "https://www.homes.co.jp/chintai/comfort-commute/stations/"

# 飯田橋 22507
# 水道橋 22758
# 赤羽橋 29341
# 芝公園 22712

# lv = [22507]  # , 22758, 29341, 22712]
lv = [22507, 22758, 29341, 22712]

def search(station_id, offset=1):
    post_info = {
        "to_station_id": station_id,
        "commute_time_to": 30,
        "transfer_count": 0,
        "offset": offset
    }

    session = requests.session()
    url_search = URL
    res = requests.post(url_search, data=post_info)
    # print(res.text)

    # parse by xpath
    root = lxml.html.fromstring(res.text)
    list_mod_station = root.xpath("//div[@class='mod-station']")
    for station in list_mod_station:
        name = station.xpath("h3/span")[0].text
        line = station.xpath("h3/span")[1].text
        result = station.xpath("div/p/a/span")[0].text
        time_span = station.xpath("div/p")[1]
        time = time_span.xpath("span")[0].text + "分"
        transit = time_span.xpath("span")[1].text
        print(name, line, result, time, transit)


for station_id in lv:
    search(station_id)
    search(station_id, 21)
    print()