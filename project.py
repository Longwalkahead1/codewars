def display_menu():
     print("1. add task.\n2. view task.\n3. delete task.\n4. quit the application.")

task= []


def add_task():
    
    question1= input(f"what task would you like to add?")
    task.append(question1)
    print(f"{question1} has been added!")
    

def view_task():
    for i, word in enumerate(task, 1):
        print(f"{1}. {word}")

def delete_task():
    view_task()
    try:
        if task:
         question2 = int(input("what task would you like to delete?")) -1
        task.pop(question2)
        print("congratuations! Your task was succesfully deleted.")
    except (IndexError, ValueError):
     print("this is an unavailable answer, try again!")
def quit_application():
    print("Thank you for using this program!")
    
def main():
    while True:
        display_menu()
        question = int(input("what option would you like to choose?"))
        
        if question == 1:
            add_task()
        elif question == 2:
            view_task()
        elif question == 3:
            delete_task()
        elif question == 4:
            print("thank you for using this application")
            break
main()