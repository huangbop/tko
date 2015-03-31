import requests
import json

JSON_HEADERS = {
    "X-Bmob-Application-Id": "e9c72808f8555c8d7846a13a50e907a6",
    "X-Bmob-REST-API-Key": "9632a84d440c4faa818f033355cb9bf3",
    "Content-Type": "application/json",
}

IMAGE_HEADERS = {
    "X-Bmob-Application-Id": "e9c72808f8555c8d7846a13a50e907a6",
    "X-Bmob-REST-API-Key": "9632a84d440c4faa818f033355cb9bf3",
    "Content-Type": "image/jpeg",
}

CLASSES_BASE_URL = 'https://api.bmob.cn/1/classes/'
FILES_BASE_URL = 'https://api.bmob.cn/1/files/'


def add_record_image(info):
    import pdb; pdb.set_trace()
    image = info['image']
    res = requests.post(FILES_BASE_URL + image, headers=IMAGE_HEADERS,
                        data=open('../server/product/images/' + image, 'rb'))
    if res.status_code == 201:
        file_desc = json.loads(res.content.decode())
        file_desc['__type'] = "File"
        info['file'] = file_desc


def add_record(table, info):
    import pdb; pdb.set_trace()
    image = info.get('image')
    if image:
        add_record_image(info)

    res = requests.post('%s%s' % (CLASSES_BASE_URL, table), headers=JSON_HEADERS,
                        data=json.dumps(info))
    print(res)
