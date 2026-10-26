"""
Mã hóa và giải mã
Mã hóa đối xứng - Mã hóa và giải mã dùng chung một khóa - DES / AES
Mã hóa bất đối xứng - Mã hóa và giải mã dùng các khóa khác nhau - RSA
pip install pycrypto
"""
import base64

from hashlib import md5

from Crypto.Cipher import AES
from Crypto import Random
from Crypto.PublicKey import RSA

# # Khóa mã hóa AES (độ dài 32 byte)
# key = md5(b'1qaz2wsx').hexdigest()
# # Vector khởi tạo AES (sinh ngẫu nhiên)
# iv = Random.new().read(AES.block_size)


def main():
    """Hàm chính"""
    # Sinh cặp khóa
    key_pair = RSA.generate(1024)
    # Nhập khóa công khai
    pub_key = RSA.importKey(key_pair.publickey().exportKey())
    # Nhập khóa riêng tư
    pri_key = RSA.importKey(key_pair.exportKey())
    message1 = 'hello, world!'
    # Mã hóa dữ liệu
    data = pub_key.encrypt(message1.encode(), None)
    # Mã hóa BASE64 dữ liệu đã mã hóa
    message2 = base64.b64encode(data[0])
    print(message2)
    # Giải mã BASE64 dữ liệu đã mã hóa
    data = base64.b64decode(message2)
    # Giải mã dữ liệu
    message3 = pri_key.decrypt(data)
    print(message3.decode())
    # # AES - Mã hóa đối xứng
    # str1 = 'Tôi yêu các bạn!'
    # cipher = AES.new(key, AES.MODE_CFB, iv)
    # # Mã hóa
    # str2 = cipher.encrypt(str1)
    # print(str2)
    # # Giải mã
    # cipher = AES.new(key, AES.MODE_CFB, iv)
    # str3 = cipher.decrypt(str2)
    # print(str3.decode())


if __name__ == '__main__':
    main()
