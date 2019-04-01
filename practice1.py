# Task 1.1 replace " '
def replace (stroka):
    print (stroka)
    i = 0
    strokanew = ""
    while i < len(stroka):
        if stroka[i] == "'":
            strokanew = strokanew + '"'
        elif stroka[i] == '"':
            strokanew = strokanew + "'"
        else:
            strokanew = strokanew + stroka[i]
        i=i+1
    return (strokanew)

print ("\n Task 1.1 replace") 
print (replace("df'dsf''fds"))
print (replace('df"sf""fds'))


# Task 1.2 palindrome
def palindrome (word):
    palindrome = "Yes its palindrome!"
    wordl = len(word)
    print (word)
    i=0
    while i < len(word)//2+1:
        if word[i] != word[-(i+1)]:
            palindrome = "Not palindrome"
#        print (i," ",word[i]," ",word[-(i+1)])
        i = i+1
    return (palindrome)

print ("\n Task 1.2 palindrome")   
print (palindrome('asdfgfdsa'))
print (palindrome('asdfggfdsa'))
print (palindrome('asdfgfsa'))


# Task 1.3 split
def split(stroka, razdelitel):
    print (stroka,'"',razdelitel,'"')
    spisok = []
    j=1
    slovo=""
    for i in stroka:
#        print (i,j,slovo,spisok)
        if i != razdelitel:
            slovo=slovo+i
        elif slovo != "":
            spisok.insert(j,slovo)
            j=j+1
            slovo=""
    if slovo != "":
        spisok.insert(j+1,slovo)      
    return spisok

print ("\n Task 1.3 split")
print (split("python is cool,isnt'it?"," "))
print (split("python, is cool,isnt'it?,",","))


# Task 1.4 split by index
index=[]
def splitindex (stroka, index):
    spisok=[]
    slovo=""
    print(stroka, index)
    j=0
    i=0
    while i < len(stroka):
#            print (i,stroka[i],slovo)
            slovo=slovo+stroka[i]
            if i+1 == index[j]:
                spisok.insert(j,slovo)
#                print("index",index[j],spisok)  
                slovo=""
                if j+1 < len(index):
                    j=j+1
            i=i+1
    if slovo !="":
        spisok.insert(j+1,slovo)
    return spisok

print ("\n Task 1.4 split by index")
print (splitindex("12345678901234567",[4,6,10,15]))
print (splitindex("pythoniscool",[6,8]))


# Task 1.5 number to tuple int
def number2tuple (num):
    print (num)
    spisok = list(str(num))
    i=0
    while i < len(spisok):
        spisok[i]=int(spisok[i])
#        print(i, spisok[i])
        i=i+1
    tup=tuple(spisok)
    return tup

print ("\n Task 1.5 number to tuple")
print (number2tuple(2643376))


# Task 1.6 longest word
def getlongest (stroka):
    print (stroka)
    longest=""
    slovo=""
    for i in stroka+" ":
        slovo = slovo + i
#        print (slovo, "==",longest)
        if i == " ":
#            print (slovo)
            if len(slovo)>len(longest):
                longest = slovo
            slovo = ""
    return (longest)    

print ("\n Task 1.6 get longest word")
print (getlongest("why Python vis simple and effectiv"))
print (getlongest("why Python is s!imple and effective!!!"))

# Task 1.7 product of array exept i
def foo (spisok):
    product=1
    print (spisok)
    for i in spisok:
        product=product*i
    i=0
    while i<len(spisok):
        spisok[i]=int(product/spisok[i])
        i=i+1
    return spisok

print ("\n Task 1.7 product of array exept i")
print (foo([1,2,3,4,5]))
print (foo([3,2,1]))


# Task 1.8
def get_pairs (onelist):
    i=0
    pairs=[]
    while i < len(onelist)-1:
        pairs.insert(i,(onelist[i],onelist[i+1]))
        i=i+1
#    print (pairs)
    return (pairs)

print ("\n Task 1.8 pairs")
stroka=(1,2,3,4,5,6,7,8)
print (stroka)
print (get_pairs(stroka))
