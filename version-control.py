from datetime import datetime

class Age:
    def __init__(self, name: str, birthdate: str):
        self.name = name
        # تحويل النص إلى تاريخ
        self.birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
        
    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.birthdate.year
        # التأكد من أن يوم الميلاد قد حدث هذا العام أو لا
        if (today.month, today.day) < (self.birthdate.month, self.birthdate.day):
            age -= 1
        return age

# مثال على الاستخدام:
person = Age("Bandr", "2001-2-4")
print(f"{person.name} is {person.calculate_age()} years old.")
