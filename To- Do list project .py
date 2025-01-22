#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# To-Do List App


# In[39]:


tasks = []

def addTask():
    task = input("Please enter a task:")
    tasks.append(task)
    print('\n')
    print(f"Task '{task}' added to the list.")
    

def listTasks():
    if not tasks:
        print("\n There are no tasks currently.")
        return
    else:
        print("\n Current Tasks:")
        for index, task in enumerate(tasks, start = 1):
            print(f"Task #{index}. {task}")
            
def deleteTask():
    listTasks()
    if not tasks:
        return
    
    try:
        taskToDelete = int(input("\n Enter the # to delete:"))
        if taskToDelete >= 1 and taskToDelete <= len(tasks):
            tasks.pop(taskToDelete -1)
            print('\n')
            print(f'Task {taskToDelete} has been removed.')
        else:
            print(f'Task #{taskToDelete} was not found.')
      
    except:
        print("Invalid input !")
    
if __name__ == "__main__":    
### Create a loop to run the app
    print('Welcome to the To-Do List App:')
    while True:
        print("\n Please select one of the following: ")
        print('-------------------------------')
        print('1. Add a new Task')
        print('2. Delete a Task')
        print('3. List Tasks ')
        print('4. Quit')
        
        choice = input('\n Enter your choice:')
        if(choice == '1'):
            addTask()
        elif(choice == '2'):
            deleteTask()
        elif(choice == '3'):
            listTasks()
        elif(choice == '4'):
            break
        else:
            print('Invalid input. Please try again.')
      
    print('Good Bye!')
    


# In[ ]:





# In[ ]:




