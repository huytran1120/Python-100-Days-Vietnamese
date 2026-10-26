"""
Coroutine - Chương trình con phối hợp có thể chuyển đổi ngữ cảnh khi cần
"""
import asyncio

from example15 import is_prime


def num_generator(m, n):
    """Generator số trong khoảng chỉ định"""
    yield from range(m, n + 1)


async def prime_filter(m, n):
    """Bộ lọc số nguyên tố"""
    primes = []
    for i in num_generator(m, n):
        if is_prime(i):
            print('Prime =>', i)
            primes.append(i)

        await asyncio.sleep(0.001)
    return tuple(primes)


async def square_mapper(m, n):
    """Bộ ánh xạ bình phương"""
    squares = []
    for i in num_generator(m, n):
        print('Square =>', i * i)
        squares.append(i * i)

        await asyncio.sleep(0.001)
    return squares


def main():
    """Hàm chính"""
    loop = asyncio.get_event_loop()
    future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
    future.add_done_callback(lambda x: print(x.result()))
    loop.run_until_complete(future)
    loop.close()


if __name__ == '__main__':
	main()
