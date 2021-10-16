#%% environment initialization
import gym
import gym_farming

env = gym.make('farming-v0')
env.reset()

#%% get samples of each tree
actions = ['walnut','cherry','apple','pear']
rewards = []
for a in actions :
    rewards.append([])
    for i in range(10):
        done = False
        while done==False:
            _,r,done = env.step(a)
            rewards[-1].append(r)


#%% show the rewards of each tree
import matplotlib.pyplot as plt
plt.figure()
for i in range(len(actions)):
    plt.subplot(4,1,i+1)
    plt.hist(rewards[i],label=actions[i])
    plt.legend()

plt.show()

#%% print mean rewards
import numpy as np
a = np.array(rewards)
print(np.mean(a,axis=1))
