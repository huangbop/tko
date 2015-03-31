import requests
import json

HEADERS = {
    "X-Bmob-Application-Id": "e9c72808f8555c8d7846a13a50e907a6",
    "X-Bmob-REST-API-Key": "9632a84d440c4faa818f033355cb9bf3",
    "Content-Type": "application/json",
}

CLASSES_BASE_URL = 'https://api.bmob.cn/1/classes/'
FILES_BASE_URL = 'https://api.bmob.cn/1/files/'


def add_record(table, record_info):
    import pdb; pdb.set_trace()
    
    print(requests.post('%s%s' % (CLASSES_BASE_URL, table), headers=HEADERS,
                        data=record_info))
