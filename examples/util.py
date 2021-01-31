def map(val, in_min, in_max, out_min, out_max):
    return (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def calculate_wave_score(min, max):
    _ABS_MINIMUM_SWELL = 4  # ft
    _ABS_MAXIMUM_SWELL = 8  # ft

    if min < _ABS_MINIMUM_SWELL or max > _ABS_MAXIMUM_SWELL:
        return 0  # Swell outside safety criteria and therefore 

    range_score = map(max - min, 0, max, 0, 1)  # Score increases as range approaches 0 with score of 1 at 0
    print(range_score)  # Debug

    height_score = map(max, 0, _ABS_MAXIMUM_SWELL, 0, 1)  # Score increases as maximum swell aproaches absolute max swell
    print(height_score)  # Debug

    return range_score + height_score / 2  # Average of wave parameter scores

def calculate_tide_score(heights, low_tide_in_range=False):
    if low_tide_in_range:
        return 1

    return map(sum(heights)/len(heights), max(heights), min(heights), 0, 1)