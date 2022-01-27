from sympy import symbols, Eq, solve

m, k = symbols('m k')

e = Eq(m *(2**k) - 560,0)

sol = solve(e,(m, k))

print(sol)