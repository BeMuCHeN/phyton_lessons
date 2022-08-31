#  8-dars . Vazifalar

# 27.08.2022

# muallif: Abror

# 1.O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar=['rossiya', 'aqsh', 'gruziya', 'baa', 'eron', 'uzbekistan','xitoy' ]
#print(davlatlar)

# 2. Ro'yxatning uzunligini konsolga chiqaring
#print(len(davlatlar))

# 3. sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
#print(sorted(davlatlar))

# 4. sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
#print(sorted(davlatlar, reverse=True))

# 5. Asl ro'yxatni qaytadan konsolga chiqaring
#print(davlatlar)

# 6. reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
davlatlar.reverse()
print(davlatlar)

# 7. sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
davlatlar.sort()
#print(davlatlar)
davlatlar.sort(reverse=True)
#print(davlatlar)

# 8. 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
juft_sonlar=list(range(120,1201,2))

# 9. Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
#print(sum(juft_sonlar))

# 10. Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
#print(max(juft_sonlar)-min(juft_sonlar))

# 11. Ro'yxatdagi elementlar sonini hisoblang
a=len(juft_sonlar)

# 12. Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
#print(juft_sonlar[:19])
#print(juft_sonlar[261:282])
#print(juft_sonlar[521:])

# 13. taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar=['qovurilgan tuxum', 'osh','salat','sariyog\'','tarvuz','mastava']
         
# 14. nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta=taomlar[:]

# 15. Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
del nonushta[1]
del nonushta[1]
del nonushta [2]
del nonushta[-1]
nonushta.append('sut')
nonushta.insert(0,'yong\'oq')

# 16. Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print('Taomlar ro\'yxati:', taomlar,'Nonushta uchun taomlar:', nonushta)

# 17. Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring
nonushta=tuple(nonushta)
#nonushta[0]='qaymoq va non' # tuple ga o'zgartirish kiritib bo'lmadi!
