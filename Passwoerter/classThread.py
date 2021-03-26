import hashlib as hshl
from datetime import datetime
import threading

def checkHash(value, verschluesselt, additional_chars, start):
    # single_word = hshl.md5(value.encode()).hexdigest()
    # if single_word == verschluesselt:
    #     #print(f"{ datetime.now()-start } | {verschluesselt} = {value}")
    #     return True, datetime.now()-start, f"{verschluesselt} = {value}"
        
    for char in additional_chars:
        temp_word = value + char
        # temp_versch_1 = hshl.md5(temp_word.encode()).hexdigest()
        # if temp_versch_1 == verschluesselt:
        #     #print(f"{ datetime.now()-start } | {verschluesselt} = {temp_word}")
        #     return True, datetime.now()-start, f"{verschluesselt} = {temp_word}"
    
        for char_2 in additional_chars:

            temp_word_2 = temp_word + char_2
            temp_versch_2 = hshl.md5(temp_word_2.encode()).hexdigest()
            if temp_versch_2 == verschluesselt:
                #print(f"{ datetime.now()-start } | {verschluesselt} = {temp_word_2}")
                return True, datetime.now()-start, f"{verschluesselt} = {temp_word_2}"

            # for char_3 in additional_chars:
            #     temp_word_3 = temp_word_2 + char_3
            #     temp_versch_3 = hshl.md5(temp_word_3.encode()).hexdigest()
            #     if temp_versch_3 == verschluesselt:
            #         #print(f"{ datetime.now()-start } | {verschluesselt} = {temp_word_3}") 
            #         return True, datetime.now()-start, f"{verschluesselt} = {temp_word_3}"
                
            #     for char_4 in additional_chars:
            #         temp_word_4 = temp_word_3 + char_4
            #         temp_versch_4 = hshl.md5(temp_word_4.encode()).hexdigest()
            #         if temp_versch_4 == verschluesselt:
            #             #print(f"{ datetime.now()-start } | {verschluesselt} = {temp_word_4}")
            #             return True, datetime.now()-start, f"{verschluesselt} = {temp_word_4}"
        
    
    
    
    
    return False, None, None

class PasswortThreader(threading.Thread):
    
    def __init__(self, id, dictonary, hash, chars, startzeit):
        threading.Thread.__init__(self)
        self.id = id
        self.dictionary = dictonary
        self.verschluesselt = hash
        self.chars = chars
        self.startzeit = startzeit
    
    def run(self):
        print(str(self.id) + " started.")
        for word in self.dictionary:
            fertig, zeit, ausgabe  = checkHash(word, self.verschluesselt, self.chars, self.startzeit)
            # print(word)
            if fertig:
                print(f"{self.id} found {ausgabe}  || {zeit}")
                
                
            
