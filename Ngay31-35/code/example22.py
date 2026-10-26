"""
Sử dụng đa tiến trình và pool tiến trình
Đa luồng vì có GIL nên không thể tận dụng hết ưu thế đa nhân của CPU
Đối với các tác vụ thiên về tính toán (CPU-bound) nên cân nhắc dùng đa tiến trình
time python3 example22.py
real    0m11.512s
user    0m39.319s
sys     0m0.169s
"""
import concurrent.futures
import math

PRIMES = [
    1116281,
    1297337,
    104395303,
    472882027,
    533000389,
    817504243,
    982451653,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419
] * 5


def is_prime(n):
    """Kiểm tra số nguyên tố"""
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    """Hàm chính"""
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))


if __name__ == '__main__':
    main()
