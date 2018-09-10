a = '---'.join('    ')
b = '   '.join('||||')
print('\n'.join((a, b, a, b, a, b, a)))


def print_board():
    size = int(input("Size of board matrix?"))
    x = 1
    while x <= size:
        print(" --- " *size + "\n"+ "|   |"*size)
        x += 1
    print(" --- " * size)



def draw(n):
    for i in range(n):
        print("---".join(" "*(n+1)))
        print("   ".join("|"*(n+1)))
    print("---".join(" "*(n+1)))

draw(3)
