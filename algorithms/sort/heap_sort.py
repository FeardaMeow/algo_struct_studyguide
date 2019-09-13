
class max_heap():
    def __init__(self, arr):
        self.arr = arr
        self.build_heap()

    def heapify(self, n, i):
        # Left = 2*i + 1
        # Right = 2*i + 2
        largest = i
        left = 2*i + 1
        right = 2*i + 2

        if left < n and self.arr[left] > self.arr[largest]:
            largest = left

        if right < n and self.arr[right] > self.arr[largest]:
            largest = right

        if largest != i:
            self.arr[largest], self.arr[i] = self.arr[i], self.arr[largest]
            self.heapify(n,largest)

    def build_heap(self):
        n = len(self.arr)
        start_idx = (n // 2) - 1
        
        for i in range(start_idx, -1, -1):
            self.heapify(n, i)

        for i in range(n-1, 0, -1): 
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i] # swap 
            self.heapify(i, 0) 


def main():
    import numpy as np
    arr = np.random.randint(low=0, high=500, size=20)
    print(arr)
    heap = max_heap(arr = list(arr))
    print(heap.arr)

if __name__ == "__main__":
    main()