
class Date_aa:

    def __init__(self, year, month, day):

        self.year = year
        self.month = month
        self.day = day
    def __str__(self):
        return f"{self.year}/{self.month}/{self.day}"

    def tomorrow(self):
        self.day += 1

    @staticmethod
    def parse_from_string(date_str):
        year, month, day = tuple(date_str.split('-'))
        return Date_aa(int(year), int(month), int(day))

    @staticmethod
    def valid_str(date_str):
        year, month, day = tuple(date_str.split('-'))
        if int(year) > 0 and int(month) > 0 and int(month) <= 12 and int(day) >0 and int(day)<=31:
            return True
        else:
            return False

    @classmethod
    def cls_parse_from_string(cls, date_str):
        year, month, day = tuple(date_str.split('-'))
        return cls(int(year), int(month), int(day))

class User:

    def __init__(self, birthday):
        # self.birthday = birthday
        self.__birthday = birthday

    def age_get(self):
        return 2023 - self.__birthday.year


class MyClass(object):

    def foo(self, x):
        print("executing foo(%s, %s)" % (self, x))
    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s, %s)" % (cls, x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % (x))

if __name__ == "__main__":
    new_day = Date_aa(2022, 6, 30)
    print(new_day)
    new_day.tomorrow()
    print(new_day)

    date_str = '2022-06-21'

    new_day1 = Date_aa.parse_from_string(date_str)
    new_day2 = Date_aa.cls_parse_from_string(date_str)

    new_day_str = '2022-06-33'
    new_day3 = Date_aa.valid_str(new_day_str)
    print(new_day1)
    print(new_day2)
    print(new_day3)

    user_day = User(Date_aa(1990,11,20))
    print(user_day._User__birthday)
    print("The age:", user_day.age_get())

    my_class = MyClass()
    my_class.foo(new_day)
    MyClass.class_foo(new_day)
    MyClass.static_foo(new_day)

    print(my_class.foo)
    print(my_class.class_foo)
    print(my_class.static_foo)