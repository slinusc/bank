class Person:
    def __init__(self, name, age, ahv, address):
        self.address = address
        self.ahv = ahv
        self.age = age
        self.name = name
    def __repr__(self):
        return f'name: {self.name}, age: {self.age}, AHV: {self.ahv}, address: {self.address}'

    def __eq__(self, other):
        return None

if __name__ == '__main__':
    test_person = Person('Larry Page', 55, '12.4312.2354.6122', 'Silicon Valley 1')
    print(test_person)