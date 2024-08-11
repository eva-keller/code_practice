"""x = float(input("What's x? "))
y = float(input("What's y? "))

#z = round(x + y)

#display numbers with commas using f strings
#print(f"{z:,}")

#round() '2' means rounding it to 2 digits
z = round(x / y, 2)

#using f string
#print(f"{z:.2f})
print(z)
"""
def main():
    x = int(input("What's x? "))
    print("x squared in ", square(x))

def square(n):
    return n*n

main():
