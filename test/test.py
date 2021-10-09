from matplotlib import pyplot as plt
import fastf1 as ff1
from fastf1 import plotting

plotting.setup_mpl()

test = ff1.get_session(2021, 'Turkey', 'Q')

laps = test.load_laps(with_telemetry = True)

# driver 1
fast_driver_1 = laps.pick_driver('HAM').pick_fastest()
driver_1_car_data = fast_driver_1.get_car_data()
vCar1 = driver_1_car_data['Speed']
rpm1 = driver_1_car_data['RPM']
g1 = driver_1_car_data['nGear']
throttle1 = driver_1_car_data['Throttle']
brake1 = driver_1_car_data['Brake']
drs1 = driver_1_car_data['DRS']
t1 = driver_1_car_data['Time']

# driver 2
fast_driver_2 = laps.pick_driver('BOT').pick_fastest()
driver_2_car_data = fast_driver_2.get_car_data()
vCar2 = driver_2_car_data['Speed']
rpm2 = driver_2_car_data['RPM']
g2 = driver_2_car_data['nGear']
throttle2 = driver_2_car_data['Throttle']
brake2 = driver_2_car_data['Brake']
drs2 = driver_2_car_data['DRS']
t2 = driver_2_car_data['Time']

fig, ax1 = plt.subplots()

ax1.plot(t1, vCar1, label = 'Hamilton', color = 'purple')
ax1.plot(t2, vCar2, label = 'Bottas', color = 'skyblue')
ax1.set_xlabel('Time')
ax1.set_ylabel('Speed [Km/h]')
ax1.set_title('Turkey 2021 Qualifying Comparison')
ax1.legend()

# 2nd y axis
'''
ax2 = ax1.twinx()
ax2.plot(t1, g1, alpha = 0.5, color = 'orange') # driver 1
ax2.plot(t2, g2, alpha = 0.5, color = 'teal') # driver 2
ax2.set_ylabel('Gear')
'''

plt.show()

# TODO automate driver/session/metric selections
