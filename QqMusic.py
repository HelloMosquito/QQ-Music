from pyquery import PyQuery as pq
import json
import random
import string
import hashlib

class QqMusic:
    def __init__(self, url):
        self.url = url
        # self.doc = pq(url=self.url).text().encode('ISO-8859-1').decode('utf-8')
        # print(self.doc)
        self.doc = json.loads(pq(url=self.url).text().encode('ISO-8859-1').decode('utf-8'))
        # print(type(self.doc))
        print(self.doc)
        print('-----------------------------------------------------------------------------')
        encryptedData = """{"detail":{"module":"musicToplist.ToplistInfoServer","method":"GetDetail","param":{"topId":26,"offset":0,"num":20,"period":"2020_45"}},"comm":{"ct":24,"cv":0}}"""
        print(QqMusic.get_qq_sign_encrypt(encryptedData))

    def get_hot_ranking(self):
        # contents = self.doc(".songlist__list").children()
        # print(contents)
        allSongsInCurrentPeriod = self.doc["detail"]["data"]["songInfoList"]
        for idx in range(0, len(allSongsInCurrentPeriod)):
            print(str(idx) + ', ' + allSongsInCurrentPeriod[idx]["name"] + ", " + allSongsInCurrentPeriod[idx]["singer"][0]["name"])

    @staticmethod
    def get_qq_sign_encrypt(encrypt_params):
        num = random.randint(10, 16)
        salt = "".join(random.sample(string.ascii_letters + string.digits, num))
        m = hashlib.md5()
        m.update(("CJBPACrRuNy7" + encrypt_params).encode())
        return "zza" + salt + m.hexdigest()
