def list2freqdict(mylist):
    mydict=dict()
    for ch in mylist:
        mydict[ch]=mydict.get(ch,0)+1
    return mydict
    
file = open("ff.txt")
sentence= file.read()
chlist=[ch for ch in sentence]

print(chlist)
chfreqdict=list2freqdict(chlist)
print(chfreqdict)