import math

daysOfTheWeek = ("Monday", "Tuesday", "Wednesday",
                 "Thursday", "Friday", "Saturday", "Sunday")


class calculatedDate:
    def __init__(self, hours, minutes):
        remainderHours = math.floor(minutes/60)
        addedHours = hours + remainderHours
        self.minutes = minutes % 60
        self.daysPassed = math.floor(addedHours / 24)
        self.hours = addedHours % 24

    def __str__(self) -> str:
        return "{{{}, {}, {}}}".format(self.hours, self.minutes, self.daysPassed)


def convertToAmPm(time):
    arr = time.split(":")
    hours = int(arr[0])
    if hours >= 12:
        hours = 12 if hours == 0 or hours == 12 else hours - 12
        return "{}:{} PM".format(str(hours), arr[1])
    else:
        hours = 12 if hours == 0 else hours
        return "{}:{} AM".format(str(hours), arr[1])


def convertTo24h(time):
    arr = time.split(" ")
    newTime = ""
    hhmm = arr[0].split(":")
    if 'PM' in arr[1]:
        hours = str(int(hhmm[0])+12)
        newTime = hours + ":" + hhmm[1]
    else:
        newTime = arr[0]
    return newTime


def add_time(start, duration, day=None):
    # add duration to date, fix date and receive days passed
    temp = convertTo24h(start)
    timeArr = temp.split(":")
    durationArr = duration.split(":")

    # adds the duration to the start hours and minutes
    hoursAdded = int(timeArr[0]) + int(durationArr[0])
    minutesAdded = int(timeArr[1]) + int(durationArr[1])

    # calculates the time and days passed
    d = calculatedDate(hoursAdded, minutesAdded)
    daysPassed = d.daysPassed
    newTime = "{}:{:0>2}".format(d.hours, d.minutes)

    # create days passed string
    daysLater = ""
    if daysPassed > 1:
        daysLater = " ({} days later)".format(daysPassed)
    if daysPassed == 1:
        daysLater = " (next day)"

    # if day parameter exists
    endDay = ""
    if day:
        startDayIndex = daysOfTheWeek.index(day.title())
        endDayIndex = (startDayIndex + daysPassed) % 7
        endDay = ", {}".format(daysOfTheWeek[endDayIndex])

    return convertToAmPm(newTime) + endDay + daysLater


# "6:18 AM, Monday (20 days later)"
print(add_time("8:16 PM", "466:02", "tuesday"))
