class Bed:
    def __init__(self, has_headboard=True, has_posts=False, material="Wood", length_of_bed_ft=6, breadth_of_bed_ft=3.5,
                 year_made=2021):
        self.length = length_of_bed_ft
        self.breadth = breadth_of_bed_ft
        self.year_made = year_made
        self.has_headboard = has_headboard
        self.has_posts = has_posts
        self.material = material
        self.area_covered_sqft = int((length_of_bed_ft * breadth_of_bed_ft))

