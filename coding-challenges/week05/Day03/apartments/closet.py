class Closet:
    def __init__(self, length_ft=6, breadth_ft=2, height_ft=8,max_capacity=20):
        self.length = length_ft
        self.breadth = breadth_ft
        self.height = height_ft
        self.items = []
        self.max_capacity=max_capacity
        self.area_covered_sqft=length_ft*breadth_ft

    def store_item(self):
        self.items.append(input("Enter the item you want to store in the closet : "))

    def fetch_item(self):
        if self.items == []:
            print("Closet is Empty")
        else:
            print(self.items[-1])

