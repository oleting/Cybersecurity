import hashlib as hshl
from datetime import datetime
import threading

from Passwoerter.classThread import PasswortThreader as Thread

threads = 2
word = "zoom_in*="

verschluesselt = hshl.md5(word.encode()).hexdigest()
#verschluesselt = "f3d32b5c842129e19779389eab03960a"


addionial_chars = "0123456789!§$%&/()=?*'"

start=datetime.now()         

insgesamte_liste = []

path_to_dictionary = "Passwoerter/dict.txt"

with open(path_to_dictionary, "r") as file:
    for line in file:
        insgesamte_liste.append(line.strip())


def split_liste(alist, end_zahl=2):
    length = len(alist)
    
    return ([ alist[i*length // end_zahl: (i+1)*length // end_zahl] 
             for i in range(end_zahl) ])

listen = split_liste(insgesamte_liste, threads)
i = 1
for liste in listen:
    thread = Thread(i, liste, verschluesselt, addionial_chars, start)
    thread.start()
    i += 1

