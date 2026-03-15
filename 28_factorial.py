# 1. Foydalanuvchidan sonni so'raymiz
son = int(input("Faktorialni hisoblash uchun son kiriting: "))

# 2. Natijani saqlash uchun o'zgaruvchi (ko'paytirish bo'lgani uchun 1 dan boshlaymiz)
faktorial = 1

# 3. Agar son manfiy bo'lsa, faktorial mavjud emas
if son < 0:
    print("Manfiy sonlarning faktoriali mavjud emas.")
elif son == 0:
    print("0 ning faktoriali 1 ga teng.")
else:
    # 4. for tsikli orqali 1 dan son+1 gacha aylanamiz
    for i in range(1, son + 1):
        faktorial = faktorial * i  # Har bir sonni natijaga ko'paytirib boramiz

    print(f"{son} ning faktoriali: {faktorial}")