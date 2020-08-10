def standard():
    for i in range(1,101):
        output = ''
        if i % 3 == 0:
            output += 'Fizz'
        if i % 5 == 0:
            output += 'Buzz'
        if output == "":
            print(i)
        else:
            print(output)


def shortened():
    for i in range(1,101):
        output = ""
        output += "Fizz" if i % 3 == 0 else ''
        output += "Buzz" if i % 5 == 0 else ''
        print(i if output == "" else output)

shortened()