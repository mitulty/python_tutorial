# -*- coding: utf-8 -*-
# @Author: Mitul Tyagi
# @Date:   2024-12-05 23:48:51
# @Description: Modules
'''
- A module is a code library. A module is a A file containing a set of functions that is included in the application. The import statement can be used to create a
  module. When using a function from a module, the syntax module_name.function_name is used.
- The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc). An alias can be created when importing a
  module. Python contains several built-in modules.
- There is a built-in function to list all the function names (or variable names) in a module. The dir() function of platform module can be used.
- The keyword from can be used to import only parts from a module. When importing using the from keyword the module name is not used when referring to elements.
- To import modules from a different director use sys module to append the path. Subdirectory can be directly used.
- Different ways of importing are:
    -> import module_name
    -> import module_name as alias_name
    -> from module_name import var_name, f_name, class_name.....
    -> from module_name import address as alias_address
    -> from module_name import *
- Before executing code, Python interpreter reads source file and define few special variables/global variables. If the python interpreter is running that module 
  (the source file) as the main program, it sets the special __name__ variable to have a value "__main__". If this file is being imported from another module, 
  __name__ will be set to the module's name. Module's name is available as value to __name__ global variable. 
- The if __name__ == '__main__' statement in Python determines if a script is being run as the main program or imported as a module into another program. The __name__ 
  variable is set to the name of the module if it's imported, and to the string __main__ if the module is the main entry point to the program. This statement allows a 
  Python file to contain executable code that won't run when a module is imported. It also helps make code more modular, readable, and avoid unintended execution.  

'''
import math

print(math.sqrt(16))
print(math.pi)
print(math.e)
print(math.log10(10000))
print(math.pow(2,5))
print(dir(math))

import calendar

cal  = calendar.month(2025,1)
print(cal)
print(calendar.isleap(2024))
print(dir(calendar))

import custom_module

custom_module.print_bye()

def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()
