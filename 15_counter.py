count = 0
for n in range(5):
	num = int(input(f"{n+1} Sonni kiriting"))
	if num % 2 == 0 and num > 0:
		count += 1
print(f"----Natija----")
print(f" Siz kiritgan sonlar ichida {count}-ta musbat va juft sonlar bor")		