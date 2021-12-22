"""Formula 1 single lap comparison."""
import fastf1 as ff1
import os

from fastf1 import plotting
from matplotlib import pyplot as plt


lap_number = 58
cache = True

if cache:
    if not os.path.exists('cache'):
        os.mkdir('cache')
    ff1.Cache.enable_cache('cache')

plotting.setup_mpl()

session = ff1.get_session(2021, 'Abu Dhabi', 'R')
laps = session.load_laps(with_telemetry=True)

# driver 1
driver_1 = laps.pick_driver('HAM')
driver_1_car_data = driver_1[driver_1['LapNumber'] ==
                             lap_number].iloc[0].get_car_data()
vCar1 = driver_1_car_data['Speed']
rpm1 = driver_1_car_data['RPM']
g1 = driver_1_car_data['nGear']
throttle1 = driver_1_car_data['Throttle']
brake1 = driver_1_car_data['Brake']
drs1 = driver_1_car_data['DRS']
t1 = driver_1_car_data['Time']

# driver 2
driver_2 = laps.pick_driver('VER')
driver_2_car_data = driver_2[driver_2['LapNumber'] ==
                             lap_number].iloc[0].get_car_data()
vCar2 = driver_2_car_data['Speed']
rpm2 = driver_2_car_data['RPM']
g2 = driver_2_car_data['nGear']
throttle2 = driver_2_car_data['Throttle']
brake2 = driver_2_car_data['Brake']
drs2 = driver_2_car_data['DRS']
t2 = driver_2_car_data['Time']

fig, ax1 = plt.subplots()

ax1.plot(t1, vCar1, label='Hamilton', color='cyan')
ax1.plot(t2, vCar2, label='Verstappen', color='blue')
ax1.set_xlabel('Time')
ax1.set_ylabel('Speed [Km/h]')
ax1.set_title('Abu Dhabi 2021 Final Lap Comparison')
ax1.legend()

# 2nd y axis
'''
ax2 = ax1.twinx()
ax2.plot(t1, throttle1, alpha=0.5, color='cyan')  # driver 1
ax2.plot(t2, throttle2, alpha=0.5, color='blue')  # driver 2
ax2.set_ylabel('Gear')
'''

if __name__ == '__main__':
    plt.show()
