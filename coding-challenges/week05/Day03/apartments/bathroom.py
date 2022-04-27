class Bathroom:
    def __init__(self, length_ft=6, breadth_ft=6, has_sink=True, has_bathtub=True,
                        has_tap=True,has_shower=True):
        self.length = length_ft
        self.breadth = breadth_ft
        self.has_sink = has_sink
        self.has_bathtub = has_bathtub
        self.has_tap=has_tap
        self.has_shower=has_shower
        self.area_covered_sqft = int((length_ft * breadth_ft))

    def bathing(self):
        if self.has_tap == True or self.has_shower ==True or self.has_bathtub ==True:
            print("Suitable for bathing")
        else:
            print("Unsuitable for bathing")