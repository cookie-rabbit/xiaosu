import json
import time

import requests


class LoginView:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.username = 'oscarwty@qq.com'
        self.password = 'tianyang1'
        # self.username = '15336108478'
        # self.password = 'liyueyun627'
        self.session = LoginView.login(self.username, self.password)
        # self.user_history_url = "https://api.bilibili.com/x/v2/history"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
            'Cookie': self.session
        }

    @staticmethod
    def login(username, password):
        from DecryptLogin import login
        lg = login.Login()
        _, session = lg.bilibili(username, password, 'pc')
        SESSDATA = session.cookies._cookies['.bilibili']['/']['SESSDATA'].value
        ss = 'SESSDATA=' + SESSDATA
        return ss

    def get(self):
        # PC端
        history = self.__history()
        return {"errcode": "0", "data": history}

    def __history(self):
        pn = 1
        ps = 100
        lis = []
        while 1:
            self.user_history_url = "https://api.bilibili.com/x/v2/history"
            self.user_history_url = self.user_history_url + "?pn=" + str(pn) + "&ps" + str(ps)
            res = requests.request("GET", self.user_history_url, headers=self.headers)
            res_json = res.content
            datas = json.loads(res_json)['data']
            if datas:
                for data in datas:
                    title = data['title'].__str__(),  # 标题
                    desc = data['desc'],  # 描述
                    tname = data['tname'],  # 分类
                    pubdate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data['pubdate'])),  # 发布时间
                    author = data['owner']['name'],  # 作者
                    view_at = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data['view_at'])),  # 浏览时间
                    redirect_link = data['redirect_link']  # 视频链接

                    result = {"title": title, "desc": desc, "tname": tname, "pubdate": pubdate, "view_at": view_at,
                              "author": author, "redirect_link": redirect_link}

                    lis.append(result)
                pn += 1
            else:
                break
        return lis
