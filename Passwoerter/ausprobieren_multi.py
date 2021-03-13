import hashlib as hshl
from multiprocessing import Pool as ThreadPool
from datetime import datetime

verschluesselt = "f3d32b5c842129e19779389eab03960a" #md5 von yr01()
path_to_dictionary = "Passwoerter/dict.txt"

additional_chars = "0123456789!§$%&/()=?*"

done = False
start = datetime.now()


def einlesen():
    liste = []
    with open(path_to_dictionary, "r") as file:
        for raw_line in file:
            liste.append(raw_line.strip())          
    return liste


def ausprobieren_md5(line):
    #print(line)
    global done

    global start

    temp_versch_0 = hshl.md5(line.encode()).hexdigest()
    if temp_versch_0 == verschluesselt:
        print(f"{ datetime.now()-start } | {verschluesselt} = {line}")
        done = True
        return None

    i = 0
    while i < len(additional_chars) and not done:
        char = additional_chars[i]
        temp_word = line + char
        temp_versch_1 = hshl.md5(temp_word.encode()).hexdigest()
        if temp_versch_1 == verschluesselt:
            print(f"{ datetime.now()-start } | {verschluesselt} = {temp_word}")
            done = True
            return None
        
        for char_2 in additional_chars:

            temp_word_2 = temp_word + char_2
            temp_versch_2 = hshl.md5(temp_word_2.encode()).hexdigest()
            if temp_versch_2 == verschluesselt:
                print(f"{ datetime.now()-start } | {verschluesselt} = {temp_word_2}")
                done = True
                return None
            

            for char_3 in additional_chars:

                temp_word_3 = temp_word_2 + char_3
                temp_versch_3 = hshl.md5(temp_word_3.encode()).hexdigest()
                if temp_versch_3 == verschluesselt:
                    print(f"{ datetime.now()-start } | {verschluesselt} = {temp_word_3}")
                    done = True
                    return None
                
                for char_4 in additional_chars:
                    temp_word_4 = temp_word_3 + char_4
                    temp_versch_4 = hshl.md5(temp_word_4.encode()).hexdigest()
                    if temp_versch_4 == verschluesselt:
                        print(f"{ datetime.now()-start } | {verschluesselt} = {temp_word_4}")
                        done = True
                        return None

        i+=1
def check_time(liste):
    global start
    global done
    line = liste[0]
    temp_versch_0 = hshl.md5(line.encode()).hexdigest()
    if temp_versch_0 == verschluesselt:
        print(f"{ datetime.now()-start } | {verschluesselt} = {line}")
        done = True
        return datetime.now()-start


    for char in additional_chars:

        temp_word = line + char
        temp_versch_1 = hshl.md5(temp_word.encode()).hexdigest()
        if temp_versch_1 == verschluesselt:
            print(f"{ datetime.now()-start } | {verschluesselt} = {temp_word}")
            done = True
            return datetime.now()-start
        
        for char_2 in additional_chars:

            temp_word_2 = temp_word + char_2
            temp_versch_2 = hshl.md5(temp_word_2.encode()).hexdigest()
            if temp_versch_2 == verschluesselt:
                print(f"{ datetime.now()-start } | {verschluesselt} = {temp_word_2}")
                done = True
                return datetime.now()-start
            

            for char_3 in additional_chars:

                temp_word_3 = temp_word_2 + char_3
                temp_versch_3 = hshl.md5(temp_word_3.encode()).hexdigest()
                if temp_versch_3 == verschluesselt:
                    print(f"{ datetime.now()-start } | {verschluesselt} = {temp_word_3}")
                    done = True
                    return datetime.now()-start
                
                for char_4 in additional_chars:
                    temp_word_4 = temp_word_3 + char_4
                    temp_versch_4 = hshl.md5(temp_word_4.encode()).hexdigest()
                    if temp_versch_4 == verschluesselt:
                        print(f"{ datetime.now()-start } | {verschluesselt} = {temp_word_4}")
                        done = True
                        return datetime.now()-start
    delta = datetime.now()-start
    print(f"expected time for all items = {delta.total_seconds()* len(liste) / 12}s")
if __name__ == "__main__":
    words = einlesen()
    print("Einlesen fertig")
    check_time(words)
    pool = ThreadPool(12)
    start = datetime.now()
    pool.map(ausprobieren_md5, words)
    pool.close()
    pool.join()