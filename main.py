from person import Person

man = Person("Василий Иванович Чапаев", 42, "6969 420420", 70.3)

print(man.fio)
print(man.age)
print(man.passport)
print(man.weight)

man.age = 34
man.weight = 144

print(man.fio)
print(man.age)
print(man.passport)
print(man.weight)

man.weight = 12