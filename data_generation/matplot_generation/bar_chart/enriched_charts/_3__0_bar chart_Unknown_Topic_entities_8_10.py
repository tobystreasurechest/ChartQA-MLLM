
import matplotlib.pyplot as plt

# Data
dates = [
    '2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', 
    '2024-01-05', '2024-01-06', '2024-01-07', '2024-01-08', 
    '2024-01-09', '2024-01-10', '2024-01-11', '2024-01-12', 
    '2024-01-13', '2024-01-14', '2024-01-15', '2024-01-16', 
    '2024-01-17', '2024-01-18', '2024-01-19', '2024-01-20', 
    '2024-01-21', '2024-01-22', '2024-01-23', '2024-01-24', 
    '2024-01-25', '2024-01-26', '2024-01-27', '2024-01-28', 
    '2024-01-29', '2024-01-30', '2024-01-31'
]
temperatures = [
    5, 6, 4, 7, 5, 6, 4, 5, 7, 6, 5, 4, 7, 5, 
    6, 4, 7, 5, 6, 4, 7, 5, 6, 4, 7, 5, 6, 4, 
    7, 5, 6
]

# Plotting the bar chart
plt.figure(figsize=(12, 6))  # changing width and height of the chart
plt.bar(dates, temperatures, width=0.6, color=[
    '#FF5733', '#33FF57', '#3357FF', '#FF33FB', 
    '#57FF33', '#FFDA33', '#FF335E', '#33FFF6', 
    '#8B33FF', '#33FFB2', '#DAFF33', '#FF8333',
    '#FF5733', '#33FF57', '#3357FF', '#FF33FB', 
    '#57FF33', '#FFDA33', '#FF335E', '#33FFF6', 
    '#8B33FF', '#33FFB2', '#DAFF33', '#FF8333',
    '#FF5733', '#33FF57', '#3357FF', '#FF33FB', 
    '#57FF33', '#FFDA33', '#FF335E'
])  # change direction and color scheme of bars

# Customizing the plot
plt.ylabel('Temperature (°C)')
plt.title('Daily Temperatures for January 2024')  # changing topic
plt.ylim(0, 10)  # adjust the limit to better spread out the bars

# Show the plot
plt.show()