import math

daysOfTheWeek = ("Monday", "Tuesday", "Wednesday",
                 "Thursday", "Friday", "Saturday", "Sunday")


class fixedDate:
    def __init__(self, hours, minutes, daysPassed):
        self.hours = hours
        self.minutes = minutes
        self.daysPassed = daysPassed

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


def fixDate(hours, minutes):
    """
    receives added hours and minutes from duration and
    returns a fixedDate object
    """
    newMinutes = minutes % 60
    remainderHours = math.floor(minutes/60)
    addedHours = hours + remainderHours
    daysPassed = math.floor(addedHours / 24)
    newHours = addedHours % 24
    return fixedDate(newHours, newMinutes, daysPassed)


def add_time(start, duration, day=None):
    # add duration to date, fix date and receive days passed
    temp = convertTo24h(start)
    timeArr = temp.split(":")
    durationArr = duration.split(":")
    hoursAdded = int(timeArr[0]) + int(durationArr[0])
    minutesAdded = int(timeArr[1]) + int(durationArr[1])
    fixeddate = fixDate(hoursAdded, minutesAdded)
    daysPassed = fixeddate.daysPassed
    newTime = "{}:{:0>2}".format(fixeddate.hours, fixeddate.minutes)

    # create days passed string
    daysLater = ""
    if daysPassed > 1:
        daysLater = " ({} days later)".format(daysPassed)
    if daysPassed == 1:
        daysLater = " (next day)"

    # if day parameter exists
    if day:
        newDay = ""
        try:
            print(daysOfTheWeek.index(day))
        except:
            return "Please enter a valid day of the week"

    return convertToAmPm(newTime) + daysLater


print(add_time("11:40 AM", "0:25"))  # expected = "12:05 PM"
