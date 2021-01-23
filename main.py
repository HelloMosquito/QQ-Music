from QqMusic import QqMusic
import urllib.parse
import pandas as pd
import time
import random
import datetime


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
    # print(request_url)
    return request_url


# def required_period(year, week, show_date_period=False, starting_date=""):
#     period = str(year) + "week" + str(week if week > 9 else "0" + str(week))
#     if show_date_period:
#         period = period + "_" + get_period_date(starting_date, week)
#     return period


def period_construct(year, week):
    return str(year)+"_"+str(week if week>9 else "0"+str(week))


def write_into_excel(data, year):
    with pd.ExcelWriter(str(year) + " all rankings.xlsx", encoding="utf8") as writer:
        for period, v in data.items():
            ranking_in_current_period = pd.DataFrame(v)
            ranking_in_current_period.rename(columns={0: "Ranking", 1: "Song", 2: "Singer"}, inplace=True)
            ranking_in_current_period.to_excel(writer, sheet_name=period, index=False)


# def get_period_date(starting_date, week):
#     delta_days = datetime.timedelta(days=(week - 1) * 7)        # week starting at 1
#     period_starting_date = starting_date + delta_days
#     period_ending_date = period_starting_date + datetime.timedelta(days=6)
#     return period_starting_date.strftime("%Y%m%d") + "-" + period_ending_date.strftime("%Y%m%d")


def user_config():
    year = 2020
    show_date_period = True
    starting_date = datetime.datetime.strptime("2019-12-27", "%Y-%m-%d")
    return year, show_date_period, starting_date


def start():
    year, show_date_period, starting_date = user_config()
    all_ranks = {}
    for week in range(1, 3):
    # for week in range(1, 54):
    #     title_period = required_period(year, week, show_date_period, starting_date)
        period_init = period_construct(year, week)
        url = get_url(period_init)
        qq_music = QqMusic(url, period_init, starting_date)
        all_ranks[qq_music.get_current_period_title()] = qq_music.get_hot_ranking()
        qq_music.save_hot_ranking_in_csv()
        # rankings_in_current_period = qq_music.get_hot_ranking()
        # print(rankings_in_current_period)
        # print(all_ranks)
        time.sleep(round(random.uniform(3, 7), 2))
    # print(all_ranks)
    write_into_excel(all_ranks, year)


if __name__ == '__main__':
    start()

    # a = "1010_02"
    # print(a[0:4])
    # print(a[5:7])



    # a = datetime.datetime.strptime("2018-12-28", "%Y-%m-%d")
    #
    # print(get_period_date(a, 2))

    # print(a)
    # print(a.strftime("%Y/%m/%d"))
    # b = a + datetime.timedelta(days=7)
    # print(b)


    # a = {'2019_02': [[1, '知否知否', '胡夏'], [2, '不为谁而作的歌', '林俊杰'], [3, '光年之外', 'G.E.M. 邓紫棋'], [4, '关键词', '林俊杰'],
    #                  [5, '东西', '林俊呈'], [6, '生僻字', '陈柯宇'], [7, '原来占据你内心的人不是我', '贺一航'], [8, '下坠Falling', 'Corki'],
    #                  [9, '一曲相思', '半阳'], [10, '可不可以', '张紫豪'], [11, '圣所', '林俊杰'], [12, '体面', '于文文'], [13, '侧脸', '于果'],
    #                  [14, '天份', '薛之谦'], [15, '年少有为', '李荣浩'], [16, '清明上河图', '李玉刚'], [17, '我不愿明白', '段奥娟'],
    #                  [18, '纸短情长', '烟把儿乐队'], [19, '再见只是陌生人', '庄心妍'], [20, '天亮以前说再见', '曲肖冰']],
    #      '2019_03': [[1, '知否知否', '胡夏'], [2, '光年之外', 'G.E.M. 邓紫棋'], [3, '清明上河图', '李玉刚'], [4, '侧脸', '于果'],
    #                  [5, '不为谁而作的歌', '林俊杰'], [6, '生僻字', '陈柯宇'], [7, '一曲相思', '半阳'], [8, '下坠Falling', 'Corki'],
    #                  [9, '可不可以', '张紫豪'], [10, '东西', '林俊呈'], [11, '体面', '于文文'], [12, '年少有为', '李荣浩'],
    #                  [13, '再见只是陌生人', '庄心妍'], [14, '关键词', '林俊杰'], [15, '天份', '薛之谦'], [16, '纸短情长', '烟把儿乐队'],
    #                  [17, '倒数', 'G.E.M. 邓紫棋'], [18, '狂浪', '花姐'], [19, 'Hello My Love', 'Westlife'], [20, '圣所', '林俊杰']],
    #      '2019_04': [[1, '知否知否', '胡夏'], [2, '光年之外', 'G.E.M. 邓紫棋'], [3, '清明上河图', '李玉刚'], [4, '我不愿明白', '段奥娟'],
    #                  [5, '侧脸', '于果'], [6, '一曲相思', '半阳'], [7, '生僻字', '陈柯宇'], [8, '下坠Falling', 'Corki'],
    #                  [9, '可不可以', '张紫豪'], [10, '沙漠骆驼', '展展与罗罗'], [11, '东西', '林俊呈'], [12, '狂浪', '花姐'],
    #                  [13, 'Wolves', 'Selena Gomez'], [14, '陪你度过漫长岁月-', '陈奕迅'], [15, '随风', '周深'], [16, '年少有为', '李荣浩'],
    #                  [17, '体面', '于文文'], [18, '浪子回头', '茄子蛋'], [19, '天亮以前说再见', '曲肖冰'], [20, 'Hello My Love', 'Westlife']]}
    # for key, value in a.items():
    #     print("period: " + key + ", " + str(value))

    # for i in range(10):
    #     print(round(random.uniform(3, 7), 2))

    # period = required_period("2020", "51")
#     url = get_url(period)
#     qq_music = QqMusic(url, period)
#     a = qq_music.get_hot_ranking()
#     print(a)
#     print("======")
#     all = {}
#     all[period] = a
#     print(all)
# #     # qq_music.save_hot_ranking_in_csv()
#     print("======")
#     r = pd.DataFrame(a)
#     s = pd.DataFrame(b)
#     r.rename(columns={0: "ranking", 1: "song", 2: "singer"}, inplace=True)
#     s.rename(columns={0: "ranking", 1: "song", 2: "singer"}, inplace=True)
#     print(r)
#
#
#     with pd.ExcelWriter("all rankings.xlsx") as writer:
#         r.to_excel(writer, sheet_name=period, index=False)
#         s.to_excel(writer, sheet_name="2019-1", index=False)
