# 5-dars Matn bilna ishlash (String)
#Created on Mon Aug 22 04:37:22 2022
#Muallif: Abror
  
#ism = "Anvar"
#familiya = "Aripov"
#print(ism,familiya)
#print(ism+familiya)
#print(ism+' '+familiya)
#print(ism +familiya)

shahar="Кокон"
viloyat="Фаргона"
#print(shahar+viloyat)
#print(shahar, viloyat)
ism = "Anvar"
familiya = "Aripov"
ism_familiya=f"{ism} {familiya}"
#print(ism_familiya)

ism= "James"
familiya="Bond"
#print(f"Salom, mening ismim {familiya}, {ism} {familiya}!")

#print("Hello WORLD")
#print("Hello \tWORLD")
#print("Hello\tWORLD")



#print("Salom, mening ismim (familiya)")

ism="James"
sharif="Bond"
ism_sharif=f"{ism} {sharif}"

#print(ism_sharif.upper())
#print(ism.lower())
#print(sharif.title())
ism_sharif=ism_sharif.upper()
#print(familiya.capitalize())
#print(ism_sharif.title())
#print(ism_sharif.capitalize())


meva="      olma      "
#print("Men", meva, "yaxshi ko'raman")
#print("Men", meva.lstrip(), "yaxshi ko'raman")
#print("Men", meva.rstrip(),"yaxshi ko'raman")
#print("Men", meva.strip(), "yaxshi ko'raman")

gap="            Men        olmani yaxshi ko'raman      "
#print(gap.strip())

ism=input('Ismingiz nima?')
print("Assalomu alaykum, ", +ism)
