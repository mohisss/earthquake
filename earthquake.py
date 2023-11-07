# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the data from the text files into a DataFrame
data = {}
for file, name in [('RSN4464_L-AQUILA_EI160YLN.txt', '64'), ('RSN4488_L-AQUILA_BU012YLN.txt', '88'), ('RSN4473_L-AQUILA_EB150YLN.txt', '73'), ('RSN4466_L-AQUILA_BY003YLN.txt', '66'), ('RSN4486_L-AQUILA_QI081YLN.txt', '86')]:
    # Read the data from the text file into a DataFrame
    df = pd.read_csv(file, header=None, names=['data'], delim_whitespace=True)
    # Store the data in a dictionary with the name as the key
    data[name] = df['data'].to_numpy()##دیتاهامون میره تو ماتریس

# Calculate the cumulative sum
speed = {} ##سرعت
dis = {} ##تغییرمکان
for name in data:
    # Calculate the speed by taking the cumulative sum of the acceleration data and multiplying by 0.005
    speed[name] = np.cumsum(data[name]) * 0.005
    # Calculate the displacement by taking the cumulative sum of the speed data and multiplying by 0.005
    dis[name] = np.cumsum(speed[name]) * 0.005 ##dt=0.005

# Create subplots for each dataset
for name in data:
    # Create a figure with 3 subplots, one for each type of data (acceleration, speed, displacement)
    fig, axs = plt.subplots(3, 1, figsize=(10, 18))

    # Plot the acceleration data on the first subplot
    axs[0].plot(data[name])
    axs[0].set_xlabel('Time (s)')
    axs[0].set_ylabel('Acceleration')
    axs[0].set_title('Acceleration/Time')

    # Plot the speed data on the second subplot
    axs[1].plot(speed[name])
    axs[1].set_xlabel('Time (s)')
    axs[1].set_ylabel('Speed')
    axs[1].set_title('Speed/Time')

    # Plot the displacement data on the third subplot
    axs[2].plot(dis[name])
    axs[2].set_xlabel('Time (s)')
    axs[2].set_ylabel('Displacement')
    axs[2].set_title('Displacement/Time')

# Show the plots
plt.show()
