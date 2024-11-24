# scientific_calculator.py

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import streamlit as st

# Streamlit Interface
st.title("Scientific Graphical Calculator")

# Sidebar for Navigation
st.sidebar.title("Calculator Options")
operation = st.sidebar.selectbox(
    "Select Operation:",
    ["Differentiation", "Integration", "Solve Equation", "Plot Function"]
)

# Define the variable for symbolic math
x = sp.symbols('x')

if operation == "Differentiation":
    st.header("Differentiation")
    func = st.text_input("Enter a function of x (e.g., x**2 + 3*x + 2):")
    if func:
        try:
            diff_func = sp.diff(func, x)
            st.write(f"Derivative of `{func}`:")
            st.latex(sp.latex(diff_func))
        except Exception as e:
            st.error(f"Invalid input. Please ensure the function is correctly formatted. Error: {e}")

elif operation == "Integration":
    st.header("Integration")
    func = st.text_input("Enter a function of x (e.g., x**2 + 3*x + 2):")
    if func:
        try:
            integral_func = sp.integrate(func, x)
            st.write(f"Integral of `{func}`:")
            st.latex(sp.latex(integral_func))
        except Exception as e:
            st.error(f"Invalid input. Please ensure the function is correctly formatted. Error: {e}")

elif operation == "Solve Equation":
    st.header("Solve Equation")
    eq = st.text_input("Enter an equation to solve (e.g., x**2 - 4):")
    if eq:
        try:
            solutions = sp.solve(eq, x)
            st.write(f"Solutions to `{eq}`:")
            st.write(solutions)
        except Exception as e:
            st.error(f"Invalid input. Please ensure the equation is correctly formatted. Error: {e}")

elif operation == "Plot Function":
    st.header("Plot Function")
    func = st.text_input("Enter a function of x to plot (e.g., x**2 - 4):")
    x_min = st.number_input("Enter minimum value of x:", value=-10.0, step=1.0)
    x_max = st.number_input("Enter maximum value of x:", value=10.0, step=1.0)

    if func:
        try:
            x_vals = np.linspace(x_min, x_max, 500)
            func_expr = sp.lambdify(x, sp.sympify(func), modules=["numpy"])
            y_vals = func_expr(x_vals)

            # Plotting
            plt.figure(figsize=(8, 6))
            plt.plot(x_vals, y_vals, label=f"${sp.latex(sp.sympify(func))}$")
            plt.title("Graph of the Function")
            plt.xlabel("x")
            plt.ylabel("y")
            plt.axhline(0, color='black', linewidth=0.5, linestyle="--")
            plt.axvline(0, color='black', linewidth=0.5, linestyle="--")
            plt.legend()
            st.pyplot(plt)
        except Exception as e:
            st.error(f"Invalid input or range. Please ensure the function is correctly formatted. Error: {e}")

