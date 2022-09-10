# 15 dars Vazifalar
"""
Created on Wed Aug 31 16:00:09 2022

@author: Abror
"""
# 1. Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.
phyton={
        'string':'matn ko\'rinishidagi qiymat',
        'konsol':'yozilgan kodning ishlashini ko\'rsatuvchi maydon',
        '#':'o\'zidan keyingi kodni bajarilishini to\'xtatuvchi belgi',
        'o\'zgaruvchi':"kompyuter xotirasida ma'lum nom bilan axborot saqlash uchun ajratilgan joy",
        'float':'o\'nli kasr',
        'integer':'butun son',
        'if':'agar',
        'elif':'bo\'lmasa, agar',
        'else':'yo\'qsa',
        'len':'uzunlik, hajm',
        'type':'turi',
        'sintax':'sintaksis, kod yozish qoidasi'        
        }
for k,q in phyton.items():
    print(f"{k.title()} - {q.capitalize()}")

# 2. Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring. 
poytaxtlar={
    'aqsh':'vashington',
    'rossiya':'moskva',
    'o\'zbekiston':'toshkent',
    'qozog\'iston':'nursulton',
    'hindiston':'nyu-dehli',
    'afg\'oniston':'qobul',
    'fransiya':'madrid',
    'germaniya':'berlin',
    'italiya':'rim',
    'meksika':'mexiko'
    }
#print('Davlatlar:\n')
#for davlat in sorted(poytaxtlar.keys()):
#    print(davlat.upper())

#print('\nPoytaxtlar:\n')
#for poytaxt in sorted(poytaxtlar.values()):
#    print(poytaxt.title())
    
# 3. Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.

davlat=input('Qaysi davlatning poytaxtini bilishni istaysiz? ').lower()

# 1-variant
poytaxt=poytaxtlar.get(davlat)
if poytaxt== None:
    print('Bizda bunday ma\'lumot yo\'q.')
else: print(f"{davlat.title()}ning poytaxi {poytaxt.title()} shahri.")



#2-variant
if davlat in poytaxtlar:
    print(f"{davlat.title()}ning poytaxi {poytaxtlar[davlat].title()}.")
else: print('Bizda bunday ma\'lumot yo\'q.')

# 4. Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
menu={
      'somsa':4000,
      'osh':20000,
      'lag\'mon':18000,
      'bifshteks':21000,
      'norin':15000,
      'manti':6000,
      'choy':2000,
      'non':3000,
      'salat':3000,
      'limonli choy':5000
      }
buyurtma=[]
print('3ta taom buyurtma qiling.')
for n in range(3):
    buyurtma.append(input(f"{n+1}-taom: ").lower())
    
for taom in buyurtma:
    if taom in menu:
        print(f"{taom.title()} {menu[taom]} so'm.")
    else: 
        print(f"Kechirasiz, bizda {taom} yo'q.")




