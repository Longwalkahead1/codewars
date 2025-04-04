def list ():
    answer1 = int(input(f"give me one number"))
    answer2 = int(input(f"give me a second number"))
    result = answer1/answer2
    try:
        0//1
    except ValueError:
        print("you cannot do this function!")   
    print(result)
   

list()