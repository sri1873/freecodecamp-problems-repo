def add_time(start, duration, day=False):
    days = [
        "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
        "Saturday"
    ]
    days_dict = {
        "Sunday": 0,
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6
    }
    amorpm = start.split(' ')[1]
    timestart = start.split(' ')[0]
    hstart = int(timestart.split(':')[0])
    mstart = int(timestart.split(':')[1])
    hduration = int(duration.split(':')[0])
    mduration = int(duration.split(':')[1])
    num_days = int(int(hduration) / 24)
    am_pm = {"PM": "AM", "AM": "PM"}
    mnow = mstart + mduration
    if mnow >= 60:
        mnow -= 60
        hstart += 1
    hnow = (hstart + hduration) % 12
    if mnow <= 9:
        mnow = "0" + str(mnow)
    else:
        mnow = mnow
    hnow = hnow = 12 if hnow == 0 else hnow
    if amorpm == "PM" and hstart + (hduration % 12) >= 12:
        num_days += 1
    a_p_count = int(hstart + hduration) // 12
    if a_p_count%2 ==1:
        amorpm = am_pm[amorpm]
    else:
      amorpm=amorpm
    timenow = (str(hnow) + ':' + str(mnow) + ' ' + str(amorpm))
    if (day):
        day = day.capitalize()
        index = int((days_dict[day]) + num_days) % 7
        daynow = days[index]
        timenow += ', ' + daynow
    if num_days == 1:
        timenow += " " + "(next day)"
    elif num_days > 1:
        timenow += " " + "(" + str(num_days) + " days later)"

    return timenow
