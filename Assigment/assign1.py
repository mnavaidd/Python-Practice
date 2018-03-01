def donuts(count):
  if count < 10:
      print("Number of donuts:", count)
  else:
      print("Numbers of donuts: many")
  return
donuts(5)
donuts(11)


def both_ends(s):
    if len(s) < 2:
        print(s)
    else:
        start = s[:2]
        last = s[-2:]
        print(start+ "" +last)
    return

both_ends("pakistan")

def greet_user(name):
    print("Hello!", name.title())
    #greet_user()

greet_user("navaid")


def describe_city(city, country="Pakistan", town="Gulshan"):
    print("I live in", town, city, country)

describe_city("Lahore")
describe_city("Washington", "America")


