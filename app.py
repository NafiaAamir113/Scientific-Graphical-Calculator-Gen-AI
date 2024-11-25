import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# App title
st.title("Scientific Graphical Calculator")

# Sidebar for selecting the mathematical function
st.sidebar.header("Calculator Options")
operation = st.sidebar.selectbox(
    "Select an operation",
    ("Sin", "Cos", "Tan", "Log", "Square Root")
)

# Input fields for range of x values
st.sidebar.subheader("Set Range for x")
min_x = st.sidebar.number_input("Enter minimum x value", value=0)
max_x = st.sidebar.number_input("Enter maximum x value", value=10)

# Ensure valid range
if min_x >= max_x:
    st.error("Minimum x value must be less than maximum x value.")

# Plot button
if st.button("Plot", key="plot_button", help="Click to generate the plot"):
    x = np.linspace(min_x, max_x, 500)  # Generate x values
    
    # Calculate the selected mathematical function
    if operation == "Sin":
        y = np.sin(x)
    elif operation == "Cos":
        y = np.cos(x)
    elif operation == "Tan":
        y = np.tan(x)
    elif operation == "Log":
        y = np.log(x + 1e-9)  # Add a small constant to avoid log(0)
    elif operation == "Square Root":
        y = np.sqrt(np.abs(x))  # Handle negative x values gracefully

    # Plot the function
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=f"{operation}(x)", color="green")
    plt.title(f"{operation} Plot")
    plt.xlabel("x")
    plt.ylabel(f"{operation}(x)")
    plt.grid(True)
    plt.legend()
    
    # Display the plot
    st.pyplot(plt)

# Footer
st.markdown("---")
st.markdown("Created with ❤️ using Streamlit")
