

def read_file():
 lwords = []
 clearwords = []
 bdbewords = {}
 bdthreewords = {}
 pairs = []
 with open("test.txt", "r", encoding="utf-8") as fh:
    for i in fh:
     lwords = i.lower().strip().split()
     if not lwords: continue
     clearwords = [i.strip(",!.?<>()[]+/") for i in lwords]
     if len(clearwords) < 2: continue
     qwe=(list(zip(clearwords, clearwords[1:])))
     pairsstap = qwe[0]+' '+qwe[1]
     pairs.append(pairsstap)
     print(pairs)

 #return pairs     

def be_grams(beparam:list): 
 pass

def three_grams(threeparam:list):
 pass

#------ main -----
read_file()