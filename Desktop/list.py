grocery = ["Harpic", "vim bar", "deodrant", "Bhindi",
           "Lollypop", 56]
# print(grocery[5])
numbers = [2, 7, 9, 11, 3]
numbers.remove(9)
print(numbers)
numbers.pop()
print(numbers)
numbers.sort()
print(numbers)
numbers = []
print(numbers)
numbers.reverse()
print(numbers)
numbers.append(1)
print(numbers)
numbers.append(72)
print(numbers)
numbers.append(5)
print(numbers)
numbers.insert(2, 67)
print(numbers)
# 3, 11, 9, 7, 2
print(numbers)
numbers[1] = 98
print(numbers)
# Mutable - can change
# Immutable - cannot change
tp = (1,)
print(tp)
a= 1
b = 8
a, b = b,a
# temp = a
# a = b
# b = temp
print(a, b)

########################### tupple ############################################
print("##### tupple ##########")
t = ("hi", "python", 2)
print(t[1:]);
print(t[0:1]);
print(t);
print(t + t);
print(t * 3);
print(type(t))
t[2] = "hi";