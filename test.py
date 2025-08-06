from pprint import pprint


class MyBox:
    def __init__(self, items):
        self.items = items  # یه لیست از آیتم‌ها

    def __iter__(self):
        return iter(self.items)  # این باعث میشه بشه روی self فور زد

    def print_items(self):
        for item in self:
            print(item)

pprint(dir(list.__itter__))