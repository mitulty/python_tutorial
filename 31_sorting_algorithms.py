# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-31 12:11:51
# @Description: 
'''
- A sorting algorithm is used to arrange elements of an array/list in a specific order. A sorting algorithm is considered stable if the two or more items with the 
  same value maintain the same relative positions even after sorting. This is widely used in different applications that include searching algorithms, data structure
  optimization, and database management.
- Comparison of various sorting alogrithms:
                    |-------------------|------------------------|--------------------------|---------------------------|-------------------|
                    | Sorting Algorithm	| Time Complexity - Best |  Time Complexity - Worst	| Time Complexity - Average	| Space Complexity  |
                    |-------------------|------------------------|--------------------------|---------------------------|-------------------|
                    | Bubble Sort	      |     n	                 |    n^2	                  |       n^2	                |        1          |
                    |-------------------|------------------------|--------------------------|---------------------------|-------------------|
                    | Selection Sort	  |     n^2	               |    n^2	                  |       n^2 	              |        1          |
                    |-------------------|------------------------|--------------------------|---------------------------|-------------------|
                    | Insertion Sort	  |     n	                 |    n^2	                  |       n^2	                |        1          |
                    |-------------------|------------------------|--------------------------|---------------------------|-------------------|
                    | Merge Sort	      |     n*logn             |    n*logn                |       n*logn	            |        n          |
                    |-------------------|------------------------|--------------------------|---------------------------|-------------------|
                    | Quicksort	        |     n*logn             |    n^2	                  |       n*logn	            |        logn/n     |
                    |-------------------|------------------------|--------------------------|---------------------------|-------------------|
                    | Counting Sort	    |     n+k	               |    n+k	                  |        n+k	              |        max        |   
                    |-------------------|------------------------|--------------------------|---------------------------|-------------------|
                    | Radix Sort	      |     n+k	               |    n+k	                  |        n+k	              |        max        |
                    |-------------------|------------------------|--------------------------|---------------------------|-------------------|
                    | Bucket Sort	      |     n+k	               |    n^2	                  |        n	                |        n+k        |
                    |-------------------|------------------------|--------------------------|---------------------------|-------------------|
                    | Heap Sort	        |     n*logn	           |    n*logn	              |        n*logn	            |        1          |
                    |-------------------|------------------------|--------------------------|---------------------------|-------------------|
                    | Shell Sort	      |     n*logn	           |    n^2	                  |        n*logn	            |        1          |
                    |-------------------|------------------------|--------------------------|---------------------------|-------------------|
- Unstable algorithms: Selection Sort, Quick Sort, Heap Sort & Shell Sort.
- Stable algorithms: Bubble Sort, Inserstion Sort, Merge Sort, Counting Sort, Radix Sort, & Bucket Sort.
- Sorting Alogrithms can be classified on the basis of: Time Complexity, Space Complexity, Stability, Recursive or Non-Recursive & Internal or External.
'''
def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()
