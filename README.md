# Flymin's Hackintosh profile on Thinkpad X1E

## ATTENTION

This repo basically is a fork repo of [Errrneist's repo](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme), except for some little change to compatible with my machine, which has different hardwares.

I will make effort to try every release and make modification if encounter with problems.

## Hardware: Thinkpad X1 Extreme Gen 1

- CPU: Core i7-8750H 2.2GHz
- Memory: 16G 2667MHz DDR4
- SSD1: intel 7600P SSDPEKKF256G8L
- SSD2: Intel 760P  SSDPEKKW256G8
- Display: 1080p, non-touch
- Graphics: Intel UHD Graphics 630
- Wireless: Broadcom BCM943602CS
- Sound card: Realtek ALC285
- BIOS: v1.23
- OS: OS X Mojave 10.14.6

## Result

<img align="middle" src="IMG/system config.png" alt="Overview" />

### What works

- Base OS
- Sleep, wakeup, hibernation
- Brightness, function keys for brightness control, NightShift
- Intel Ethernet LAN (mini RJ45) and WIFI
- Touchpad ~~and TrackPoint~~
- Audio, function keys for volume control, headphone jack
- USB 3.1 ports, USB-C ports (only can be connected to USB 3.0 devices)

### What doesn't work

- Function keys Fn+F4, Fn+F7-F12
- Smooth brightness adjustment
- Nvidia Graphics Card 1050Ti
- Thunderbolt 3
- HDMI output to external display

## Add-ons

## kext modifications

- Customized AppleALC.kext

  Set `alcid=31` in `E/C/config.plist`. I made a custom version to ALC285 with layout 31, see [pull #442](https://github.com/acidanthera/AppleALC/pull/442) and my [codec#0 paths](https://github.com/flymin/Hackintosh-Thinkpad-X1-Extreme/blob/master/IMG/codec%230.svg)
  
- Deleted VoodooI2C*.kext

  kexts above will cause about 5min boot lag for machines have no I2C devices

# Acknowledgements

- [zysuper's Hackintosh](https://github.com/zysuper/Thinkpad-X1-extreme-EFI) 
- [Errrneist's Hackintosh](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme)
- [xuzhao9's Hackintosh](https://github.com/xuzhao9/ThinkPad-X1E-Hackintosh)
  - we have very similiar hardware config, but his DSDT table won't work on me. You can try it out if there is some problems with my version. 
- [RehabMan's DSDT patches](https://github.com/RehabMan/Laptop-DSDT-Patch)
- [Telegram Hackintosh Group](https://t.me/joinchat/FSuP2UI4ALt1uIVmQ5E6lg)