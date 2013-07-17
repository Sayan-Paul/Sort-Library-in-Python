
#######################################################################################################################################################################
####File : sortlib.py
####
####Author : Sayan Paul
####
####Objective : This file contains most of the common and uncommon sorting algorithms
####            implemented . This can be used for eductional or commercial purposes.
########################################################################################################################################################################

#!/usr/bin/python
import random
class bintree(object):          ###structure for binary tree formulation
    "Binary Tree Container"
    def __init__(self):
        self.val=None
        self.left=None
        self.right=None
        
    def insert(self,val):
        "Insert node in tree"
        if self.val==None:
            self.val=val
            self.left=bintree()
            self.right=bintree()
        else:
            if val<self.val:
                self.left.insert(val)
            else:
                self.right.insert(val)
        return
    
    def inorder(self):
        "Inoder traversal of tree"
        if self.val==None:
            return
        self.left.inorder()
        print self.val,
        self.right.inorder()
        
def insertion(ar):
    "Insertion sort"
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
    "Selection Sort"
    for i in range(len(ar)):
        pos=i
        for j in range(i,len(ar)):
            if(ar[pos]>ar[j]):
                pos=j
        ar[i],ar[pos]=ar[pos],ar[i]
        print ar

def bubble(ar):
    "Bubble sort"
    for i in range(len(ar)):
        sorted=True
        for j in range(len(ar)-i-1):
            if(ar[j]>ar[j+1]):
                ar[j],ar[j+1]=ar[j+1],ar[j]
                sorted=False
        if sorted:
            break
        print ar

def quickSort(ar):          #This function returns the sorted list but does not change the original array like others . Uses extra array and not in place .
    "Quicksort implementation"
    if len(ar)<=1:              
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
    "Cocktail sort implementation"
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

def oddeven(ar):
    "Odd-Even sort implementation"
    sorted =False
    while(not sorted):
        sorted=True
        for i in range(1,len(ar)-1,2):
            if ar[i]>ar[i+1]:
                ar[i],ar[i+1]=ar[i+1],ar[i]
                sorted=False
        for i in range(0,len(ar)-1,2):
            if ar[i]>ar[i+1]:
                ar[i],ar[i+1]=ar[i+1],ar[i]
                sorted=False
        if not sorted:
            print ar

def combsort(ar):
    "Comb sort implementation"
    gap=len(ar)
    shrink=1.3
    swapped=False
    while not (gap==1 and not swapped):
        gap=int(gap/shrink)
        if gap<1:
            gap=1
        swapped=False
        for i in range(0,len(ar)-gap):
            if ar[i]>ar[i+gap]:
                ar[i],ar[i+gap]=ar[i+gap],ar[i]
                swapped =True
        print ar

def gnomesort(ar):
    "Gnomesort implementation"
    pos=1
    last=0
    while pos<len(ar):
        if ar[pos]>=ar[pos-1]:
            if last:
                pos=last
                last=0
            pos+=1
        else:
            ar[pos],ar[pos-1]=ar[pos-1],ar[pos]
            if pos>1:
                if not last:
                    last=pos
                pos-=1
            else:
                pos+=1
        print ar

def stoogesort(ar,i=0,j=-1):
    "Stooge sort implementation"
    if j==-1:
        j=len(ar)-1
    if ar[j]<ar[i]:
        ar[i],ar[j]=ar[j],ar[i]
    if (j-i+1)>=3:
        t=(j-i+1)/3
        stoogesort(ar, i  , j-t)
        stoogesort(ar, i+t, j  )
        stoogesort(ar, i  , j-t)
    #print ar   #-->prints too many steps in recursive tree
    return ar

def bogosort(ar):
    "Bogosort implementation"
    sorted=False
    while not sorted:
        sorted=True
        for i in range(len(ar)-1):
            if ar[i]>ar[i+1]:
                sorted=False
                break
        if sorted:
            break
        for i in range(1,len(ar)):
            j=random.choice(range(i+1))
            ar[i],ar[j]=ar[j],ar[i]
        #print ar

def heapsort(ar):
    "Heapsort implementation"
    heapify(ar)
    end=len(ar)-1
    while end>0:
        ar[end],ar[0]=ar[0],ar[end]
        end-=1
        siftdown(ar,0,end)
        print ar
def heapify(ar):
    "Changes array to heap"
    start=(len(ar)-1)/2
    while start>=0:
        siftdown(ar,start,len(ar)-1)
        start-=1
def siftdown(ar,start,end):
    "finds approprite position in heap"
    root=start
    while root*2+1<=end:
        child=root*2+1
        swap=root
        if ar[swap]<ar[child]:
            swap=child
        if child+1<=end and ar[swap]<ar[child+1]:
            swap=child+1
        if not (swap==root):
            ar[root],ar[swap]=ar[swap],ar[root]
            root=swap
        else:
            return

def shellsort(ar):
    "Shellsort implementation"
    gaps=[701,301,132,57,23,10,4,1]
    for gap in gaps:
        for i in range(gap,len(ar)):
            t=ar[i]
            j = i
            while j >= gap and ar[j - gap] > t:
                 ar[j] = ar[j - gap]
                 j -= gap
            ar[j]=t
            print ar


def treesort(ar):
    "Tree sort implementation"
    root=bintree()
    for i in ar:
        root.insert(i)
    root.inorder()
    print

def mergesort(ar):
    "Merge sort implementation"
    if len(ar)<=1:
        return ar
    middle=len(ar)/2
    left =ar[:middle]
    right=ar[middle:]
    left=mergesort(left)
    right=mergesort(right)
    res=merge(left,right)
    print res
    return res
def merge(left,right):
    "Merging left and right array in order"
    res=[]
    while len(left)+len(right):
        if len(left)*len(right):
            if left[0]<=right[0]:
                res.append(left[0])
                left=left[1:]
            else:
                res.append(right[0])
                right=right[1:]
        elif len(left):
            res.append(left[0])
            left=left[1:]
        elif len(right):
            res.append(right[0])
            right=right[1:]
    return res


def strandsort(ar):
    "Strandsort implementation"
    items = len(ar)
    sortedBins = []
    while( len(ar) > 0 ):
        highest = float("-inf")
        newBin = []
        i = 0
        while( i < len(ar) ):
            if( ar[i] >= highest ):
                highest = ar.pop(i)
                newBin.append( highest )
            else:
                i=i+1
        sortedBins.append(newBin)
     
    sorted = []
    while( len(sorted) < items ):
        lowBin = 0
        for j in range( 0, len(sortedBins) ):
            if( sortedBins[j][0] < sortedBins[lowBin][0] ):
                lowBin = j
        sorted.append( sortedBins[lowBin].pop(0) )
        if( len(sortedBins[lowBin]) == 0 ):
            del sortedBins[lowBin]
    print sorted
    return sorted


if __name__=='__main__':                                            #Driver Code
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
    quickSort(unsorted[:])
    print "Odd-Even Sort : "
    oddeven(unsorted[:])
    print "Comb Sort : "
    combsort(unsorted[:])
    print "Gnome Sort : "
    gnomesort(unsorted[:])
    print "Stooge Sort : "
    stoogesort(unsorted[:])
    print "Bogosort : "
    bogosort(unsorted[:])
    print "Heapsort : "
    heapsort(unsorted[:])
    print "Shellsort : "
    shellsort(unsorted[:])
    print "Treesort : "
    treesort(unsorted[:])
    print "Mergsort : "
    mergesort(unsorted[:])
    print "Strand Sort : "
    strandsort(unsorted[:])
