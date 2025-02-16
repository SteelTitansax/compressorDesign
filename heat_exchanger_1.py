


class heatExchanger:
    def __init__(self,m_air,T_air_in,T_air_out,T_cooling_flow_in,T_cooling_flow_out,Q_water,D,n,L,cp_fluid_to_refrigerate):

        self.m_air = m_air
        self.T_air_in = T_air_in
        self.T_air_out = T_air_out
        self.T_coolin_flow_in = T_coolin_flow_in
        self.T_coolin_flow_out = T_coolin_flow_out
        self.m_water = m_water
        self.D = D
        self.n = n
        self.L = L
        self.cp_fluid_to_refrigerate = cp_fluid_to_refrigerate

        print("Heat exchanger initial variables")
        print("--------------------------------")
        print("--------------------------------")
        print("m_air",m_air)
        print("T_air_in",T_air_in)
        print("T_air_out",T_air_out)
        print("T_coolin_flow_in",T_coolin_flow_in)
        print("T_coolin_flow_out",T_coolin_flow_out)
        print("Q_water",Q_water)
        print("D",D)
        print("n",n)
        print("L",L)

    def kern_dimensioning(self,rho_air,mu_air,rho_water):

        # Air speed calculation 
        # ----------------------------------------

        A_tubes = self.n * 3.1416 * (D**2/4)

        print("A tubes",A_tubes)
        print("-------------------")

        v_air = m_air/ ( rho_air * A_tubes )

        print("V air",v_air)
        print("-------------------")

        # Reynolds calculation
        # ----------------------------------------

        reynolds_air = (rho_air * v_air * D) / mu_air
 
        print("Reynolds air",reynolds_air)
        print("----------------------------")

        # Air friction factor 
        # ----------------------------------------

        f_air = 0.079 * (reynolds_air**-0.25)
        
        print("f air",f_air)
        print("---------------------------")
        
        # Pressure air fall 
        # ----------------------------------------

        delta_P_air = (f_air * L * rho_air * (v_air**2))/D

        print("Delta_P Pa",delta_P_air)
        print("----------------------------")

        print("Delta-P Bar",delta_P_air/101300)
        print("------------------------------")

        # Speed water calculation 
        # ----------------------------------------

        v_water = m_water / (rho_water * A_tubes) 
        
        print("v water :", v_water)
        print("------------------------------")

        reynolds_water = (rho_water * v_water * D)/ mu_water 

        print("reynolds water :", reynolds_water)
        print("--------------------------------")

        f_water = 0.079 * (reynolds_water ** -0.25)

        print("f water", f_water)
        print("--------------------------------")

        delta_water = (f_water * L * rho_water * (v_water**2)) / D

        print("Delta water Pa", delta_water)
        print("--------------------------------")

        print("Delta water Atm", delta_water/101300)
        print("-----------------------------------")

        Q = m_air * self.cp_fluid_to_refrigerate * (T_air_in - T_air_out)     

        print("Heat Exchanged Q (Kj) : ", Q/1000)
        print("-----------------------------------")   

if __name__ == "__main__":

    # Heath exchanger dimensioning using kern method 
    # ----------------------------------------------
    
    # Note : We consider that air speed does not change when temperature fall down 
    # ----------------------------------------------------------------------------

    # General Parameters
    # ----------------------------------------------

    m_air = 4.93 # kg/s
    T_air_in = 298 # Kº
    T_air_out = 100 # Cº
    T_coolin_flow_in = 25 + 273 # Kº
    T_coolin_flow_out = 35 + 273 # Kº
    m_water = 2.78 # kg/s
    D = 0.02 # m (tubes diameter) 
    n = 50 # (number of tubes)
    L = 5 # m (heath exchanger length)
    cp_fluid_to_refrigerate = 1005 # J/(Kg·K)

    # Reynolds parameters 
    # ---------------------------------------------

    rho_air = 1.18 # kg /m3 at 150 Cº
    mu_air = 0.0000217 # Pa * s
    rho_water = 997 # kg/m3
    mu_water = 0.00089

    heatExchanger = heatExchanger(m_air,T_air_in,T_air_out,T_coolin_flow_in,T_coolin_flow_out,m_water,D,n,L,cp_fluid_to_refrigerate)

    heatExchanger.kern_dimensioning(rho_air,mu_air,rho_water)






