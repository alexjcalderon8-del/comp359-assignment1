import time



# Showing how in-place Mergesorting works in a python sctript
# main idea : use a list with multiple pointers and make the comparison within the premade list
# use two pointers, one at the begining of the array and another at the start of the second segment of the array (mid + 1)
# there is no need for separate array to merge as a placeholder





arr = [5, 2, 8, 1, 9, 3,] # defining the array with 6 values for testing

def merge_comp(arr, point1, mid, end):
    point2 = mid + 1
    if (arr[mid] <= arr[point2]):
        return
    
    while (point1 <= mid and point2 <= end): #the first pointer should always be before the mid point, while the second pointer will point before the end point
        if (arr[point1] <= arr[point2]):
            point1 += 1 # move index up one when value on left side is smaller than the right side
        else:
            value = arr[point2] # temporary values are used to store the value and the index of point2 variable when the point2 value holds something smaller than point1
            index = point2 

            while (index != point1): # 
                arr[index] = arr[index - 1]
                index -= 1 # index moves back one space since the new value was pushed to where index of point 1 was. This ensures that all of the values will face comparison in the array.
            arr[point1] = value # value of point2 now in position of point1 index

#increasing the points of each counter to move to the next index
            point1 += 1
            mid += 1
            point2 += 1

def merge_sort(arr, start, end):
    if start >= end:
        return
    mid = (start + end ) // 2 # defining the mid point by taking the index of the values in the array and dividing by 2
   
    merge_sort(arr, start, mid) 
    merge_sort(arr, mid + 1, end)
    merge_comp(arr, start, mid, end) # after we have two sorted halves, the final interation will occur



# implementing the timer for the function in nanoseconds
start_timer = time.perf_counter_ns()
merge_sort(arr, 0, len(arr) - 1) # using the merge function on the full length of indexes in the starting array. The array start point will always start at the start of the array 0, and the end will alwaysbe and the end of the array with len(arr) - 1
end_timer = time.perf_counter_ns()
total_time = (end_timer - start_timer)

print(f"in-place mergesorted list : {arr}") # printing the results of the in-place merge, hopefully a sorted list.
print(f"time for code: {total_time} nanoseconds")