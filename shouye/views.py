import json
import time

from django.db import transaction
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from shouye.logger import web_logger
from shouye.models import History
from utils import login


class WelcomeView(View):
    def get(self, request):
        return render(request, 'search.html')


class SearchView(View):
    def get(self, request):
        q = request.GET.get('q')
        error_msg = ''

        if not q:
            error_msg = '请输入关键词'
            return render(request, 'errors.html', {'error_msg': error_msg})

        post_list = History.objects.filter(title__icontains=q)
        return render(request, 'result.html', {'error_msg': error_msg, 'post_list': post_list})


@method_decorator(transaction.atomic)
def update(request):
    get_data = login.LoginView()
    datas = get_data.get()['data']
    for data in datas:
        title = data['title'][0],  # 标题
        title = str_format(title)

        desc = data['desc'][0],  # 描述
        desc = str_format(desc)

        tname = data['tname'][0],  # 分类
        tname = str_format(tname)

        pubdate = data['pubdate'][0],  # 发布时间
        pubdate = str_format(pubdate)

        author = data['author'][0],  # 作者
        author = str_format(author)

        view_at = data['view_at'][0],  # 浏览时间
        view_at = str_format(view_at)

        redirect_link = data['redirect_link']  # 视频链接

        try:
            if History.objects.filter(view_at=view_at):
                break
            else:
                History.objects.create(title=title, desc=desc, tname=tname, pubdate=pubdate, author=author, view_at=view_at,
                                       redirect_link=redirect_link)
        except Exception as e:
            web_logger.error(e)
            errmsg = {"errcode": "102", "errmsg": "数据库错误，浏览历史记录失败"}
            return HttpResponse(json.dumps(errmsg, ensure_ascii=False))

    sucmsg = {r"errcode": "0", "errmsg": "浏览历史记录成功"}
    return HttpResponse(json.dumps(sucmsg, ensure_ascii=False))


def str_format(content):
    try:
        content = str(content).split("(\'")[1].split("\',)")[0]
    except Exception as e:
        web_logger.error(e)
        web_logger.error(content)
        content = str(content)
    return content
