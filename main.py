def fizzBuzz( i: int) :
    if i % 3 == 0 and i % 5 == 0:
        return "FizzBuzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
    else:
        return i 


def main():
    num = int(input('enter a number'))
    print(fizzBuzz(num))


if __name__ == '__main__':
    main()