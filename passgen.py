import random
Lburti = "QWERTYUIOPASDFGHJKLZXCVBNM"
Mburti = "qwertyuiopasdfghjklzxcvbnm"
Kburti = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
cipari = "1234567890"
zimes = "!@£$*;:?"
Vkopa = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@$*:?"
skaits = int(input("Character Amount: "))

rando = random.choices(Vkopa, k=skaits)
print (*rando, sep='')