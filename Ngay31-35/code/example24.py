"""
aiohttp - Truy cập mạng HTTP bất đồng bộ
I/O bất đồng bộ (lập trình bất đồng bộ) - Chỉ dùng một luồng (đơn luồng) để xử lý yêu cầu người dùng
Một khi yêu cầu của người dùng được tiếp nhận, phần còn lại đều là thao tác I/O, thông qua I/O multiplexing cũng có thể đạt được hiệu quả đồng thời
Cách làm này so với đa luồng có thể giúp tận dụng CPU cao hơn vì không có chi phí chuyển đổi ngữ cảnh giữa các luồng
Redis/Node.js - Đơn luồng + I/O bất đồng bộ
Celery - Xử lý bất đồng bộ các tác vụ tốn thời gian
Vòng lặp sự kiện I/O bất đồng bộ - uvloop
"""
import asyncio
import re

import aiohttp


async def fetch(session, url):
    async with session.get(url, ssl=False) as resp:
        return await resp.text()


async def main():
    pattern = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/')
    async with aiohttp.ClientSession() as session:
        for url in urls:
            html = await fetch(session, url)
            print(pattern.search(html).group('title'))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
