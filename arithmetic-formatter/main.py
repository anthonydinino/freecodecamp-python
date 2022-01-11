import re


def errorHandler(problems):
    if len(problems) > 5:
        return "Error: Too many problems."
    for strEquation in problems:
        equation = strEquation.split(" ")
        if (len(equation[0]) > 4 or len(equation[2]) > 4):
            return "Error: Numbers cannot be more than four digits."
        if equation[1] != "+" and equation[1] != "-":
            return "Error: Operator must be '+' or '-'."
        if not (re.search('^\d+$', equation[0]) and re.search('^\d+$', equation[2])):
            return "Error: Numbers must only contain digits."
    return ""


def getMaxDigits(values):
    maxValue = len(values[0])
    for value in values:
        if(len(value) > maxValue):
            maxValue = len(value)
    return maxValue


def arithmetic_arranger(problems, answer=False):
    error = errorHandler(problems)
    if error:
        return error

    gap = 4 * " "
    firstRow = secondRow = dashedRow = answerRow = ""
    maxWidths = []

    for i, strEquation in enumerate(problems):
        notLastEquation = i != len(problems)-1
        equation = strEquation.split(" ")
        maxWidths.append(getMaxDigits(equation) + 2)
        firstRow += '{:>{width}}'.format(
            equation[0], width=maxWidths[i]) + \
            (gap if notLastEquation else "")
        secondRow += '{}{:>{width}}'.format(
            equation[1], equation[2], width=maxWidths[i]-1) + \
            (gap if notLastEquation else "")
        dashedRow += "-" * maxWidths[i] + \
            (gap if notLastEquation else "")
        if answer:
            result = int(equation[0]) + int(equation[2]) if equation[1] == "+" \
                else int(equation[0]) - int(equation[2])
            answerRow += '{:>{width}}'.format(result, width=maxWidths[i]) + \
                (gap if notLastEquation else "")

    resultString = "\n".join([firstRow, secondRow, dashedRow])
    if answer:
        resultString += "\n" + answerRow
    return resultString


print(arithmetic_arranger(
    ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
