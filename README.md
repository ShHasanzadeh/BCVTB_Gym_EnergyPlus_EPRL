Q&A:
https://www.linkedin.com/in/sh-hasanzadeh

# BCVTB_Gym_EnergyPlus_EPRL
A Complete Installation guide on UBUNTU 16.04 LTS, Included EnergyPlus Simulation for Reinforcement Learning (EPRL) codes that wraps an EnergyPlus model in a Python-based OpenAI Gym interface.
EPRL is available at https://github.com/zhangzhizza/Gym-Eplus

# This environment has been only tested in Ubuntu 16.04 OS.
This environment wraps the EnergyPlus-v-8-6 into the OpenAI gym environment interface.

# Installation
EnergyPlus is platform dependent. So this repository does not include the EnergyPlus software. Please download the EnergyPlus-v-8-6 from https://energyplus.net/downloads, extract it, and place it to the directory eplus_env/envs/EnergyPlus-8-6-0.

The environment depends on BCVTB-1.6.0 (https://simulationresearch.lbl.gov/bcvtb). There is no need to re-install it since this repository already had it. But BCVTB-1.6.0 is compiled with Java-1.8. Make sure you have Java-1.8 on your OS.

$ java --v
$ sudo apt-get update
$ sudo apt-get install openjdk-8-jdk
$ java -version

~/Downloads$ wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tar.xz
~/Downloads/Python-3.6.8$ ./configure
~/Downloads/Python-3.6.8$ make
~/Downloads/Python-3.6.8$ sudo make install
~/Downloads/Python-3.6.8$ python3.6 --version


~/home/linux-1604/Gym-Eplus/
$ virtualenv virt_env --python=python3
$ source virt_env/bin/activate
$ pip install gym==0.19.0
$ pip install -e .

to exit from Your virtualenv (after finished your compile) , you need to insert:
$ deactivate


# Overview

Gym-Eplus is implemented based on EnergyPlus ExternalInterface function. The EnergyPlus model should be configured based on the guidelines here (https://simulationresearch.lbl.gov/bcvtb/releases/latest/doc/manual/tit-EnePluCon.xhtml).
Create a new environment

A new environment should be registered in eplus_env/init.py file.
EnergyPlus simulation output

EnergyPlus logs its own output. The output will be stored under the directory $pwd/Eplus-env-{environment name}-res{x}/Eplus-env-sub_run{x}/output. The "sub_run" directory is the directory for each episode (each EnergyPlus simulation run period) that the environment runs.
Public attributes

    start_year: EnergyPlus simulation start year, int.
    start_mon: EnergyPlus simulation start month, int.
    start_day: EnergyPlus simulation start day of the month, int.
    start_weekday: EnergyPlus simulation start weekday, int. 0 is Monday.
    env_name: The environment name.


### Configure EnergyPlus
Gym-Eplus is implemented based on EnergyPlus ExternalInterface function. The EnergyPlus model should be configured based on the guidelines here (https://simulationresearch.lbl.gov/bcvtb/releases/latest/doc/manual/tit-EnePluCon.xhtml).

1. Under ExternalInterface, add "Ptolemy" server as the name of external interface.

2. Under ExternalInterface:Schedule, add the name of your external control (e.g., ExternalControl1), type of control (e.g., Temperature) and initial value (e.g., 25)

3. To control thermostat set point, add the name of your external control to "ThermostatSetpoint:SingleCooling"


# Usage
1. Copy EnergyPlus IDF and weather files: 
* Copy the IDF file to '/eplus_env/envs/eplus_models/demo_5z/learning/idf/'
* Copy the EPW file to '/eplus_env/envs/weather/'

2. Edit The 'variables' file: 
The 'variables' file is located at '/eplus_env/envs/eplus_models/demo_5z/learning/cfg/'. Please specify the variables to be retrived from EnergyPlus, and the variables to be sent to EnergyPlus (e.g., external control).

3. Create a new environment: Create a new environment in '/eplus_env/__init__.py' file.  This file sets the paths to: EnergyPlus, weather file, BCVTB, variables, IDF file, and specify the environment name.


# My Eplus-demo-v1 Example
You need to create one Example.py on below directory:
~/home/linux-1604/Gym-Eplus


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

# To Run
See Eplus-demo-v1
1. Make the environment, env = gym.make('environment name')
2. Reset the environment, env.reset()
3. Run the environment, env.step()
4. Save the data in a DataFrame
5. Close the environment, env.close()

You need to compile the Example.py by below command:
~/home/linux-1604/Gym-Eplus/
$python Example.py

# Output Result
 You could see Your Output Files on below Directory:
 ~/home/linux-1604/Gym-Eplus/Eplus-env-Example-resx

