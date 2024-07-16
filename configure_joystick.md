Install joystick and jstest

```bash
sudo apt install joystick jstest
```


To connect joystick to rpi using cmd

there is a bash script with all the below commands available. You can execute it directly, but first update to the MAC address of your joystick
```cmd
./connect_bluetooth.sh
```

or do the following steps

run `bluetoothctl`
```bash
sudo bluetoothctl
```

Then turn agent on
```cmd
[bluetooth]# agent on
Agent is already registered
```

Then set default agent
```cmd
[bluetooth]# default-agent
Default agent request successful
```

Then run scan and put joystick in pairing mode

```cmd
[bluetooth]# scan on
Discovery started
[CHG] Controller D8:3A:DD:18:1F:09 Discovering: yes
[NEW] Device 41:5E:5A:3B:4D:1F 41-5E-5A-3B-4D-1F
[NEW] Device 7A:3F:67:B3:43:9A 7A-3F-67-B3-43-9A
[NEW] Device 65:C8:98:EB:C7:36 65-C8-98-EB-C7-36
[NEW] Device E3:23:B0:B1:7F:4A Wireless Controller
```

Notice the MAC address. You need to connect then add to trusted devices to store
```
[bluetooth]# connect E3:23:B0:B1:7F:4A
Attempting to connect to E3:23:B0:B1:7F:4A
[CHG] Device E3:23:B0:B1:7F:4A Connected: yes
[CHG] Device E3:23:B0:B1:7F:4A UUIDs: 00001124-0000-1000-8000-00805f9b34fb
[CHG] Device E3:23:B0:B1:7F:4A UUIDs: 00001200-0000-1000-8000-00805f9b34fb
[CHG] Device E3:23:B0:B1:7F:4A ServicesResolved: yes
[CHG] Device E3:23:B0:B1:7F:4A WakeAllowed: yes
```
```
[Wireless Controller]# trust E3:23:B0:B1:7F:4A
[CHG] Device E3:23:B0:B1:7F:4A Trusted: yes
Changing E3:23:B0:B1:7F:4A trust succeeded
```


## Custom Joystick Names
If you're connecting multiple joysticks to the rpi. And you want to dedicate a gamepad to the rover and arm respectively. You have to create a custom symbolic name for the joysticks based on their mac address. 

Use the `99-custom-joystick.rules` for reference, and change the respective MAC addresses (they have to be lowercase to match). 

For non-PS4 clone gamepads. You can discover the attribute details (You need the ATTR{name} and ATTR{uniq} or ATTR{address}, depending on which one has the MAC address)
The following command will display the joystick info, use it to edit the `99-custom-joystick.rules` for each joystick used.
```cmd
udevadm info -a -n /dev/input/js0
```

When ready, copy the rules file to the `udev/rules.d` folder
```cmd
sudo cp 99-custom-joystick.rules /etc/udev/rules.d/99-custom-joystick.rules
```

and reload and trigger the new rules
```
sudo udevadm control --reload-rules && sudo udevadm trigger
```

If you discover the input devices you should see the new symbolic names
```cmd
ls -l /dev/input/
```

```
kars@robot-ali:~/rpi-rover-setup $ ls -l /dev/input/
by-path/        event2          event5          event8          joystick-rover  mice
event0          event3          event6          event9          js0             mouse0
event1          event4          event7          joystick-arm    js1             mouse1
```


