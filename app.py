# scientific_calculator.py

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import streamlit as st

# Streamlit Interface
st.title("Scientific Graphical Calculator")

# Mathematical Functions
st.header("Mathematical Functions")
x = sp.symbols('x')

# Select function
operation = st.selectbox(
    "Select Operation:",
    ["Differentiation", "Integration", "Solve Equation", "Plot Function"]
)

if operation == "Differentiation":
    func = st.text_input("Enter function (e.g., x**2 + 3*x + 2):")
    if func:
        diff_func = sp.diff(func, x)
        st.write(f"Derivative of {func} is:")
        st.latex(sp.latex(diff_func))

elif operation == "Integration":
    func = st.text_input("Enter function (e.g., x**2 + 3*x + 2):")
    if func:
        integral_func = sp.integrate(func, x)
        st.write(f"Integral of {func} is:")
        st.latex(sp.latex(integral_func))

elif operation == "Solve Equation":
    eq = st.text_input("Enter equation to solve (e.g., x**2 - 4):")
    if eq:
        solutions = sp.solve(eq, x)
        st.write(f"Solutions to {eq} are:")
        st.write(solutions)

elif operation == "Plot Function":
    func = st.text_input("Enter function to plot (e.g., x**2 - 4):")
    x_min = st.number_input("Enter minimum value of x:", value=-10)
    x_max = st.number_input("Enter maximum value of x:", value=10)

    if func:
        x_vals = np.linspace(x_min, x_max, 500)
        y_vals = [sp.sympify(func).subs(x, val) for val in x_vals]
        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, label=f"${sp.latex(sp.sympify(func))}$")
        plt.title("Graph of the Function")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.axhline(0, color='black', linewidth=0.5, linestyle="--")
        plt.axvline(0, color='black', linewidth=0.5, linestyle="--")
        plt.legend()
        st.pyplot(plt)
