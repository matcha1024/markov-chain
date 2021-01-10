# -*- coding: utf-8
import random
from janome.tokenizer import Tokenizer

limit = int(input("limit:"))

def wakati(text):
   text = text.replace('\n','')
   text = text.replace('\r','')
   t = Tokenizer()
   result =t.tokenize(text, wakati=True)
   return result
def generate_text(num_sentence=50):
   #素材ファイル名
   filename = "./hanshin-awazi.txt"
   src = open(filename, "r").read()
   wordlist = wakati(src)
   markov = {}
   w2 = ""
   w1 = ""
   for word in wordlist:
       if w1 and w2:
           if (w1, w2) not in markov:
               markov[(w1, w2)] = []
           markov[(w1, w2)].append(word)
       w1, w2 = w2, word
 
   count_kuten = 0
   num_sentence= num_sentence
   sentence = ""
   w1, w2  = random.choice(list(markov.keys()))

   i = 0
   while count_kuten < num_sentence:
       tmp = random.choice(markov[(w1, w2)])
       sentence += tmp
       if(tmp=='。'):
           count_kuten += 1
           sentence += '\n'
       w1, w2 = w2, tmp
       i += 1
       #if(i > limit):
        #break
    
   print(sentence)
    
if __name__ == "__main__":
   generate_text()
