# 10-dars vazifalar


# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car.lower()=='gm':
        print(car.upper())
    else: print(car.title())

# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car.lower()!='gm':
        print(car.title())
    else: print(car.upper())
    
# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.
ism=input("Loginni kiriting")
if ism.lower()=='admin':
    print('Xush kelibsiz, Admin. Foydalanuvchilar ro\'yxatini ko\'rasizmi?')
else: print(f"Xush kelibsiz, {ism.title()}!")

# Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
print('Ikkita istalgan son kiriting.')
a=float(input("1-son:"))
b=float(input('2-son:'))
if a==b:
    print('Sonlar teng.')
    
# Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 
son=float(input('Istalgan son kiriting: '))
if son>0:
    print('Musbat son')
else: print('Manfiy son')

#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring
son=float(input('Islatgan son kiriting: '))
if son>0:
    print(son**(1/2))
else: print('Musbat son kiriting')