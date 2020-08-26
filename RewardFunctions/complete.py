def reward_function(params):
    distance_from_center = params['distance_from_center']
    progress = params['progress']
    speed = params['speed']
    off_track = params['is_offtrack']

    # HELPERS
    # 1. Close to center
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

    # SECONDARY: Speed
    MAX_SPEED = 4.0
    reward *= 1.0 + (speed / MAX_SPEED)

    # PUNISHMENTS
    # Going out of track
    if off_track:
        reward -= 10

    # PRIMARY: Exponential Progress Reward (One time rewards)
    progress_dict = {
        0: 0,
        10: 2,
        20: 4,
        30: 8,
        40: 16,
        50: 32,
        60: 64,
        70: 128,
        80: 256,
        90: 512,
        100: 1024
    }
    int_progress = int(progress)
    if int_progress % 10 == 0:
        try:
            reward += progress_dict[int_progress]
        except:
            pass

    return float(reward)
