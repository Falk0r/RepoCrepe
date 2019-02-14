import random
import string

def generer(nb_caracteres):
    caracteres = string.ascii_letters + string.digits
    aleatoire = [random.choice(caracteres) for _ in range(nb_caracteres)]

    return ''.join(aleatoire)

print(generer(5))
