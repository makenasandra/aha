from pymetawear.client import MetaWearClient

from model import BodyAccX, BodyAccY, BodyAccZ, BodyGyroX, BodyGyroY, BodyGyroZ
from utils import Session, stream_data


def record_data(label: str, device: MetaWearClient) -> None:
    """
    This function commits the data streamed to the database
    :param label:
    :param device:
    :return None:
    """
    print(f"Logging data for {label}")
    acc, gyr = stream_data(device=device)
    print("Finished!")

    gx = gyr[0].replace('[', '').replace(']', '')
    gy = gyr[1].replace('[', '').replace(']', '')
    gz = gyr[2].replace('[', '').replace(']', '')

    ax = acc[0].replace('[', '').replace(']', '')
    ay = acc[1].replace('[', '').replace(']', '')
    az = acc[2].replace('[', '').replace(']', '')

    body_acc_x = BodyAccX(row_data=ax, label=label)
    body_acc_y = BodyAccY(row_data=ay, label=label)
    body_acc_z = BodyAccZ(row_data=az, label=label)

    body_gyr_x = BodyGyroX(row_data=gx, label=label)
    body_gyr_y = BodyGyroY(row_data=gy, label=label)
    body_gyr_z = BodyGyroZ(row_data=gz, label=label)

    print(f"Committing {label} data to database...")
    s = Session()

    s.add_all([body_acc_x, body_acc_y, body_acc_z, body_gyr_x, body_gyr_y, body_gyr_z])

    s.commit()
    print("Finished!")
    s.close()


if __name__ == "__main__":
    # Create a MetaWear device
    d = MetaWearClient('EE:50:E7:BF:21:83')  # Substitute with your MAC

    exercise = int(input(
        "\nChoose a number for an exercise below\n"
        "1. Jumping Jacks\n"
        "2. Squats\n"
        "3. Jogs\n"
        "4. Body Stretch(Arms)\n"
    ))

    while exercise not in [1, 2, 3, 4]:
        exercise = int(input(
            "\nChoose a number for an exercise below\n"
            "1. Jumping Jacks\n"
            "2. Squats\n"
            "3. Jogs\n"
            "4. Body Stretch(Arms)\n"
        ))

    if exercise == 1:
        action = 'jumping jacks'
    elif exercise == 2:
        action = 'squats'
    elif exercise == 3:
        action = 'jogs'
    else:
        action = 'body stretch'

    # Start to stream and record data
    record_data(label=action, device=d)

    # Disconnect device
    d.disconnect()
