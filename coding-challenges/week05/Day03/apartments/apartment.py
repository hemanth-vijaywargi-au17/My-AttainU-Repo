from flat import Flat


class Apartment:
    def __init__(self, flats, builder_name="L&t", amenities=["Gym", "Park"], parking_spots=50, number_floors=5,
                 maintenance_monthly=1000, has_elevator=True,
                 num_stairs=2, fire_safety=True):
        self.flats = flats
        self.builder_name = builder_name
        self.amenities = amenities
        self.parking_spots = parking_spots
        self.number_floors = number_floors
        self.maintenance_monthly = maintenance_monthly
        self.has_elevator = has_elevator
        self.num_stairs = num_stairs
        self.fire_safety = fire_safety

    def rent_flat(self):
        for i in range(0, len(self.flats)):
            if self.flats[i].current_renter is None:
                flat = self.flats[i]
                if self.has_elevator is True:
                    flat.rent += 500
                if self.fire_safety is True:
                    flat.rent += 500
                for i in range(1, len(self.amenities) + 1):
                    flat.rent += 500
                flat.rent += self.maintenance_monthly
                flat.rent_out()
                self.parking_spots -= 1
                print("Flat rented successfully")
                break
            else:
                print("No flats to rent out")

    def issue_parking_spot(self, flat):
        if self.parking_spots >= 1:
            flat.has_parking_permission = True
            print("Parking spot Issued")

    def revoke_parking_spot(self, flat):
        flat.has_parking_permission = False
        print("Parking spot revoked")

# NOTE :
# Pass Flats as list of flats to Apartment
# example: new_apartment = Apartment([Flat(), Flat()], "L&T", ["Gym", "Park"],.....)
