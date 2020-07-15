import sympy as sym

class BisectionMethod():
    def __init__(self, x_upper, x_lower, n_iter=100, stopping_factor=1e-4):

        self.x_upper = x_upper
        self.x_lower = x_lower
        self.x_mid = (self.x_upper+self.x_lower)/2
        self.n_iter = n_iter
        self.stopping_factor = stopping_factor


    def find_root(self):
        
        for _ in range(self.n_iter):

            f_xl = func.evalf(subs={x: self.x_lower})
            f_xu = func.evalf(subs={x: self.x_upper})
            f_xm = func.evalf(subs={x: self.x_mid})

            print(f"xl: {self.x_lower:.4f}\txu: {self.x_upper:.4f}\txm: {self.x_mid:.4f}")
            print(f"fxl: {f_xl:.4f}\tfxu: {f_xu:.4f}\tfxm: {f_xm:.4f}\n")
            
            if self.decision(f_xl, f_xm):
                print(f"\nStopping factor reached... \nroot of function with given x_upper and x_lower: {self.x_mid:.4f}")
                return self.x_mid
                break

            print()

        return self.x_mid
    
    def decision(self, f_xl, f_xm):
        
        if f_xl * f_xm < 0:
            self.x_upper = self.x_mid

        elif f_xl * f_xm > 0:
            self.x_lower = self.x_mid

        foo = self.x_mid
        self.x_mid = (self.x_upper+self.x_lower)/2
        self.error = abs((self.x_mid - foo)/self.x_mid)*100

        if self.error <= self.stopping_factor:
            return True
            
x = sym.Symbol('x')
func = 3*(x**2) - 5*x + 1

print('-')

