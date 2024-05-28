from dataclasses import dataclass


@dataclass
class Vacancy:
    id:str
    name: str
    salary_min: float
    salary_max: float
    url: str

    def __init__(self,id,name,salary_min,salary_max,url):
        self.id = id
        self.name = name
        self.salary_min = float(salary_min)
        self.salary_max = float(salary_max)
        self.url = url

    def is_valid(self):
        if self.salary_min + self.salary_max: return True
        return False

    def __eq__(self, other):
        return self.salary_min + self.salary_max == other.salary_min + other.salary_max

    def __ne__(self, other):
        return self.salary_min + self.salary_max != other.salary_min + other.salary_max

    def __gt__(self, other):
        return self.salary_min + self.salary_max > other.salary_min + other.salary_max

    def __ge__(self, other):
        return self.salary_min + self.salary_max >= other.salary_min + other.salary_max

    def __lt__(self, other):
        return self.salary_min + self.salary_max < other.salary_min + other.salary_max

    def __le__(self, other):
        return self.salary_min + self.salary_max <= other.salary_min + other.salary_max

