def insertion(ar):
    for i in range(len(ar)):
        j=i-1
        ch=i
        while j>=0:
            if (ar[ch]<ar[j]):
                ar[ch],ar[j]=ar[j],ar[ch]
                ch=j
            j-=1
        print ar
            

def selection(ar):
    for i in range(len(ar)):
        pos=i
        sorted=True
        for j in range(i,len(ar)):
            if(ar[pos]>ar[j]):
                pos=j
                sorted=False
        ar[i],ar[pos]=ar[pos],ar[i]
        if(sorted):
            break
        print ar

def bubble(ar):
    for i in range(len(ar)):
        sorted=True
        for j in range(len(ar)-i-1):
            if(ar[j]>ar[j+1]):
                ar[j],ar[j+1]=ar[j+1],ar[j]
                sorted=False
        if sorted:
            break
        print ar

def quickSort(ar):          #This function returns the sorted list but does 
    if len(ar)<=1:              #not change the original array like others
        return ar
    lf,rt=[],[]
    p=ar[0]
    for j in ar:
        if j>=p:
            rt.append(j)
        else:
            lf.append(j)
    l=quickSort(lf)
    r=quickSort(rt[1:])
    c=l+[rt[0]]+r
    for u in c:
        print u,
    print
    return c


def cocktailsort(ar):
    swapped=True
    while(swapped):
        swapped=False
        for i in range(len(ar)-1):
            if ar[i]>ar[i+1]:
                ar[i],ar[i+1]=ar[i+1],ar[i]
                swapped=True
        if swapped==False:
            break
        swapped=False
        print ar
        i=len(ar)-2
        while i>=0:
            if ar[i]>ar[i+1]:
                ar[i],ar[i+1]=ar[i+1],ar[i]
                swapped=True
            i-=1
        print ar



if __name__=='__main__':
    unsorted=[int(x) for x in raw_input().split(" ")]
    print "Insertion Sort : "
    insertion(unsorted[:])
    print "Selection Sort : "
    selection(unsorted[:])
    print "Bubble Sort : "
    bubble(unsorted[:])
    print "Cocktail Sort : "
    cocktailsort(unsorted[:])
    print "Quicksort : "
    print quickSort(unsorted[:])
    
