#  8-dars. Ro'yxatlar bilan ishlash.

#  27.08.2022

# muallif: Abror

cars=['tesla', 'audi','wolksvagen','honda','lada']
#cars.sort()
#cars.sort(reverse=True)
#print(sorted(cars))
#print(sorted(cars, reverse=True))
cars.reverse()


sonlar2=list(range(33,46))
sonlar=list(range(1,11))

toq_sonlar=list(range(1,21,2))
juft_sonlar=list(range(0,21,2))

#print('Eng kchigi;', min(sonlar))
#print('Eng kattasi:', max(sonlar))
#print("Jami: ",sum(sonlar))

cars.append('bmw')
cars.append( 'hummer')
cars.append('mersedes benz')

my_cars=cars[0:2]
#print(cars[:4])
#print(cars[4:])
my_cars=cars
my_cars.append('gm')
my_cars=cars[:]
del my_cars[1]
my_cars.remove('hummer')