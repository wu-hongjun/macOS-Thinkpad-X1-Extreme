# Hackintosh for Thinkpad X1 Extreme
[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
[![BIOS](https://img.shields.io/badge/BIOS-1.23-brightgreen.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
[![Clover](https://img.shields.io/badge/Clover-4972-green.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
[![macOS](https://img.shields.io/badge/macOS-10.15.0-orange.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
> Oh! This thing you guys made, excited!  ——— [Zemin Jiang](https://errrneist.github.io/elder/).    
### Current Release: [10.15.0-V1.2](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases)
#### Developer: [@Errrneist](https://www.tonymacx86.com/members/errrneist.1550861/)
#### Don't forget to star this project if you like it! 
#### READ THE ENTIRE README.MD BEFORE YOU TAKE ANY ACTION.
> 英语并非你的首选语言？[中文版文档](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/README_zh_CN.md)

<img align="middle" src="https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/IMG/sysinfo.png" alt="Sys Info" width="1000">

## Update
##### Recent | [Changelog Archive](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/UPDATES.md)
* [20190725] Updated readme.MD with touchscreen and displaylink issues based on a [discussion](https://www.tonymacx86.com/threads/macos-10-15-0-thinkpad-x1-extreme-hackintosh.263916/post-1986487).
* [20190724] Updated BIOS to 1.23, no major issue or changes.
* [20190723] Released [v10.15.0.1.2](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v10.15.0.1.2) that disabled the integrated IR camera. Merged change in [Issue#33](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/33#issuecomment-514062099)

## Instructions
##### Pre-Install
##### *FORK* the project to your own repository and clone it to your machine using Github Desktop to make changes.
* Windows drivers for Wifi Adapters:
    * [Windows Driver for BRCM94360CS2](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v943602CS.1): If you try to use an [BCM94360CS2/BCM94360CD Card To NGFF(M.2)Key A/E Adapter For macOS](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/IMG/Readme.MD) to install the native card used on Macbook Pro. 
    * [Windows Driver for BRCM943602BAED](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v943602BAED.1): To get DW1830 working in Windows. 
    * [Windows Driver for Asus USB-AC53](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/Softwares/ASUS_USB-AC53-Nano/Realtek-A1600_Comfast%20810-ASUS_AC53.zip): If you are using a ASUS usb wifi adapter, also make sure to download this. 
    * These cards are not natively supported by Microsoft so download it before you swap out your wireless card.
* [Kinivo BTD-400 Bluetooth 4.0 Low Energy USB Adapter](https://www.amazon.com/Kinivo-BTD-400-Bluetooth-4-0-USB/dp/B007Q45EF4/ref=sr_1_fkmrnull_3?keywords=kinivo+bluetooth+dongle&qid=1555648213&s=gateway&sr=8-3-fkmrnull): This is the BlueTooth adapter I use before I got internal BT working. Read more about the internal BT [here](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/IMG/Readme.MD).This USB adapter works well with Airpods 2, but you can always use other compatible ones. Just here if you just want to buy a cheap and working BT for nobrainers. It's BT4.0, because it is cheap and not many BT5.0 dongle exist in the market yet.

##### Issue Report
* We welcome people to submit issue and report them! This will help all of us to figure out what can be done to the laptop. Please file a issue in the **Issues** module.
* I recognize that there are a lot of Chinese speaking people participating in the discussion which is good! But if you can, please also leave an English version of your message when you post your discussion so we can have the world solve problems together.

##### Clover Bootloader
* [Configuration Release](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases): If you want to download the EFI Clover Bootloader .
* [Minimalism](https://github.com/Errrneist/Hackintosh-Theme-Minimalism): If you are interested in the theme I used, check it out over here.
* [Clover Configurator](https://mackie100projects.altervista.org/download-clover-configurator/): I recommend users to use to configure your config.plist in order to eliminate typos.
* [Guide for mounting EFI using TERMINAL](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/MOUNTEFI.MD): If you cannot mount EFI via Clover Configurator.
##### Post-Install and Issues
* Wifi issues:
    * [Problem with BCM94360CS2](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/15#issuecomment-477450037): 
       * BCM94360CS2 and BCM943602CS are two **DIFFERENT** cards. 
       * BCM94360CS2 is an ABSOLUTELY NIGHTMARE. DON'T buy.
* Bluetooth issues:
   * **Bluetooth** is SOLVED using a ribbon cable connecting to Smartcard slot. 
   * A more in depth discussion of how to make it work is here: [Issue #11](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/11)
   * But now, it seems like you can buy a [Customized adapter card](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/11#issuecomment-498715154) thanks to zysuper and wdxxfu's effort on taobao.com.
   * [Intel is embedding BT chips into PCH which does not work in macOS.](https://www.guru3d.com/news-story/intel-makes-wireless-ac-9560-a-bit-more-embedded.html) 
   * You can use an USB BT adapter mentioned above, or [DIY a board](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/IMG/Readme.MD) to make internal BT working. 
   * This requires some tech skills!!! You could toast your laptop if you do it wrong. I am serious.
* Time sync issues:
   * [Time sync issues](https://www.tonymacx86.com/threads/fix-incorrect-time-in-windows-osx-dual-boot.133719/): Some might also experience between Windows and macOS. Here is a [Fix](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/timesync-v1.0) (cr. [SwampFox82](https://www.tonymacx86.com/threads/fix-incorrect-time-in-windows-osx-dual-boot.133719/)).
* Boot issues:
   * [Special Simplified Edition](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v10.14.0.SE): Many people are experiencing unknown issues to boot into macOS. 
   * I released a EFI configuration to at least boot into the OS and see what we can do. Read more in the release comment. (It is for 10.14.3 idk if it works in 10.14.4 or newer).
* Touchpad issues:
    * People are experiencing weird **touchpad issues** when boot windows from clover. So far not much can be done, so I recommend you to just set auto boot time in clover be 2sec or -1sec, and just use F12 to switch OS.
* OpenGL issues:
    * For video editors who use FinalCutPro and Davenci be aware that updating to 10.14.3 might cause [**OpenGL issue**](https://www.tonymacx86.com/threads/macos-10-14-0-thinkpad-x1-extreme-hackintosh.263916/post-1900369) that makes rendering take forever. (cr. [cthetoy](https://www.tonymacx86.com/members/cthetoy.152906/)).
* PM981 issues:
    * Recently, people on TonyMacX86 are having **issue with PM981**. PM981 is troublesome for Hackintosh and I am not using it for install. I'm using a Toshiba XG3. However, you can check out [zysuper's repo](https://github.com/zysuper/Thinkpad-X1-extreme-EFI/blob/master/readme.md) on ACPI files to make PM981 working.
* External Display issues: 
   * IMPORTANT! I HEARD (Haven't confirm by myself) that for now in Catalina there is limited displaylink support (Although they did published their newest 5.1.1 driver for Catalina beta). Be careful on updateing to Catalina if you need to use displaylink. More info from [DisplayLink's Support on Catalina](https://support.displaylink.com/knowledgebase/articles/1916602-macos-catalina-10-15-beta).
   * [Plugable USB3-6950-HDMI](https://www.amazon.com/Plugable-Ethernet-Supports-Displays-3840x2160/dp/B075HMWLJF/ref=sr_1_fkmrnull_1?keywords=Plugable+USB3-6950-HDMI&qid=1555380658&s=gateway&sr=8-1-fkmrnull): Inspired by this [issue](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/13) I bought an adapter and was able to achieve 4K60P via USB3.0 and HDMI2.0. Now output issue is solved. You can download the driver [via their website](https://www.displaylink.com/downloads/macos). 
   * Relative question: [Will the one with USB-C plug work?](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/20) Short answer, I don't know. You can buy one and try if you want to.
   * Alternative [Lenovo USB Dock](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/13#issuecomment-507499718), a dock by Lenovo and I suppose it might work as well, but I am not sure as it has not ben tested. (cr. [darkal](https://github.com/darkal))
   * However, it has its own limitations of [not being able to scale 4K into 1080P with 60FPS](http://assets.displaylink.com/live/downloads/release-notes/f1303_DisplayLink+USB+Graphics+Software+for+macOS+5.1-Release+Notes.txt). This is a known issue and we can only hope future update fix this.
* Touchscreen and Gesture Issues (VoodooI2C.kext):
   * A interesting [discussion](https://www.tonymacx86.com/threads/macos-10-15-0-thinkpad-x1-extreme-hackintosh.263916/post-1986487) with [jamesxxx1997](https://www.tonymacx86.com/members/jamesxxx1997.2184482/) implies that (At least on 10.14) you can use [VoodooI2C.kext](https://github.com/alexandred/VoodooI2C) to achieve touch screen and touchpad gesture support.
   * However, it was not working on 10.15 based on my tests.
   * I suspect that it is a Catalina compatiability issue, because 10.15 lose touchscreen support even if it was supported in 10.14.
   * The author of VoodooI2C hasn't been updating the repo since WWDC2019, so I suspect so far there is no Catalina support.
   * To test it out on your own, you need VoodooI2C.kext and VoodooI2CCHID.kext, and in theory it would just work.
* Camera Issues:
   * There is an [issue](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/33#issuecomment-514062099) that macOS would use the integrated IR camera to make video calls which does not quite work.
   * This is fixed in v10.15.0.1.2, credit to [flymin](https://github.com/flymin), [kk1987](https://github.com/kk1987), and [ColeXJ](https://github.com/ColeXJ).
* [System Report](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/SPEC.md): If you want to see system specs.
* More Hackintosh EFI Resource:
   * Hackintosh Laptop Index: EFI for other laptop might help as a useful reference. Navigate to [here](https://github.com/daliansky/Hackintosh) (cr. [daliansky](https://github.com/daliansky)) if you need more reference from other laptops. Note: The word “链接” in Chinese means “link” so click on it it will take you to the repo you are looking for.

## Other Contributors
| Name | Contributions |
| --- | --- |
| [Rehabman](https://github.com/RehabMan) | Many kernel extensions and guides. |
| [Acidanthera](https://github.com/acidanthera) | Lilu.kext and WhateverGreen.kext. |
| [zysuper](https://github.com/zysuper) | Original development and M.2 Adapter order. |
| [darkal](https://github.com/darkal) | USB external display via DisplayLink issues and minor debugging. |
| [SwampFox82](https://www.tonymacx86.com/threads/fix-incorrect-time-in-windows-osx-dual-boot.133719/) | Time sync issue solution. |
| [cthetoy](https://www.tonymacx86.com/members/cthetoy.152906/) | OpenGL issue. |
| [jamesxxx1997](https://www.tonymacx86.com/members/jamesxxx1997.2184482/) | Touchscreen and Multi-touch gesture. |
| [alexandred](https://github.com/alexandred) | Voodool2C.kext and its satellites. |
| [flymin](https://github.com/flymin) | IR Camera ACPI patching. |
| [kk1987](https://github.com/kk1987) | IR Camera ACPI patching methods. |
| [ColeXJ](https://github.com/ColeXJ) | IR Camera issue. |
| [daliansky](https://github.com/daliansky) | Hackintosh index maintainer. |

## Discussions and News
* [zysuper's Work](https://github.com/zysuper/Thinkpad-X1-extreme-EFI): Here is another helpful **alternative Thinkpad X1 Extreme Clover EFI configuration** repository. Please check out his work as well as some some issues are addressed in both of our repositories. Star his work too!
* [Apple won't work with NVIDIA to release graphics card driver for 10.14](https://www.macrumors.com/2018/11/01/nvidia-comment-on-macos-mojave-drivers/). Currently, there is nothing we can do. We also have not tweaked on Thunderbolt 3 since we don't have proper hardware to test it. 

## License
* This work is issued under the [996 license](https://github.com/996icu/996.ICU/blob/master/LICENSE).

## Donate
* Donating to this project is OPTIONAL. 
* However, if you would like to buy me a coffee, you can do that using QR codes (WechatPay or Venmo).
<img align="middle" src="https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/IMG/wechatpay.jpg" alt="wechatpay" width="300">
<img align="middle" src="https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/IMG/venmo.jpg" alt="venmo" width="300">

### Cheers, Errrneist.

