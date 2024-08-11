#ask user for their name
name = input("What's your name? ").strip().title()

#remove whitespace from str, acpitalize user's name
#name = name.strip().title()

#split user's name into first name and last name
first, last = name.split(" ")

#say hello to user
print(f"hello, {first}")

#print("apple", "banana", "cherry", sep="...", end="okay")
#how to tailor the print fucntion

