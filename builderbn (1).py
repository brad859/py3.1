def area(length, width):
    return length * width
print("What is the length?")
length = int(input())
print("What is the width?")
width = int(input())
result = area(length, width)
print(f"Area of Rectangle:{result}")