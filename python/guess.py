# Write code below 💖
import time

guess = 0
tries = 0

while guess != 6 and tries < 5:
  guess = int(input("Guess the number:  "))
  tries += 1

print("You got it!")
print("Nice, let's see how many tries that took...")

time.sleep(3)

print(tries)

