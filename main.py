#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/3/13 12:45
# @Author  : Kiriya
# @File    : main.py
# @Description : 宅基地日常任务

import requests
import yaml


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
        'Origin': 'https://300zjdclient.tygms.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://300zjdclient.tygms.cn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }


# 点赞请求
def like_post(token, msgid, unique_id, posts_id, like_type):
    url = "https://300zjd.tygms.cn/"
    headers = get_headers()

    data = {
        "msgid": msgid,
        "unique_id": unique_id,
        "posts_id": posts_id,
        "like_type": like_type,
        "token": token
    }

    response = requests.post(url, headers=headers, json=data)
    return response.text


# 查询战绩请求
def query_performance(token, msgid, account_id, guid, role_name, role_id):
    url = "https://300zjd.tygms.cn/"
    headers = get_headers()

    data = {
        "msgid": msgid,
        "AccountID": account_id,
        "Guid": guid,
        "RoleName": role_name,
        "RoleID": role_id,
        "token": token
    }

    response = requests.post(url, headers=headers, json=data)
    return response.text


# 查询历史战绩请求
def query_history(token, msgid, role_id, match_type, search_index):
    url = "https://300zjd.tygms.cn/"
    headers = get_headers()

    data = {
        "msgid": msgid,
        "RoleID": role_id,
        "MatchType": match_type,
        "SearchIndex": search_index,
        "token": token
    }

    response = requests.post(url, headers=headers, json=data)
    return response.text


# 关注请求
def follow_user(token, msgid, unique_id, follow_id, follow_type):
    url = "https://300zjd.tygms.cn/"
    headers = get_headers()

    data = {
        "msgid": msgid,
        "unique_id": unique_id,
        "follow_id": follow_id,
        "follow_type": follow_type,
        "token": token
    }

    response = requests.post(url, headers=headers, json=data)
    return response.text


# 签到请求
def sign_in(token, msgid, unique_id):
    url = "https://300zjd.tygms.cn/"
    headers = get_headers()

    data = {
        "msgid": msgid,
        "unique_id": unique_id,
        "token": token
    }

    response = requests.post(url, headers=headers, json=data)
    return response.text


# 主程序
if __name__ == "__main__":
    config = load_config('config.yaml')
    token = config['token']

    # 点赞
    like_response = like_post(token, 1018, "p492304087396782080", 6697, 1)
    print("点赞响应:", like_response)
    # 取消点赞
    like_response = like_post(token, 1018, "p492304087396782080", 6697, 2)
    print("点赞响应:", like_response)

    # 查询战绩
    performance_response = query_performance(token, 1009, 223164563, 20031, "", 0)
    print("查询战绩响应:", performance_response)
    # 查询历史战绩
    history_response = query_history(token, 1011, 2419290158, 1, 1)
    print("查询历史战绩响应:", history_response)

    # 关注
    follow_response = follow_user(token, 1029, "p492304087396782080", "p492210972677771264", 1)
    print("关注响应:", follow_response)
    # 取消关注
    follow_response = follow_user(token, 1029, "p492304087396782080", "p492210972677771264", 2)
    print("关注响应:", follow_response)

    # 签到示例
    sign_in_response = sign_in(token, 1072, "p492304087396782080")
    print("签到响应:", sign_in_response)
