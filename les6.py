#step1, make your key value as the second item of the list
#step3, compare the key with all the values before it
#step4, shift all the values>key, to the right
#step5, insert the key in the right position
#step5, make the next element of the original list, the key
#step6, repeat step 3,4,5 untill ever element in the list is scanned

list=[3,6,4,7,1]
for i in range(1,len(list)):
    key=list[i]
    j=i-1
    while key>list[j] and j>=0:
        list[j+1]=list[j]
        j-=1
    list[j+1]=key
    print(key)
    print(list)
print (list)
