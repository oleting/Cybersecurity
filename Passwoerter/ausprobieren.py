import hashlib as hshl
from datetime import datetime

word = "zoom_in"

verschluesselt = hshl.md5(word.encode()).hexdigest()
verschluesselt = "f3d32b5c842129e19779389eab03960a"
path_to_dictionary = "Passwoerter/dict.txt"

addionial_chars = "0123456789!§$%&/()=?*'"



start=datetime.now()

with open(path_to_dictionary, "r") as file:
    for line in file:
        temp_versch = hshl.md5(line.strip().encode()).hexdigest()
        if temp_versch == verschluesselt:
            print(verschluesselt + " = " + line.strip())
            print(datetime.now()-start)
        
        for char in addionial_chars:
            temp_word = line.strip() + char
            temp_versch = hshl.md5(temp_word.encode()).hexdigest()
            if temp_versch == verschluesselt:
                print(verschluesselt + " = " + temp_word)
                print(datetime.now()-start)
                
            for sign in addionial_chars:
                temp_sign = temp_word + sign
                temp_versch = hshl.md5(temp_sign.encode()).hexdigest()
                if temp_versch == verschluesselt:
                    print(verschluesselt + " = " + temp_sign)
                    print(datetime.now()-start)
                
                for signs in addionial_chars:
                    temp_signs = temp_sign + signs
                    temp_versch = hshl.md5(temp_signs.encode()).hexdigest()
                    if temp_versch == verschluesselt:
                        print(verschluesselt + " = " + temp_signs)
                        print(datetime.now()-start)
                    
                    for signs2 in addionial_chars:
                        temp_signs2 = temp_signs + signs2
                        temp_versch = hshl.md5(temp_signs2.encode()).hexdigest()
                        if temp_versch == verschluesselt:
                            print(verschluesselt + " = " + temp_signs)
                            print(datetime.now()-start)

print(datetime.now()-start)