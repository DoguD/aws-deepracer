def reward_function(params):
    progress = params['progress']
    steps = params['steps']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    steering = params['steering_angle']
    all_wheels_on_track = params['all_wheels_on_track']
    off_track = params['is_offtrack']

    TRACK_WIDTH = params['track_width']
    # Change below based on car type
    MAX_SPEED = 2.5
    MAX_STEERING = 30.0

    # Initial reward
    reward = 0.001

    # Multipliers
    # center_distance_multiplier = 1 + (((TRACK_WIDTH / 2) - distance_from_center) / (TRACK_WIDTH / 2))  # x1
    steering_multiplier = 1 + ((MAX_STEERING - steering) / MAX_STEERING)  # x1
    speed_multiplier = (1 + (speed / MAX_SPEED)) ** 2  # Squared importance

    # Calculate reward
    if all_wheels_on_track:
        reward = (progress ** 2) / steps * steering_multiplier * speed_multiplier

    # Penalty
    '''
    if off_track:
        reward -= 10000
    '''

    return float(reward)
