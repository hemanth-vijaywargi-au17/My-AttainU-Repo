from bedroom import Bedroom
from kitchen import Kitchen
from bathroom import Bathroom


class Flat:
    def __init__(self, bed_rooms, bathrooms, kitchens):
        self.bed_rooms = bed_rooms
        self.bath_rooms = bathrooms
        self.kitchens = kitchens
        self.owner_name = None
        self.current_renter = None
        self.carpet_area = self.bed_rooms.carpet_area_sqft + self.kitchens.area_covered_sqft + self.bath_rooms.area_covered_sqft

    def rent_out(self):
        if self.current_renter is None:
            print(f"Rent of the Flat : {5 * self.carpet_area} Per Month")
            response = input("Do you agree to pay the amount ? (yes or no) : ")
            if response == "y" or "yes" or "Yes":
                self.current_renter = input("Please Provide Your Name : ")

    def change_owner(self):
        self.owner_name = input("Enter the Name of the New owner : ")


my_flat = Flat(Bedroom(), Kitchen(), Bathroom())
print(f"{my_flat.carpet_area} Sqft")
