import python.equations as eq
# import tkinter as tk

def main():

    input = eq.c1v1(200, 'hello', 200, None)
    return eq.c1v1.missing_var(input)

    # input = eq.ncv_triangle(None, 1, 200, 450)
    # return eq.ncv_triangle.missing_var(input)

if __name__ == '__main__':
    print(main())
