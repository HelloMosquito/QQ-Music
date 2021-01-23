from pyquery import PyQuery as pq
import json
import random
import string
import hashlib
import csv


class QqMusic:
    def __init__(self, url, period):
        self.url = url
        self.period = period
        # self.doc = pq(url=self.url).text().encode('ISO-8859-1').decode('utf-8')
        # print(self.doc)
        self.doc = json.loads(pq(url=self.url).text().encode('ISO-8859-1').decode('utf-8'))
        self.rankings = []
        # print(type(self.doc))
        # print(self.doc)
        # print('-----------------------------------------------------------------------------')
        # encryptedData = """{"detail":{"module":"musicToplist.ToplistInfoServer","method":"GetDetail","param":{
        # "topId":26,"offset":0,"num":20,"period":"2020_45"}},"comm":{"ct":24,"cv":0}} """
        # print(QqMusic.get_qq_sign_encrypt(encryptedData))

    def get_hot_ranking(self):
        # contents = self.doc(".songlist__list").children()
        # print(contents)
        allSongsInCurrentPeriod = self.doc["detail"]["data"]["songInfoList"]
        # rankings = {}
        for idx in range(0, len(allSongsInCurrentPeriod)):
            # rankings["ranking"] = idx + 1
            # rankings["song"] = allSongsInCurrentPeriod[idx]["name"]
            # rankings["singer"] = allSongsInCurrentPeriod[idx]["singer"][0]["name"]
            self.rankings.append([
                idx + 1,
                allSongsInCurrentPeriod[idx]["name"],
                allSongsInCurrentPeriod[idx]["singer"][0]["name"]
            ])
            # rankings.append(idx)
            # rankings.append(allSongsInCurrentPeriod[idx]["name"])
            # rankings.append(allSongsInCurrentPeriod[idx]["singer"][0]["name"])
            # print(str(idx) + ", "
            #       + allSongsInCurrentPeriod[idx]["name"] + ", "
            #       + allSongsInCurrentPeriod[idx]["singer"][0]["name"])
        print("crawling period: " + self.period)
        return self.rankings

    def save_hot_ranking_in_csv(self):
        with open(self.period+".csv", "w", newline="", encoding="utf8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["ranking", "song", "singer"])
            # allSongsInCurrentPeriod = self.doc["detail"]["data"]["songInfoList"]
            for idx in range(len(self.rankings)):
                writer.writerow([
                    self.rankings[idx][0],
                    self.rankings[idx][1],
                    self.rankings[idx][2]
                ])

    def combine_csv_as_excel_one_sheet(self):
        pass

    @staticmethod
    def get_qq_sign_encrypt(encrypt_params):
        num = random.randint(10, 16)
        salt = "".join(random.sample(string.ascii_letters + string.digits, num))
        m = hashlib.md5()
        m.update(("CJBPACrRuNy7" + encrypt_params).encode())
        return "zza" + salt + m.hexdigest()
