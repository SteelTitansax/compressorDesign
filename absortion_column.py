from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

class AbsorptionColumn:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def design(self):
        # 3rd-degree polynomial regression for equilibrium curve
        model = np.poly1d(np.polyfit(self.x, self.y, 3))
        myline = np.linspace(0, 16, 100)

        plt.plot(myline, model(myline), label="Regression curve (equilibrium data)", color='g')
        plt.ylabel('Y (mols H2O/dry air mols)')
        plt.xlabel('X (H2O mols/ NaOH mols)')
        plt.title("Example 6-16, Ocon and Tojo, Vol II")
        plt.grid()

        print("\nRegression equation for equilibrium curve:")
        print(model)
        print("\nR² = ", r2_score(self.y, model(self.x)))

        # (L/V) min - Operating line at minimum solvent flow
        x_op = [2.22, 6]
        y_op = [0.0048, 0.0126]
        model2 = np.poly1d(np.polyfit(x_op, y_op, 1))
        plt.plot(myline, model2(myline), label="(L/V)min", color='r')

        print("\nRegression equation for (L/V) min:")
        print(model2)
        print("\nR² = ", r2_score(y_op, model2(x_op)))

        # Increase flow rate by 40%
        a = np.polyfit(x_op, y_op, 1)
        new_slope = a[0] * 1.4  # Adjust slope

        # Calculate Xn for new operating line
        intercept = -0.00161358
        Y_nplus_one = 0.019
        Xn = (Y_nplus_one - intercept) / new_slope
        print("\nCalculated Xn =", Xn)

        # New operating line with increased solvent
        x_new_op = [2.22, Xn]
        y_new_op = [0.0048, Y_nplus_one]
        model2 = np.poly1d(np.polyfit(x_new_op, y_new_op, 1))
        plt.plot(myline, model2(myline), label="(L/V) operative", color="b")

        print("\nRegression equation for new operating line (40% more solvent):")
        print(model2)

        # Define f(x) and its derivative fp(x) for Newton-Raphson
        def f(x, y):
            return 6.139e-6 * x**3 - 0.0003032 * x**2 + 0.005088 * x - 0.008814 - y

        def fp(x):
            return 3 * 6.139e-6 * x**2 - 2 * 0.0003032 * x + 0.005088

        # Newton-Raphson for equilibrium stages calculation
        print("\nConcentrations at equilibrium stages:")
        print("--------------------------------------")

        i = 0
        epsilon = 0.001
        x_vals = [0]  # Initialize x values
        y_vals = [0.0048]  # Initialize y values (starting point)

        xv = 0.1
        xN = 0

        while xN <= Xn:
            xN = xv - (f(xv, y_vals[i]) / fp(xv))  # Newton-Raphson iteration
            if abs(xv - xN) > epsilon:
                xv = xN
            elif xN <= Xn:
                x_vals.append(xN)
                y_vals.append(model2(xN))  # Compute new y from the operating line equation
                print(f"Stage {i+1}: x = {xN:.4f}, y = {y_vals[i+1]:.4f}")
                i += 1

        ns = i  # Number of stages
        print("\nNumber of theoretical stages =", ns)

        i=1 
        while i<ns:
            # Horizontal
            x1=[x[i-1],x[i]]
            y1=[y[i-1],y[i]]
            plt.plot(x1,y1,color='g')
            # Vertical
            x1=[x[i],x[i]]
            print('x[',i,']=',x[i],'y[',i,']=',y[i])
            y1=[y[i],y[i+1]]
            plt.plot(x1,y1,color='r')
            i+=1
        
        if i>=ns:
            x1=[x[i-1],x[i]]
            y1=[y[i],y[i]]
            print('x[',i,']=',x[i],'y[',i,']=',y[i])
            plt.plot(x1,y1,color='g')
        
        plt.show()
        # Packed column height calculation
        HETP = 0.98  # Height Equivalent to a Theoretical Plate (m)
        HE = HETP * ns
        print("Packing height =", HE, "m")

        plt.scatter(self.x, self.y, color='black', label="Equilibrium data")
        plt.legend()
        plt.show()

if __name__ == "__main__":
    # Equilibrium data
    x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 16]
    y = [0.001, 0.0028, 0.0067, 0.01, 0.0126, 0.0142, 0.0157, 0.0170, 0.0177, 0.0190, 0.0202]

    print("Equilibrium data")
    print("----------------")
    results = list(zip(x, y))
    print(tabulate(results, headers=["H2O mols/NaOH", "H2O mols/dry air mols"]))

    absorption_column = AbsorptionColumn(x, y)
    absorption_column.design()
