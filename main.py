import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Setting up font properties for the plot
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
plt.rcParams["font.size"] = "10"

# Parameters for the simulation
length = 1.0  # Length of the wire in meters
nx = 50  # Number of divisions (discretization points)
dx = length / nx  # Spatial step size
dt = 0.01  # Time step in seconds
alpha = 0.01  # Thermal diffusivity (m^2/s)
total_time_steps = 500  # Total number of time steps

# Initial temperature distribution (wire starts at 0°C except for one end)
temperature = np.zeros(nx)
temperature[0] = 100  # One end of the wire is heated to 100°C

# A list to store the temperature distribution at each time step
temperatures_over_time = [temperature.copy()]

# Time loop for thermal diffusion simulation
for _ in range(total_time_steps):
    new_temperature = temperature.copy()  # Make a copy of the current temperature distribution
    for i in range(1, nx - 1):  # Iterating over the wire (ignoring the boundaries)
        # Applying the heat diffusion equation (finite difference method)
        new_temperature[i] = temperature[i] + alpha * dt / dx ** 2 * (
                    temperature[i - 1] - 2 * temperature[i] + temperature[i + 1])
    temperature = new_temperature.copy()  # Update the temperature distribution
    temperatures_over_time.append(temperature)  # Store the updated temperature distribution

# Visualization setup
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 7))  # Creating two subplots

# Plot the temperature distribution along the wire
line, = ax1.plot(np.linspace(0, length, nx), temperatures_over_time[0], color='blue', label="Temperature")
time_text = ax1.text(0.8, 90, '', fontsize=12, color='blue')  # Text displaying the current time

# Setting axis limits and labels
ax1.set_ylim(0, 100)  # Temperature axis (°C)
ax1.set_xlim(0, length)  # Length axis (m)
ax1.set_xlabel("Length of the Wire (m)")  # X-axis label
ax1.set_ylabel("Temperature (°C)")  # Y-axis label
ax1.set_title("Temperature Distribution Along the Wire Over Time")  # Title for the plot

# Thermal map visualization (Heatmap) of the wire's temperature distribution
thermal_map = ax2.imshow(np.tile(temperatures_over_time[0], (1, 1)), cmap='coolwarm', aspect='auto', origin='lower')
ax2.set_xlim(0, nx)  # Adjusting the x-axis limits for the heatmap
ax2.set_title("Thermal Map of the Wire")  # Title for the thermal map

# Hide the axis for the thermal map to focus on the colors
ax2.set_xticks([])  # Hiding the X-axis ticks
ax2.set_yticks([])  # Hiding the Y-axis ticks

# Adding a color bar to indicate temperature values
cbar = fig.colorbar(thermal_map, ax=ax2, orientation='horizontal')
cbar.set_label('Temperature (°C)')  # Label for the color bar

# Move the colorbar label higher and adjust position of the colorbar
cbar.set_label('Temperature (°C)', fontsize=12, labelpad=25)  # Adjust the label position
cbar.ax.tick_params(axis='x', direction='in', length=5)  # Adjusting tick parameters
cbar.ax.set_position([0.1, 0.35, 0.8, 5])

# Adjust the position and size of the bottom plot (thermal map)
fig.subplots_adjust(hspace=0.4)  # Increase the space between the two subplots
ax2.set_position([0.1, 0.25, 0.8, 0.15])  # Reducing the height of the thermal map plot

# Adding a legend for the thermal map and adjusting its position

# Remove axis lines from plot
ax2.set_frame_on(False)

# Function to update the plot for each frame in the animation
def animate(i):
    # Update the line plot with the temperature distribution at the current time step
    line.set_ydata(temperatures_over_time[i])
    time_text.set_text(f'Time: {i * dt:.2f} s')  # Update the time text

    # Update the thermal map with the temperature distribution for the current time step
    thermal_map.set_array(np.tile(temperatures_over_time[i], (1, 1)))

    return line, time_text, thermal_map

# Create the animation by updating the plot for each time step
ani = FuncAnimation(fig, animate, frames=len(temperatures_over_time), interval=50, blit=True)

# Display the animation in the window
plt.show()

# Save the animation as a GIF
ani.save("heat_distribution_animation.gif", writer=PillowWriter(fps=20))  # Saving the animation with 20 frames per second
