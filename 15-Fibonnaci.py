def fibonnaci():
    num = int(input("How many numbers to generate?"))
    i = 1
    if num == 0:
        fibo = []
    elif num == 1:
        fibo = [1]
    elif num == 2:
        fibo = [1,1]
    elif num > 2:
        fibo = [1,1]
        while i < num - 1:
            fibo.append(fibo[i] + fibo[i - 1])
            i += 1
    return fibo


print(fibonnaci())
