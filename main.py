i = int(input("type some numbers(1 to 100) : "))

if i % 15 == 0:
    print("fizbuzz")
elif i % 3 == 0:
    print("fizz")
elif i % 5 == 0:
    print("buzz")
else:
    print(i)
