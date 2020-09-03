from time import sleep

from pymetawear.client import MetaWearClient
from xlwt import Workbook


def stream_acc_data(device, seconds=10.0, data_rate=100.0, data_range=16.0):

    data_points = []

    # Set data rate to 200 Hz and measuring range to +/- 1000 DPS
    device.accelerometer.set_settings(data_rate=data_rate, data_range=data_range)

    def gyro_callback(data_struct):
        """Handle a (epoch, (x,y,z)) gyroscope tuple."""
        data_points.append(data_struct)

    # Enable notifications and register a callback for them.
    print("Logging acc data...")
    device.accelerometer.notifications(gyro_callback)

    sleep(seconds)
    print("Finished logging!")

    return data_points


def stream_gyro_data(device, seconds=10.0, data_rate=200.0, data_range=1000.0):
    data_points = []

    # Set data rate to 200 Hz and measuring range to +/- 1000 DPS
    device.gyroscope.set_settings(data_rate=data_rate, data_range=data_range)

    def gyro_callback(data_struct):
        """Handle a (epoch, (x,y,z)) gyroscope tuple."""
        data_points.append(data_struct)

    # Enable notifications and register a callback for them.
    print("Logging gyr data...")
    device.gyroscope.notifications(gyro_callback)

    sleep(seconds)
    print("Finished logging!")

    return data_points


def write_to_excel(acc_data, gyro_data, fname):
    # Workbook is created
    wb = Workbook()

    # add_sheet is used to create sheet.
    acc = wb.add_sheet('Acceleration')
    gyr = wb.add_sheet('Gyroscope')

    print("Writing accelerometer data...")
    acc.write(0, 0, 'Epoch')
    acc.write(0, 1, 'x')
    acc.write(0, 2, 'y')
    acc.write(0, 3, 'z')
    for i in range(len(acc_data)):
        acc.write(i+1, 0, acc_data[i]['epoch'])
        acc.write(i+1, 1, acc_data[i]['value'].x)
        acc.write(i+1, 2, acc_data[i]['value'].y)
        acc.write(i+1, 3, acc_data[i]['value'].z)

    print("Writing gyroscope data...")
    gyr.write(0, 0, 'Epoch')
    gyr.write(0, 1, 'x')
    gyr.write(0, 2, 'y')
    gyr.write(0, 3, 'z')
    for i in range(len(gyro_data)):
        gyr.write(i+1, 0, gyro_data[i]['epoch'])
        gyr.write(i+1, 1, gyro_data[i]['value'].x)
        gyr.write(i+1, 2, gyro_data[i]['value'].y)
        gyr.write(i+1, 3, gyro_data[i]['value'].z)

    print("Finished!")
    print(f"Saving data to '{fname}'")
    wb.save(fname)


if __name__ == '__main__':
    c = MetaWearClient('EE:50:E7:BF:21:83')

    acc = stream_acc_data(c)
    gyro = stream_gyro_data(c)

    write_to_excel(acc, gyro, fname='test.xls')

    c.disconnect()
