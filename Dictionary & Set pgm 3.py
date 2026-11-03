# WAP to enter marks of 3 subjects from the user & store them in a dictionary.
# start with an empty dictionary & add one bt one.
# use subject name as key & marks as value.

marks={}

x=int(input("enter physics marks:"))
marks.update({"phy":x})
x=int(input("enter maths marks:"))
marks.update({"math":x})
x=int(input("enter chemistry marks:"))
marks.update({"chem":x})

print(marks)