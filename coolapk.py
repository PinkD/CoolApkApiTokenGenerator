import json
import time
import urllib.request

from common import *

if __name__ == "__main__":
    r_built_in = reverse_str(built_in_str)
    r_built_in_decoded = base64_decode(r_built_in)
    cut_r_built_in = r_built_in_decoded[32:-32]
    r_cut = reverse_str(cut_r_built_in)
    token = base64_decode(r_cut)

    print(token)

    timestamp = int(time.time())
    timestamp_md5 = md5_hex_digest(str(timestamp))

    salt = token + timestamp_md5 + "$" + device_id + "&" + package_name

    salt_encoded = base64_encode(salt)
    salt_md5 = md5_hex_digest(salt_encoded)

    result = salt_md5 + device_id + f'0x{timestamp:x}'
    print(result)

    test_token(result)
