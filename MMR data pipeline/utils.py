from time import sleep

from mbientlab.metawear import libmetawear
from pymetawear.client import MetaWearClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import Base

from config import DATABASE_URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)


def stream_data(device: MetaWearClient, seconds: float = 11.0, data_rate: float = 25.0, acc_data_range: float = 16.0,
                gyr_data_range: int = 500):
    """
    This function streams accelerometer and gyroscope data
    :param device: MetaWearClient
    :param seconds: float
    :param data_rate: float
    :param acc_data_range: float
    :param gyr_data_range: int
    :return accelerometer and gyroscope tuples of x, y, z axis:
    """
    acc_data_points = []
    gyr_data_points = []

    # Set data rate and measuring range
    device.accelerometer.set_settings(data_rate=data_rate, data_range=acc_data_range)
    device.gyroscope.set_settings(data_rate=data_rate, data_range=gyr_data_range)

    def acc_callback(data_struct):
        """Handle a (epoch, (x,y,z)) data tuple."""
        acc_data_points.append(data_struct)

    def gyr_callback(data_struct):
        """Handle a (epoch, (x,y,z)) data tuple."""
        gyr_data_points.append(data_struct)

    # Enable notifications and register a callback for them.
    device.accelerometer.notifications(callback=acc_callback)
    device.gyroscope.notifications(callback=gyr_callback)

    sleep(seconds)

    acc = (str([i['value'].x for i in acc_data_points]), str([j['value'].y for j in acc_data_points]),
           str([k['value'].z for k in acc_data_points]))

    gyr = (str([i['value'].x for i in gyr_data_points]), str([j['value'].y for j in gyr_data_points]),
           str([k['value'].z for k in gyr_data_points]))

    return acc, gyr


def recreate_database() -> None:
    """
    his function creates tables in a database in None exist
    else it deletes and creates them again
    :return None:
    """
    try:
        Base.metadata.drop_all(engine)
    except:
        pass
    Base.metadata.create_all(engine)


def reset(device) -> None:
    """
    This function resets your device if its stuck in a bad state
    :param device:
    :return None:
    """
    # Stops data logging
    libmetawear.mbl_mw_logging_stop(device.board)
    # Clear the logger of saved entries
    libmetawear.mbl_mw_logging_clear_entries(device.board)
    # Remove all macros on the flash memory
    libmetawear.mbl_mw_macro_erase_all(device.board)
    # Restarts the board after performing garbage collection
    libmetawear.mbl_mw_debug_reset_after_gc(device.board)
    libmetawear.mbl_mw_debug_disconnect(device.board)
    device.disconnect()
