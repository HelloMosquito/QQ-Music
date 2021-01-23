from QqMusic import QqMusic
import urllib.parse
import pandas as pd
import time
import random
import datetime


def user_config():
    """
        All the following parameters must be carefully configured before using
    """
    year = 2019
    starting_date = datetime.datetime.strptime("2018-12-28", "%Y-%m-%d")
    need_specific_week = False
    specific_week = 54
    return year, starting_date, specific_week, need_specific_week


def get_url(request_data_period):
    url_request_data = '{"detail":{"module":"musicToplist.ToplistInfoServer","method":"GetDetail",' \
                       '"param":{"topId":26,"offset":0,"num":20,"period":"' \
                       + request_data_period + '"}},"comm":{"ct":24,"cv":0}}'
    url_request_data_encode = urllib.parse.quote(url_request_data)
    url_prefix = "https://u.y.qq.com/cgi-bin/musics.fcg?-=getUCGI9722602623516272&g_tk=97949831&"
    url_infix = "&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&" \
                "platform=yqq.json&needNewCode=0&data="
    sign = "sign=" + QqMusic.get_qq_sign_encrypt(url_request_data)

    request_url = url_prefix + sign + url_infix + url_request_data_encode
    return request_url


def period_construct(year, week):
    return str(year)+"_"+str(week if week > 9 else "0"+str(week))


def write_into_excel(data, year):
    with pd.ExcelWriter(str(year) + " all rankings.xlsx", encoding="utf8") as writer:
        for period, v in data.items():
            ranking_in_current_period = pd.DataFrame(v)
            ranking_in_current_period.rename(columns={0: "Ranking", 1: "Song", 2: "Singer"}, inplace=True)
            ranking_in_current_period.to_excel(writer, sheet_name=period, index=False)


def crawling_data_in_one_week(year, week, year_starting_date):
    period_init = period_construct(year, week)
    url = get_url(period_init)
    qq_music = QqMusic(url, period_init, year_starting_date)
    qq_music.save_hot_ranking_in_csv()
    return qq_music


def start():
    year, starting_date, specific_week, need_specific_week = user_config()
    all_ranks = {}
    if need_specific_week:
        crawling_data_in_one_week(year, specific_week, starting_date)
    else:
        for week in range(1, 55):
            qq_music = crawling_data_in_one_week(year, week, starting_date)
            all_ranks[qq_music.get_current_period_title()] = qq_music.get_hot_ranking()
            time.sleep(round(random.uniform(3, 7), 2))
        write_into_excel(all_ranks, year)


if __name__ == '__main__':
    start()
