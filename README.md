# Multi-Agent Task allocation with LLMs

## Literature
AutoTAMP: https://yongchao98.github.io/MIT-REALM-AutoTAMP/  
SMART-LLM: https://arxiv.org/abs/2309.10062 

## TO-Do
- Try few prompts on gpt-4 LLM and log results
    - try 3/4 different tasks: area coverage, search, exploration
    - define map area in square meters
    - constraint1: number of robots
    - constraint2: time to solve task
    - constraint3: velocity of robots

## LLM features/Task Adaptation
- Chain-of-Thought Prompting
- Few-shot fine tuning
- In-context learning(ICL)
- Fine tuning with LoRA
- Function call task adaptation


## LLM Capabalities
- Task Planning with LLM
- Motion Planning with LLM
- Zero-Shot Trajectory Generators from LLM
- LLM as translators


## ROS2 LLM 
- This repository is derived from [ROS-LLM](https://github.com/Auromix/ROS-LLM). 

## Changes
- Runs locally on machine without AWS
