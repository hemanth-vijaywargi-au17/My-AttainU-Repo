class Bed:
    def __init__(self, length_of_bed, breadth_of_bed, has_headboard, has_posts, material, year_made=2021):
        self.length = length_of_bed
        self.breadth = breadth_of_bed
        self.year_made = year_made
        self.has_headboard = has_headboard
        self.has_posts = has_posts
        self.material = material


class Closet:
    def __init__(self, length_of_bed, breadth_of_bed, height, max_capacity):
        self.length = length_of_bed
        self.breadth = breadth_of_bed
        self.height = height
        self.max_capacity = max_capacity
        self.items = []

    def store_item(self):
        self.items.append(input("Enter the item you want to store in the closet : "))

    def fetch_item(self):
        if self.items == []:
            print("Closet is Empty")
        else:
            print(self.items[-1])


class Bedroom:
    def __init__(self, length, breadth, height, has_balcony, has_window, num_lights, has_ac, has_fan,
                 num_charging_points):
        self.length = length
        self.breadth = breadth
        self.height = height
        self.bed = None
        self.closet = None
        self.has_balcony = has_balcony
        self.has_windows = has_window
        self.num_lights = num_lights
        self.has_ac = has_ac
        self.has_fan = has_fan
        self.num_charging_points = num_charging_points

    def carpet_area(self):
        return self.length * self.breadth

    def add_bed(self):
        print("--------> Add Bed")
        length_of_bed = int(input("Enter the required Length : "))
        breadth_of_bed = int(input("Enter the required Breadth : "))
        has_headboard = input("Do you want headboard on bed ? : ")
        has_posts = input("Should the bed have posts ? : ")
        material = input("What material should the bed be made of ? : ")
        self.bed = Bed(length_of_bed, breadth_of_bed, has_headboard, has_posts, material)
        print("----- A Bed was Added to the bedroom -----")

    def add_closet(self):
        print("--------> Add Closet")
        length_of_bed = int(input("Enter the required Length : "))
        breadth_of_bed = int(input("Enter the required Breadth : "))
        height = int(input("Enter the required height : "))
        max_capacity = int(input("Enter the required max_capacity : "))
        self.closet = Closet(length_of_bed, breadth_of_bed, height, max_capacity)
        print("----- A Closet was Added to the bedroom -----")

    def remove_bed(self):
        if self.bed != None:
            self.bed = None
            print("bed removed from the room")
        else:
            print("No bed found in the room")

    def remove_closet(self):
        if self.closet != None:
            self.closet = None
            print("closet removed from the room")
        else:
            print("No closet found in the room")


my_bedroom = Bedroom(15, 15, 10, True, True, 3, True, True, 3)
print(f"Carpet Area of the Bedroom = {my_bedroom.carpet_area()}")
my_bedroom.add_bed()
my_bedroom.add_closet()
print("my_bedroom Object :", my_bedroom.__dict__)
print("my_bedroom bed Object :", my_bedroom.bed.__dict__)

my_bedroom.closet.store_item()
print("my_bedroom closet items :", my_bedroom.closet.items)
print("my_bedroom closet Object :", my_bedroom.closet.__dict__)
