score = 0

print("\n Math Game")
print()

multiple = int(input("Choose your multiples: "))
print()

for round in range(1, 11):
  result = round * multiple
  answer = int(input(f"{round} * {multiple} = "))
  if answer == result:
    score += 1
    print("Good one, my brother!")
  else:
    print(f"Dumbass! The answer was {result}")
  print()
print()

print("-" * 10)
print()

print(f"You've scored {score} out of 10.")
print()

if score == 10:
  print("My brother!")
elif score >= 6:
  print("That's a good score!")
elif score == 5:
  print("You're dumb, but not too dumb!")
elif 0 < score <= 4:
  print("Brother, just study a little more! you're dumb!")
else:
  print("Nigga, you've scored 0! you're stupid!")
