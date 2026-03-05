#4a) 
import matplotlib.pyplot as plt # type: ignore

Ez_axis = Ez[0, :]   # eerste r-index 

plt.figure()
plt.plot(z_for_E, Ez_axis)
plt.axvline(z_pos_disk1, color='red', linestyle='--')
plt.axvline(z_pos_disk2, color='green', linestyle='--') # type: ignore
plt.xlabel('z (m)')
plt.ylabel('Ez (V/m)')
plt.title('z-component van E op de as')
plt.grid()
plt.show()

#4b)
