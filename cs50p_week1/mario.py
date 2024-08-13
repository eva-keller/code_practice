def main():
    print_column(3)
    print_row(4)
    print_square(3)

def print_column(height):
    for _ in range(3):
        print("#")
    #another possible solution:
    #print("#\n" * height, end="")

def print_row(width):
    print("?" * width)

def print_square(size):

    #for each row in square
    for i in range(size):

        #for each brick in row
        for j in range(size):

            #print brick
            print("#", end="")

        print() #prints a new line for the new row

   #  instead of j, we can do: 
   # print("#" * size)   


main()