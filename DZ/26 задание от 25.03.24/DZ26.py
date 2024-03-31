class Student:
    def __init__(self, name: str, laptop: 'Laptop'):
        self.name = name
        self.laptop = laptop

    def __str__(self) -> str:
        return f"{self.name} => {self.laptop.model}, {self.laptop.cpu}, {self.laptop.memory}"

    class Laptop:
        def __init__(self, model: str, cpu: str, memory: int):
            self.model = model
            self.cpu = cpu
            self.memory = memory


laptop1 = Student.Laptop("HP", "i7", 16)
student1 = Student("Roman", laptop1)

laptop2 = Student.Laptop("HP", "i7", 16)
student2 = Student("Vladimir", laptop2)

print(student1)
print(student2)
