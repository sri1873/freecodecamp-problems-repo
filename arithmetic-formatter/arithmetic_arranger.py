def arithmetic_arranger(problems, ans=False):
    pos = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', ' ']
    l1 = ""
    l2 = ""
    l3 = ""
    l4 = ""
    for i in problems:
        if len(problems) > 5:
            return ("Error: Too many problems.")
        if '*' in i or '/' in i:
            return ("Error: Operator must be '+' or '-'.")
        for j in i:
            if j not in pos:
                return ("Error: Numbers must only contain digits.")
        j = i.split(" ")
        fnum = j[0]
        snum = j[2]
        sign = j[1]
        if len(fnum) > 4 or len(snum) > 4:
            return ("Error: Numbers cannot be more than four digits.")

        if sign == '+':
            sol = str(int(fnum) + int(snum))
        elif sign == '-':
            sol = str(int(fnum) - int(snum))
        length = max(len(fnum), len(snum)) + 2
        fline = str(fnum).rjust(length)
        sline = sign + str(snum).rjust(length - 1)
        aline = sol.rjust(length)
        line = ""
        for s in range(length):
            line += '-'
        if i != problems[-1]:
            l1 += fline + '    '
            l2 += sline + '    '
            l3 += line + '    '
            l4 += aline + '    '
        else:
            l1 += fline
            l2 += sline
            l3 += line
            l4 += aline

    if ans:
        toprint = l1 + '\n' + l2 + '\n' + l3 + '\n' + l4
    else:
        toprint = l1 + '\n' + l2 + '\n' + l3

    return toprint
