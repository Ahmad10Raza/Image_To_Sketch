import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Sidebar input
st.sidebar.header("Settings")
data_range = st.sidebar.slider("Select a range:", 0.0, 10.0, (2.0, 8.0))

# Main content
st.title("Simple Streamlit App")

# Generate data based on user input
x = np.linspace(data_range[0], data_range[1], 100)
y = np.sin(x)

# Plot data
st.write("### Plot")
plt.plot(x, y)
st.pyplot(plt)
