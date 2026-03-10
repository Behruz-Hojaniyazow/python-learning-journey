import math

#1.Funksiyalar hisop kitop qisimlari
def kvadrat():
	a = float(input("Tamonini kiriting"))
	return a**2
def doira():
	r = float(input("Radiusni kiriting"))
	return math.pi * r**2
def togri_tortburchak():
	a = float(input("Boyini kiriting"))
	b = float(input("Enini kiriting"))
	return a * b
def uchburchak():
	a = float(input("Asosini kiriting"))
	h = float(input("Balandligini kiriting"))
	return (a * h) / 2
def kub_hajm():
	a = float(input("Qirrasini kiriting"))
	return a**3
def shar_hajm():
	r = float(input("Radiusini kiriting"))
	return (4 / 3) * math.pi * r**3
	
#2.Dictionary, Endi bu yerda funksiyalar turibdi
formulalar = {
			"kvadrat" : kvadrat,
			"doira" : doira,
			"togri tortburchak" : togri_tortburchak,
			"uchburchak" : uchburchak,
			"kub hajm" : kub_hajm,
			"shar hajm" : shar_hajm
}
#3.Foydalanuvchidan sorash
shakl = input("Qaysi shakl kerak").lower()

#4.Dictionary-dan chiqarish
if shakl in formulalar:
	result = formulalar[shakl] ()
	print(f"Natija {result}")
else:
	print("Bunday shakl yoq")