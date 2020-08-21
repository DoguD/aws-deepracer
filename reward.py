def reward_function(params):
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    SPEED_THRESHOLD = 0.5 

    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # CLOSER TO CENTRAL LINE
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track
    
    # EXTRA REWARD FOR SPEED
    if (speed - SPEED_THRESHOLD) > 0:
        reward = reward + speed + SPEED_THRESHOLD
        
    # PENALTY FOR NOT BEING ON TRACK
    if not all_wheels_on_track:
		# Penalize if the car goes off track
        reward = 1e-3

    return float(reward)