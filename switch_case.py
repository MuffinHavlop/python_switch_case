import math
import time


def decorator():
    def wrapper():
        print(f"Running {func.__name__}...")
        time.sleep(2)
        func()
    return wrapper

@decorator
def ptb1():
    a = int(input("nhap a: "))
    b = int(input("nhap b: "))
    loi_giai(a, b)


def loi_giai(a, b):
    x = -a/(2*b)
    print("x = ", x)


@decorator
def ptb2():
    a = int(input("nhap a: "))
    b = int(input("nhap b: "))
    c = int(input("nhap c: "))
    print(f"phuong trinh cua ban la: y = {a}x^2 + {b}x + {c}")
    if a + b + c == 0:
        truong_hop_1_ptb2(a, c)
    elif a + b - c == 0:
        truong_hop_2_ptb2(a, c)
    else:
        truong_hop_con_lai_ptb2(a, b, c)


def truong_hop_1_ptb2(a, c):
    print("x1 = 1")
    print("x2 = ", c/a)


def truong_hop_2_ptb2(a, c):
    print("x1 = -1")
    print("x2 = ", -c/a)


def truong_hop_con_lai_ptb2(a, b, c):
    delta = b**2 - 4*a*c
    delta_squared = math.sqrt(delta)
    x1 = (-delta_squared + b)/(2*a)
    x2 = (-delta_squared - b)/(2*a)
    print("x1 = ", x1)
    print("x2 = ", x2)


def quit():
    print("Shutting down")
    time.sleep(2)
    exit()


while True:
    match input("ptb1 hay ptb2 (quit de thoat): "):
        case "ptb1":
            ptb1()
        case "ptb2":
            ptb2()
        case "quit":
            quit()
        case _:
            print("Invalid Input")  
