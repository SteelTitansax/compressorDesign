import CoolProp.CoolProp as CP

class Joule_Thompson_Valve:
    def __init__(self, gas, P_in, T_in,P_out):        
        self.gas = gas
        self.P_in = P_in
        self.T_in = T_in
        self.P_out = P_out

    def design(self):
        
        # Entry entrophy calculation
        # --------------------------------
        
        s_in = CP.PropsSI("S", "P", self.P_in, "T", self.T_in, self.gas)

        # Out temperature with constant entrophy (isentrópica expansion)
        # --------------------------------------------------------------

        T_out = CP.PropsSI("T", "P", self.P_out, "S", s_in, self.gas)

        return T_out




if __name__ ==  "__main__" :

    # Gas set up
    # --------------------------------------------

    gas = "Nitrogen"

    # Entry conditions 
    # --------------------------------------------
    # Example: 200 bar a 100 K (Nitrogen)

    P_in = 200 * 1e5  # Entry pressure in Pascals (200 bar)
    T_in = 100  # Entry Temp in Kelvin


    # Out Pressure
    # --------------------------------

    P_out = 1 * 1e5  # 1 bar in Pascales

    print("Joule-thompson valv initialied ...")

    JT_valve = Joule_Thompson_Valve(gas,P_in,T_in,P_out)

    T_out = JT_valve.design()

    # Mostrar resultados
    print(f"Temperatura de entrada: {T_in} K")
    print(f"Temperatura de salida: {T_out:.2f} K")



