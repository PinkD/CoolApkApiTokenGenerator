import time

from common import md5_hex_digest, package_name, base64_encode

token = "token://com.coolapk.market/c67ef5943784d09750dcfbb31020f0ab?"


def get_as(device_id="00000000-0000-0000-0000-000000000000") -> str:
    '''
    generate coolapk api token with device id
    :param device_id: uuid
    :return: token
    '''
    timestamp = int(time.time())
    timestamp_md5 = md5_hex_digest(str(timestamp))

    salt = token + timestamp_md5 + "$" + device_id + "&" + package_name

    salt_encoded = base64_encode(salt)
    salt_md5 = md5_hex_digest(salt_encoded)

    return salt_md5 + device_id + f'0x{timestamp:x}'
