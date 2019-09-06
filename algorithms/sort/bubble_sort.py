'''
Description:
    Selection sort is a unstable, in-place sorting algorithm known for its 
    simplicity, and it has performance advantages over more complicated 
    algorithms in certain situations, particularly where auxiliary memory 
    is limited. It can be implemented as a stable sort. selection sort 
    almost always outperforms bubble sort and generally performs worse 
    than the similar insertion sort. Has max n swaps (memory writes).
Performance: 
    Comparisons:
        worst = O(n^2)
        best = O(n^2)
        average = O(n^2)
    Swaps:
        worst = O(n)
        best = O(n)
        average = O(n)
    Space Complexity:
        worst = O(n)
        aux space = O(1)
Pseudocode:
    Step 1 − Set MIN to location 0
    Step 2 − Search the minimum element in the list
    Step 3 − Swap with value at location MIN
    Step 4 − Increment MIN to point to next element
    Step 5 − Repeat until list is sorted
'''