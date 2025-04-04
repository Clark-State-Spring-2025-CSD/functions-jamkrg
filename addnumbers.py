#This is a teacher led demo.
#Watch this video or follow along in class.

def AddTwoNumbers(number1, number2):
    result = number1 + number2
    return result

def HelloTen():
    for _ in range(10):
        print("Hello!")

def CheckHit(hitTarget, diceRoll):
    if diceRoll >= hitTarget:
        print("That is a hit!")
        return True
    else:
        print("That is a miss!")
        return False


x = 5
y = 10

result = AddTwoNumbers(x,y)

HelloTen()

print(result)

print(CheckHit(5,10))
print()
print(CheckHit(10,5))