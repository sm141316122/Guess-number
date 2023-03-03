import random

r1 = int(input("請輸入範圍 第1個數字: "))
r2 = int(input("請輸入範圍 第2個數字(要比第1個數字大): "))
num = random.randint(r1, r2)
guess_num = 0

while True:
	guess_num += 1
	ans = int(input(f"猜個數字: "))
	print(f"猜第{guess_num}次")
	if num == ans:
		print("猜對了!")
		break
	elif num > ans:
		print(f"{ans}太小了")
	else:
		print(f"{ans}太大了")
