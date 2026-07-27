
def style(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        return "***************\n" + text.upper() + "\n***************"
    return wrapper


class Report:

    templates = {}

    def __init__(self, title, content):
        self.title = title
        self.content = content


    @classmethod
    def create_template(cls, name, heading):
        cls.templates[name] = heading


    @style
    def generate(self):
        return f"{self.title}\n{self.content}"


    def __str__(self):
        return f"Report Title : {self.title}"

    
    def __add__(self, other):
        new_title = self.title + " & " + other.title
        new_content = self.content + "\n" + other.content
        return Report(new_title, new_content)



Report.create_template("Student", "Student Report")
Report.create_template("Employee", "Employee Report")

print("Available Templates")
for i in Report.templates:
    print("-", i)

print()

choice = input("Enter Template Name: ")

if choice in Report.templates:
    heading = Report.templates[choice]
else:
    heading = "General Report"

title = input("Enter Report Title: ")
content = input("Enter Report Content: ")

r1 = Report(heading + " - " + title, content)

print("\nGenerated Report")
print(r1.generate())

print("\nUsing __str__ Method")
print(r1)

print("\nCreate another report to combine")

title2 = input("Second Report Title: ")
content2 = input("Second Report Content: ")

r2 = Report(title2, content2)

combined = r1 + r2

print("\nCombined Report")
print(combined.generate())