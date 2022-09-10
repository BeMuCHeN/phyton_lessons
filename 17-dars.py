#  17-dars. While sikli
"""
Created on Fri Sep  9 17:57:28 2022

@author: Abror
"""
#input
ism=input("Ismingiz nima? ")
savol=(f"Salom {ism.title()}, yoshingiz nechida? ")
yosh=input(savol)
yosh=int(yosh)
boy=input("Bo'yingiz necha metr? ")
boy=float(boy)

#while

savol='Istalgan sonni kitiring.'
savol+="(dasturni tugatish uchun 'exit' deb yozing): \n"
qiymat=''
while qiymat!='exit':
    qiymat=input(savol).lower()
    if qiymat!='exit':
        print(f"{qiymat}^2={float(qiymat)**2}")
print("Dastur tugadi!")

#ishora
savol='Istalgan sonni kitiring.'
savol+="(dasturni tugatish uchun 'exit' deb yozing):\n"
sabab=True
while sabab:
    qiymat=input(savol)
    if qiymat.lower()=='exit':
        sabab=False
    else:
        print(f"{qiymat}^2={float(qiymat)**2}")
print("Dastur tugadi!")

#break
savol='Istalgan sonni kitiring.'
savol+="(dasturni tugatish uchun 'exit' deb yozing):\n"
while True:
    qiymat=input(savol)
    if qiymat.lower()=='exit':
        break
    else: print(f"{qiymat}^2={float(qiymat)**2}")
print("Dastur tugadi!")


#continue #while
#barcha juft sonlarni chiqaruvchi dastur.
#abadiy silk
son=0
while True:
    son+=1
    if son%2!=0:
        continue
    else: print(son)
#10 gacha juft sonlarni chiqaruvchi dastur
son=0
while son<10:
    son+=1
    if son%2!=0:
        continue
    else: print(son)
    







