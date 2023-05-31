import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

#Read the CSV files of cylinder embers
df1 = pd.read_csv('C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/Ember 1 post-processing/Particles_Tracking_Ember_1/Particle_tracking_XY_plane/plotXY_Cylinder_Ember1_small_distance.csv', skiprows=0)
df2 = pd.read_csv('C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/Ember 1 post-processing/Particles_Tracking_Ember_1/Particle_tracking_XY_plane/plotXY_Cylinder_Ember2_small_distance.csv', skiprows=0)
df3 = pd.read_csv('C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/Ember 1 post-processing/Particles_Tracking_Ember_1/Particle_tracking_XY_plane/plotXY_Cylinder_Ember3_medium_distance.csv', skiprows=0)
df4 = pd.read_csv('C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/Ember 1 post-processing/Particles_Tracking_Ember_1/Particle_tracking_XY_plane/plotXY_Cylinder_Ember4_medium_distance.csv', skiprows=0)
df5 = pd.read_csv('C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/Ember 1 post-processing/Particles_Tracking_Ember_1/Particle_tracking_XY_plane/plotXY_Cylinder_Ember5_medium_distance.csv', skiprows=0)
df6 = pd.read_csv('C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/Ember 1 post-processing/Particles_Tracking_Ember_1/Particle_tracking_XY_plane/plotXY_Cylinder_Ember6_long_distance.csv', skiprows=0)
df7 = pd.read_csv('C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/Ember 1 post-processing/Particles_Tracking_Ember_1/Particle_tracking_XY_plane/plotXY_Cylinder_Ember7_long_distance.csv', skiprows=0)
df8 = pd.read_csv('C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/Ember 1 post-processing/Particles_Tracking_Ember_1/Particle_tracking_XY_plane/plotXY_Cylinder_Ember8_long_distance.csv', skiprows=0)

#Read the CSV files of Sphere embers
df9 = pd.read_csv('C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/Ember 2 post-processing/Particle_Tracking_Ember_2/Particle_tracking_XY_plane/plotXY_Sphere_Ember1_small_distance.csv', skiprows=0)
df10 = pd.read_csv('C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/Ember 2 post-processing/Particle_Tracking_Ember_2/Particle_tracking_XY_plane/plotXY_Sphere_Ember2_small_distance.csv', skiprows=0)
df11 = pd.read_csv('C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/Ember 2 post-processing/Particle_Tracking_Ember_2/Particle_tracking_XY_plane/plotXY_Sphere_Ember3_medium_distance.csv', skiprows=0)
df12 = pd.read_csv('C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/Ember 2 post-processing/Particle_Tracking_Ember_2/Particle_tracking_XY_plane/plotXY_Sphere_Ember4_medium_distance.csv', skiprows=0)
df13 = pd.read_csv('C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/Ember 2 post-processing/Particle_Tracking_Ember_2/Particle_tracking_XY_plane/plotXY_Sphere_Ember5_medium_distance.csv', skiprows=0)
df14 = pd.read_csv('C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/Ember 2 post-processing/Particle_Tracking_Ember_2/Particle_tracking_XY_plane/plotXY_Sphere_Ember6_long_distance.csv', skiprows=0)
df15 = pd.read_csv('C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/Ember 2 post-processing/Particle_Tracking_Ember_2/Particle_tracking_XY_plane/plotXY_Sphere_Ember7_long_distance.csv', skiprows=0)
df16 = pd.read_csv('C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/Ember 2 post-processing/Particle_Tracking_Ember_2/Particle_tracking_XY_plane/plotXY_Sphere_Ember8_long_distance.csv', skiprows=0)

#Read the CSV files of cube embers
df17 = pd.read_csv('C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/Ember 3 post-processing/Particle_Tracking_Ember_3/Particle_tracking_XY_plane/plotXY_Cube_Ember1_small_distance.csv', skiprows=0)
df18 = pd.read_csv('C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/Ember 3 post-processing/Particle_Tracking_Ember_3/Particle_tracking_XY_plane/plotXY_Cube_Ember2_small_distance.csv', skiprows=0)
df19 = pd.read_csv('C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/Ember 3 post-processing/Particle_Tracking_Ember_3/Particle_tracking_XY_plane/plotXY_Cube_Ember3_medium_distance.csv', skiprows=0)
df20 = pd.read_csv('C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/Ember 3 post-processing/Particle_Tracking_Ember_3/Particle_tracking_XY_plane/plotXY_Cube_Ember4_medium_distance.csv', skiprows=0)
df21 = pd.read_csv('C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/Ember 3 post-processing/Particle_Tracking_Ember_3/Particle_tracking_XY_plane/plotXY_Cube_Ember5_medium_distance.csv', skiprows=0)
df22 = pd.read_csv('C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/Ember 3 post-processing/Particle_Tracking_Ember_3/Particle_tracking_XY_plane/plotXY_Cube_Ember6_long_distance.csv', skiprows=0)
df23 = pd.read_csv('C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/Ember 3 post-processing/Particle_Tracking_Ember_3/Particle_tracking_XY_plane/plotXY_Cube_Ember7_long_distance.csv', skiprows=0)
df24 = pd.read_csv('C:/Users/amilaw/Desktop/Ember project/5. prt files processing/test4_proceeding_V3/Ember 3 post-processing/Particle_Tracking_Ember_3/Particle_tracking_XY_plane/plotXY_Cube_Ember8_long_distance.csv', skiprows=0)



