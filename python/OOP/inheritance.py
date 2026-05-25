# Create a class Employee that has:
# 	attributes: name, dob, age, salary, skill_sets.
# Create class Developer inheriting Employee that has:
# 	Additional  attribute: github_link, is_fullstack.
# 	method: display_profile that returns {name} has skills: s1, s2. Git: {github_link}.
# Create class HR inheriting Employee that has:
# 	Additional  attribute: is_manager, onboard_rate.
# 	method: display_profile that displays {name} has skills: s1, s2. Onboard rate: {rate}.
# 5 developers and 2 HR joined the company. Create objects for them with random attribute.
# Create list developers_list with all developer objects and list hr_list with all HR objects.
# Loop through developers_list to display developer's name with both Python and Git skill.


class Employee:
    def __init__(self, name, dob, age, salary, skill_sets):
        self.name = name
        self.dob = dob
        self.age = age
        self.salary = salary
        self.skill_sets = skill_sets


class Developer(Employee):
    def __init__(self, name, dob, age, salary, skill_sets, github_link, is_fullstack):
        super().__init__(name, dob, age, salary, skill_sets)
        self.github_link = github_link
        self.is_fullstack = is_fullstack

    def display_profile(self):
        skills = ", ".join(self.skill_sets)
        print(f"{self.name} has skills: {skills}. Git: {self.github_link}")


class HR(Employee):
    def __init__(self, name, dob, age, salary, skill_sets, is_manager, onboard_rate):
        super().__init__(name, dob, age, salary, skill_sets)
        self.is_manager = is_manager
        self.onboard_rate = onboard_rate

    def display_profile(self):
        skills = ", ".join(self.skill_sets)
        print(f"{self.name} has skills: {skills}. Onboard rate: {self.onboard_rate}")


# Creating Developer objects

dev1 = Developer(
    "John", "1998-02-10", 27, 5000, ["Python", "Git", "Django"], "github.com/john", True
)
dev2 = Developer(
    "Emma",
    "1997-07-15",
    28,
    5500,
    ["JavaScript", "React", "Git"],
    "github.com/emma",
    True,
)
dev3 = Developer(
    "Alex", "1999-01-20", 26, 4800, ["Python", "Git", "Flask"], "github.com/alex", False
)
dev4 = Developer(
    "Sophia",
    "1996-05-12",
    29,
    6000,
    ["Java", "Spring", "Git"],
    "github.com/sophia",
    True,
)
dev5 = Developer(
    "David",
    "2000-09-18",
    25,
    4500,
    ["Python", "HTML", "CSS"],
    "github.com/david",
    False,
)

# Creating HR objects

hr1 = HR("Mia", "1995-11-11", 30, 4000, ["Communication", "Recruitment"], True, 85)
hr2 = HR("Liam", "1994-03-25", 31, 4200, ["Management", "Excel"], False, 78)

# Lists
developers_list = [dev1, dev2, dev3, dev4, dev5]
hr_list = [hr1, hr2]

for dev in developers_list:
    dev.display_profile()
for hr in hr_list:
    hr.display_profile()

# print("\nDevelopers with both Python and Git skills:")

# Loop through developers_list
for dev in developers_list:
    if "Python" in dev.skill_sets and "Git" in dev.skill_sets:
        print(dev.name)
