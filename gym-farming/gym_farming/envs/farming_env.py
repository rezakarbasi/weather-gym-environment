import gym
from gym import error, spaces, utils
from gym.utils import seeding

import pandas as pd
import numpy as np

class FarmingEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.reset()

    def step(self, action:str):
        data = self.df.iloc[self.index]
        self.index += 1

        reward = 0.0

        if action.lower() == 'pear':
            if data['rainfall_mm']>600:
                reward+=1.2
        
            if data['max_temp_C']<36:
                reward += 1


        elif action.lower() == 'apple':
            if data['rainfall_mm']>600:
                reward+=1

            if data['max_temp_C']<37:
                reward += 1
        

        elif action.lower() == 'cherry':
            if data['min_temp_C']>1:
                reward+=1

            if data['rainfall_mm']>900:
                reward+=1.5
            elif data['rainfall_mm']<650:
                reward-=1.5
        

        elif action.lower() == 'walnut':
            if data['min_temp_C']<0.2:
                reward+=1

            if 700<data['rainfall_mm']<950:
                reward+=1


        done = False
        if self.index>=len(self.df):
            done = True
            self.reset()

        return int(data['Year']+1) , reward+np.random.randn()*0.6 , done

    def reset(self):
        self.df = pd.read_csv('weather-yearly.csv')
        self.index = 0

    # def render(self, mode='human', close=False):
