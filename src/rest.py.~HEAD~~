"""
"""

import drest

APPID = 'e9c72808f8555c8d7846a13a50e907a6'
RESTKEY = '9632a84d440c4faa818f033355cb9bf3'


HEADERS = {
    'X-Bmob-Application-Id': APPID,
    'X-Bmob-REST-API-Key': RESTKEY,
    'Content-Type': 'application/json',
}

CLASSES_URL = 'https://api.bmob.cn/1/classes/'
table_api = drest.API(CLASSES_URL)


def get_records(table):
    """Path use "/path/" format
    """
    path = '/%s/' % table
    res = table_api.make_request('GET', path, headers=HEADERS)
    print(res)
    return res.data['results']


def new_record(table, params):
    """
    """
    table_api = drest.API("https://api.bmob.cn/1/classes")
    # path = '/%s/' % table
    path = '/GameScore/'
    res = table_api.make_request('POST', path, headers=None, params=None)
    return res


if __name__ == '__main__':
    import pdb; pdb.set_trace()
    new_record('GameScore', {'score': 1000, })
    
