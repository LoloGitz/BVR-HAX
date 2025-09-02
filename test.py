# rect_height = int(input("height?"))
# rect_width = int(input("width"))

# print("perimeter: " + str(rect_height * 2 + rect_width * 2) + " area: " + str(rect_height * rect_width))

# # str, int, float, bool

# score = int(input("Your score?"))


# if (score > 100 or score <= 0):
#     print("pumpkin eater.")
# elif (score >= 90):
#     print("A")
# elif (score >= 80):
#     print("B")
# elif (score >= 70):
#     print("C")
# elif (score >= 60):
#     print("D")
# else:
#     print("F. You failed.")

classes = {"math": 100, "english": 50, "history": 75, "art":150}

pick_class = input("Pick a class.")
pick_direction = input("Read, or write? (r/w)")
print("Your " + pick_class + " grade is currently " + str(classes[pick_class]) + ".")
if pick_direction == "w":
    pick_grade = input("What do you want to change it to?")
    classes[pick_class] = float(pick_grade)
    print("Your " + pick_class + " grade is now " + str(classes[pick_class]) + ".")