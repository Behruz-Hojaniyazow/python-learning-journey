try:
	day = int(input("1-dan 7-gacha son kiriting"))
	if day == 1:
		print("Dushanba")
	elif day == 2:
		print("Sheshanba")
	elif day == 3:
		print("Chorshanba")
	elif day == 4:
		print("Payshanba")
	elif day == 5:
		print("Juma")
	elif day == 6:
		print("Shanba")
	elif day == 7:
		print("Yakshanba")
	else:
		print("Xato bunday kun yoq")
except ValueError:
	print("Iltimos faqat son kiriting")