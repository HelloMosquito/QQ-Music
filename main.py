from QqMusic import QqMusic
import urllib.parse

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
    print(request_url)
    return request_url



if __name__ == '__main__':

#     # 2018-12-28 to 2019-1-3
#     # t1=2019 & t2=1 & t3=song & t4=55 & t5=1
#     url2019 = """
#         https://u.y.qq.com/cgi-bin/musics.fcg?-=getUCGI9722602623516272&g_tk=97949831&sign=zzaptt3alajkevt18427a8f2766fdf57b4163da879f0c8e&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A26%2C%22offset%22%3A0%2C%22num%22%3A20%2C%22period%22%3A%222019_01%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D
#     """
#
#     # 2019-12-27 to 2020-1-2
#     # t1=2020 & t2=1 & t3=song & t4=55 & t5=1
#     url2020 = """
#     https://u.y.qq.com/cgi-bin/musics.fcg?-=getUCGI6524734975297883&g_tk=97949831&sign=zzaniadiwm7nukc63c7cd0eee44ff7e23aef4320b61ac8b&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A26%2C%22offset%22%3A0%2C%22num%22%3A20%2C%22period%22%3A%222020_53%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D
# """

    url = get_url("2020_53")
    qq_music = QqMusic(url)
    qq_music.get_hot_ranking()

