"""Formula 1 single lap comparison."""
import fastf1 as ff1
import os

from fastf1 import plotting
from matplotlib import pyplot as plt


def main():
    """Primary function for data analysis and plotting."""
    if cache:
        if not os.path.exists('cache'):
            os.mkdir('cache')
        ff1.Cache.enable_cache('cache')

    def get_time(time):
        """Reconstruct time in a readable format."""
        minutes = 0
        seconds, ms = str(time).split('.')
        while int(seconds) >= 60:
            seconds = int(seconds) - 60
            minutes += 1

        return f'{str(minutes).zfill(2)}:'\
            f'{str(seconds).zfill(2)}.'\
            f'{ms.ljust(3, "0")}'

    plotting.setup_mpl()

    session = ff1.get_session(year, race, 'R')
    laps = session.load_laps(with_telemetry=True)

    # Driver 1 declaration and plot options.
    driver_1 = laps.pick_driver(driver_1_initials)
    driver_1_lap_data = driver_1[driver_1['LapNumber'] ==
                                 lap_number].iloc[0]
    driver_1_car_data = driver_1[driver_1['LapNumber'] ==
                                 lap_number].iloc[0].get_car_data()
    vCar1 = driver_1_car_data['Speed']
    rpm1 = driver_1_car_data['RPM']
    g1 = driver_1_car_data['nGear']
    throttle1 = driver_1_car_data['Throttle']
    brake1 = driver_1_car_data['Brake']
    drs1 = driver_1_car_data['DRS']
    t1 = driver_1_car_data['Time']

    # Driver 2 declaration and plot options.
    driver_2 = laps.pick_driver(driver_2_initials)
    driver_2_lap_data = driver_2[driver_2['LapNumber'] ==
                                 lap_number].iloc[0]
    driver_2_car_data = driver_2[driver_2['LapNumber'] ==
                                 lap_number].iloc[0].get_car_data()
    vCar2 = driver_2_car_data['Speed']
    rpm2 = driver_2_car_data['RPM']
    g2 = driver_2_car_data['nGear']
    throttle2 = driver_2_car_data['Throttle']
    brake2 = driver_2_car_data['Brake']
    drs2 = driver_2_car_data['DRS']
    t2 = driver_2_car_data['Time']

    driver_1_lap_time = driver_1_lap_data['LapTime'].total_seconds()
    driver_2_lap_time = driver_2_lap_data['LapTime'].total_seconds()

    fig, ax1 = plt.subplots()

    ax1.plot(t1,
             vCar1,
             label=f'{driver_1_initials} [{get_time(driver_1_lap_time)}]',
             color=driver_1_color)
    ax1.plot(t2,
             vCar2,
             label=f'{driver_2_initials} [{get_time(driver_2_lap_time)}]',
             color=driver_2_color)
    ax1.set_xlabel('Time [Seconds]')
    ax1.set_ylabel('Speed [Km/h]')
    ax1.set_title(f'{race} {year} Lap {lap_number} '
                  f'{driver_1_initials} vs. {driver_2_initials}')
    ax1.legend()

    if second_y_axis:
        ax2 = ax1.twinx()
        ax2.plot(t1, drs1, linestyle='dashed', color=driver_1_color)
        ax2.plot(t2, drs2, linestyle='dashed', color=driver_2_color)
        ax2.set_ylabel('DRS')

    plt.show()


if __name__ == '__main__':
    """Easy options, for advanced options edit main() function."""
    year = 2021
    race = 'Abu Dhabi'
    lap_number = 58
    driver_1_initials = 'HAM'
    driver_1_color = 'cyan'
    driver_2_initials = 'VER'
    driver_2_color = 'blue'

    cache = True
    second_y_axis = False

    main()
