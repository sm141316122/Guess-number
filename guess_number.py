import random

num = random.randint(1, 100)
guess_num = 0
while True:
	guess_num += 1
	ans = int(input("猜個1~100的數字"))
	print(f"猜第{guess_num}次")
	if num == ans:
		print("猜對了!")
		break
	else:
		if num > ans:
			print("比較大")
		else:
			print("比較小")
