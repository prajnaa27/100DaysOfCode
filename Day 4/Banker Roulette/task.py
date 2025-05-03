import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]


print("Welcome to the Russian Roulette!!..\n")
index=random.randint(0,4)
print(f"index = {index}")
print(f"The unlucky person chosen is.....\n{friends[index]}")


print(random.choice(friends))