#Extract the X, Y data of each cylinder ember from relevant Columns
column_cylinder_ember1X_small_distance = df1.iloc[:, 0]#1st column (index 0)
column_cylinder_ember1Y_small_distance = df1.iloc[:, 1]#3rd column (index 2)
column_cylinder_ember2X_small_distance = df2.iloc[:, 0]#1st column (index 0)
column_cylinder_ember2Y_small_distance = df2.iloc[:, 1]#3rd column (index 2)
column_cylinder_ember3X_medium_distance = df3.iloc[:, 0]#1st column (index 0)
column_cylinder_ember3Y_medium_distance = df3.iloc[:, 1]#3rd column (index 2)
column_cylinder_ember4X_medium_distance = df4.iloc[:, 0]#1st column (index 0)
column_cylinder_ember4Y_medium_distance = df4.iloc[:, 1]#3rd column (index 2)
column_cylinder_ember5X_medium_distance = df5.iloc[:, 0]#1st column (index 0)
column_cylinder_ember5Y_medium_distance = df5.iloc[:, 1]#3rd column (index 2)
column_cylinder_ember6X_long_distance = df6.iloc[:, 0]#1st column (index 0)
column_cylinder_ember6Y_long_distance = df6.iloc[:, 1]#3rd column (index 2)
column_cylinder_ember7X_long_distance = df7.iloc[:, 0]#1st column (index 0)
column_cylinder_ember7Y_long_distance = df7.iloc[:, 1]#3rd column (index 2)
column_cylinder_ember8X_long_distance = df8.iloc[:, 0]#1st column (index 0)
column_cylinder_ember8Y_long_distance = df8.iloc[:, 1]#3rd column (index 2)

#Extract the X, Y data of each Sphere ember from relevant Columns

column_Sphere_ember1X_small_distance = df9.iloc[:, 0]#1st column (index 0)
column_Sphere_ember1Y_small_distance = df9.iloc[:, 1]#3rd column (index 2)
column_Sphere_ember2X_small_distance = df10.iloc[:, 0]#1st column (index 0)
column_Sphere_ember2Y_small_distance = df10.iloc[:, 1]#3rd column (index 2)
column_Sphere_ember3X_medium_distance = df11.iloc[:, 0]#1st column (index 0)
column_Sphere_ember3Y_medium_distance = df11.iloc[:, 1]#3rd column (index 2)
column_Sphere_ember4X_medium_distance = df12.iloc[:, 0]#1st column (index 0)
column_Sphere_ember4Y_medium_distance = df12.iloc[:, 1]#3rd column (index 2)
column_Sphere_ember5X_medium_distance = df13.iloc[:, 0]#1st column (index 0)
column_Sphere_ember5Y_medium_distance = df13.iloc[:, 1]#3rd column (index 2)
column_Sphere_ember6X_long_distance = df14.iloc[:, 0]#1st column (index 0)
column_Sphere_ember6Y_long_distance = df14.iloc[:, 1]#3rd column (index 2)
column_Sphere_ember7X_long_distance = df15.iloc[:, 0]#1st column (index 0)
column_Sphere_ember7Y_long_distance = df15.iloc[:, 1]#3rd column (index 2)
column_Sphere_ember8X_long_distance = df16.iloc[:, 0]#1st column (index 0)
column_Sphere_ember8Y_long_distance = df16.iloc[:, 1]#3rd column (index 2)

#Extract the X, Y data of each Cube ember from relevant Columns

column_Cube_ember1X_small_distance = df17.iloc[:, 0]#1st column (index 0)
column_Cube_ember1Y_small_distance = df17.iloc[:, 1]#3rd column (index 2)
column_Cube_ember2X_small_distance = df18.iloc[:, 0]#1st column (index 0)
column_Cube_ember2Y_small_distance = df18.iloc[:, 1]#3rd column (index 2)
column_Cube_ember3X_medium_distance = df19.iloc[:, 0]#1st column (index 0)
column_Cube_ember3Y_medium_distance = df19.iloc[:, 1]#3rd column (index 2)
column_Cube_ember4X_medium_distance = df20.iloc[:, 0]#1st column (index 0)
column_Cube_ember4Y_medium_distance = df20.iloc[:, 1]#3rd column (index 2)
column_Cube_ember5X_medium_distance = df21.iloc[:, 0]#1st column (index 0)
column_Cube_ember5Y_medium_distance = df21.iloc[:, 1]#3rd column (index 2)
column_Cube_ember6X_long_distance = df22.iloc[:, 0]#1st column (index 0)
column_Cube_ember6Y_long_distance = df22.iloc[:, 1]#3rd column (index 2)
column_Cube_ember7X_long_distance = df23.iloc[:, 0]#1st column (index 0)
column_Cube_ember7Y_long_distance = df23.iloc[:, 1]#3rd column (index 2)
column_Cube_ember8X_long_distance = df24.iloc[:, 0]#1st column (index 0)
column_Cube_ember8Y_long_distance = df24.iloc[:, 1]#3rd column (index 2)



