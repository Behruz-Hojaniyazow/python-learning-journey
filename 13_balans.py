try:
	balance = 100000
	for i in range(3):
		taken_cash = float(input(f"{i+1} Qancha pul olmokchisiz"))
		if taken_cash > balance:
			print("Balanceda mablag yetarli emas")
		elif taken_cash <= balance:
			balance -= taken_cash
			print(f"Muwaffaqqiyatli qolgan balans {balance}")
		if balance == 0:
			print("Hisobingizda pul qolmadi")
			break
except:
	print("Iltimos faqat son kiriting")