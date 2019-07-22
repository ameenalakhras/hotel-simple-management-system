def calculate_datetime_difference(first_datetime, second_datetime):
    """
    calculates the difference between two datetime objects in minutes
    """
    difference = second_datetime - first_datetime
    difference_in_minutes = difference.total_seconds()
    return difference_in_minutes


def seconds_to_days(seconds:int):
    minute_seconds = 60
    hour_minutes = 60
    day_hours = 24

    value_in_minutes = seconds / minute_seconds
    value_in_hours = value_in_minutes / hour_minutes
    value_in_days = value_in_hours / day_hours

    return int(value_in_days)