#Plotting Cylinder embers
plt.plot(column_cylinder_ember1X_small_distance, column_cylinder_ember1Y_small_distance, color= "dimgrey", label = "Cylinder (small distance)")
plt.plot(column_cylinder_ember2X_small_distance, column_cylinder_ember2Y_small_distance, color= "black", label = "Cylinder (small distance)")
plt.plot(column_cylinder_ember3X_medium_distance, column_cylinder_ember3Y_medium_distance, color= "darkorange", label = "Cylinder (medium distance)")
plt.plot(column_cylinder_ember4X_medium_distance, column_cylinder_ember4Y_medium_distance, color= "seagreen", label = "Cylinder (medium distance)")
plt.plot(column_cylinder_ember5X_medium_distance, column_cylinder_ember5Y_medium_distance, color= "orchid", label = "Cylinder (medium distance)")
plt.plot(column_cylinder_ember6X_long_distance, column_cylinder_ember6Y_long_distance, color= "darkblue", label = "Cylinder (long distance)")
plt.plot(column_cylinder_ember7X_long_distance, column_cylinder_ember7Y_long_distance, color= "teal", label = "Cylinder (long distance)")
plt.plot(column_cylinder_ember8X_long_distance, column_cylinder_ember8Y_long_distance, color= "fuchsia", label = "Cylinder (long distance)")

#Plotting Sphere embers
plt.plot(column_Sphere_ember1X_small_distance, column_Sphere_ember1Y_small_distance, color= "chocolate", label = "Sphere (small distance)")
plt.plot(column_Sphere_ember2X_small_distance, column_Sphere_ember2Y_small_distance, color= "crimson", label = "Sphere (small distance)")
plt.plot(column_Sphere_ember3X_medium_distance, column_Sphere_ember3Y_medium_distance, color= "indigo", label = "Sphere (medium distance)")
plt.plot(column_Sphere_ember4X_medium_distance, column_Sphere_ember4Y_medium_distance, color= "cyan", label = "Sphere (medium distance)")
plt.plot(column_Sphere_ember5X_medium_distance, column_Sphere_ember5Y_medium_distance, color= "lawngreen", label = "Sphere (medium distance)")
plt.plot(column_Sphere_ember6X_long_distance, column_Sphere_ember6Y_long_distance, color= "peru", label = "Spherer (long distance)")
plt.plot(column_Sphere_ember7X_long_distance, column_Sphere_ember7Y_long_distance, color= "crimson", label = "Sphere (long distance)")
plt.plot(column_Sphere_ember8X_long_distance, column_Sphere_ember8Y_long_distance, color= "turquoise", label = "Sphere (long distance)")

#Plotting Cube embers
plt.plot(column_Cube_ember1X_small_distance, column_Cube_ember1Y_small_distance, color= "darkslateblue", label = "Cube (small distance)")
plt.plot(column_Cube_ember2X_small_distance, column_Cube_ember2Y_small_distance, color= "gold", label = "Cube (small distance)")
plt.plot(column_Cube_ember3X_medium_distance, column_Cube_ember3Y_medium_distance, color= "olive", label = "Cube (medium distance)")
plt.plot(column_Cube_ember4X_medium_distance, column_Cube_ember4Y_medium_distance, color= "saddlebrown", label = "Cube (medium distance)")
plt.plot(column_Cube_ember5X_medium_distance, column_Cube_ember5Y_medium_distance, color= "lime", label = "Cube (medium distance)")
plt.plot(column_Cube_ember6X_long_distance, column_Cube_ember6Y_long_distance, color= "maroon", label = "Cube (long distance)")
plt.plot(column_Cube_ember7X_long_distance, column_Cube_ember7Y_long_distance, color= "yellow", label = "Cube (long distance)")
plt.plot(column_Cube_ember8X_long_distance, column_Cube_ember8Y_long_distance, color= "red", label = "Cube (long distance)")


# Create a Rectangle patch for forest
rect = patches.Rectangle((325, 355), 00, 210, linewidth=50, edgecolor='green', facecolor='none')

# Add the volume of firebrand generation
rectangle = plt.Rectangle((325,0), width=30, height=210, facecolor="None",edgecolor="green", linewidth=3)
ax =plt.gca()
ax.add_patch(rectangle)


plt.title("Embers' Trajectories XY plane")
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.xlim(325, 700)
plt.ylim(0,210)
plt.legend(fontsize="6", loc ="lower right")

plt.grid()
plt.show()