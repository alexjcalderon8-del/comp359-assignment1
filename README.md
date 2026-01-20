# Assignment 1  

COMP 359, ON1 Design and Analysis Algorithms

---

## Authors  

- Alexander Calderon   


---

## Objective  

Implement different merge function for Mergesort and compare the difference between an in-place sort versus a not in-place sort.  


---

## Tools used  

- python
 
### Libraries

- time (built-in python library)

---

## How it works  

### Not-in-place merge

The not in place merge sort or standard version of merge sort, will take an unordered list and sort it recursively.
The process begins with splitting the array into halves. The split is determined based on if the value is less than the previous value. once, the array is broken down into its subarrays, the merge process begins and the comparisons to find order will be made.
A preallocated array will help with the process of separating the merged items and maintain the order for the final output. Using a preallocated will increase the space complexity.
A limitation of this method, is if the system is required to utilize limited memory.

### In-place merge

The main component behind using the In-place merge is completing the mergesort all within the same array. This means that there is so extra memory dedicated to an empty array.
All of the sorting is done in the original array. This can bring a challenge as there is no additional space to work with, the algortihm must meet the requirement of working in the initial array
This can be useful if systems have some kind of memory limit or if the requirement calls for a lower utilization percentage of memory. To understand how the example of the In-place merge works, it is important to note that there a different variations such as rotation-based, block-swap, and shifting for in-place merge.

The shifting merge, will take an array of numbers  and begin the process with spliting the array in halves. This is fundamental to a merge sorting algortihm. Making comparisons recursively will split the array based in whether the value indicated at
point1 is less than or greater than the value indicated at point2. if the value is less than, this means that the two values are in-order and point1 will move to the next index and make another comparison. In the case
that point2 is less than the value held at the index of point1, a shift will occur and the value of point two will then be placed where the index of point1 was. This will cause all the values beyond the index of point1 to shift one spot towards the next index.

Once there are two fully sorted halves, the final iteration of the sort comparison will occur and the final merge will happen between the two sub-arrays.

---

## Instructions to run  

Run each program in an IDE, the results will be provided within the terminal as standard output. The output will provide information on the results of the program and the timing

---

## Supporting Documentation  

located in docs/

- shift_merge.png
- inplace_analysis.md

---

## Analysis of methods

The largest difference from an in-place merge compared to a not in-place merge will be seen through its efficiency. If there are no restrictions in memory or required resources,
the not in-place merge sort will prove to be more efficient than the in-place merge. Having extra space to work with in the array can help improve time.
The one take away the in-place merge excels in is the constant space it uses. Since the in-place merge uses constant space, it has the trade off in its efficiency. 
The in-place merge will take longer time for its execution as all of the actions are completed within the same array. Especially with the shift method, the sorting will take time as it will have to go 
through all the values of the array to determine its placement in order. 

---


## References  

GeeksforGeeks. (2025, October 3). Merge sort. [https://www.geeksforgeeks.org/dsa/merge-sort/](https://www.geeksforgeeks.org/dsa/merge-sort/) 

Panday, A. (2024, May 11). Understanding time complexity: And why is it essential to learn? | by Ankush Panday | medium. Medium. [https://medium.com/@ankushpanday/understanding-time-complexity-and-why-is-it-essential-to-learn-f409c25bf256](https://medium.com/@ankushpanday/understanding-time-complexity-and-why-is-it-essential-to-learn-f409c25bf256)

Sryheni, S. (2024, March 18). In-place sorting with merge sort | Baeldung on computer science. Baeldung. [https://www.baeldung.com/cs/merge-sort-in-place](https://www.baeldung.com/cs/merge-sort-in-place)

---