# Thermal Diffusion Simulation with Python

This project simulates the heat diffusion along a wire using the finite difference method and provides a dynamic visualization of temperature distribution over time. It includes both a line plot and a thermal map to represent the evolution of the temperature distribution.

![heat_distribution_animation](https://github.com/user-attachments/assets/eea1f554-a7c1-4d6f-a4f6-3e4865980b63)


# Project Overview
The simulation models thermal diffusion along a 1-meter-long wire divided into discrete segments. 
The wire is initially heated at one end, and the heat spreads along the wire over time. 
The temperature distribution is computed at each time step using the finite difference method. 
The project visualizes the results in two forms:

1. A line plot showing the temperature distribution along the wire.
2. A thermal map illustrating the spatial distribution of temperature along the wire.


# Parameters Setup

length: The length of the wire (1 meter).

nx: Number of divisions (discretization points).

dx: Spatial step size.

dt: Time step.

alpha: Thermal diffusivity.

total_time_steps: Number of time steps for the simulation.

# Heat Diffusion Simulation

An initial temperature distribution is created with one end of the wire heated to 100°C.

The temperature at each discretization point is updated using the finite difference method.

This process is repeated for the specified number of time steps.

# Visualization

The first plot shows the temperature distribution along the wire.

The second plot shows the thermal map (heatmap) of the wire's temperature distribution.

A colorbar is included for reference, showing temperature values.

# Customization
Adjusting the Wire Length: Modify the length variable to change the length of the wire.

Time and Space Resolution: You can change nx for more/less resolution along the wire and dt for finer/rougher time steps.

Thermal Diffusivity: Modify the alpha variable to simulate different materials with different thermal properties.
