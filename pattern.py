list1=[]
num=int(input("Enter how many lines? "))
for i in range(2,1000):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        list1.append(i)

for i in range(0,num+1):
    for j in range(0,i):
        print(list1[j], end=' ')
    print('\n') 
