#11-dars. if-elif-else

#28.08.2022

#muallif:Abror

kun=input("Bugun qaysi kun?>>>")
harorat=int(input("Harorat qanday?>>>"))

#if (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat>=30:
#    print('Qani, cho\'milishga ketdik!')
#elif (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat<30:
#    print('Uyda dam olamiz!')
#else: print('Bugun ishga borish kerak!')

menu=['sho\'rva','manti','osh','qozonkabob','lag\'mon','bifshteks']
buyurtma=['somsa','limonli choy','assorti']

if buyurtma:
    for taom in buyurtma:
        if taom in menu:
            print(f"{taom.title()} menuda bor.")
        else: print(f"Kechirasiz, {taom} menuda yo\'q.")
else:print("Biror nima buyurtma qilasizmi?")
