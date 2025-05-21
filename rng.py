import random as r

import time as t

rewards = [100, 200, 300,]
                                                                                    #weights_for_7_items=[40, 20, 13, 10, 6, 4, 3]
loop = True

time = 0
cooldown = 0

try:
    while loop == True:
        reward = r.choice(rewards)
        time += 0.2
        cooldown += 0.1
        t.sleep(cooldown)
        if time < 1.6:
            print(reward)
            continue
        else:
            print(f"The winner is: {reward}")
            break

except KeyboardInterrupt:
    print("Error the wheel was forcefully stopped")