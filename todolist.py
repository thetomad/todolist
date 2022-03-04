
from random import randint
import numpy as np



def main():
    
    tasks = []
    while True:
        
    
        command = input('\n What you want to do? (new task, do task, show tasks, delete task, exit = n/d/s/del/x)   ')

        if command == 'n':
            new_task = input(' Call new task:  ')

            tasks.append(new_task)
            print(tasks)
        elif command == 'd':
            if len(tasks) > 0:
                index_task = np.random.randint(0,len(tasks))
                do_task = tasks[index_task]
                print(do_task)
                done = input(' Are you done? (y/n)  ')

                if done == 'y':
                    print(' good job!')
                    tasks.remove(do_task)
                elif done == 'n': 
                    print(' :( ')
            else: 
                print(" No tasks right now")

        elif command == "s":
            for task in tasks:
                print(' ' + task)
        
        elif command == 'del':
            index_task = int(input(" The index of the task: "))
            if index_task < len(tasks):
                tasks.remove(tasks[index_task])
            else:
                print(' Bad index')

        elif command == 'x':
            break

if __name__ == '__main__':
    main()