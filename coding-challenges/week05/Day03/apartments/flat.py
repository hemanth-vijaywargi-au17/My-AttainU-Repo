from bedroom import Bedroom
from kitchen import Kitchen
from bathroom import Bathroom


class Flat:
    def __init__(self, bed_rooms=Bedroom(), bathrooms=Bathroom(), kitchens=Kitchen()):
        self.bed_rooms = [bed_rooms]
        self.bath_rooms = [bathrooms]
        self.kitchens = [kitchens]
        self.owner_name = None
        self.current_renter = None
        self.has_parking_permission = False
        self.rent=5*self.carpet_area_sqft()

    def carpet_area_sqft(self):
        self.carpet_area = 0
        for i in range(0, len(self.bed_rooms)):
            self.carpet_area += self.bed_rooms[i].carpet_area_sqft

        for i in range(0, len(self.bath_rooms)):
            self.carpet_area += self.bath_rooms[i].area_covered_sqft

        for i in range(0, len(self.kitchens)):
            self.carpet_area += self.kitchens[i].area_covered_sqft

        return self.carpet_area

    def rent_out(self):
        if self.current_renter is None:
            print(f"Rent of the Flat : {self.rent} Per Month")
            response = input("Do you agree to pay the amount ? (yes or no) : ")
            if response == "y" or "yes" or "Yes":
                self.current_renter = input("Please Provide Your Name : ")

    def change_owner(self):
        self.owner_name = input("Enter the Name of the New owner : ")





