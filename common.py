import base64
import json
import urllib.request
from _md5 import md5

api = "https://api.coolapk.com/v6/main/init"
built_in_str = "ldTM3cTZiFTMhFzMlFWN2cjMjVDNzQWYxYTOwU2MwIDZHljcadFN2wUe5omYyATdZJTO2J2RGdXY5VDdZhlSypFWRZXW6l1MadVWx8EVRpnT6dGMaRUQ14keVdnWH5UbZ1WS61EVBlXTHl1dZdVSvcDZzI2YmVWMjF2NwAjZkN2YmVTY4UTO1YWO4Y2NwQGO"
device_id = "00000000-0000-0000-0000-000000000000"
package_name = "com.coolapk.market"


def base64_encode(data):
    return base64.b64encode(data.encode()).decode()


def base64_decode(data):
    return base64.b64decode(data.encode()).decode()


def reverse_str(s):
    return s[::-1]


def md5_hex_digest(data):
    m = md5()
    m.update(data.encode())
    return m.hexdigest()


def test_token(token: str):
    opener = urllib.request.build_opener()
    opener.addheaders.clear()
    opener.addheaders.append(("User-Agent", "Dalvik/2.1.0 (Linux; U; Android 7.1.2; VirtualBox Build/N2G48H) (#Build; Android-x86; VirtualBox; android_x86-userdebug 7.1.2 N2G48H eng.cwhuan.20180502.160334 test-keys; 7.1.2) +CoolMarket/9.0.2"))
    opener.addheaders.append(("X-Requested-With", "XMLHttpRequest"))
    opener.addheaders.append(("X-Sdk-Int", "25"))
    opener.addheaders.append(("X-Sdk-Locale", "zh-CN"))
    opener.addheaders.append(("X-App-Id", "com.coolapk.market"))
    opener.addheaders.append(("X-App-Version", "9.0.2"))
    opener.addheaders.append(("X-App-Code", "1902151"))
    opener.addheaders.append(("X-App-Version", "9"))
    opener.addheaders.append(("X-App-Token", token))
    response = opener.open(api).read().decode()
    print(json.dumps(json.loads(response), indent=2, ensure_ascii=False))
   