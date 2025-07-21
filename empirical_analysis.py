import random
import time
from heapsort import heapsort
from priority_queue import PriorityQueue, Task

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randint(0, len(arr) - 1)]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + mid + quicksort(right)

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def benchmark():
    sizes = [1000, 5000, 10000]
    for size in sizes:
        arr = [random.randint(0, 100000) for _ in range(size)]
        # Heapsort
        arr1 = arr.copy()
        start = time.time()
        heapsort(arr1)
        print(f"Heapsort - Size: {size}, Time: {time.time() - start:.4f} seconds")
        # Quicksort
        arr2 = arr.copy()
        start = time.time()
        quicksort(arr2)
        print(f"Quicksort - Size: {size}, Time: {time.time() - start:.4f} seconds")
        # Mergesort
        arr3 = arr.copy()
        start = time.time()
        mergesort(arr3)
        print(f"Mergesort - Size: {size}, Time: {time.time() - start:.4f} seconds")
        print("-" * 40)

def test_priority_queue():
    pq = PriorityQueue()
    pq.push(2, Task('Write code'))
    pq.push(5, Task('Do research'))
    pq.push(1, Task('Submit assignment'))
    print("Priority Queue order (max-priority first):")
    while not pq.is_empty():
        print(pq.pop())

if __name__ == "__main__":
    print("Empirical Sorting Benchmark:")
    benchmark()
    print("\nPriority Queue Demo:")
    test_priority_queue()
