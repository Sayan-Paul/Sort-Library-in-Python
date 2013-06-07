Sort-Library-in-Python
======================

A Library of various list sorting algorithms being implemented in Python

Insetion Sort:
======================

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list. On a repetition, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there. It repeats until no input elements remain.
Sorting is typically done in-place, by iterating up the array, growing the sorted list behind it. At each array-position, it checks the value there against the largest value in the sorted list (which happens to be next to it, in the previous array-position checked). If larger, it leaves the element in place and moves to the next. If smaller, it finds the correct position within the sorted list, shifts all the larger values up to make a space, and inserts into that correct position.

Selection Sort:
======================

In computer science, a selection sort is a sorting algorithm, specifically an in-place comparison sort. It has O(n2) time complexity, making it inefficient on large lists, and generally performs worse than the similar insertion sort. Selection sort is noted for its simplicity, and it has performance advantages over more complicated algorithms in certain situations, particularly where auxiliary memory is limited.
The algorithm divides the input list into two parts: the sublist of items already sorted, which is built up from left to right at the front (left) of the list, and the sublist of items remaining to be sorted that occupy the rest of the list. Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, exchanging it with the leftmost unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right.

Bubble Sort:
======================

Bubble sort, sometimes incorrectly referred to as sinking sort, is a simple sorting algorithm that works by repeatedly stepping through the list to be sorted, comparing each pair of adjacent items and swapping them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted. The algorithm gets its name from the way smaller elements "bubble" to the top of the list. Because it only uses comparisons to operate on elements, it is a comparison sort. Although the algorithm is simple, most of the other sorting algorithms are more efficient for large lists.
Bubble sort has worst-case and average complexity both ?(n2), where n is the number of items being sorted. There exist many sorting algorithms with substantially better worst-case or average complexity of O(n log n). Even other ?(n2) sorting algorithms, such as insertion sort, tend to have better performance than bubble sort. Therefore, bubble sort is not a practical sorting algorithm when n is large.

Quicksort:
======================

Quicksort is a divide and conquer algorithm. Quicksort first divides a large list into two smaller sub-lists: the low elements and the high elements. Quicksort can then recursively sort the sub-lists.

The steps are:

    Pick an element, called a pivot, from the list.
    Reorder the list so that all elements with values less than the pivot come before the pivot, while all elements with values greater than the pivot come after it (equal values can go either way). After this partitioning, the pivot is in its final position. This is called the partition operation.
    Recursively apply the above steps to the sub-list of elements with smaller values and separately the sub-list of elements with greater values.

The base case of the recursion are lists of size zero or one, which never need to be sorted.
Quicksort, or partition-exchange sort, is a sorting algorithm developed by Tony Hoare that, on average, makes O(n log n) comparisons to sort n items. In the worst case, it makes O(n2) comparisons, though this behavior is rare.

Odd-Even Sort:
======================

In computing, an odd–even sort or odd–even transposition sort (also known as brick sort) is a relatively simple sorting algorithm, developed originally for use on parallel processors with local interconnections. It is a comparison sort related to bubble sort, with which it shares many characteristics. It functions by comparing all (odd, even)-indexed pairs of adjacent elements in the list and, if a pair is in the wrong order (the first is larger than the second) the elements are switched. The next step repeats this for (even, odd)-indexed pairs (of adjacent elements). Then it alternates between (odd, even) and (even, odd) steps until the list is sorted.

Comb Sort:
======================

The basic idea is to eliminate turtles, or small values near the end of the list, since in a bubble sort these slow the sorting down tremendously. Rabbits, large values around the beginning of the list, do not pose a problem in bubble sort.
In bubble sort, when any two elements are compared, they always have a gap (distance from each other) of 1. The basic idea of comb sort is that the gap can be much more than 1 (Shell sort is also based on this idea, but it is a modification of insertion sort rather than bubble sort).
In other words, the inner loop of bubble sort, which does the actual swap, is modified such that gap between swapped elements goes down (for each iteration of outer loop) in steps of shrink factor. i.e. [ input size / shrink factor, input size / shrink factor^2, input size / shrink factor^3, ...., 1 ]. Unlike in bubble sort, where the gap is constant i.e. 1.
The gap starts out as the length of the list being sorted divided by the shrink factor (generally 1.3; see below), and the list is sorted with that value (rounded down to an integer if needed) as the gap. Then the gap is divided by the shrink factor again, the list is sorted with this new gap, and the process repeats until the gap is 1. At this point, comb sort continues using a gap of 1 until the list is fully sorted. The final stage of the sort is thus equivalent to a bubble sort, but by this time most turtles have been dealt with, so a bubble sort will be efficient

Gnome Sort:
======================

Gnome sort (Stupid sort) is a sorting algorithm which is similar to insertion sort, except that moving an element to its proper place is accomplished by a series of swaps, as in bubble sort. It is conceptually simple, requiring no nested loops. The running time is O(n^2), but tends towards O(n) if the list is initially almost sorted. In practice the algorithm can run as fast as Insertion sort. The average runtime is O(n^2).

The algorithm always finds the first place where two adjacent elements are in the wrong order, and swaps them. It takes advantage of the fact that performing a swap can introduce a new out-of-order adjacent pair only right before or after the two swapped elements. It does not assume that elements forward of the current position are sorted, so it only needs to check the position directly before the swapped elements.

Stooge Sort:
======================

