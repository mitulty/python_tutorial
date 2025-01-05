# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2025-01-05 00:42:49
# @Description: Analysis of Algorithms
'''
- The efficiency of an algorithm depends on the amount of time, storage and other resources required to execute the algorithm. The efficiency is measured with the 
  help of asymptotic notations. An algorithm may not have the same performance for different types of inputs. With the increase in the input size, the performance 
  will change. The study of change in performance of the algorithm with the change in the order of the input size is defined as asymptotic analysis.
- Asymptotic notations are the mathematical notations used to describe the running time of an algorithm when the input tends towards a particular value or a 
  limiting value. There are mainly three asymptotic notations:
                    -> Big-O notation
                    -> Omega notation
                    -> Theta notation
                    
- Big-O notation represents the upper bound of the running time of an algorithm. Thus, it gives the worst-case complexity of an algorithm. Since it gives the 
  worst-case running time of an algorithm, it is widely used to analyze an algorithm as we are always interested in the worst-case scenario.
- If f(n) describes the running time of an algorithm, f(n) is O(g(n)) if there exist a positive constant C and n0 such that, 0 ≤ f(n) ≤ cg(n) for all n ≥ n0.
- { 100 , log (2000) , 10^4 } belongs to O(1)
  { (n/4) , (2n+3) , (n/100 + log(n)) } belongs to O(n)
  { (n^2+n) , (2n^2) , (n^2+log(n))} belongs to O(n^2) 
  
- Omega notation represents the lower bound of the running time of an algorithm. Thus, it provides the best case complexity of an algorithm.
- Let g and f be the function from the set of natural numbers to itself. The function f is said to be Ω(g), if there is a constant c > 0 and a natural number n0 
  such that c*g(n) ≤ f(n) for all n ≥ n0.
- { (n^2+n) , (2n^2) , (n^2+log(n))} belongs to Ω( n^2)
  { (n/4) , (2n+3) , (n/100 + log(n)) } belongs to Ω(n)
  { 100 , log (2000) , 10^4 } belongs to Ω(1)

- Theta notation encloses the function from above and below. Since it represents the upper and the lower bound of the running time of an algorithm, it is used for 
  analyzing the average-case complexity of an algorithm.
- Let g and f be the function from the set of natural numbers to itself. The function f is said to be Θ(g), if there are constants c1, c2 > 0 and a natural number 
  n0 such that c1*g(n) ≤ f(n) ≤ c2*g(n) for all n ≥ n0.
- In academia, Θ means both O and Ω. That is an algorithm is Θ(N) is if it is both O(N) and Ω(N). Θ gives a tight bound.
  
- { 100 , log (2000) , 10^4 } belongs to Θ(1)
  { (n/4) , (2n+3) , (n/100 + log(n)) } belongs to Θ(n)
  { (n^2+n) , (2n^2) , (n^2+log(n))} belongs to Θ( n^2)

- If f(n) is O(g(n)) then a*f(n) is also O(g(n)), where a is a constant.
- If f(n) is Θ(g(n)) then a*f(n) is also Θ(g(n)), where a is a constant. 
- If f(n) is Ω (g(n)) then a*f(n) is also Ω (g(n)), where a is a constant.
- If f(n) is O(g(n)) and g(n) is O(h(n)) then f(n) = O(h(n)).
- If f(n) is Θ(g(n)) and g(n) is Θ(h(n)) then f(n) = Θ(h(n)) .
- If f(n) is Ω (g(n)) and g(n) is Ω (h(n)) then f(n) = Ω (h(n)).
- If f(n) is Θ(g(n)) then g(n) is Θ(f(n)).

- The big O, big Θ and big Ω notations describe the upper, tight and lower bound for the runtime. Best, worst and expected cases describe the big O (or big Θ) time 
  for particular inputs or scenarios.

- The rate at which the time, required to run a code, changes with respect to the input size, is considered the time complexity. Basically, the time complexity of a
  particular code depends on the given input size, not on the machine used to run the code.
- Time complexity measures the amount of time an algorithm takes to complete as a function of the size of its input. It helps to understand how the runtime of an 
  algorithm grows with respect to the size of the input.
- The time complexity of an algorithm quantifies the amount of time taken by an algorithm to run as a function of the length of the input. Note that the time to run
  is a function of the length of the input and not the actual execution time of the machine on which the algorithm is running on.4

- Calculating the time complexity of an algorithm involves analyzing how the runtime of the algorithm grows as the size of the input increases. It is calculated for
  the worst-case sceanrios. The constant terms are not included. The lower values are igonred.
- Amortized time complexity in data structures analysis will give the average time taken per operation, which will be better than worst-case time complexity. 
  Amortized analysis is a method used in computer science to analyze the average performance of an algorithm over multiple operations. Instead of analyzing the 
  worst-case time complexity of an algorithm, which gives an upper bound on the running time of a single operation, amortized analysis provides an average-case 
  analysis of the algorithm by considering the cost of several operations performed over time.
- The term space complexity generally refers to the memory space that a code uses while being executed.
- Constant Time (O(1)): Algorithms with constant time complexity execute in the same amount of time regardless of the size of the input. This means that the 
  algorithm's runtime does not depend on the size of the input.
- Linear Time (O(n)): Algorithms with linear time complexity have their runtime linearly proportional to the size of the input.
- Logarithmic Time (O(log n)): Algorithms with logarithmic time complexity reduce the size of the input in each step, typically halving it. These algorithms are 
  often found in binary search or divide-and-conquer approaches. Logarithmic time complexity indicates that the algorithm's runtime grows logarithmically with the 
  size of the input.
- Quadratic Time (O(n²)): Algorithms with quadratic time complexity have a runtime that is proportional to the square of the size of the input. This usually occurs 
  in nested loops where each iteration of an outer loop triggers another loop to run through the entire input. As a result, the time taken by the algorithm increases
  quadratically with the size of the input.

- The space complexity of recursive algorithm is proportinal to maximum depth of recursion tree generated. If each function call of recursive algorithm takes O(m) 
  space and if the maximum depth of recursion tree is 'n' then space complexity of recursive algorithm would be O(nm).
- The time complexity for recursice algorithm looks like O(branches^depth), where branches is the number of times each recursive call branches.

'''

def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()
