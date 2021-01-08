string='Vegetable pizza'


def reverse(r):
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    for i in range (97,123):
        list1.append(i)
    for j in range(122,96,-1):
        list2.append(j)
    for k in range (65,91):
        list3.append(k)
    for l in range (90,64,-1):
        list4.append(l)


    # print(list3)
    # print(list4)
    reversed=0
    if r in list1:
        a=list1.index(r)
        reversed= list2[a]
    elif r in list3:
        a=list3.index(r)
        reversed= list4[a]
    else:
        reversed=ord(" ")

    return reversed
    
def result(string):
    final=""
    for i in string:
        reversed= reverse (ord(i))
        letter= chr (reversed)
        final=final+letter
    print(final)
    
result(string)

reverse(string)