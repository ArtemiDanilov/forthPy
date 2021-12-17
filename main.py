def Autotest_1():
    test = open("Autotest.txt", "w+")
    test.write("1 10 1 3")
    test.close()
    func("AutoTest.txt")
    if func("AutoTest.txt") == 2:
        return 1
    return 0


def Autotest_2():
    test = open("Autotest.txt", "w+")
    test.write("2 2 2 17 2")
    test.close()
    func("AutoTest.txt")
    if func("AutoTest.txt") == 1:
        return 1
    return 0

def Autotest_3():
    test = open("Autotest.txt", "w+")
    test.write("2 2 2 5 1")
    test.close()
    func("AutoTest.txt")
    if func("AutoTest.txt") == 3:
        return 1
    return 0


def autotest():
    if Autotest_1() == 1:
        print("First autotest passed")
    else:
        print("First autotest failed")
    if Autotest_2() == 1:
        print("Second autotest passed")
    else:
        print("Second autotest failed")
    if Autotest_3() == 1:
        print("Third autotest passed\n")
    else:
        print("Third autotest failed\n")


def func(name_of_file):
    a = 0
    b = 0
    k = False
    file = open(name_of_file, "r")
    if file.closed:
        print('file is closed')
        return 0
    for line in file:
        seq = line.split()
        for i in range(len(seq)):
            if int(seq[i])%2 == 0:
                a += int(seq[i])
            else:
                b += int(seq[i])
    file.close()
    if a < b:
        return 1
    if a > b:
        return 2
    return 3

autotest()
print("Write name of file:")
f = input()
if func(f) == 1:
    print('The sum of odd elements is greater \n')
else:
    if func(f) == 2:
      print('The sum of even elements is greater \n')
    else:
     if func(f) == 3:
         print('The sums of even and odd elements are equal')