Stooge sort is a recursive sorting algorithm with a time complexity of O(nlog 3 / log 1.5 ) = O(n2.7095...). The running time of the algorithm is thus extremely slow compared to efficient sorting algorithms, such as Merge sort, and is even slower than Bubble sort, a canonical example of a fairly inefficient and simple sort.

The algorithm is defined as follows:

    If the value at the end is smaller than the value at the start, swap them.
    If there are three or more elements in the current list subset, then:
        Stooge sort the initial 2/3 of the list
        Stooge sort the final 2/3 of the list
        Stooge sort the initial 2/3 of the list again
    else: exit the procedure

Bogosort:
======================

This sorting algorithm is probabilistic in nature. If all elements to be sorted are distinct, the expected number of comparisons in the average case is asymptotically equivalent to (e-1) n!, and the expected number of swaps in the average case equals (n-1) n!. The expected number of swaps grows faster than the expected number of comparisons, because if the elements are not in order, this will usually be discovered after only a few comparisons no matter how many elements there are, but the work of shuffling the collection is proportional to its size. In the worst case, the number of comparisons and swaps are both unbounded, for the same reason that a tossed coin might turn up heads any number of times in a row.

Heapsort:
======================

Heapsort is a comparison-based sorting algorithm to create a sorted array (or list), and is part of the selection sort family. Although somewhat slower in practice on most machines than a well-implemented quicksort, it has the advantage of a more favorable worst-case O(n log n) runtime. Heapsort is an in-place algorithm, but it is not a stable sort.
The heapsort algorithm can be divided into two parts.

In the first step, a heap is built out of the data.

In the second step, a sorted array is created by repeatedly removing the largest element from the heap, and inserting it into the array. The heap is reconstructed after each removal. Once all objects have been removed from the heap, we have a sorted array. The direction of the sorted elements can be varied by choosing a min-heap or max-heap in step one.

Heapsort can be performed in place. The array can be split into two parts, the sorted array and the heap. The storage of heaps as arrays is diagrammed here. The heap's invariant is preserved after each extraction, so the only cost is that of extraction.

Shellsort:
======================

Shellsort, also known as Shell sort or Shell's method, is an in-place comparison sort. It generalizes an exchanging sort, such as insertion or bubble sort, by starting the comparison and exchange of elements with elements that are far apart before finishing with neighboring elements. Starting with far apart elements can move some out-of-place elements into position faster than a simple nearest neighbor exchange. 
The running time of Shellsort is heavily dependent on the gap sequence it uses. For many practical variants, determining their time complexity remains an open problem.Shellsort is a multi-pass algorithm. Each pass is an insertion sort of the sequences consisting of every h-th element for a fixed gap h (also known as the increment). This is referred to as h-sorting.

Tree Sort:
======================

A tree sort is a sort algorithm that builds a binary search tree from the keys to be sorted, and then traverses the tree (in-order) so that the keys come out in sorted order. Its typical use is when sorting the elements of a stream from a file. Several other sorts would have to load the elements to a temporary data structure, whereas in a tree sort the act of loading the input into a data structure is sorting it.
Adding one item to a binary search tree is on average an O(log(n)) process, so adding n items is an O(n log(n)) process, making tree sort a so-called 'fast sort'. But adding an item to an unbalanced binary tree needs O(n) time in the worst-case, when the tree resembles a linked list (degenerate tree), causing a worst case of O(n2) for this sorting algorithm. The worst case scenario then is triggered by handing a Tree Sort algorithm an already sorted set. This would make the time needed to insert all elements into the binary tree O(n2). The dominant process in the Tree Sort algorithm is the "insertion" into the binary tree, assuming that the time needed for retrieval is O(n).

Merge Sort:
======================

In computer science, a merge sort (also commonly spelled mergesort) is an O(n log n) comparison-based sorting algorithm. Most implementations produce a stable sort, which means that the implementation preserves the input order of equal elements in the sorted output. 
Conceptually, a merge sort works as follows

    Divide the unsorted list into n sublists, each containing 1 element (a list of 1 element is considered sorted).
    Repeatedly merge sublists to produce new sublists until there is only 1 sublist remaining. This will be the sorted list.

A natural merge sort is similar to a bottom up merge sort except that any naturally occurring runs (sorted sequences) in the input are exploited. In the bottom up merge sort, the starting point assumes each run is one item long. In practice, random input data will have many short runs that just happen to be sorted. In the typical case, the natural merge sort may not need as many passes because there are fewer runs to merge. For example, in the best case, the input is already sorted (i.e., is one run), so the natural merge sort need only make one pass through the data.

Stran Sort:
======================

Strand sort is a sorting algorithm. It works by repeatedly pulling sorted sublists out of the list to be sorted and merging them with a result array. Each iteration through the unsorted list pulls out a series of elements which were already sorted, and merges those series together.
The name of the algorithm comes from the "strands" of sorted data within the unsorted list which are removed one at a time. It is a comparison sort due to its use of comparisons when removing strands and when merging them into the sorted array.
The strand sort algorithm is O(n2) in the average case. In the best case (a list which is already sorted) the algorithm is linear, or O(n). In the worst case (a list which is sorted in reverse order) the algorithm is O(n2).
Strand sort is most useful for data which is stored in a linked list, due to the frequent insertions and removals of data. Using another data structure, such as an array, would greatly increase the running time and complexity of the algorithm due to lengthy insertions and deletions. Strand sort is also useful for data which already has large amounts of sorted data, because such data can be removed in a single strand.
