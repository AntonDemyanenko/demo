number = int(input())

def check_number(n: int) -> None:
    if n % 3 == 0 and n % 5 == 0:
        print("Foobar")
    elif n % 3 == 0:
        print("Foo")
    elif n % 5 == 0:
        print("Bar")

result = check_number(number)