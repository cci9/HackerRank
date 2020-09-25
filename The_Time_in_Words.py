def timeInWords(h, m):
    hrs = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",                "seventeen", "eighteen", "ninteen", "twenty",
            "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine"]
    num = ''
    if m == 0:
        num = num + hrs[h] + " " + "o' clock"
    if 1 <= m <= 30:
        if m == 1:
            num = num + hrs[m] + ' ' + 'minute' + ' ' + 'past' + ' ' + hrs[h]
        if m == 15:
            num = num + 'quarter' + " " + 'past' + " " + hrs[h]
        if m == 30:
            num = num + 'half' + " " + 'past' + " " + hrs[h]
        if (1< m < 30) and (m != 15):
            num = num + hrs[m] + ' ' + 'minutes' + ' ' + 'past' + ' ' + hrs[h]
    if m > 30:
        if m == 45:
            num = num + 'quarter' + ' ' + 'to' + ' ' + hrs[h + 1]
        else:
            m = 60 - m
            num = num + hrs[m] + ' ' + 'minutes' + ' ' + 'to' + ' ' + hrs[h + 1]
    return num