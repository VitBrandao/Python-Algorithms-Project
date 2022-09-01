def study_schedule(permanence_period, target_time):
    counter = 0
    if (target_time is None):
        return None

    for entry, leave in permanence_period:
        not_valid_entry = entry is None or type(entry) != int
        not_valid_leave = leave is None or type(leave) != int

        if (not_valid_entry or not_valid_leave):
            return None

        if (entry <= target_time <= leave):
            counter += 1
    return counter


# estudante             1       2       3       4       5       6
# permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
# permanence_periods = [(4, None), ("0", 4)]
# print(study_schedule(permanence_periods, 5))
