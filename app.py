!pip install streamlit
!pip install matplotlib
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title of the app
st.title("Graphical Scientific Calculator")

# Dropdown menu for selecting a mathematical operation
operation = st.selectbox(
    "Select an operation:",
    [
        "Sine (sin)",
        "Cosine (cos)",
        "Tangent (tan)",
        "Exponential (exp)",
        "Logarithm (log)",
        "Square Root (sqrt)",
        "Square (x^2)",
    ]
)

# Input fields for the range of x-values
min_x = st.number_input("Enter minimum x value:", value=-10.0, format="%.2f")
max_x = st.number_input("Enter maximum x value:", value=10.0, format="%.2f")

# Plot button with green color
plot_button = st.button("Plot", key="plot_button")

if plot_button:
    # Check if minimum x is less than maximum x
    if min_x >= max_x:
        st.error("Minimum x value should be less than maximum x value.")
    else:
        # Generate x values
        x = np.linspace(min_x, max_x, 500)

        # Compute y values based on the selected operation
        try:
            if operation == "Sine (sin)":
                y = np.sin(x)
            elif operation == "Cosine (cos)":
                y = np.cos(x)
            elif operation == "Tangent (tan)":
                y = np.tan(x)
            elif operation == "Exponential (exp)":
                y = np.exp(x)
            elif operation == "Logarithm (log)":
                y = np.log(x)
            elif operation == "Square Root (sqrt)":
                y = np.sqrt(np.maximum(x, 0))  # Prevent negative values
            elif operation == "Square (x^2)":
                y = x**2

            # Plotting
            fig, ax = plt.subplots()
            ax.plot(x, y, label=f"y = {operation}")
            ax.axhline(0, color="black", linewidth=0.5, linestyle="--")
            ax.axvline(0, color="black", linewidth=0.5, linestyle="--")
            ax.legend()
            ax.grid(True)
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.set_title(f"Graph of {operation}")
            st.pyplot(fig)

        except Exception as e:
            st.error(f"An error occurred: {e}")

