# this class stores the details of screen time
class ScreenSession:
    def __init__(self, name, cat, time_spent, date_time):
        self.name = name
        self.cat = cat
        self.time_spent = time_spent
        self.date_time = date_time

    # function to return a list so we can easily put it in csv
    def make_list(self):
        # converting time_spent to string just in case
        return [self.name, self.cat, str(self.time_spent), self.date_time]