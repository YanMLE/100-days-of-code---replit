import random

print("Guess the Number Game")
print()

attempt = 0


number = random.randint(1, 1000000)
while True:
  guess = int(input("What is your guess? "))
  if guess > number:
    print("That's too high, just like you!")
    attempt += 1
    continue
  elif guess < number:
    print("Nigga, that's too low")
    attempt += 1
    print()
    continue
  elif guess == number:
    print("Good one, mate!")
    attempt += 1
    print()
    print(f"It took you {attempt} attemps to get the number correct!")
    break
    exit()
print()