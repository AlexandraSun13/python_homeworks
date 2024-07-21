def fizz_buzz(a):
    for n in range(1, a + 1):
       if n % 3 == 0 and n % 5 == 0:
           print("FizzBuzz")
       elif n % 3 == 0:
           print("Fizz")
       elif n % 5 == 0:
           print("Buzz")
       else:
           print(n)

user_input = input("Введите число: ")
a = int(user_input)
fizz_buzz(a)