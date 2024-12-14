import random
a = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
e = int(input("di con un numero qué tan larga quieres la contraseña: "))
o = ""
for i in range(e):
    c = random.choice(a)
    o +=c
print(o)
