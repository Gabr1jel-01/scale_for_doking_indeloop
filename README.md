# DOK-ING Indeloop Dynamic Scale

## Project overview

- [Goal](#goal)
- [Overview](#overview)
- [Hardware](#hardware)
  - [Scale](#hardware)
  - [Custom Wiring](#hardware)
- [Software](#software)
  - [How to use](#software)
    - Download
    - Extract
    - Run
- [Code explanation](#code-explanation)

# Goal

The goal of this project was to develop a software for [DOK-ING](https://dok-ing.hr/)'s [Indeloop](https://indeloop.hr/) department which enables continous logging of data that is measured by the [Kern](https://www.kern-sohn.com/shop/en/)'s scale [CFS50K-3](https://www.kern-sohn.com/cosmoshop/default/pix/a/media/CFS%2050K-3/TD_CFS+50K-3_en.pdf).

# Overview

I made this project as a part of a much bigger project called T25. The T25 project is a gasification system that uses thermal energy to convert organic material into syngas (hydrogen) and black carbon. By developing this custom software I was able to get a precise and continous measuring from the scale. The scale's task was to measure how fast could the organic material be delivered to the plant T25.

# Hardware

- [Kern](https://www.kern-sohn.com/shop/en/)'s [CFS50K-3](https://www.kern-sohn.com/cosmoshop/default/pix/a/media/CFS%2050K-3/TD_CFS+50K-3_en.pdf)

- Custom wiring

# Software

- How to use:

  - Download

    - By clicking the code dropdown the user needs to download ZIP file of this project which includes the code.

  - Extract

    - When the folder containing the code is downloaded to the user's device, the user should locate the Zipped folder and extract that same folder to a desired location on their device.

  - Run

    - Once the folder has been extracted the user can open the folder in any desired IDE (Integrated Development Environment).

#

#### Code explanation:

First step is to create two variables that will later be used to connect to the scale and to send a command that the scale can interpret to give back desired data.

```python
ser = serial.Serial("COM3", 9600)
command = "\W"
```

"ser" variable is used to establish a connection with the scale. First parameter in the method serial.Serial() is the COM port on your device. COM ports are used to establish a communication with external devices.

Command "\W" can be found in the scales documentation and is used to return Total Weight value.

> [!IMPORTANT]
> When connecting the scale to your device, the COM port can differ from the one that is in the code so be aware if there is a need to change which COM port to listen to.

The while loop is running and getting a reading from the scale until the "s" key on keyboard is pressed. ⬇️

```python
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
```

At the end of the while loop each reading is appended to a list called "my_list" and also printed to the terminal. I chose to print the readings to the terminal to have an immidiate overview of the measuring for convenience purposes. ⬇️

```python
.
.
.
my_list.append(formatted_reading)
print(formatted_reading)
```

The readings which are appended to the list are stored in a CSV file.

```python
.
.
.
readings_csv = f"./{string}{formatted_time}.csv"
.
.
.
with open(readings_csv, "w") as csv_file:
    for item in my_list:
        csv_file.write(item)
```
