# https://www.youtube.com/watch?v=Qf-TDPr0nYw&t=4s - Referance video
# Reason for requiring heaps
# we use a heap whenever we want to get a max/min item from a data structure in constant time
# if we insert or delete a item, data structure will rearrange itself in O(logn) time 
# instead of O(nlogn)(sorting) so that, you can fetch the min/max element in O(1)

# Heap is generally stored in a array/list but to visualize, but think of heap like a tree
# Heap - max/min
# Any max heap node is greater than all of the children nodes
# Any min heap node is smaller than all of the children nodes

# Heap is stored as a list so to find children or parent of the nodes in a tree, we use the following formulas
# if node is at index i
# then Left Child = 2*i+1
# Right Child = 2*i+2
# Parent = (i-1)/2

# Heapify Up  ⬆️
# Used in insertion to maintain the heap property.
# Start from the newly inserted node and compare it with its parent.
# If the node is smaller (min-heap) or larger (max-heap) than the parent, swap them.
# Repeat until the heap property is restored or the root is reached.
# Time Complexity: O(log n) (height of the heap).

# Heapify Down  ⬇️
# Used in deletion (usually after removing the root).
# Start from the root and compare it with its smallest (min-heap) or largest (max-heap) child.
# If the parent violates the heap property, swap it with the correct child.
# Repeat until the heap property is restored or a leaf node is reached.
# Time Complexity: O(log n) (height of the heap).

# Importing Heapq
import heapq

# Heap Insert (Heapify Up) - O(logn)
# Called as top to bottom appoarch
def min_heapify_up(heap, index):
    child = index
    parent = (child - 1) // 2

    while heap[parent] > heap[child] and child > 0:
        print(child, parent)
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = (child - 1) // 2

def max_heapify_up(heap, index):
    child = index
    parent = (child - 1) // 2

    while heap[parent] < heap[child] and child > 0:
        print(child, parent)
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = (child - 1) // 2
            
# Insert with a heapify up operation - top to bottom appoarch
# building a heap with top to bottom insert appoarch is nlogn (logn(heapify up) for n elements)
def insert_minheap(heap, n):
    heap.append(n)
    min_heapify_up(heap, len(heap)-1)
    return heap

def insert_maxheap(heap, n):
    heap.append(n)
    max_heapify_up(heap, len(heap)-1)
    return heap

# Delete element
# Will delete the max/min element
# Heapify Down
def min_heapify_down(heap, index):
     parent = index
     while True:
        left_child = 2 * parent + 1
        right_child = 2 * parent + 2

        smallest = parent  # Assume the parent is the smallest, this is for break codn

        # Check if left child exists and is smaller
        if left_child < len(heap) and heap[left_child] < heap[smallest]:
            smallest = left_child

        # Check if right child exists and is smaller
        if right_child < len(heap) and heap[right_child] < heap[smallest]:
            smallest = right_child

        # If the parent is the smallest, the heap is valid
        if smallest == parent:
            break

        # Swap parent and smallest child
        heap[parent], heap[smallest] = heap[smallest], heap[parent]

        # Move to the next level
        parent = smallest


def delete_minheap(heap):
    if len(heap) == 0:
        return None  # No elements to delete
    if len(heap) == 1:
        return heap.pop()  # Only one element, remove and return it

    # Swap the root with the last element and pop it
    heap[0], heap[-1] = heap[-1], heap[0]
    deleted_element = heap.pop()

    # Heapify down to restore the min heap property
    min_heapify_down(heap, 0)
   
    return deleted_element

# Bottom to top appoarch for building heap
# Just remember this, for a unsorted array with random numbers, we check the non-leaf nodes and do heapify down for them
# because for the leaf nodes, it's useless to do heapify down
# There are n//2 non leaf nodes for a complete binary tree so, for (n/2,0) index do heapify and you will get a max/min heap
# Time for this operation is O(n) which is better than O(nlogn)
def bottomTopInsert(heap):
    n = len(heap)
    for i in range(n//2,-1,-1):
        min_heapify_down(heap, i)

# Call the test function
if __name__ == "__main__":
    # min heap example
    min_heap = [7,8,9,10,11,12,14,13]
    insert_minheap(min_heap, 6)
    print("min heap: ",min_heap)

    #max heap example
    max_heap = [50, 30, 40, 10, 5, 20]
    insert_maxheap(max_heap, 60)
    print("max heap: ",max_heap)

    deleted_value = delete_minheap(min_heap)
    print("Deleted from Min Heap:", deleted_value)
    print("Min Heap after deletion:", min_heap)

    # Heap Sort
    to_sort = [34, 12, 5, 67, 2, 78, 23, 56, 89, 11]

    # min heap creation with top to bottom appoarch -> O(nlogn) time
    min_heap=[]
    for i in to_sort:
        print("inserting: ", i)
        insert_minheap(min_heap, i)
        print(min_heap)
    
    # heap sort
    heap_sort = []
    while min_heap:
      deleted_val = delete_minheap(min_heap)
      heap_sort.append(deleted_val)
      print(heap_sort)
    print("heap sort: ", heap_sort)

    # Bottom to top insert -> O(n) time
    bottomTopInsert(to_sort)
    print("min heap via bottom to top: ", to_sort)


    # Using heapq
    print("####### Using Heapq ##########")
    min_heap = [34, 12, 5, 67, 2, 78, 23, 56, 89, 11]
    heapq.heapify(min_heap)
    print("min heap : ", min_heap)

    heapq.heappush(min_heap,4)
    print("min heap : ", min_heap)

    poped_element = heapq.heappop(min_heap)
    print("poped element: ", poped_element)
    print("min heap : ", min_heap)

    # if we want to simulate max heap, then we have store negative values in heapify 
    # since heapq can do only min heap

    max_heap = []
    heapq.heappush(max_heap, -3)
    heapq.heappush(max_heap, -1)
    heapq.heappush(max_heap, -5)
    heapq.heappush(max_heap, -4)

    print(len(max_heap))

    print("max heap: ", max_heap) # max heap * -1

    # Pop the largest value (convert back to positive)
    max_value = -heapq.heappop(max_heap)
    print(max_value)  # Output: 5

    # for heapify, everything negative values and do heapify

    # n largest for a min heap -> complexity for this is n * log(size of heap) or you can perform delete two times
    print(heapq.nlargest(2,min_heap)) 

    print(heapq.nsmallest(2, min_heap)) # same complexity