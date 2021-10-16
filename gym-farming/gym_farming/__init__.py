from gym.envs.registration import register

register(
    id='farming-v0',
    entry_point='gym_farming.envs:FarmingEnv',
)