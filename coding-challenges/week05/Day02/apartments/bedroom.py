from bed import Bed
from closet import Closet


class Bedroom:
    def __init__(self, length_ft=12, breadth_ft=12, height_ft=9, has_balcony=True, has_window=True, num_lights=3,
                 has_ac=True, has_fan=True,
                 num_charging_points=3):
        self.length = length_ft
        self.breadth = breadth_ft
        self.height = height_ft
        self.bed = None
        self.closet = None
        self.has_balcony = has_balcony
        self.has_windows = has_window
        self.num_lights = num_lights
        self.has_ac = has_ac
        self.has_fan = has_fan
        self.num_charging_points = num_charging_points
        self.carpet_area_sqft = self.length * self.breadth

    def carpet_area(self):
        print(f"Current Carpet Area of the bedroom = {self.carpet_area_sqft} Sqft")
        print()

    def add_bed(self):
        print("--------> Add Bed")
        length_of_bed_ft = int(input("Enter the required Length_ft : "))
        breadth_of_bed_ft = int(input("Enter the required Breadth_ft : "))
        has_headboard = input("Do you want headboard on bed ? : ")
        has_posts = input("Should the bed have posts ? : ")
        material = input("What material should the bed be made of ? : ")
        if length_of_bed_ft * breadth_of_bed_ft <= self.carpet_area_sqft:
            self.bed = Bed(has_headboard, has_posts, material, length_of_bed_ft, breadth_of_bed_ft)
            self.carpet_area_sqft = self.carpet_area_sqft - self.bed.area_covered_sqft
            print("----- A Bed was Added to the bedroom -----")
            print()
        else:
            print("----- Cannot Add Bed, the Room has no more Space Available -----")


    def add_closet(self):
        print("--------> Add Closet")
        length_of_closet_ft = int(input("Enter the required Length : "))
        breadth_of_closet_ft = int(input("Enter the required Breadth : "))
        height_ft = int(input("Enter the required height : "))
        if height_ft>self.height:
            print("----- Closet too high for the Room -----")
        else:
            if length_of_closet_ft * breadth_of_closet_ft <= self.carpet_area_sqft:
                self.closet = Closet(length_of_closet_ft, breadth_of_closet_ft, height_ft)
                self.carpet_area_sqft = self.carpet_area_sqft - self.closet.area_covered_sqft
                print("----- A Closet was Added to the bedroom -----")
                print()
            else:
                print("----- Cannot Add Closet, the Room has no more Space Available -----")


    def remove_bed(self):
        if self.bed is not None:
            self.carpet_area_sqft = self.carpet_area_sqft + self.bed.area_covered_sqft
            self.bed = None
            print("----- The bed was removed from the room -----")
        else:
            print("----- No bed found in the room -----")
        print()

    def remove_closet(self):
        if self.closet is not None:
            self.carpet_area_sqft = self.carpet_area_sqft + self.closet.area_covered_sqft
            self.closet = None
            print("----- closet removed from the room -----")
        else:
            print("----- No closet found in the room -----")
        print()