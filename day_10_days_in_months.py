month_days = [ 31, 28, 31, 30, 31, 30,
               31, 31, 30, 31, 30, 31]
def getyear():
  return int(input("Enter a year: "))

def get_month():
  return int(input("Enter a month: "))

def is_leap():
  year = getyear()
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month():
  month = get_month()-1
  leapyear = is_leap()
  if leapyear is True:
      month_days[1] = 29
  total_days_in_month =month_days[month]
  return total_days_in_month

def tela():
    days_total = days_in_month()
    print(f'The total days is {days_total} ')


def main():
    tela()

main()
