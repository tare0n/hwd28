class Person:
    @staticmethod
    def verify_fio(fio):
        if not isinstance(fio, str):
            raise ValueError("fio must be string")
        if " " not in fio:
            raise ValueError("incorrect format of fio")
        list_of_names = fio.split(" ")
        for name in list_of_names:
            if not name.isalpha():
                raise ValueError("every name must contain only letters")
            if len(name) < 1:
                raise ValueError("every name must be longer, than 1")
        return True

    @staticmethod
    def verify_age(age):
        if not isinstance(age, int):
            raise ValueError("age must be int")
        if not 14 <= age <= 150:
            raise ValueError("incorrect age")
        return True

    @staticmethod
    def verify_passport(passport):
        if " " not in passport:
            raise ValueError("incorrect format of passport")
        list_of_numbers = passport.split(" ")
        if len(list_of_numbers[0]) != 4 or len(list_of_numbers[1]) != 6:
            raise ValueError("incorrect format of passport")
        for number in list_of_numbers:
            if isinstance(number, int):
                raise ValueError("series and number must be int")
        return True

    @staticmethod
    def verify_weight(weight):
        if not (isinstance(weight, int) or isinstance(weight, float)):
            raise ValueError("incorrect format of weight")
        if weight < 25.0:
            raise ValueError("incorrect weight: must be bigger than 25 kg")
        return True

    def __init__(self, fio, age, passport, weight):
        if self.verify_fio(fio):
            self.__fio = fio.split(" ")
        else:
            self.__fio = "default"

        if self.verify_age(age):
            self.__age = age
        else:
            self.__age = 0

        if self.verify_passport(passport):
            self.__passport = passport
        else:
            self.__passport = "0000 000000"

        if self.verify_weight(weight):
            self.__weight = weight
        else:
            self.__weight = 0

    @property
    def fio(self):
        return " ".join(self.__fio)

    @property
    def age(self):
        return self.__age

    @property
    def passport(self):
        return self.__passport

    @property
    def weight(self):
        return self.__weight

    @fio.setter
    def fio(self, new_fio):
        if not self.verify_fio(new_fio):
            return None
        self.__fio = new_fio.split(" ")

    @age.setter
    def age(self, new_age):
        if not self.verify_age(new_age):
            return None
        self.__age = new_age

    @passport.setter
    def passport(self, new_passport):
        if not self.verify_passport(new_passport):
            return None
        self.__passport = new_passport

    @weight.setter
    def weight(self, new_weight):
        if not self.verify_weight(new_weight):
            return None
        self.__weight = new_weight


