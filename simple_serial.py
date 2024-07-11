import serial
import time

# Replace '/dev/ttyUSB0' with your serial port name
# Replace 9600 with the baud rate of your device
serial_port = '/dev/ttyUSB0'
baud_rate = 115200

def main():
    try:
        # Open serial port
        ser = serial.Serial(serial_port, baud_rate, timeout=1)
        print(f"Opened serial port {serial_port} at {baud_rate} baud rate.")

        # Continuously read and print data
        while True:
            if ser.in_waiting > 0:
                data = ser.readline().decode('utf-8')  # Read a line and remove trailing newline
                print(f"Received: {data}")
            time.sleep(0.1)  # Small delay to prevent overwhelming the CPU

    except serial.SerialException as e:
        print(f"Failed to open serial port {serial_port}. Error: {e}")
    finally:
        ser.close()
        print("Closed serial port.")

if __name__ == "__main__":
    main()