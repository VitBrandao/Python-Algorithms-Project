def study_schedule(permanence_period, target_time):
    if (permanence_period is None or target_time is None):
        return None

    counter = 0
    for period in permanence_period:
        for item in period:
            if (item is None or type(item) != int):
                return None
        if(period[0] <= target_time <= period[1]):
            counter += 1
    return counter


# estudante             1       2       3       4       5       6
# permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
# permanence_periods = [(4, None), ("0", 4)]
# print(study_schedule(permanence_periods, 5))
