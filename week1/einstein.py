#E = mc**
#E - energy in Joules
#m - mass in kg
#c - speed of light - 300000000meters per second

#prompt the user for mass as an integer, in kg
#output the equivalent number of Joules as an integer

def  formula():
    m = int(input("Give me a mass in kg! "))
    c = 300000000
    E = m*c*c
    print(f"The energy is {E:,} Joules")
    
    
formula()
