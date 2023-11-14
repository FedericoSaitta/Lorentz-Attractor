# Lorentz-Attractor:

Point class can generated the number of points (masses) needed by the user and via Animation class they can all be rendered at once 
in a single mp4 file. Rendering of mp4 is hihgly dependent on graphic capabilities of hardware, give about 2 minutes for 50 points, 2000 frames. 

## ODE SOLVER: 

Uses scipy's odeint solver, and the spacing in time inputted by the user, non-linear time spacings can be tested out to emphasize different parts of the final animations 

## Animation Class: 

Uses Matplotlib's Animation tools and blits consecutive images, ability to spin around during animation can be enabled, dark background is default and can be changed
