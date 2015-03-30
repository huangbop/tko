"""
"""

import requests
import json

HEADERS = {
    "X-Bmob-Application-Id": "e9c72808f8555c8d7846a13a50e907a6",
    "X-Bmob-REST-API-Key": "9632a84d440c4faa818f033355cb9bf3",
}


FILES_BASE_URL = 'https://api.bmob.cn/1/files/'


# b = requests.post('https://api.bmob.cn/1/classes/GameScore',
#                   headers=HEADERS, data='{"score": 1000}' )

f = requests.post(FILES_BASE_URL + 'emacs1.png', headers=HEADERS,
                  data=open('emacs.png', 'rb'))


# import drest

# APPID = 'e9c72808f8555c8d7846a13a50e907a6'
# RESTKEY = '9632a84d440c4faa818f033355cb9bf3'


# # HEADERS = {
# #     'X-Bmob-Application-Id': APPID,
# #     'X-Bmob-REST-API-Key': RESTKEY,
# #     'Content-Type': 'application/json',
# # }

# CLASSES_URL = 'https://api.bmob.cn/1/classes/'
# table_api = drest.API(CLASSES_URL)


# a = requests.get('https://api.bmob.cn/1/classes/GameScore/', headers=HEADERS)


# def get_records(table):
#     """Path use "/path/" format
#     """
#     path = '/%s/' % table
#     res = table_api.make_request('GET', path, headers=HEADERS)
#     print(res)
#     return res.data['results']

