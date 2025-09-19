import cmath

def root2(a, b, c, tol=1e-10):

    d = b**2 - 4*a*c
    sqrt_d = cmath.sqrt(d)
    
    x1 = (-b + sqrt_d) / (2*a)
    x2 = (-b - sqrt_d) / (2*a)
    
    def clean(z):

        real = 0 if abs(z.real) < tol else z.real
        imag = 0 if abs(z.imag) < tol else z.imag
        return real if imag == 0 else complex(real, imag)
    
    x1 = clean(x1)
    x2 = clean(x2)
    
    return x1, x2

def f(a, b, c, x):
    return a*x*x + b*x + c

a, b, c = 1, -3, 2    
r1, r2 = root2(a,b,c)
print("根：", r1, r2)
print("代回檢查 f(x)：", f(a,b,c,r1), f(a,b,c,r2))

a, b, c = 1, 2, 5      
r1, r2 = root2(a,b,c)
print("\n根：", r1, r2)
print("代回檢查 f(x)：", f(a,b,c,r1), f(a,b,c,r2))
