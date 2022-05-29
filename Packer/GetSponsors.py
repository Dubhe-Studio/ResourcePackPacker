import json
import os
from typing import Dict

from Packer import config_path

import requests

sponsors_file = os.path.join(config_path, 'sponsors.json')


def reload():
    try:
        text = requests.get(
            "https://afdian.net/api/creator/get-top-sponsors?user_id=b0333d22d78811ecb3cd52540025c377"
        ).json()["data"]["list"]
        x: dict = {}
        names = [i["name"] for i in text]
        for i in range(len(names)):
            x[names[i]] = text[i]["avatar"]
        text = json.dumps(x, ensure_ascii=False, indent=4)
        if not os.path.isdir(config_path):
            os.mkdir(config_path)
        if not os.path.isfile(sponsors_file):
            f = open(sponsors_file, 'w', encoding='utf8')
            f.write("{}")
            f.close()
        with open(sponsors_file, 'w+', encoding='utf8') as f:
            f.write(text)
            f.close()
    except:
        return


def get_sponsors() -> Dict:
    with open(sponsors_file, 'r') as f:
        return json.loads(f.read())


print(get_sponsors())
