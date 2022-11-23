class School:
    def __init__(self, name, location, enrollment):
        self.name = name
        self.location = location
        self.enrollment = enrollment
        School.num_of_schools += 1

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def get_enrollment(self):
        return self.enrollment

    @classmethod
    def get_num_of_schools(cls):
        return cls.num_of_schools


if __name__ == "__main__":
    school1 = School("Pine Ridge High School", "Omaha, NE", 1000)
    school2 = School("Central High School", "Omaha, NE", 1500)
    school3 = School("South High School", "Lincoln, NE", 2000)

    print("There are {} schools".format(School.get_num_of_schools()))