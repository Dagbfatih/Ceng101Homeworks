###
### AYBU CENG101 Homework 2
### Author::
### Beşir Fatih Dağ | 23050111034
###

# There are 3 tasks that separated by comment lines.
# Each task can be executed by run_task<task_no>() function.


# If len() function (coz it is built-in) is not allowed we need to write our own method.
# That's why I wrote len_of() method below.


def len_of(val):
    if (type(val) is not str) and (type(val) is not list):
        return

    length = 0
    for i in val:
        length += 1
    return length


###---------------
### Task 1
###---------------
def run_task1():

    a = int(input("How many books did you buy?\n"))
    x = int(input("What is the number of books to get a new book for free?\n"))

    # Check whether a or x is between 0-1001
    if not (0 < a < 1001) or not (0 < x < 1001):
        print("Invalid input")
        return

    how_many_books(a, x)


def how_many_books(a, x):
    existing = a
    readed = a

    while not (existing < x):
        received = int(existing / x)
        leftover = existing % x

        existing = received + leftover
        readed += received

    print("The maximum number of books you can read is ", readed)


###---------------
### Task 2
###---------------
def run_task2():
    print(days_to_write("ada"))
    print(days_to_write("j"))
    print(days_to_write("code"))
    print(days_to_write("buzz"))


def required_days(message):
    biggest = ord("a")
    for ch in message:
        unicode = ord(ch)

        if biggest < unicode:
            biggest = unicode

    letter_count = biggest - ord("a") + 1
    return letter_count


def days_to_write(message):
    # If message len is greater than 100 do not do anything
    if type(message) is not str:
        return

    if len_of(message) > 100:  # If message len is greater than 100 do not do anything
        return

    letter_count = required_days(message=message)

    # Python ternary operator as same as "?"" and ":" operators in Java. I assume we are allowed to use that operator here too.
    holidays = (
        ((letter_count // 5) * 2) - 2
        if letter_count % 5 == 0
        else (letter_count // 5) * 2
    )
    days = letter_count + holidays

    return days


###---------------
### Task 3
###---------------
def run_task3():
    print(calculate(6, 2, 1, 2))
    print(calculate(5, 2, 2, 3))
    # print(calculate(8, 3, 2, 5))
    # print(calculate(9, 4, 3, 7))
    # print(calculate(10, 5, 1, 4))
    # print(calculate(7, 2, 2, 3))
    # print(calculate(3, 5, 2, 4))
    # print(calculate(4, 3, 2, 8))
    # print(calculate(40, 6, 1, 7))


## I deeply dive into math calculations to ensure that one
## of the possibilities below is exactly the minimum value.
## It is about that the function of cost is a line. That shows
## middle points of that line cannot be minimum than one of the enpoint.
## Which endpoint is the minimum depends on the sign of the function.
## Finally I removed all the complicated codes that I've written before
## and then calculated only two possibilities below.
def calculate(n, m, a, b):
    m_ride_count = n // m
    one_ride_count = n % m

    poss1 = m_ride_count * b + one_ride_count * a
    poss2 = n * a

    if poss1 > poss2:
        return poss2

    return poss1


###---------------
### Running Tasks
###---------------

### Uncomment the lines you want to run:

# run_task1()
# run_task2()
# run_task3()

### OR simply run the methods:

# days_to_write("ada")
# calculate(6, 2, 1, 2)
