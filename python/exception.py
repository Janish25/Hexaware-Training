def divide():
    try:
        n1 = int(input("Enter Numerator: "))
        n2 = int(input("Enter Denominator: "))
        ans = n1/n2
        print(ans)
    except ValueError as e:
        print("Values should be int..", e)
    except ZeroDivisionError as e:
        print("Cannot divisible by 0..", e)
    except Exception as e:
        print(e)
    finally:
        print("Operation Completed")
        
        
divide()


#ValueError: invalid literal for int() with base 10: '10e'
#ZeroDivisionError: division by zero