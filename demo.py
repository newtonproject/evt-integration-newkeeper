import urllib
import base64
import hashlib
import json
import time
import requests
import collections
from Crypto.Cipher import AES
from newchain_web3 import Web3
from newchain_account.messages import encode_defunct


'''
First of all, install newchain-web3:
pip install -r requirements.txt
'''

# LIBS

'''
AES ENCRYPT
'''
# 
def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes
# AES ENCRYPT
def aes_encrypt(key, text):
    aes = AES.new(add_to_16(key), AES.MODE_ECB)  # 初始化加密器
    encrypt_aes = aes.encrypt(add_to_16(text))  # 先进行aes加密
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回bytes
    return encrypted_text
# AES DECRYPT
def aes_decrypt(key, text):
    aes = AES.new(add_to_16(key), AES.MODE_ECB)  # 初始化加密器
    base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))  # 优先逆向解密base64成bytes
    decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8').replace('\0', '')  # 执行解密密并转码返回str
    return decrypted_text


def generate_digest(data):
    return hashlib.md5(data.encode('utf-8')).hexdigest()


def sign_hmac(data, secret, prefix='', use_urlencode=False, joint='&'):
    data = collections.OrderedDict(sorted(data.items()))
    sign_string = prefix
    n = 0
    for k, v in data.items():
        if n != 0 and k != 'sign':
            sign_string += joint
        n += 1
        if k != 'sign':
            sign_string += u'%s=%s' % (k, v)
    sign_string += secret
    if use_urlencode:
        sign_string = urllib.quote_plus(sign_string)
    signed_string = generate_digest(sign_string)
    return signed_string


wallet_private_key = '0x37f4e6e04eb21ee5af76f680de85bde687efbf2b5e71e1adacb38ab2784a1b4f'
message = 'evt' + str(time.time())

rpc_url = "https://rpc1.newchain.newtonproject.org/"
w3 = Web3(Web3.HTTPProvider(rpc_url))
signable_message = encode_defunct(text=message)
signed_message = w3.eth.account.sign_message(signable_message, private_key=wallet_private_key)

app_key = 'd41d8cd98f00b204e9800998ecf8427e'
app_secret = '75d78bdb89dd0baeaeacdbef66ba4240'

data = {
    'contract_address': '0xCFeAA0345b6b8B9C701f01e519875455A90D435b',
    'token_id': '1',
    'sign_r': hex(signed_message.r),
    'sign_s': hex(signed_message.s),
    'sign_v': signed_message.v,
    'sign_message': aes_encrypt(app_secret, message),
    'app_key': app_key,
    'timestamp': time.time(),
}

generate_sign = sign_hmac(data, app_secret)
headers = {
    'content-type': 'application/json',
    'Authorization': generate_sign,
}
api_url = 'https://newkeeper-test.devnet.newtonproject.org/api/v1/evt/check/'
response = requests.post(api_url, data=json.dumps(data), headers=headers)
result = json.loads(response.text)

if result['error_code'] == 1:
    csm_version = result['result']['csm_version']
    private_key = result['result']['private_key']
    private_key = aes_decrypt(app_secret, private_key)
    print(private_key)