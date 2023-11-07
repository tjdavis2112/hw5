import random
import timeit
import matplotlib.pyplot as plt

 # https://www.pythoncentral.io/merge-sort-implementation-guide/
def hybrid_sort(alist, k = None):

    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        #recursion
        if k != None and len(alist) <= k:
            return insertion_sort(alist)
        else:
            hybrid_sort(lefthalf)
            hybrid_sort(righthalf)

        i=0
        j=0
        k=0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

def merge_sort(alist):

   if len(alist)>1:
       mid = len(alist)//2
       lefthalf = alist[:mid]
       righthalf = alist[mid:]

       #recursion
       merge_sort(lefthalf)
       merge_sort(righthalf)

       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               alist[k]=lefthalf[i]
               i=i+1
           else:
               alist[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           alist[k]=righthalf[j]
           j=j+1
           k=k+1



 # https://www.geeksforgeeks.org/python-program-for-insertion-sort/
def insertion_sort(arr):
    n = len(arr)  # Get the length of the array
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position

def measure_sorting_time(sorting_function, arr, n=None):
    # Measure execution time for sorting function
    start_time = timeit.default_timer()
    if n != None:
        sorting_function(arr, n)
    else:
        sorting_function(arr)
    end_time = timeit.default_timer()
    return end_time - start_time

n_values = [i for i in range(1, 251, 2)]  # Adjust this list as needed
k_values = [25, 150]  # Adjust this list as needed

merge_sort_times = []
insertion_sort_times = []
hybrid_sort_times = [[] for _ in range(len(k_values))]

for n in n_values:
    arr = [random.randint(1, 1000) for _ in range(n)]
    
    merge_time = 0
    insertion_time = 0
    hybrid_time = 0

    for _ in range(1000):
        merge_time += measure_sorting_time(merge_sort, arr.copy())
        insertion_time += measure_sorting_time(insertion_sort, arr.copy())

    for i, k in enumerate(k_values):
        for _ in range(1000):
            hybrid_time += measure_sorting_time(hybrid_sort, arr.copy(), k)
        hybrid_sort_times[i].append(hybrid_time)
        hybrid_time = 0

    merge_sort_times.append(merge_time)
    insertion_sort_times.append(insertion_time)

plt.plot(n_values, merge_sort_times, label='Merge Sort')
plt.plot(n_values, insertion_sort_times, label='Insertion Sort')
for i, k in enumerate(k_values):
    plt.plot(n_values, hybrid_sort_times[i], label='Hybrid Sort (k = {})'.format(k))

plt.xlabel('n (Array Size)')
plt.ylabel('Execution Time (s)')
plt.legend()
plt.show()

# Create a bar chart
# bar_width = 0.35
# index = range(len(n_values))

# plt.bar(index, merge_sort_times, bar_width, label='Merge Sort', alpha=0.7)
# plt.bar([i + bar_width for i in index], insertion_sort_times, bar_width, label='Insertion Sort', alpha=0.7)

# plt.xlabel('n (Array Size)')
# plt.ylabel('Execution Time (s)')
# plt.xticks([i + bar_width / 2 for i in index], n_values)
# plt.legend()
# plt.show()