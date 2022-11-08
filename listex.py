#!/usr/bin/env python3

wordbank = ["indentation", "spaces"]

tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

wordbank.append(4)

num = int(input("Enter a number between 0 and 18:"))
student_name = tlgstudents[num]

print(student_name + " always uses " + str(wordbank[2]) + " "  + str( wordbank[1]) + " to indent.")



