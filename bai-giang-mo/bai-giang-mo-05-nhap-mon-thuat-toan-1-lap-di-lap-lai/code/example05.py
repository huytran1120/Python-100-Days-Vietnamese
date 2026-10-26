"""
Gà trống 5 đồng một con, gà mái 3 đồng một con, gà con 1 đồng ba con, dùng 100 đồng mua một trăm con gà, hỏi có bao nhiêu gà trống, gà mái, gà con?
"""
for x in range(21):
    for y in range(34):
        z = 100 - x - y
        if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:
            print(x, y, z)

