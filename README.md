# AWS DeepRacer Reward Function Experimentation

These are my experimentation with [AWS DeepRacer](https://aws.amazon.com/deepracer/) training.

## Reward Functions

|Iteration|Name|Strategy| 
| :---: |:---:|:-----|
|1|["Complete"](./RewardFunctions/complete.py)|A "complete" model which considers distance_to_center, speed, and progress(exponentially) as rewards and is_offtrack as penalty.|
|2|["Centerline Following"](./RewardFunctions/line_speed_progress.py)|A version of "Complete" modal, which rewards based on distance_to_center and progress(exponentially) and decreases rewards if car goes too slow.|

### Inspirations
- [Scott Pletcher](https://github.com/scottpletcher) / [deepracer](https://github.com/scottpletcher/deepracer)

### Authors
- [Dogu Deniz Ugur(Full Stack Developer)](https://dogudenizugur.me)
