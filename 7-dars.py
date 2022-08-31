#7-dars. ro'yxatlar. Lists

#25/08.2022

#muallif: Abror

fanlar=['kimyo', 'fizika', 'tarix', 'algebra']
narxlar=[23, 45000, 33.4, -11]
aralash=['she', -23000, 12.3]
ismlar=[]
#print(narxlar[2]) # 0,1,2,3 deb sanab chaqirish mn
#print(fanlar[-1])
#print(fanlar[-2]) # -1, -2, -3 deb oxiridan sanab chaqirish ham mn

#print(fanlar[1].upper())
#print(float(narxlar[1]))
#a=narxlar[1]+aralash[-2]
#print(a)

fanlar[2]='geografiya'

#   .append()  list ga element qoshish. Oxiriga qo'shish
fanlar.append('english')


#   .insert(o'rni, element)    Elementni ma'lum joyga qo'shish

fanlar.insert(1,"biologiya")

# del list[] ro'yxatdan elementni indexi bo'yicha o'chirish
# index -1 lar ishlamadi!!!

del aralash[2]
#del fanlar[-1]   # ishlamadi!!!

#   .remove()  nomi bo'yicha  ro'yxatdan o'chirish.  chapdan boshlab bittadan o'chiradi

fanlar.insert(5, 'fizika')

fanlar.remove("fizika")

#   .pop()   ro'yxatdan elementni sug'urib olib ishlatish.

fan=fanlar.pop(-1)
#print(fanlar)
