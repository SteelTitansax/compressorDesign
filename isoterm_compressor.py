# Compressor ecuations 

# -------------------------------------------------------
# -------------------------------------------------------
import numpy as np 

class Compressor:

    def __init__(self,P1,P2,Vm,R,T,Q,rho):
   
        self.P1 = P1   
        self.P2 = P2
        self.Vm = Vm
        self.R = R
        self.T = T
        self.Q = Q
        self.rho = rho

    def design(self):

        density1 = self.P1/(self.R * self.T) # air density

        print("density (kg/m3)",density1)

        m = density1 * self.Q # molar mass flow

        print("m (kg/s)",m)

        W_total = m * R * T *  np.log(P2/P1) 

        print("W total(KW)",(W_total/1000))

        P_real = (W_total / rho) 
       
        print("P real (Kw)", (P_real/1000))




if __name__ ==  "__main__" :

    P1 = 101325 # Pa
    P2 = 20268000 # Pa
    Vm = 22.414 # m3 /kmol at 1 atm 273 K
    R = 287 # J / Kg ·mol
    T = 298 # K
    Q = (15000/3600)  # m3/s
    rho = 0.97 # percentage
    compressor = Compressor(P1,P2,Vm,R,T,Q,rho)

    print("Compressor initialied ...")

    compressor.design()
