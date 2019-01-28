class Age:
    def __init__(self, year, month, day):
        self.name = name
        self.year = year
        self.month = month
        self.day = day
    def __eq__(self, other):
    	print(self, other)
    	return True if self.year == other.year else False

    def __repr__(self):
    	return f'name:{self.name} age: {self.year}-{self.month}-{self.day}'


n = Age(nima',1998,7,12)
u = age('dawa',1998,7,12)
n == u
