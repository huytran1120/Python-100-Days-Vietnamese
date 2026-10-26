"""
Mã hóa và giải mã - BASE64
0-9A-Za-z+/
1100 0101 1001 0011 0111 0110
00110001 00011001 00001101 00110110
base64
b64encode / b64decode
-------------------------------------
Tuần tự hóa và giải tuần tự hóa
Tuần tự hóa - Biến đối tượng thành chuỗi byte (bytes) hoặc chuỗi ký tự (str) - serialization / pickling
Giải tuần tự hóa - Khôi phục chuỗi byte hoặc chuỗi ký tự thành đối tượng
Hỗ trợ tuần tự hóa của thư viện chuẩn Python:
json - Tuần tự hóa dạng ký tự
pickle - Tuần tự hóa dạng byte
dumps / loads
"""
import base64
import json
import redis

from example02 import Person


class PersonJsonEncoder(json.JSONEncoder):

    def default(self, o):
        return o.__dict__


def main():
    cli = redis.StrictRedis(host='120.77.222.217', port=6379, 
                            password='123123')
    data = base64.b64decode(cli.get('guido'))
    with open('guido2.jpg', 'wb') as file_stream:
        file_stream.write(data)
    # with open('guido.jpg', 'rb') as file_stream:
    #     result = base64.b64encode(file_stream.read())
    # cli.set('guido', result)
    # persons = [
    #     Person('jackfrued', 39), Person('Vương Đại Chùy', 18),
    #     Person('Bạch Nguyên Phương', 25), Person('Địch Nhân Kiệt', 37)
    # ]
    # persons = json.loads(cli.get('persons'))
    # print(persons)
    # cli.set('persons', json.dumps(persons, cls=PersonJsonEncoder))


if __name__ == '__main__':
    main()

