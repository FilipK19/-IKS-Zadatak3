import multiprocessing
import time
import random
import sys

class Objekt(multiprocessing.Process):
    def __init__(self, ime, kašnjenje):
        super().__init__()
        self.ime = ime
        self.kašnjenje = kašnjenje

    def run(self):
        print(f"Objekt {self.ime} je kreiran, PID={self.pid}, kašnjenje {self.kašnjenje} ms \n")
        time.sleep(self.kašnjenje/1000)  # Pretvaramo kašnjenje u sekunde
        #print(f"Objekt {self.ime} je završio obradu")

if __name__ == '__main__':
    imena = [str(item) for item in sys.argv[1:]]  # Replace with imena from another code
    objekti = []

    # Otvaramo novi proces za svako ime
    for ime in imena:
        kašnjenje = random.randint(1, 1000) # Slučajno kašnjenje od 1 do 1000 ms
        objekt = Objekt(ime.strip(), kašnjenje)
        objekt.start()
        objekti.append(objekt)

    # Čekamo da se svi procesi završe
    for objekt in objekti:
        objekt.join()
