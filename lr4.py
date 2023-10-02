from datetime import datetime

def days_between_dates():
    date1_str=input("Введите первую дату в формате гггг-мм-дд: ")
    date2_str = input("Введите вторую дату в формате гггг-мм-дд: ")
    date1=datetime.strptime(date1_str, '%Y-%m-%d')
    date2 = datetime.strptime(date2_str, '%Y-%m-%d')
    days_diff=abs(date2.toordinal()-date1.toordinal())
    return days_diff


print(days_between_dates())