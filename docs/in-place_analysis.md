# Shift in-place merge analysis

---

## Author : Alexander Calderon

---

## Objective

Sort the array utilizing an in-place merge method.

---

## Time Complexity

for time complexity we must consider the functions of the merge and the comparisons we make. As part of the merge process we will recursively break down the array in to two subarrays, then continue to split the array
if the left halves are greater than the right halves. For the comparison portion we take the subarrays in their simpilest form and use pointers to ensure that the left value is less than the right value.(log(n)) In the case that 
the right value is greater than the left value, the right value will shift to the index just before the previous "left" value. This shift will have to check every value for the array and check to see if it is in the right order (n^2^).
for the example of the shift in-place merge we have a complexity of O(n^2^ * log(n)).

---


## Space Complexity

Space complexity for an in-place sort should be O(1). by having constant space this means that there is a fixed amount that the program is dealing with. In the example provided there is a fixed array with 6 values.
The memory also includes temporary variables for the purpose of utilizing the pointers and the temp values for shifts. Since we are only accessing the one array with no additional arrays the space remain constant throughout the 
running of the program.

---