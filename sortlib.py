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
        sorte=True
        for j in range(i,len(ar)):
            if(ar[pos]>ar[j]):
                pos=j
                sorte=False
        ar[i],ar[pos]=ar[pos],ar[i]
        if(sorte):
            print i
            break
        print ar

if __name__=='__main__':
    unsorted=[int(x) for x in raw_input().split(" ")]
    print "Insertion : "
    insertion(unsorted[:])
    print "Selection : "
    selection(unsorted[:])
    
