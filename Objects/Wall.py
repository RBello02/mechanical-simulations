
# this wall doesn't move

class Wall:

    def __init__(self, dim, elasticity = None):

        self.x = dim[0]
        self.y = dim[1]
        self.elasticity = elasticity

        if len(dim) == 3:
            self.add_param(dim)

    def add_param(self,dim):
        
        self.z = dim[2]

