from sympy import symbols, Eq, solve, Rational

print("Tenglamalar sistemasi yechish dasturiga xush kelibsiz")
print("Sizdan tenglamalarni quyidagi korinishda kiritish soralaladi: ax+by=c")

#-1: (---1 tenglama uchun malumotlarni sorash)
print("---TENGLAMALAR SISTEMASINI YECHISH---")
print("DIQQAT: Agar tenglamada ayirish bolsa (masalan: 4x - y = 9),")
print("sonni minus belgisi bilan kiriting (yani -1 yoki -2).")
print("☆" * 43)

print("---1-TENGLAMA UCHUN---")
a1 = Rational(input("x-ning oldidagi son :"))
b1 = Rational(input("y-ning oldidagi son :"))
c1 = Rational(input("Barobardan keyingi son :"))


#-2 (---2 tenglama uchun malumotlarni sorash)
print("---2-TENGLAMA UCHUN---")
a2 = Rational(input("x-ning oldidagi son :"))
b2 = Rational(input("y-ning oldidagi son : "))
c2 = Rational(input("Barobardan keyingi son :"))


#SymPy orqali hisoblash
x, y = symbols("x y")

#Foydalanuvchi kiritgan sonlardan tenglama yigamiz
eq1 = Eq(a1*x + b1*y, c1)
eq2 = Eq(a2*x + b2*y, c2)

solution = solve((eq1, eq2), (x, y))
print("\n"  +  "="  *  43)
print("NATIJA :")
if solution:
	print(f"x = {solution[x]}")
	print(f"y = {solution[y]}")
else:
	print("Bu tenglamalar sistemasining yechimi yoq")
print("=" * 43)
