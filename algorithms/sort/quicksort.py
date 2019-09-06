'''
Description:
    Quicksort is an efficient in-place sorting algorithm, which usually 
    performs about two to three times faster than merge sort and heapsort. 
Performance: 
    Comparisons:
        worst = O(n^2)
        best = O(n log n)
        average = O(n log n)
    Swaps:
        worst = 
        best = 
        average = 
    Space Complexity:
        worst aux space = O(n)
        best aux space = O(log n)
Pseudocode:
    algorithm quicksort(A, lo, hi) is
        if lo < hi then
            p := partition(A, lo, hi)
            quicksort(A, lo, p)
            quicksort(A, p + 1, hi)

    algorithm partition(A, lo, hi) is
        mid := (lo + hi) / 2
        if A[mid] < A[lo]
            swap A[lo] with A[mid]
        if A[hi] < A[lo]
            swap A[lo] with A[hi]
        if A[mid] < A[hi]
            swap A[mid] with A[hi]
        pivot := A[hi]
        loop forever
            while A[lo] < pivot         
                lo := lo + 1

            while A[hi] > pivot
                hi := hi - 1
    
            if lo >= hi then
                return hi

            swap A[lo] with A[hi]

            lo := lo + 1
            hi := hi - 1
'''

def quicksort(arr, low, high):
    if low < high:
        p_idx = partition(arr, low, high)
        quicksort(arr, low, p_idx)
        quicksort(arr, p_idx+1, high)
    return

def partition(arr, low, high):
    mid_idx = low + ((high-low) // 2)
    if arr[mid_idx] < arr[low]:
        arr[mid_idx], arr[low] = arr[low], arr[mid_idx]
    if arr[high] < arr[low]:
        arr[high], arr[low] = arr[low], arr[high]
    if arr[mid_idx] < arr[high]:
        arr[mid_idx], arr[high] = arr[high], arr[mid_idx]
    pivot_elmnt = arr[high]

    while True:
        while arr[low] < pivot_elmnt:
            low += 1
        
        while arr[high] > pivot_elmnt:
            high -= 1

        if low >= high:
            return high

        arr[low], arr[high] = arr[high], arr[low]

        low += 1
        high -= 1

def main():
    import numpy as np

    test_arr = np.arange(0,100)
    np.random.shuffle(test_arr)
    test_arr = list(test_arr)
    print(test_arr)
    quicksort(test_arr, 0, len(test_arr)-1)
    print(test_arr)

if __name__ == "__main__":
    main()