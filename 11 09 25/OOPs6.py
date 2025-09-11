def Division(a,b):
    try:
        print(a/b)
    except ArithmeticError:
        print("Arithmetic error occured!")
    else:
        print("Division completed")
    finally:
        print("Execution done")
        
Division(10,8)
        