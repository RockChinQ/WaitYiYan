from pkg.plugin.models import *
from pkg.plugin.host import EventContext, PluginHost
import json
import requests
import traceback
import time

"""
获取文心一言排队人数
"""

def get_cnt() -> int:
    # 读取yiyancookies.json
    with open("yiyancookies.json", "r", encoding="utf-8") as f:
        cookies = json.loads(f.read())
    
    # 包装成requests的cookies
    cookies = {i["name"]: i["value"] for i in cookies}

    # yiyan.baidu.com/eb/user/wait/cnt
    resp = requests.post("https://yiyan.baidu.com/eb/user/wait/cnt", 
        cookies=cookies,
        data={
            "timestamp": time.time()*1000,
            "deviceType": "pc",
        },
        headers={
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Host": "yiyan.baidu.com",
            "Origin": "https://yiyan.baidu.com/welcome",
            "sec-ch-ua": '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Content-Type": "application/json",
            "Content-length": "45",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41"
        }
    )

    # 返回排队人数
    resp_json = resp.json()
    print(resp_json)

    return resp_json["data"]


@register(name="WaitYiYan", description="获取文心一言排队人数", version="0.1", author="RockChinQ")
class WaitYiYanPlugin(Plugin):

    def __init__(self, plugin_host: PluginHost):
        pass

    # 私聊发送指令
    @on(PersonCommandSent)
    def person_command_sent(self, event: EventContext, **kwargs):
        cmd = kwargs['command']

        if cmd == "wyy":
            try:
                # 获取排队人数
                cnt = get_cnt()
                event.add_return("reply", ["当前排队人数为：{}人".format(cnt)])
                event.prevent_default()
                event.prevent_postorder()
            except Exception as e:
                event.add_return("reply", ["获取失败: \n{}".format(traceback.format_exc())])
                event.prevent_default()
                event.prevent_postorder()

    def __del__(self):
        pass
