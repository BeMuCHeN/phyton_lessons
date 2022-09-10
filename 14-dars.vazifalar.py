# 14-dars. Lug'atlar 
#          +vazifalar

# Created on Wed Aug 31 10:25:39 2022

# author: Abror

book={'nom':'biokimyo','rang':'ko\'k','til':'rus'}
#print(book['rang'])
#print(book['nom'])

book['muallif']='Severin'
book['yil']=2008
book['yil']=2012

# 1. otam (onam, akam, ukam, va hokazo) degan lug'at yarating\ 
#    va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting \
#    (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi \
#     ma'lumotni matn shaklida konsolga chiqaring :Otamning \
#    ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan

akam={"ism":'Ahror','yil':'1996','kasb':'haydovchi','shahar':'Toshkent'}
#print(f"Akamning ismi {akam['ism']}, {akam['yil']}-yilda tug'ilgan. {akam['kasb'].title()} bo'lib ishlaydi. {akam['shahar'].title()}da yashaydi.")

# 2. Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh

meals={'suxrob':'lag\'mon','ali':'osh','yusuf':'tandir kabob','jamshid':'shashlik','sardor':'manti'}
#print(f"Suxrobning sevimli taomi {meals['suxrob']}.")
#print(f"Jmashidning  sevimli taomi {meals['jamshid']}.")
#print(f"{meals['yusuf'].capitalize()} Yusufning sevimli taomi.")

# 3. Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.

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

# 4. Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
kalit=input("Kalit so'zni kiriting: ")
izoh=phyton.get(kalit.lower(),'Bunday so\'z mavjud emas')
print(izoh.capitaliz())

# 5. Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.
kalit=input("Kalit so'zni kiriting: ")
if kalit in phyton:
    print(f"{kalit.capitalize()} so'zi {phyton[kalit].capitalize()} deb tarjima qilinadi.")
else: print("Bunday so'z mavjud emas!")
