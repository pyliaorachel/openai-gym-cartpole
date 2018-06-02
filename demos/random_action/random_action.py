"""
Agent taking random actions.
Based on the example on the official website.
"""
import gym


if __name__ == '__main__':
    env = gym.make('CartPole-v0')

    for i_episode in range(200):
        observation = env.reset() # reset environment to initial state for each episode
        rewards = 0 # accumulate rewards for each episode
        for t in range(250):
            env.render()

            action = env.action_space.sample() # choose a random action
            observation, reward, done, info = env.step(action) # do the action, get the reward
            rewards += reward

            if done:
                print('Episode finished after {} timesteps, total rewards {}'.format(t+1, rewards))
                break

    env.close() # need to close, or errors will be reported
