# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-05 23:48:51
# @Description: Custom Module


print("First Module's Name: {}".format(__name__))

def print_bye():
    print("Bye!!!!")
    
def main():
    print("Hello, World in Custom Module!")


if __name__ == "__main__": # if this file is directly run
    print("Run Directly!!!")
    main()
else:
    print("This is imported!!!")
