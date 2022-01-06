

def convert_to_24(time_):
    time_f = time_.split()
    time_p = time_f[1]
    time_t = time_f[0].split(":")
    add_12 = True if (time_p == "PM" and time_t[0] != "12") or (
        time_p == "AM" and time_t[0] == "12") else False
    time_n_h = int(time_t[0])+(12 if add_12 else 0)
    return f'{time_n_h%24}:{time_t[1]}'


def convert_to_ampm(time_):
    time_f = time_.split(":")
    past = int(time_f[0]) > 11
    time_h = int(time_f[0]) % 12
    time_h = 12 if time_h == 0 else time_h
    time_p = "PM" if past else "AM"
    time_f[1] = f"{'0'*(2-len(str(time_f[1])))}{time_f[1]}"
    return f'{time_h}:{time_f[1]} {time_p}'


def convert_to_mins(time_):
    time_a = time_.split(":")
    total_mins = int(time_a[0])*60+int(time_a[1])
    return total_mins


def convert_to_time(mins):
    [mins_d, mins_h] = [24*60, 60]
    used = 0
    days = mins//mins_d
    used += days*mins_d
    hours = (mins-used) // mins_h
    used += hours*mins_h
    mins_ = (mins-used)
    return [days, hours, mins_]


def remaining_mins(time):
    mins_in_day = 60*24
    return mins_in_day - convert_to_mins(time)


def add_time(time_, time_to_add, day=None):
    day = day.capitalize() if day else False
    days_dict = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday",
                 4: "Friday", 5: "Saturday", 6: "Sunday"}
    current_day_indx = list(days_dict.values()).index(day) if day else 0
    mins_a = remaining_mins(convert_to_24(time_))
    mins_b = convert_to_mins(time_to_add)
    if not mins_b:
        return time_
    mins_b = mins_b-mins_a
    [days, hours, mins] = convert_to_time(mins_b)
    t_ = convert_to_24(time_).split(":")
    midfix = f", {days_dict[(current_day_indx+days+1)%7]}" if day else ""
    postfix = " (next day)" if (hours, mins) <= (
        int(t_[0]), int(t_[1])) else ""
    postfix = f" ({days+1} days later)" if days >= 1 else postfix
    return convert_to_ampm(f"{hours}:{mins}")+midfix+postfix
