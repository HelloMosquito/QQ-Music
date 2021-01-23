from pyquery import PyQuery as pq
import json
import random
import string
import hashlib
import csv
import datetime


class QqMusic:
    def __init__(self, url, period, year_starting_date):
        """
        year_starting_date: i.e., if the first week of 2019 is from 2018-12-28 to 2019-01-03, then 2018-12-28 is the
            year_starting_date
        """
        self._url = url
        self._period = period        # initial period is like 2020_01, which is used to construct the request url
        self._year_starting_date = year_starting_date
        self._year = self._period[0:4]    # used to build the file name
        self._week = self._period[5:7]   # used to build the file name
        self._period_title = self._period_title_init()
        self._doc = json.loads(pq(url=self._url).text().encode('ISO-8859-1').decode('utf-8'))
        self._rankings = []
        self._crawl_hot_ranking()

    def _crawl_hot_ranking(self):
        allSongsInCurrentPeriod = self._doc["detail"]["data"]["songInfoList"]
        for idx in range(0, len(allSongsInCurrentPeriod)):
            self._rankings.append([
                idx + 1,
                allSongsInCurrentPeriod[idx]["name"],
                allSongsInCurrentPeriod[idx]["singer"][0]["name"]
            ])
        print("crawling period: " + self._period)
        return self._rankings

    def get_hot_ranking(self):
        return self._rankings

    def save_hot_ranking_in_csv(self):
        with open(self._period_title + ".csv", "w", newline="", encoding="utf8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["ranking", "song", "singer"])
            # allSongsInCurrentPeriod = self.doc["detail"]["data"]["songInfoList"]
            for idx in range(len(self._rankings)):
                writer.writerow([
                    self._rankings[idx][0],
                    self._rankings[idx][1],
                    self._rankings[idx][2]
                ])

    def _period_title_init(self):
        period_title = self._year + "week" + self._week \
                       + "_" + QqMusic.get_period_date(self._year_starting_date, int(self._week))
        return period_title

    def get_current_period_title(self):
        return self._period_title

    def combine_csv_as_excel_one_sheet(self):
        pass

    @staticmethod
    def get_qq_sign_encrypt(encrypt_params):
        num = random.randint(10, 16)
        salt = "".join(random.sample(string.ascii_letters + string.digits, num))
        m = hashlib.md5()
        m.update(("CJBPACrRuNy7" + encrypt_params).encode())
        return "zza" + salt + m.hexdigest()

    @staticmethod
    def get_period_date(starting_date, week):
        delta_days = datetime.timedelta(days=(week - 1) * 7)  # week starting at 1
        period_starting_date = starting_date + delta_days
        period_ending_date = period_starting_date + datetime.timedelta(days=6)
        return period_starting_date.strftime("%Y%m%d") + "-" + period_ending_date.strftime("%Y%m%d")
