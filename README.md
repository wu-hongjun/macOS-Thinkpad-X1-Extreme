# Hackintosh for Thinkpad X1 Extreme [@Errrneist](https://www.tonymacx86.com/members/errrneist.1550861/)
### *Current Clover Version: 4772*
### *Current macOS Version: 10.14.0*
#### Don't forget to star this project if you like it!

## Update
* [20181118] Modified and released version 5.0 based on [zysuper's work](https://github.com/zysuper/Thinkpad-X1-extreme-EFI).
* [20181113] My laptop showed defects and I have to send it back to Lenovo to replace a new one...ugggh.
* [20181112] Got an eGPU but TB3 not enabled for macOS in 10.13. 
* [20181111] Still stuck at getting iGPU working. Tried to downgrade to 10.13.
* [20181030] Uploaded BOOT4.0 which installed most KEXT into S/L/E. See "./KernalExtentions/".
* [20181029] Uploaded INSTALL4.0 and BOOT3.0 post installations. iGPU weird with injected io-reg and fakeid on intelGFX.
* [20181028] Clover have UEFI64Driver support FileVault2. Still, make sure you get everything else working first.
* [20181027] ~~DO NOT USE FILEVAULT!!! 100% DISK BREAK AFTER REBOOT GUARANTEED.~~ 
* [20181027] Project Started. Initial INSTALL1.0 posted.

## Introduction
* *FORK* the project to your own repository and clone it to your machine using Github Desktop to make changes.
* If you want to download the EFI files to try your luck, you can check out the ~~[Configuration Release](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases)~~ => Haven't get a working version yet.
* Or, if you are interested in the theme I used, check it out over here: [Minimalism](https://github.com/Errrneist/Hackintosh-Theme-Minimalism).
* If you cannot mount EFI via the recommended [Clover Configurator](https://mackie100projects.altervista.org/download-clover-configurator/), then here is a *[Guide for mounting EFI using TERMINAL](https://github.com/Errrneist/Hackintosh-Aero-15W/blob/master/Mount%20EFI%20on%20macOS.MD).*


## Specifications
* Model: Thinkpad X1 Extreme 20MF000DUS
* BIOS: LENOVO N2EET30W(1.12)
* SMBIOS: Apple Macbook Pro 15,1
* CPU: Intel Core i7-8850H vPro 6C12T @2.6GHz
* ~~iGPU: Intel UHD Graphics 630(Lilu.kext / WhateverGreen.kext)~~
* ~~dGPU: NVIDIA GTX 1050TI MAX-Q 4GB GDDR5(Disabled / DDGPU.SSDT)~~
* ~~eGPU: AORUS Gaming Box GeForce GTX 1080 8GB GDDR5X~~
* Wifi: BCM943602BAED DW1830 802.11AC
* RAM: 32GB DDR4 2666MHZ Dual-Channel SODIMM
* Screen: Lenovo 15' 3840x2160 FlexView Display
* SSD1: Samsung PM981 MZVLB1T0HALR-000L7 1024GB (Windows)
* SSD2: Toshiba XG3 THNSN51T02DU7 1024GB (macOS)
* ~~SDXC: Samsung EVO select 128GB microSDXC~~
* Ethernet: Intel I219-LM Ethernet(IntelMausiEthernetController.kext)
* ~~BlueTooth: DW1830 BRCMBT4.1(BrcmFixup.kext)~~
* WebCamera: Integrated Camera & Integrated IR Camera
* Audio: Realtek ALC285 (VoodooHDA.kext)~~(AppleALC.kext)~~
* Microphone: Integrated Long Range Microphone Array
* ~~Backlight Control: AppleIntelBacklight~~
* Pen & Touch: WACOM Multi-Touch & Pen (Pen not tested)
* Pointing Devices: Synaptics Trackpoint and Trackpad(VoodooPS2Controller.kext)
* ~~Finger Print Reader: Synaptics Fingerprint Reader~~
* USB: AppleIntelXHCIController USB3.1 Bus(USBInjectAll.kext)

### Cheers, Errrneist.


