import serial

import time


from datetime import datetime

import keyboard

import csv

my_list = []


# Open the serial connection


ser = serial.Serial("COM3", 9600)

command = "\W"


check = False

exit_flag = False


def on_key_event(e):

    global check, exit_flag

    if e.name == "s":

        exit_flag = True


keyboard.hook(on_key_event)


string = "Vaganje_"

dateandtime = datetime.now()

formatted_time = (
    dateandtime.strftime("%Y-%m-%d %H:%M:%S")
    .replace(" ", "_")
    .replace("-", "_")
    .replace(":", "_")
)

readings_csv = f"./{string}{formatted_time}.csv"


while not exit_flag:

    # Send command to request weight

    command_bytes = command.encode()

    ser.write(command_bytes)

    # Read response from the scale

    response = str(ser.readline().decode().strip().replace("ST,GS", ""))

    modified_response = response[3:]

    realtime = datetime.now()

    # Format the datetime up to seconds

    formatted_time = realtime.strftime("%Y-%m-%d %H:%M:%S.%f")[:-4]

    # Create a formatted string for each reading with time up to seconds

    formatted_reading = f"{modified_response} - {formatted_time}\n"

    my_list.append(formatted_reading)

    print(formatted_reading)


# Close the serial connection

ser.close()


# Append the formatted reading directly to the file

with open(readings_csv, "w") as csv_file:

    for item in my_list:

        csv_file.write(item)
