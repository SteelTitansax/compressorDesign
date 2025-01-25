# Compressor ecuations 

# -------------------------------------------------------
# -------------------------------------------------------

class Compressor:

    def __init__(self,P1,P2,k,R,T1,Q,rho,n):
   
        self.P1 = P1   
        self.P2 = P2
        self.k = k
        self.R = R
        self.T1 = T1
        self.Q = Q
        self.rho = rho
        self.n = n 

    def design(self):

        density1 = self.P1/(self.R * self.T1) # air density

        print("density",density1)

        m = density1 * self.Q # molar mass flow

        print("m",m)

        Rp_stages = (self.P2/self.P1) ** (1/self.n)
        
        print(Rp_stages)

        Rp_stages_k_1_k = Rp_stages ** ((self.k-1)/self.k)
    
        print(Rp_stages_k_1_k)

        W_etapa = (self.k/(self.k-1)) * self.R * self.T1 * ( Rp_stages_k_1_k - 1 )

        print(W_etapa)

        W_total = W_etapa * n 

        print(W_total)

        P_real = ( W_total * m ) / ( rho * 1000 ) 
       
        print(P_real)




if __name__ ==  "__main__" :

    P1 = 101325 # Pa
    P2 = 20268000 # Pa
    k = 1.4 # Specific heat coefitient
    R = 287 # J / Kg ·mol
    T1 = 298 # K
    Q = 4.167 # m3/h
    n = 3 #  number of stages 
    rho = 0.85 # efficciency coeffitient
    compressor = Compressor(P1,P2,k,R,T1,Q,rho,n)

    print("Compressor initialied ...")

    compressor.design()
