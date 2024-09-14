from numpy import abs, pi

class rocket_config():    
    def __init__(self) -> None:
        # Rocket Parameters with Defualt values
        self.rocket_mass_0 = 32098/1000 # kilograms
        self.drag_coeffitiant = 0.36 #cf
        self.diameter = 0.155 # meters
        self.cross_sect_area = self.cross_sect_area_calc(self.diameter)
        pass
    
    def cross_sect_area_calc(self,diameter) -> float:
        return pi*(diameter/2)**2  # meters^2 
        


class Motor():
    GRAVITY = -9.81
    
    def __init__ (self, mass_fuel, trust_avg, total_impulse, total_burn_time) -> None:
        self.mass_fuel = mass_fuel
        self.trust_avg = trust_avg
        self.total_impulse = total_impulse
        self.burn_time = total_burn_time
        self.ISP = self.spcific_impulse()
        pass
    
    def spcific_impulse(self) -> float:
        return self.total_impulse/(self.mass_fuel*abs(self.GRAVITY))
    
    def motor_output(self, t: float) -> tuple [float, float]:
        """motor_output is the returns the thrust and mass_dot

        Args:
            t (float): simulation time

        Returns:
            tuple [float, float]: f_thrust, mass_dot
        """
                        
        if (t < self.burn_time):
            f_thrust = self.trust_avg
        else:
            f_thrust = 0.0
            
        exit_velcoity = self.ISP * self.GRAVITY
        mass_dot = f_thrust/exit_velcoity
        return f_thrust, mass_dot
        
        

if __name__ == "__main__":
    # n Rocket Motor Perameters
    FuelMass = 7512.0/1000.0 # kg
    ThrustAvg = 3168.0 # F
    TotalImpulse = 14041.0 # Ns
    burn_time = 4.4 #s
    Nmotor = Motor(FuelMass, ThrustAvg, TotalImpulse, burn_time)
    
    rocket = rocket_config()
    
    
    Nmotor.f_thrust
    print(Nmotor.f_thrust(1), type(Nmotor.f_thrust(1)) )