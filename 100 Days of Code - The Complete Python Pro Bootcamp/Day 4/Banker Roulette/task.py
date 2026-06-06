friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

import random

print(random.choice(friends))

# Or

friends_random = random.randint(0, 4)

if friends_random == 0:
    print("Alice")
elif friends_random == 1:
    print("Bob")
elif friends_random == 2:
    print("Charlie")
elif friends_random == 3:
    print("David")
elif friends_random == 4:
    print("Emmanuel")

# Or

print(friends[friends_random])



