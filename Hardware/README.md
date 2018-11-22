# Hackintosh for Thinkpad X1 Extreme
### Developer: [@Errrneist](https://www.tonymacx86.com/members/errrneist.1550861/)
### *Current Clover Version: 4772*
### *Current macOS Version: 10.14.0*
#### Don't forget to star this project if you like it!

## Introduction
* *FORK* the project to your own repository and clone it to your machine using Github Desktop to make changes.
* For windows drivers, here is the [Driver for BRCM943602BAED](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v943602BAED.1) to get DW1830 working. Also, here is [Driver for BRCM943602CS](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v943602CS.1) if you try to use an adapter to install the native card used on macbook. These cards are not natively supported by Microsoft so download it before you swap out your wireless card.
* If you want to download the EFI Clover Bootloader, you can check out the [Configuration Release](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases).
* Or, if you are interested in the theme I used, check it out over here: [Minimalism](https://github.com/Errrneist/Hackintosh-Theme-Minimalism).
* I recommend users to use [Clover Configurator](https://mackie100projects.altervista.org/download-clover-configurator/) to configure their config.plist to eliminate typos.
* If you cannot mount EFI via Clover Configurator, then here is a *[Guide for mounting EFI using TERMINAL](https://github.com/Errrneist/Hackintosh-Aero-15W/blob/master/Mount%20EFI%20on%20macOS.MD).*
* Some might also experience [Time sync issues](https://www.tonymacx86.com/threads/fix-incorrect-time-in-windows-osx-dual-boot.133719/) between Windows and macOS. Here is a [Fix](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/timesync-v1.0) credit to [SwampFox82](https://www.tonymacx86.com/threads/fix-incorrect-time-in-windows-osx-dual-boot.133719/).
* Also, here are the [Issues and discussions](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues) as well as [Another helpful repository by zysuper](https://github.com/zysuper/Thinkpad-X1-extreme-EFI).

## Pinned Discussions
* [Bluetooth Issues](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/3)

## Update
* [20181121] Added [Driver for BRCM943602CS in WINDOWS](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v943602CS.1).
* [20181120] Added [Driver for DW1830 in WINDOWS](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v943602BAED.1) Also had some [Discussion on getting bluetooth working](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/3).
* [20181119] Uploaded [BOOT5.0](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/tree/master/10.14.0/5.0-AllEnabled).
* [20181118] Modified and released [Configuration for macOS 10.14.0](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v10.14.0.1) based on [zysuper's work](https://github.com/zysuper/Thinkpad-X1-extreme-EFI).
* [20181115] TB3 not working. Upgraded back to 10.14.0.
* [20181113] My laptop showed defects and I have to send it back to Lenovo to replace a new one...ugggh.
* [20181112] Got an eGPU but TB3 not enabled for macOS in 10.13. 
* [20181111] Still stuck at getting iGPU working. Tried to downgrade to 10.13.
* [20181030] Uploaded BOOT4.0 which installed most KEXT into S/L/E. See ["./KernalExtentions/"](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/tree/master/KernalExtentions).
* [20181029] Uploaded [INSTALL5.0](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/tree/master/10.14.0/INSTALL-5.0) installations. iGPU weird with injected io-reg and fakeid on intelGFX.
* [20181028] Clover have UEFI64Driver support FileVault2. Still, make sure you get everything else working first.
* [20181027] DO NOT USE FILEVAULT!!! 100% DISK BREAK AFTER REBOOT GUARANTEED.
* [20181027] Project Started. Initial [INSTALL1.0](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/tree/master/10.14.0/1.0-Initlal_BootAble) posted.


## Specifications
* Model: Thinkpad X1 Extreme 20MF000DUS
* BIOS: LENOVO N2EET30W(1.12)
* SMBIOS: Apple Macbook Pro 15,2
* CPU: Intel Core i7-8850H vPro 6C12T @2.6GHz
* iGPU: Intel UHD Graphics 630 1536MB
* ~~dGPU: NVIDIA GTX 1050TI MAX-Q 4GB GDDR5(Disabled / DDGPU.SSDT)~~
* ~~eGPU: Thunderbolt 3: AORUS Gaming Box GeForce GTX 1080~~
* **Wifi: BRCM943602BAED DW1830 802.11AC**
* RAM: 32GB DDR4 2666MHZ Dual-Channel SODIMM
* Screen: Lenovo 15' 3840x2160 FlexView Display
* SSD1: Samsung PM981 MZVLB1T0HALR-000L7 1024GB (Windows)
* **SSD2: Toshiba XG3 THNSN51T02DU7 1024GB (macOS)**
* SDXC: Samsung EVO select 128GB microSDXC
* Ethernet: Intel I219-LM Ethernet(IntelMausiEthernetController.kext)
* ~~BlueTooth: DW1830 BRCMBT4.1(Due to M.2. connector lack USB channel)~~ 
* WebCamera: Integrated Camera & Integrated IR Camera
* Audio: Realtek ALC285 (VoodooHDA.kext)~~(AppleALC.kext)~~
* Microphone: Integrated Long Range Microphone Array
* Backlight Control: AppleIntelBacklight
* Pen & Touch: WACOM Multi-Touch & Pen (Pen not tested)
* Pointing Devices: Synaptics Trackpoint and Trackpad(VoodooPS2Controller.kext)
* ~~Finger Print Reader: Synaptics Fingerprint Reader (TouchID not supported.)~~
* USB: AppleIntelXHCIController USB3.1 Bus

### Cheers, Errrneist.


