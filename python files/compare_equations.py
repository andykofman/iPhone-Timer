import sympy as sp

def compare_equations():
    # Define the variable
    x = sp.symbols('x')

    # Equation from the text
    equation_text = 64*(1-2*x)**2*(1-8*x+8*x**2)**2 - 256*x*(1-x)*(1-2*x)*(1-8*x+8*x**2)**2 + 128*x*(1-x)*(1-2*x)**2*(1-8*x+8*x**2)*(-8+16*x)
    # Equation from the image
    equation_image = 128*x*(1 - x)*(-8 + 16*x)*(1 - 2*x)**2*(1 - 8*x + 8*x**2) + 64*(1 - x)*(1 - 2*x)**2*(1 - 8*x + 8*x**2)**2 - 64*x*(1 - 2*x)**2*(1 - 8*x + 8*x**2)**2 - 256*x*(1 - x)*(1 - 2*x)*(1 - 8*x + 8*x**2)**2

    # Simplify both equations
    simplified_text = sp.simplify(equation_text)
    simplified_image = sp.simplify(equation_image)

    # Compare the simplified equations
    are_equal = sp.simplify(simplified_text - simplified_image) == 0

    return are_equal

# Run the comparison
result = compare_equations()
print("The equations are equal:" if result else "The equations are not equal.")