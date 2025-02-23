import math

class heatExchanger:
    def __init__(self, m_air, T_air_in, T_air_out, T_cooling_flow_in, T_cooling_flow_out, m_nitrogen, D, n, L, C_p_air, C_p_nitrogen_liquid):
        # Variables set up 
        self.m_air = m_air
        self.T_air_in = T_air_in
        self.T_air_out = T_air_out
        self.T_cooling_flow_in = T_cooling_flow_in
        self.T_cooling_flow_out = T_cooling_flow_out
        self.m_nitrogen = m_nitrogen
        self.D = D
        self.n = n
        self.L = L
        self.C_p_air = C_p_air
        self.C_p_nitrogen_liquid = C_p_nitrogen_liquid

        print("Heat exchanger initial variables")
        print("--------------------------------")
        print(f"m_air: {m_air}")
        print(f"T_air_in: {T_air_in}")
        print(f"T_air_out: {T_air_out}")
        print(f"T_cooling_flow_in: {T_cooling_flow_in}")
        print(f"T_cooling_flow_out: {T_cooling_flow_out}")
        print(f"m_nitrogen: {m_nitrogen}")
        print(f"D: {D}")
        print(f"n: {n}")
        print(f"L: {L}")
        print(f"C_p_air: {C_p_air}")
        print(f"C_p_nitrogen_liquid: {C_p_nitrogen_liquid}")

    def kern_dimensioning(self, rho_air, mu_air, rho_nitrogen, mu_nitrogen):
        # Air thermic load (Q)
        Q_air = self.m_air * self.C_p_air * (self.T_air_in - self.T_air_out)
        print(f"Q_air: {Q_air} J/s")
        
        # Liquide nytrogen thermic load (Q)
        Q_nitrogen = self.m_nitrogen * self.C_p_nitrogen_liquid * (self.T_cooling_flow_out - self.T_cooling_flow_in)
        print(f"Q_nitrogen: {Q_nitrogen} J/s")
        print("------------------------")

        # LMTD calculation
        delta_T1 = self.T_air_in - self.T_cooling_flow_out  # Bigger temperature difference
        delta_T2 = self.T_air_out - self.T_cooling_flow_in  # Smaller temperature difference

        if delta_T1 > 0 and delta_T2 > 0:
            delta_T_ml = (delta_T2 - delta_T1) / math.log(delta_T2 / delta_T1)
            print(f"T Delta (LMTD): {delta_T_ml} K")
        else:
            delta_T_ml = None
            print("Error: Not valid temperatures for LMTD calculation")
        
        # Cooling refrigerant mass calculation 
        
        m_cooling = Q_air / (self.C_p_nitrogen_liquid * (self.T_cooling_flow_out - self.T_cooling_flow_in))
        print(f"required m_cooling: {m_cooling} kg/s")
        print("------------------------")

        # Dimension parameters calculation and details 

        A_tubes = self.n * 3.1416 * (self.D**2 / 4)
        print(f"Tubes area: {A_tubes} m²")
        v_air = self.m_air / (rho_air * A_tubes)
        print(f"air velocity: {v_air} m/s")
        reynolds_air = (rho_air * v_air * self.D) / mu_air
        print(f"Reynolds air: {reynolds_air}")
        f_air = 0.079 * (reynolds_air**-0.25)
        print(f"frictión factor air: {f_air}")
        delta_P_air = (f_air * self.L * rho_air * (v_air**2)) / self.D
        print(f"air pressure fall: {delta_P_air} Pa")
        print(f"air pressure fall: {delta_P_air / 101300} atm")

        # Liquide nitrogen calculation 

        v_nitrogen = self.m_nitrogen / (rho_nitrogen * A_tubes)
        reynolds_nitrogen = (rho_nitrogen * v_nitrogen * self.D) / mu_nitrogen
        f_nitrogen = 0.079 * (reynolds_nitrogen ** -0.25)
        delta_nitrogen = (f_nitrogen * self.L * rho_nitrogen * (v_nitrogen**2)) / self.D
        print(f"liquid nytrogen pressure fall: {delta_nitrogen} Pa")
        print(f"liquid nytrogen pressure fall: {delta_nitrogen / 101300} atm")

if __name__ == "__main__":
    # Heat exchanger parameters
    
    m_air = 4.93  # kg/s
    T_air_in = 298  # K
    T_air_out = 100  # K
    T_cooling_flow_in = 77  # K (phase change liquide nytrogen)
    T_cooling_flow_out = 100  # K
    m_nitrogen = 2.78  # kg/s
    D = 0.02  # m (tubes diameter )
    n = 50  # number of tubes
    L = 5  # m (exchange length)

    # Heat calorific capacity parameters
    
    C_p_air = 1005  # J/kg·K (air heat capacity)
    C_p_nitrogen_liquid = 2.9 * 1000  # J/kg·K (nytrogen liquide heat capacity J/kg·K)

    # Reynolds parameters
    
    rho_air = 1.18  # kg/m³
    mu_air = 0.0000217  # Pa·s
    rho_nitrogen = 800  # kg/m³ (nytrogen líquide density)
    mu_nitrogen = 0.00019  # Pa·s (liquide nytrógen viscosity)

    # Heat exchanger initialization
    
    heatExchanger = heatExchanger(m_air, T_air_in, T_air_out, T_cooling_flow_in, T_cooling_flow_out, m_nitrogen, D, n, L, C_p_air, C_p_nitrogen_liquid)
    heatExchanger.kern_dimensioning(rho_air, mu_air, rho_nitrogen, mu_nitrogen)


