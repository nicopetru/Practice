import datetime

reloj = datetime.datetime.now()
hoy = datetime.date.today()

print(reloj)
print("hoy",hoy)

nico = datetime.date(1986,2,23) # variable nico con fecha 23-2-86
print(nico)
print("año:",nico.year,"mes:",nico.month,"dia:",nico.day)

def edad(x):
    years = hoy.year - x.year - ((hoy.month, hoy.day) < (x.month, x.day))
    print((hoy.month, hoy.day) < (x.month, x.day))
    return years

print("edad",edad(nico))