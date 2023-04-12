import subprocess

# Definiramo funkciju za pokretanje skripte 3 puta
def pokreni_skriptu(imena):
    for _ in range(3):
        subprocess.Popen(['python', 'imena.py'] + [str(item) for item in imena]).wait()

if __name__ == '__main__':
    while True:
        imena = input("Unesite listu imena odvojenih zarezom (ili 'q' za izlaz): ").split(',')
        if 'q' in imena:
            break
        pokreni_skriptu(imena)
