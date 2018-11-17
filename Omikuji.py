import random

omikuji = ["大凶", "凶", "吉", "小吉", "大吉", "大大凶"]

count = random.randint(0, 5)

decision = omikuji[count]

print(f"今日の運勢は... {decision}")
