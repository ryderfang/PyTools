#! /usr/local/bin/python3
# -*- coding:utf-8 -*-

import requests
import getpass

def login(user, passwd):
    douban_login_url = "https://www.douban.com/service/auth2/token"

    post_data = {
        "apikey": "02646d3fb69a52ff072d47bf23cef8fd",
        "client_id": "02646d3fb69a52ff072d47bf23cef8fd",
        "client_secret": "cde5d61429abcd7c",
        "udid": "b88146214e19b8a8244c9bc0e2789da68955234d",
        "douban_udid": "b635779c65b816b13b330b68921c0f8edc049590",
        "device_id": "b88146214e19b8a8244c9bc0e2789da68955234d",
        "grant_type": "password",
        "redirect_uri": "http://www.douban.com/mobile/fm",
        "username": user,
        "password": passwd
    }

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    r = requests.post(douban_login_url, data=post_data, headers=headers)

    print('[Login] Resp:{}'.format(r.text))


if __name__ == '__main__':
    print("Pls Enter Douban FM USERNAME and PASSWORD.")
    user = input("USERNAME:")
    passwd = getpass.getpass("PASSWORD:")
    login(user, passwd)
