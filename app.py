import asyncio
from os import listdir
from os.path import isfile, join

path = "operations"
files = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith(".py")]

def import_from(module, name):
    module = __import__(module, fromlist=[name])
    return getattr(module, name)

def print_ops(lst):
    for f in lst:
        print(f.split(".")[0]) 

async def handle_op(task):
    """Operate on user-defined input"""
    values = input('Enter numbers separated by a comma: ')
    str_list  = list(values.split(','))
    numbs = list(map(int, str_list))

    task = import_from(path, task)
    task = asyncio.create_task(
         task.operation(*numbs))
    
    print("Calculating ....")
    print(f'Done result: {await task}')

async def main():

    print('Available operations are')
    print_ops(files)
    task = input()
    await handle_op(task)
            
    while True:
        choice = input('Keep calculating? (y/n)').lower()
        continuation = choice == 'y' or choice == 'yes'

        if continuation:
            print('Choose your operation. Available operations are')
            print_ops(files)
            strat = input()
            await handle_op(strat)
        else:
            print('Goodbye!')
            break
          
if __name__ == '__main__':
    asyncio.run(main())
