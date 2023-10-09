# Sniffer

# Raspberry Pi GPIO Button and LED Control

This Python script utilizes the RPi.GPIO library to control an LED using a button press on a Raspberry Pi. The script sends UDP messages to control the state of an LED connected to another device on the network.

## Requirements

- Raspberry Pi with GPIO support
- Python 3
- RPi.GPIO library

## Setup

1. Connect a button to GPIO pin 21 on your Raspberry Pi.
2. Make sure the RPi.GPIO library is installed on your Raspberry Pi.
   ```bash
   pip install RPi.GPIO
   ```

## Usage

Run the script on your Raspberry Pi:

```bash
python Sniffer.py
```

Press the button connected to GPIO pin 21. The script alternates between turning the LED on and off, sending UDP messages to the specified IP and port.

## UDP Messages

The script sends UDP messages to control the state of the LED on another device. The messages are defined as follows:

- UDP_MESSAGE_LED_ON: Message to turn the LED on.
- UDP_MESSAGE_LED_OFF: Message to turn the LED off.

## Note

- The script assumes an LED control protocol based on UDP messages. Make sure the receiving device is configured to interpret these messages correctly.

