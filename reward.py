def reward_function(params):
    track_width = params['track_width']
    one_side_track_width = track_width / 2
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    is_offtrack = params['is_offtrack']
    speed = params['speed']
    progress = params['progress']
    steps = params['steps']
    MAX_SPEED = 2.0 # CHANGE HERE: Dependent on car

    # Initial reward
    reward = 1e-3

    # REWARDS (importance in decreasing order)
    # 1. Progress (x unknown)
    reward += progress/steps

    # 2. Being close to center (x2)
    reward += (one_side_track_width-distance_from_center) * 2 / one_side_track_width

    # 4. Extra benefit if all wheels on track (x1)
    if all_wheels_on_track:
        reward = +1

    # 3. Speed (x0.25)
    reward += (speed/MAX_SPEED) * 0.25
        
    # PENALTIES
    # If out of track major penalty
    #if is_offtrack:
    #    reward = -100

    return float(reward)