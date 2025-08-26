def checkSign(n):
    if n < 0:
        print("Negative")
    elif n == 0:
        print("Zero")
    elif n > 0:
        print("Positive")
    else:
        print("Infinity")


checkSign(10)
checkSign(-10)
checkSign(0)