#! /usr/local/bin/python3
# -*- coding:utf-8 -*-


import getpass
import json

import requests

ACCESS_KEY = ''

def login(user, passwd):
    douban_login_url = 'https://www.douban.com/service/auth2/token'
    post_data = {
        'apikey': '02646d3fb69a52ff072d47bf23cef8fd',
        'client_id': '02646d3fb69a52ff072d47bf23cef8fd',
        'client_secret': 'cde5d61429abcd7c',
        'udid': '07e0335d0c38a73384f709fa3102b33a94710d60',
        'douban_udid': 'b635779c65b816b13b330b68921c0f8edc049590',
        'device_id': '07e0335d0c38a73384f709fa3102b33a94710d60',
        'grant_type': 'password',
        'redirect_uri': 'http://www.douban.com/mobile/fm',
        'username': user,
        'password': passwd
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post(douban_login_url, data=post_data, headers=headers)
    print("[LOGIN] Resp - {}".format(r.text))

    resp = json.loads(r.text) 
    global ACCESS_KEY
    ACCESS_KEY = resp['access_token']

def get_redheart_sids():
    redheart_basic_url = 'https://api.douban.com/v2/fm/redheart/basic'
    headers = {'Authorization': 'Bearer ' + ACCESS_KEY}
    query_data = {
        'alt': 'json',
        'apikey': '02646d3fb69a52ff072d47bf23cef8fd',
        'app_name': 'radio_iphone',
        'audio_patch_version': 4,
        'client': 's:mobile|y:iOS 11.2.2|f:122|d:07e0335d0c38a73384f709fa3102b33a94710d60|e:iPhone8,1|m:appstore',
        'douban_udid': '677209cb05feeb5aa10fd34ed2d25765d8284f33',
        'kbps': 128,
        'udid': '07e0335d0c38a73384f709fa3102b33a94710d60'
    }
    r = requests.get(redheart_basic_url, params=query_data, headers=headers)
    #print("[READHEART] Resp - {}".format(r.text))
    resp = json.loads(r.text)
    songs_array = resp['songs']
    songs_str = ''
    for s in songs_array:
         songs_str = songs_str + s['sid'] + '|'
    songs_str = songs_str[:-1]
    #print("[SIDS] -" + songs_str)
    get_redheart_names(songs_str)

def get_redheart_names(sids):
    songs_url = 'https://api.douban.com/v2/fm/songs'
    headers = {'Authorization': 'Bearer ' + ACCESS_KEY}
    post_data = {
        'alt': 'json',
        'apikey': '02646d3fb69a52ff072d47bf23cef8fd',
        'app_name': 'radio_iphone',
        'audio_patch_version': 4,
        'client': 's:mobile|y:iOS 11.2.2|f:122|d:07e0335d0c38a73384f709fa3102b33a94710d60|e:iPhone8,1|m:appstore',
        'douban_udid': '677209cb05feeb5aa10fd34ed2d25765d8284f33',
        'sids': sids,
        'udid': '07e0335d0c38a73384f709fa3102b33a94710d60',
        'user_accept_play_third_party': 1,
        'version': 122
    }
    r = requests.post(songs_url, data=post_data, headers=headers)
    #print("[NAMES] Resp - " + r.text)
    resp = json.loads(r.text)
    song_list = []
    for s in resp:
        temp = {}
        temp['artist'] = s['artist']
        temp['title'] = s['title']
        song_list.append(temp)
    print("[SONGS] Result - ", end="")
    print(song_list)
    

if __name__ == '__main__':
    print('Pls Enter Douban FM USERNAME and PASSWORD.')
    u = input('USERNAME:')
    p = getpass.getpass('PASSWORD:')
    login(u, p)
    get_redheart_sids()
