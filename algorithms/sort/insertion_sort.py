'''
Description:
    Given an array of integers, sort it using insertion sort algorithm. 
    Insertion sort is stable, in-place sorting algorithm that builds final 
    sorted array one item at a time. 
Performance:
    Comparisons:
        worst = O(n^2)
        best = O(n)
        average = O(n^2)
    Swaps:
        worst = O(n^2)
        best = O(1)
    Space Complexity:
        worst = O(n)
        aux space = O(1)
Pseudocode:
    i ← 1
    while i < length(A)
        x ← A[i]
        j ← i - 1
        while j >= 0 and A[j] > x
            A[j+1] ← A[j]
            j ← j - 1
        end while
        A[j+1] ← x[4]
        i ← i + 1
    end while
'''

def insertion_sort(arr, compare_fn):
    for i in range(len(arr)-1):
        key = arr[i+1]
        j = i
        while j >= 0 and compare_fn(arr[j], key):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def main():
    import numpy as np

    test_arr = np.arange(0,100)
    np.random.shuffle(test_arr)
    test_arr = list(test_arr)
    print(test_arr)
    insertion_sort(test_arr, lambda x,y: x > y)
    print(test_arr)

if __name__ == "__main__":
    main()