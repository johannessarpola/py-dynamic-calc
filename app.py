from os import listdir
from os.path import isfile, join
from abc import ABC, abstractmethod

path = "./strats"
files = [f for f in listdir(path) if isfile(join(path, f))]

def import_from(module, name):
    module = __import__(module, fromlist=[name])
    return getattr(module, name)

def printStrats(lst):
    for f in lst:
        print(f.split(".")[0]) 

def operateOnInput(task):
    """Operate on user-defined input"""
    values = input('Enter two integers separated by a comma and whitespace: ')
    str_list  = list(values.split(', '))
    int_list = list(map(int, str_list))

    task = import_from("strats", task)
    value = task.operation(1,2)
    print(value)

def main():

    print('Welcome to the Small Calculator! What do you want to do? Available operations are')
    printStrats(files)
    task = input()
    operateOnInput(task)
            
    while True:
        continuation = input('Keep calculating? Enter Y for yes, or N for no: ')
        if continuation == 'Y':
            print('Choose your operation. Available operations are')
            printStrats(files)
            strat = input()
            operateOnInput(strat)
        elif continuation == 'N':
            print('Goodbye!')
            break
          
if __name__ == '__main__':
    main()
