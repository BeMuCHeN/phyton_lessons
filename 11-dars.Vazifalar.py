#11-dars. Vazifalar

#31.08.2022/Abror

# 1. Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
son=int(input("Juft son kiriting: "))
if son%2==0:
  print('Rahmat!')
else: print('Bu juft son emas!')

# 2. Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
#Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
#Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
#Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

yosh=int(input("Yoshingiz nechida?>>>"))
if yosh<4 or yosh>60:
    narx='bepul'
if yosh>=4 and yosh<18:
    narx=10000
if yosh>=18 and yosh<=60:
    narx=20000

if narx=='bepul':
    print('Chipta bepul')
else: print('Chipta narxi: ', narx)

# 3. Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
a=float(input("Ikkita son kiriting.\nBirinchi sonni kiriting: "))
b=float(input("Ikkinchi sonni kiriting: "))
if a>b: 
    print(f"{a}>{b}")
elif a<b:
    print(f"{a}<{b}")
else: print(f"{a}={b}")

# 4. mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

mahsulotlar=['olma','non','tuxum','tarvuz',"sariyog'",'coca cola','rollton','pampers','sut','tort','pista']
savat=[]
for n in range(5):
    savat.append(input(f"{n+1}-mahsulotni kiriting: "))

for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"{mahsulot.title()} do'konimizda bor.")
    else: print(f"{mahsulot.title()} do'konimizda yo'q.")
    
# 5. Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.

mahsulotlar=['olma','non','tuxum','tarvuz',"sariyog'",'coca cola','rollton','pampers','sut','tort','pista']
savat=[]
for n in range(5):
    savat.append(input(f"{n+1}-mahsulotni kiriting: "))
bor_mahsulotlar=[]
mavjud_emas=[]
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
    print("Quyidagi mahsulotlar do'konimizda yo'q:")
    for n in mavjud_emas:
        print(n)
else:
  print("Do'konimizda barcha mahsulotlar bor.")

# 6. foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

foydalanuvchilar=['ani','jokker','alex','konsta','mira']
login=input("Loginni kiriting:>>>")
if login.lower() in foydalanuvchilar:
    print('Login band. Yangi login tanlang!')
else: print("Xush kelibsiz!")

# 7. Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.

son=int(input("Istalgan butun son kiriting: "))
if son%2==0:
    print(f"{son} soni 2 ga qoldiqsiz bo'linadi.")
if son%3==0:
    print(f"{son} soni 3 ga qoldiqsiz bo'linadi.")
if son%4==0:
    print(f"{son} soni 4 ga qoldiqsiz bo'linadi.")
if son%5==0:
    print(f"{son} soni 5 ga qoldiqsiz bo'linadi.")
if son%6==0:
    print(f"{son} soni 6 ga qoldiqsiz bo'linadi.")
if son%7==0:
    print(f"{son} soni 7 ga qoldiqsiz bo'linadi.")
if son%8==0:
    print(f"{son} soni 8 ga qoldiqsiz bo'linadi.")
if son%9==0:
    print(f"{son} soni 9 ga qoldiqsiz bo'linadi.")
if son%10==0:
    print(f"{son} soni 10 ga qoldiqsiz bo'linadi.")

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")




