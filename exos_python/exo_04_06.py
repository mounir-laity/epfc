def convert_secs(secs):
    years = secs // 31536000
    secs = secs - (years * 31536000)
    months = secs // (31536000 // 12)
    secs = secs - (months * 31536000 // 12)
    days = secs // 86400
    secs = secs - (days * 86400)
    hours = secs // 3600
    secs = secs - (hours * 3600)
    minutes = secs // 60
    secs = secs - (minutes * 60)
    return years, months, days, hours, minutes, secs


print(convert_secs(10))
