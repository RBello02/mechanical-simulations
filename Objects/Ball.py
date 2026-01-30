
# this is the object ball

class Ball:

    def __init__ (self, mass, initial_pos, initial_velocity, elasticity = None, radios = None):

        self.mass = mass

        self.radios = radios     # graphical thing

        self.x = initial_pos[0]
        self.y = initial_pos[1]

        self.vx = initial_velocity[0]
        self.vy = initial_velocity[1]

        self.elasticity = elasticity

        if len(initial_pos) == 3:    # in case 3D sim
            self.add_param(initial_pos, initial_velocity)

    def add_param(self, pos, vel):
        
        self.z = pos[2]
        self.vz = vel[2]
        