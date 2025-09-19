import cmath 

def root2(a, b, c):

    d = b**2 - 4*a*c

    sqrt_d = cmath.sqrt(d)
    
    x1 = (-b + sqrt_d) / (2*a)
    x2 = (-b - sqrt_d) / (2*a)
    
    return x1, x2

print(root2(1, -3, 2))
print(root2(1, 2, 5)) 
