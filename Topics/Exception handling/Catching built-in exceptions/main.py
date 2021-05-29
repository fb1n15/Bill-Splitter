def exception_check(a, b):
    try:
        ans = a / b
    except ZeroDivisionError:
        print("The Error!")
    else:
        print(ans)

