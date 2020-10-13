''' Print the maximum value of m(i.e. the size of the largest
unbroken sequence of sorted consecutive integer whose adjacent
element have a maximum absolute difference of 1)
'''
def max_Array_length(a):
    ar=max_sub(a)
    print(ar)
    b=[]
    for i in range(len(ar)):
        b.append(len(ar[i]))
    print(b)
    print(max(b))

def max_sub(a):
    c=sorted(a)
    b,d=[],[]
    n=0
    i=0
    while (i<len(a)-1):
        if (i ==(len(a)-2)):
            for j in range(n,len(a)):
                b.append(c[j])
            d.append(b)
        elif(c[i+1]-c[i]>1):
            for j in range(n,i+1):
                n=i+1
                b.append(c[j])
            d.append(b)
            b=[]
        i=i+1
    return d      

a=[1,2,2,3,4,3,4,6,7,9,11,12,12,13,15]
max_Array_length(a)
