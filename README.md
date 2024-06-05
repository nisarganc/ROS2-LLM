# Multi-Agent Task allocation with LLMs

## Literature
- AutoTAMP: https://yongchao98.github.io/MIT-REALM-AutoTAMP/  
- SMART-LLM: https://arxiv.org/abs/2309.10062  
- Co-NavGPT: https://arxiv.org/abs/2310.07937  

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
- re-prompting teqniques
- Fine tuning with LoRA
- Function call task adaptation

## LLM Capabalities
- Task Planning with LLM
- Motion Planning with LLM
- LLM as translators: AutoTAMP
- LMM as trajectory generators: https://arxiv.org/pdf/2310.11604 

## ROS2 LLM 
- This repository is derived from [ROS-LLM](https://github.com/Auromix/ROS-LLM). 
- Also includes task planning code from [smart-llm](https://github.com/SMARTlab-Purdue/SMART-LLM?tab=readme-ov-file)
- Runs locally on machine without AWS

## Commands
- cd ros2_ws
- colcon build --symlink-install   
- ros2 launch llm_bringup gpt_taskplanner.launch.py
- ros2 topic pub /llm_input_message std_msgs/msg/String "data: 'Prompt message goes here'" -1

