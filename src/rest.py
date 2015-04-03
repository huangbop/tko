"""*
"""
import requests
import json

RAW_HEADERS = {
    "X-Bmob-Application-Id": "e9c72808f8555c8d7846a13a50e907a6",
    "X-Bmob-REST-API-Key": "9632a84d440c4faa818f033355cb9bf3",
}

JSON_HEADERS = {
    "X-Bmob-Application-Id": "e9c72808f8555c8d7846a13a50e907a6",
    "X-Bmob-REST-API-Key": "9632a84d440c4faa818f033355cb9bf3",
    "Content-Type": "application/json",
}

JPG_HEADERS = {
    "X-Bmob-Application-Id": "e9c72808f8555c8d7846a13a50e907a6",
    "X-Bmob-REST-API-Key": "9632a84d440c4faa818f033355cb9bf3",
    "Content-Type": "image/jpeg",
}

PNG_HEADERS = {
    "X-Bmob-Application-Id": "e9c72808f8555c8d7846a13a50e907a6",
    "X-Bmob-REST-API-Key": "9632a84d440c4faa818f033355cb9bf3",
    "Content-Type": "image/png",
}



CLASSES_BASE_URL = 'https://api.bmob.cn/1/classes/'
FILES_BASE_URL = 'https://api.bmob.cn/1/files/'


def add_image(info):
    """*
    """
    import pdb; pdb.set_trace()
    image_headers = JPG_HEADERS
    if info['type'] == 'png':
        image_headers = PNG_HEADERS
    res = requests.post(FILES_BASE_URL + info['name'], headers=image_headers,
                        data=info['bin'])
    if res.status_code == 201:
        file_desc = json.loads(res.content.decode())
        file_desc['__type'] = "File"
        info['file'] = file_desc
        del info['bin']
        res = requests.post('%s%s' % (CLASSES_BASE_URL, 'images'),
                            headers=JSON_HEADERS, data=json.dumps(info))
        print(res)


def add_product(info):
    """*
    """
    res = requests.post('%s%s' % (CLASSES_BASE_URL, 'products'),
                        headers=JSON_HEADERS, data=json.dumps(info))
    print(res)


def modify_image(info):
    """*
    """
    # get objectid
    import pdb; pdb.set_trace()
    params = 'where={"name": "%s"}' % info['name']
    res = requests.get(CLASSES_BASE_URL + 'images', headers=RAW_HEADERS,
                       params=params)
    if res.status_code == 200:
        record = json.loads(res.content.decode())
        objectid = record['results'][0]['objectId']
        # load file first
        image_headers = JPG_HEADERS
        if info['type'] == 'png':
            image_headers = PNG_HEADERS
        res = requests.post(FILES_BASE_URL + info['name'],
                            headers=image_headers, data=info['bin'])
        if res.status_code == 201:
            file_desc = json.loads(res.content.decode())
            file_desc['__type'] = "File"
            info['file'] = file_desc
            del info['bin']
            del info['name']
            res = requests.put('%simages/%s' % (CLASSES_BASE_URL, objectid),
                               headers=JSON_HEADERS, data=json.dumps(info))
            print(res)


def modify_product(info):
    """*
    """
    import pdb; pdb.set_trace()
    # get objectid
    res = requests.get(CLASSES_BASE_URL + 'products', headers=RAW_HEADERS,
                       data="where={'name': '%s'}" % info['name'])
    if res.status_code == 200:
        record = json.loads(res.content.decode())
        objectid = record['results'][0]['objectId']
        # modify special record
        del info['name']
        res = requests.put('%sproducts/%s' % (CLASSES_BASE_URL, objectid),
                           headers=JSON_HEADERS, data=json.dumps(info))
        print(res)
