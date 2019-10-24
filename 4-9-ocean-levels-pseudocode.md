# Scope
Assuming the ocean's level is currently rising at about 1.8 millimeters per year, create an application that displays the number of millimeters that the ocean will have risen each year for the next 25 years.

## Sample Run
    Year		Ocean Rise (in millimeters)
    --------------------------------------------
    1 		 1.80
    2 		 3.60
    3 		 5.40
    4 		 7.20
    5 		 9.00
    6 		 10.80
    7 		 12.60
    8 		 14.40
    9 		 16.20
    10 		 18.00
    11 		 19.80
    12 		 21.60
    13 		 23.40
    14 		 25.20
    15 		 27.00
    16 		 28.80
    17 		 30.60
    18 		 32.40
    19 		 34.20
    20 		 36.00
    21 		 37.80
    22 		 39.60
    23 		 41.40
    24 		 43.20
    25 		 45.00

# Pseudocode
    START
    Set level rise constant = 1.8
    Display header
      Year		Ocean Rise (in millimeters)
      --------------------------------------------
    FOR each year from 1 to 25
      Calculate the cumulative rise in ocean level
        ocean rise = year * level rise
      Print year and ocean rise
    END
