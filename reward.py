def reward_function(params):
    track_width = params['track_width']
    one_side_track_width = track_width / 2
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    is_offtrack = params['is_offtrack']
    speed = params['speed']
    progress = params['progress']
    MAX_SPEED = 3.0 # CHANGE HERE: Dependent on car

    # Initial reward
    reward = 1e-3

    # REWARDS (importance in decreasing order)
    # 1. Progress (x2)
    reward += progress/50 # Between 0 and 2

    # 2. Being close to center (x1)
    reward += (one_side_track_width-distance_from_center) / one_side_track_width

    # 3. Speed (x0.5)
    reward += (speed/MAX_SPEED) * 0.5    
        
    # PENALTIES
    # If not all wheels on track minor penalty
    if not all_wheels_on_track:
        reward = -1
    # If out of track major penalty
    if is_offtrack:
        reward = -100

    return float(reward)