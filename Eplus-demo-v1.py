import gym;
import eplus_env;

env = gym.make('Eplus-demo-v1');
curSimTime, ob, isTerminal = env.reset(); # Reset the env (creat the EnergyPlus subprocess)
while not isTerminal:
    action = [20, 20];
    curSimTime, ob, isTerminal = env.step(action);
curSimTime, ob, isTerminal = env.reset(); # Start a new episode (creat a new EnergyPlus subprocess)
while not isTerminal:
    action = [20, 20];
    curSimTime, ob, isTerminal = env.step(action);
env.end_env(); # Safe termination of the environment after use. 
