import random
import time
from typing import List 

class MergeSortTempParam:
    
    def sort(self, arr: List[int]) -> List[int]: 
        if len(arr) <= 1:
            return arr 
        
        temp = [0] * len(arr)
        self._mergesort(arr, 0, len(arr) - 1, temp)
        return arr
    
    def _mergesort(self, arr: List[int], left: int, right: int, temp: List[int]) -> None:
        if left < right:
            mid = (left + right) // 2
            
            self._mergesort(arr, left, mid, temp)
            self._mergesort(arr, mid + 1, right, temp)
            
            self._merge(arr, left, mid, right, temp)
    
    def _merge(self, arr: List[int], left: int, mid: int, right: int, temp: List[int]) -> None:
        for i in range(left, right + 1):
            temp[i] = arr[i]
        
        i = left
        j = mid + 1
        k = left
        
        while i <= mid and j <= right:
            if temp[i] <= temp[j]:
                arr[k] = temp[i]
                i += 1
            else:
                arr[k] = temp[j]
                j += 1
            k += 1
        
        while i <= mid:
            arr[k] = temp[i]
            i += 1
            k += 1
    
    def is_sorted(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True


class PerformanceAnalyzer:
    
    @staticmethod
    def generate_random_array(size: int) -> List[int]:
        return [random.randint(1, 10000) for _ in range(size)]
    
    @staticmethod
    def time_sort(sorter, arr: List[int], iterations: int = 3) -> float:
        total_time = 0
        
        for _ in range(iterations):
            test_arr = arr.copy()
            start_time = time.perf_counter()
            sorter.sort(test_arr)
            end_time = time.perf_counter()
            
            if not sorter.is_sorted(test_arr):
                raise ValueError("Sorting failed!")
            
            total_time += (end_time - start_time)
        
        return total_time / iterations
    
    def run_performance_test(self, sorter, sizes: List[int] = None) -> dict:
        if sizes is None:
            sizes = [100, 500, 1000, 5000, 10000]
        
        results = {}
        
        print("\nPerformance Analysis")
        
        for size in sizes:
            test_array = self.generate_random_array(size)
            avg_time = self.time_sort(sorter, test_array)
            results[size] = avg_time
            print(f"Array size: {size:6,} -> Time: {avg_time:.6f} seconds")
        
        return results


def test_basic():
    sorter = MergeSortTempParam()
    
    print("Testing MergeSort with Temp Array Parameter")
    
    test_cases = [
        [5, 2, 8, 1, 9, 3],
        [1, 2, 3, 4, 5],
        [9, 8, 7, 6, 5],
    ]
    
    all_passed = True
    for i, test_arr in enumerate(test_cases, 1):
        print(f"\nTest {i}: {test_arr}")
        
        sorted_arr = sorter.sort(test_arr.copy())
        is_correct = sorter.is_sorted(sorted_arr)
        
        print(f"Sorted: {sorted_arr}")
        print(f"Correct: {is_correct}")
        
        if not is_correct:
            all_passed = False
    
    if all_passed:
        print("\nAll correctness tests passed!")
    else:
        print("\nSome tests failed!")


def main():
    print("MERGE SORT: TEMP ARRAY PARAMETER")
    
    sorter = MergeSortTempParam()
    analyzer = PerformanceAnalyzer()
    
    test_basic()
    
    results = analyzer.run_performance_test(sorter)
    
    print("\nSummary")
    print("Algorithm: MergeSort with temporary array parameter")
    print("Time Complexity: O(n log n)")
    print("Space Complexity: O(n)")
    print(f"Performance tested on sizes: {list(results.keys())}")


if __name__ == "__main__":
    main()