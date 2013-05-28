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

def quicksort(ar):
    return

if __name__=='__main__':
    unsorted=[int(x) for x in raw_input().split(" ")]
    print "Insertion : "
    insertion(unsorted[:])
    print "Selection : "
    selection(unsorted[:])
    print "Bubble : "
    bubble(unsorted[:])
    
