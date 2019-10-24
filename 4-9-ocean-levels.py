# Program 4-9 Ocean Levels
# Shaun Hayworth
# CIS 2
# 10-24-2019
# Original source code and revision history can be found at https://github.com/SCHayworth/4-9-Ocean-Levels

# Calculates cumulative ocean rise each yar for 25 years given a rate of 1.8 millimeters per year.

# Initialize the RISE_RATE constant at 1.8
# Change this value for a different rate of ocean level rise.
RISE_RATE = 1.8

# Print header
print('''
Year		Ocean Rise (in millimeters)
--------------------------------------------
'''
    )

# Loop the calulation for each year from 1 to 25
for year in range(1, 26):

    # Calculate the ocean level rise for the current years
    ocean_level = year * RISE_RATE

    # Print the year and ocean_level
    print(f'{year:<3} {ocean_level:>20.2f}')   
