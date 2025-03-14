import requests
import yaml
import ssl
import time
import json  # 导入 json 模块用于解析 JSON 字符串
from requests.adapters import HTTPAdapter


# 自定义适配器以使用 pyOpenSSL
class PyOpenSSLAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = ssl.create_default_context()
        context.load_default_certs()
        kwargs['ssl_context'] = context
        return super(PyOpenSSLAdapter, self).init_poolmanager(*args, **kwargs)


# 读取 YAML 配置文件
def load_config(file_path):
    with open(file_path, 'r', encoding='utf-8') as config_file:
        return yaml.safe_load(config_file)


# 获取请求头
def get_headers():
    return {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'http://300zjdclient.tygms.cn',
        'Pragma': 'no-cache',
        'Referer': 'http://300zjdclient.tygms.cn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }


# 创建会话并使用自定义适配器
session = requests.Session()
session.mount('https://', PyOpenSSLAdapter())


# 校验 token 请求
def validate_token(token):
    url = "https://300zjd.tygms.cn/"
    headers = get_headers()

    data = {
        "msgid": 1004,
        "token": token
    }

    response = session.post(url, headers=headers, json=data)
    return response.json()  # 返回 JSON 格式的响应


# 点赞请求
def like_post(token, unique_id, posts_id, like_type):
    url = "https://300zjd.tygms.cn/"
    headers = get_headers()

    data = {
        "msgid": 1018,
        "unique_id": unique_id,
        "posts_id": posts_id,
        "like_type": like_type,
        "token": token
    }

    response = session.post(url, headers=headers, json=data)
    return response.text


# 查询战绩请求
def query_performance(token, unique_id, account_id, guid, role_name, role_id):
    url = "https://300zjd.tygms.cn/"
    headers = get_headers()

    data = {
        "msgid": 1009,
        "AccountID": account_id,
        "Guid": guid,
        "RoleName": role_name,
        "RoleID": role_id,
        "token": token
    }

    response = session.post(url, headers=headers, json=data)
    return response.text


# 查询历史战绩请求
def query_history(token, unique_id, role_id, match_type, search_index):
    url = "https://300zjd.tygms.cn/"
    headers = get_headers()

    data = {
        "msgid": 1011,
        "RoleID": role_id,
        "MatchType": match_type,
        "SearchIndex": search_index,
        "token": token
    }

    response = session.post(url, headers=headers, json=data)
    return response.text


# 关注请求
def follow_user(token, unique_id, follow_id, follow_type):
    url = "https://300zjd.tygms.cn/"
    headers = get_headers()

    data = {
        "msgid": 1029,
        "unique_id": unique_id,
        "follow_id": follow_id,
        "follow_type": follow_type,
        "token": token
    }

    response = session.post(url, headers=headers, json=data)
    return response.text


# 签到请求
def sign_in(token, unique_id):
    url = "https://300zjd.tygms.cn/"
    headers = get_headers()

    data = {
        "msgid": 1073,
        "unique_id": unique_id,
        "token": token
    }

    response = session.post(url, headers=headers, json=data)
    return response.text


# 一键领取请求
def claim_rewards(token, unique_id, task_id_list):
    url = "https://300zjd.tygms.cn/"
    headers = get_headers()

    data = {
        "msgid": 1074,
        "unique_id": unique_id,
        "task_id_list": task_id_list,
        "token": token
    }

    response = session.post(url, headers=headers, json=data)
    return response.text


# 评论请求
def comment_post(token, unique_id, posts_id, content):
    url = "https://300zjd.tygms.cn/"
    headers = get_headers()

    data = {
        "msgid": 1028,
        "unique_id": unique_id,
        "posts_id": posts_id,
        "content": content,
        "imgs": "",
        "links": {},
        "ats": {},
        "extras": {},
        "token": token
    }

    response = session.post(url, headers=headers, json=data)
    return response.text


# 主程序
if __name__ == "__main__":
    config = load_config('config.yaml')
    token = config['token']

    # 校验 token
    validation_response = validate_token(token)
    if not validation_response.get("MSG"):  # 检查 MSG 字段是否为空
        print("Token 无效，请检查您的 token。")
    else:
        # 解析 MSG 字段
        msg_data = json.loads(validation_response["MSG"])
        unique_id = msg_data["UniqueId"]  # 保持为字符串
        account_id = msg_data["JumpwUID"]
        guid = msg_data["JumpwGuid"]
        role_id = int(msg_data["JumpwRoleId"])  # 转换为整数
        role_name = msg_data["JumpwRoleName"]

        # 点赞
        like_response = like_post(token, unique_id, 6697, 1)
        print("点赞响应:", like_response)
        time.sleep(1)  # 延迟1秒

        # 取消点赞
        like_response = like_post(token, unique_id, 6697, 2)
        print("取消点赞响应:", like_response)
        time.sleep(1)  # 延迟1秒

        # 查询战绩
        performance_response = query_performance(token, unique_id, account_id, guid, "", role_id)
        print("查询战绩响应:", performance_response)
        time.sleep(1)  # 延迟1秒

        # 查询历史战绩
        history_response = query_history(token, unique_id, role_id, 1, 1)
        print("查询历史战绩响应:", history_response)
        time.sleep(1)  # 延迟1秒

        # 关注
        follow_response = follow_user(token, unique_id, "p492210972677771264", 1)
        print("关注响应:", follow_response)
        time.sleep(1)  # 延迟1秒

        # 取消关注
        follow_response = follow_user(token, unique_id, "p492210972677771264", 2)
        print("取消关注响应:", follow_response)
        time.sleep(1)  # 延迟1秒

        # 签到
        sign_in_response = sign_in(token, unique_id)
        print("签到响应:", sign_in_response)
        time.sleep(1)  # 延迟1秒

        # 回帖
        comment_post_response = comment_post(token, unique_id, "6697", "嘤嘤嘤\\n")
        print("回帖响应:", comment_post_response)
        time.sleep(1)  # 延迟1秒

        # 一键领取
        claim_response = claim_rewards(token, unique_id, "1,2,3,4,5,6,7,8,9")
        print("一键领取响应:", claim_response)
