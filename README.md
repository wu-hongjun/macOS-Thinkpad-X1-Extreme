# Hackintosh for Thinkpad X1 Extreme
[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
> This hackintosh you guys made, excited!  ——— [Zemin Jiang](https://errrneist.github.io/elder/).
### Current Release: [10.14.4-V1.1](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases)
#### *Current Clover Version: 4920*
#### *Current macOS Version: 10.14.4*
#### Developer: [@Errrneist](https://www.tonymacx86.com/members/errrneist.1550861/)
#### Don't forget to star this project if you like it!
#### I recommend read the entire readme.MD before you take any action.

## Update
##### Recent
* [20190417] Displaylink has its own [known limitations](http://assets.displaylink.com/live/downloads/release-notes/f1303_DisplayLink+USB+Graphics+Software+for+macOS+5.1-Release+Notes.txt) (cannot rescale 4K to 1080P in 60FPS). So just use naive 4K.
* [20190416] Released [v10.14.4-V1.1](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v10.14.4.1.1). Fixed an issue with AppleALC.
* [20190415] Had [HDMI output working via USB Displaylink](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/13).

##### Archive
* [Past Update History Archive](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/tree/master/Updates): For earlier update logs.

## Instructions
##### Pre-Install
* *FORK* the project to your own repository and clone it to your machine using Github Desktop to make changes.
* [Windows Driver for BRCM943602CS](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v943602CS.1): If you try to use an [BCM94360CS2/BCM94360CD Card To NGFF(M.2)Key A/E Adapter For macOS](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/IMG/Readme.MD) to install the native card used on Macbook Pro. 
* [Windows Driver for BRCM943602BAED](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v943602BAED.1): To get DW1830 working in Windows. 
* [Windows Driver for Asus USB-AC53](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/Softwares/ASUS_USB-AC53-Nano/Realtek-A1600_Comfast%20810-ASUS_AC53.zip): If you are using a ASUS usb wifi adapter, also make sure to download this. 
* These cards are not natively supported by Microsoft so download it before you swap out your wireless card.
* [Problem with purchasing a wrong card](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/15#issuecomment-477450037): BCM94360CS2 and BCM943602CS are two **DIFFERENT** cards. Please be careful which you buy as others have problems causing freezing and lead to ultimate not responding.

##### Clover Bootloader
* [Configuration Release](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases): If you want to download the EFI Clover Bootloader .
* [Minimalism](https://github.com/Errrneist/Hackintosh-Theme-Minimalism): If you are interested in the theme I used, check it out over here.
* [Clover Configurator](https://mackie100projects.altervista.org/download-clover-configurator/): I recommend users to use to configure your config.plist in order to eliminate typos.
* [Guide for mounting EFI using TERMINAL](https://github.com/Errrneist/Hackintosh-Aero-15W/blob/master/Mount%20EFI%20on%20macOS.MD): If you cannot mount EFI via Clover Configurator.
##### Post-Install 
* [System Report](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/tree/master/Hardware): If you want to see system specs.
* [Time sync issues](https://www.tonymacx86.com/threads/fix-incorrect-time-in-windows-osx-dual-boot.133719/): Some might also experience between Windows and macOS. Here is a [Fix](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/timesync-v1.0) credit to [SwampFox82](https://www.tonymacx86.com/threads/fix-incorrect-time-in-windows-osx-dual-boot.133719/).
* [Special Simplified Edition](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v10.14.0.SE): Many people are experiencing unknown issues to boot into macOS. I released a EFI configuration to at least boot into the OS and see what we can do. Read more in the release comment.
* [Plugable USB3-6950-HDMI](https://www.amazon.com/Plugable-Ethernet-Supports-Displays-3840x2160/dp/B075HMWLJF/ref=sr_1_fkmrnull_1?keywords=Plugable+USB3-6950-HDMI&qid=1555380658&s=gateway&sr=8-1-fkmrnull): Inspired by this [issue](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/13) I bought an adapter and was able to achieve 4K60P via USB3.0 and HDMI2.0. Now output issue is solved. You can download the driver [via the main website](https://www.displaylink.com/downloads/file?id=1302) or [via my repo](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/Softwares/DisplayLink/DisplayLink%20USB%20Graphics%20Software%20for%20macOS%205.1.dmg). Relative question: [Will the one with USB-C plug work?](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/20) It has its own limitations of [not being able to scale 4K into 1080P with 60FPS](http://assets.displaylink.com/live/downloads/release-notes/f1303_DisplayLink+USB+Graphics+Software+for+macOS+5.1-Release+Notes.txt). This is a known issue and we can only hope future update fix this. 
* [Hackintosh Laptop Index](https://github.com/daliansky/Hackintosh): EFI for other laptop might help as a useful reference. Navigate to here if you need more reference from other laptops.
##### Issue Report
* We welcome people to submit issue and report them! This will help all of us to figure out what can be done to the laptop. Please file a issue in the **Issues** module.
* I recognize that there are a lot of Chinese speaking people participating in the discussion which is good! But if you can, please also leave an English version of your message when you post your discussion so we can have the world solve problems together. （我也发现有很多同胞积极讨论，但是如果可以的话请随手附上一份英语翻译，不会英语直接有道翻译就好，这样我们就可以和全世界一起完善这个项目啦！）
## Discussions and News
* [zysuper's Work](https://github.com/zysuper/Thinkpad-X1-extreme-EFI): Here is another helpful **alternative Thinkpad X1 Extreme Clover EFI configuration** repository. Please check out his work as well as some some issues are addressed in both of our repositories. Star his work too!
* **Bluetooth** is not working. A lot of further work needs to be done here. [Intel is embedding BT chips into PCH which does not work in macOS.](https://www.guru3d.com/news-story/intel-makes-wireless-ac-9560-a-bit-more-embedded.html) We also have a long discussion in the issues so check it out if you are interested in this issue. Link below in the Pinned Discussions. After research (cr. [darkal](https://github.com/darkal)) we found out that using AC9560 and a USB-AC53 Nano would somehow implement the Bluetooth feature, so currently we are moving toward that direction. We are also exploring with BT USB adapter.
* [Apple won't work with NVIDIA to release graphics card driver for 10.14](https://www.macrumors.com/2018/11/01/nvidia-comment-on-macos-mojave-drivers/). Currently, there is nothing we can do. We also have not tweaked on Thunderbolt 3 since we don't have proper hardware to test it. 
* Recently, people on TonyMacX86 are having **issue with PM981**. PM981 is troublesome for Hackintosh and I am not using it for install. I'm using a Toshiba XG3. However, you can check out [zysuper's repo](https://github.com/zysuper/Thinkpad-X1-extreme-EFI/blob/master/readme.md) on ACPI files to make PM981 working.
* People are experiencing weird **touchpad issues** when boot windows from clover. So far not much can be done, so I recommend you to just set auto boot time in clover be 2sec or -1sec, and just use F12 to switch OS.
* For video editors who use FinalCutPro and Davenci be aware that updating to 10.14.3 might cause [**OpenGL issue**](https://www.tonymacx86.com/threads/macos-10-14-0-thinkpad-x1-extreme-hackintosh.263916/post-1900369) that makes rendering take forever. (cr. [cthetoy](https://www.tonymacx86.com/members/cthetoy.152906/)).

## Pinned Discussions
* [Main Post on TonyMacX86](https://www.tonymacx86.com/threads/macos-10-14-0-thinkpad-x1-extreme-hackintosh.263916/)
* [Bluetooth Issues with BCM94360 Devices](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/3) 


## Specifications
* [Hardware Specifications](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/tree/master/Hardware)

## License
* This work is issued under the [996 license](https://github.com/996icu/996.ICU/blob/master/LICENSE).

### Cheers, Errrneist.


