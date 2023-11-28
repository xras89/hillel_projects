def calculateArea(l,h,w):
    square = 2 * (w*l + w*h + l*h)
    return square

lenght = int(input("Please enter lenght (cm): "))
height = int(input("Please enter height (cm): "))
width = int(input("Please enter width (cm): "))

answer = calculateArea(lenght, height, width)

print(f"Surface area of a rectangular parallelepiped {answer} (square cm).")