# Range function generates the arithmetic progression
for i in range(10):
    print(i)

# Range b/w 5 to 10 - 5, 6, 7, 8, 9 will be generated
for i in range(5, 10):
    print(i)

# Range b/w 0 to 10, the increments of 2 will be generated.
for i in range(0, 10, 2):
    print(i)

# To iterate over the indices of a sequence with range() and len()
a = ["I", "Love", "India"]
for i in range(len(a)):
    print(i, a[i])

print(range(10))

print('Sum of first 10 numbers is : ', sum(range(10)))
