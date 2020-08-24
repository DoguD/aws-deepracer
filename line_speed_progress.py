def reward_function(params):
    distance_from_center = params['distance_from_center']
    progress = params['progress']
    on_track = params["all_wheels_on_track"]
    '''
    Example that penalizes slow driving. This create a non-linear reward function so it may take longer to learn.
    '''

    # Calculate 3 marks that are farther and father away from the center line
    marker_1 = 0.1 * params['track_width']
    marker_2 = 0.25 * params['track_width']
    marker_3 = 0.5 * params['track_width']

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track

    # penalize reward for the car taking slow actions
    # speed is in m/s
    # we penalize any speed less than 0.5m/s
    SPEED_THRESHOLD = 1.0
    if params['speed'] < SPEED_THRESHOLD:
        reward *= 0.5

    # Experimental (Huge Boost for progress)
    progress_dict = {
        10: 10,
        20: 20,
        30: 40,
        40: 80,
        50: 160,
        60: 320,
        70: 640,
        80: 1280,
        90: 2560,
        100: 5120
    }
    int_progress = int(progress)
    if int_progress % 10 == 0:
        try:
            reward += progress_dict[int_progress]
        except:
            pass
    return float(reward)
