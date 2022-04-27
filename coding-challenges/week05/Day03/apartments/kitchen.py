class Kitchen:
    def __init__(self,length_ft=8, breadth_ft=10,slab_material="marble",has_sink=True,has_slab=True,furnishing_material="Wood",lpg_pipeline=True):
        self.length = length_ft
        self.breadth = breadth_ft
        self.slab_material = slab_material
        self.has_sink = has_sink
        self.has_slab = has_slab
        self.furnishing_material = furnishing_material
        self.lpg_pipeline=lpg_pipeline
        self.area_covered_sqft = int((length_ft * breadth_ft))

    def cook(self):
        if self.lpg_pipeline==True:
            print("Kitchen can be used for cooking")
        else:
            print("Kitchen unsuitable for cooking")