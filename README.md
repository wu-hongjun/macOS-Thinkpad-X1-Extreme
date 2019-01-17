# Hackintosh for Thinkpad X1 Extreme
### Developer: [@Errrneist](https://www.tonymacx86.com/members/errrneist.1550861/)
### *Current Clover Version: 4772*
### *Current macOS Version: 10.14.0*
#### Don't forget to star this project if you like it!

> This hackintosh you guys made, excited!  ————Zemin Jiang

## Instructions
##### Pre-Install
* *FORK* the project to your own repository and clone it to your machine using Github Desktop to make changes.
* For windows drivers, here is the [Driver for BRCM943602BAED](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v943602BAED.1) to get DW1830 working. Also, here is [Driver for BRCM943602CS](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v943602CS.1) if you try to use an adapter to install the native card used on macbook. These cards are not natively supported by Microsoft so download it before you swap out your wireless card.
##### Clover Bootloader
* If you want to download the EFI Clover Bootloader, you can check out the [Configuration Release](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases).
* Or, if you are interested in the theme I used, check it out over here: [Minimalism](https://github.com/Errrneist/Hackintosh-Theme-Minimalism).
* I recommend users to use [Clover Configurator](https://mackie100projects.altervista.org/download-clover-configurator/) to configure their config.plist to eliminate typos.
* If you cannot mount EFI via Clover Configurator, then here is a *[Guide for mounting EFI using TERMINAL](https://github.com/Errrneist/Hackintosh-Aero-15W/blob/master/Mount%20EFI%20on%20macOS.MD).*
##### Post-Install and Discussions
* If you want to see system specs, check out [System Report](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/tree/master/Hardware).
* Some might also experience [Time sync issues](https://www.tonymacx86.com/threads/fix-incorrect-time-in-windows-osx-dual-boot.133719/) between Windows and macOS. Here is a [Fix](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/timesync-v1.0) credit to [SwampFox82](https://www.tonymacx86.com/threads/fix-incorrect-time-in-windows-osx-dual-boot.133719/).
* Also, here are the [Issues and discussions](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues) as well as [Another helpful Clover EFI configuration repository by zysuper](https://github.com/zysuper/Thinkpad-X1-extreme-EFI).
* [Apple won't work with NVIDIA to release graphics card driver for 10.14](https://www.macrumors.com/2018/11/01/nvidia-comment-on-macos-mojave-drivers/). Currently, there is nothing we can do.

## Pinned Discussions
* [Main Post Thread](https://www.tonymacx86.com/threads/macos-10-14-0-thinkpad-x1-extreme-hackintosh.263916/)
* [Bluetooth Issues](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/3) (PS: This is the biggest issue we are working on.)
* [Thunderbolt 3 Post](https://www.tonymacx86.com/threads/coffeelake-laptop-thunderbolt-3-support.265692/#post-1857305)
* [Trackpad not working with Clover-booted Windows](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/5)



## Update
##### Recent
* [20190111] Got BCM943602CS working. Turned out I didn't stuck it in enough.
* ~~[20190105] I still cannot get BCM943602CS on adaptor working...~~
* [20181225] Happy holiday humans.
* [20181222] I ordered ribbon cable for smartcard slot in China. Will need to design a PCB tho...
* [20181207] My laptop is dead due to I was stupid enough to tear it down without unplug the battery.
* [20181121] Added [Driver for BRCM943602CS in WINDOWS](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v943602CS.1).
* [20181120] Added [Driver for DW1830 in WINDOWS](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v943602BAED.1) Also had some [Discussion on getting bluetooth working](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/3).
* [20181119] Uploaded [BOOT5.0](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/tree/master/10.14.0/5.0-AllEnabled).
* [20181118] Modified and released [Configuration for macOS 10.14.0](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v10.14.0.1) based on [zysuper's work](https://github.com/zysuper/Thinkpad-X1-extreme-EFI).
##### Archive
* For earlier update logs, see [Past Update History Archive](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/tree/master/Updates).


## Specifications
* [Hardware Specifications](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/tree/master/Hardware)

### Cheers, Errrneist.


