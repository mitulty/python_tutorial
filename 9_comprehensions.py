# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-05 23:48:51
# @Description: Comprehensions
'''
- The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item 
  in each passed iterator are paired together etc.
- If the passed iterables have different lengths, the iterable with the least items decides the length of the new iterator.
- The syntax is zip(iterator1, iterator2, iterator3 ...).

'''
nums = [1,2,3,4,5,6,7,8,9,10]

my_lists = [n for n in nums]
print(my_lists)

my_lists = [(n*n) for n in nums]
print(my_lists)

my_even_lists = [n for n in nums if (n%2==0)]
print(my_even_lists)

my_zip = [(a,b) for a in 'abcd' for b in nums]
print(my_zip)

names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heros = ["Batman", "Superman", "Spiderman", "Wolverine", "Deadpool"]

print("Zip: ",zip(names,heros), list(zip(names,heros)))
my_dict = dict()
for n,h in zip(names, heros):
    my_dict[n] = h
print(my_dict)    

my_dict = {name:hero for name, hero in zip(names,heros)}
print(my_dict)

my_dict = {name:hero for name, hero in zip(names,heros) if name != "Peter"}
print(my_dict)

my_set = {x for x in names}
print(my_set, type(my_set))

# Generator 
my_tuple = (x for x in names)
print(my_tuple, type(my_tuple))


a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)
print(list(x))
def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()
