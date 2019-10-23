# Hackintosh for Thinkpad X1 Extreme Gen I
[![macOS](https://img.shields.io/badge/macOS-10.15.0-orange.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
[![Clover](https://img.shields.io/badge/Clover-5070-yellowgreen)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
[![BIOS](https://img.shields.io/badge/BIOS-1.24-brightgreen)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
[![MODEL](https://img.shields.io/badge/Model-20MF000DUS-blue)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)

<img align="right" src="https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/IMG/catcritter.png" alt="Critter" width="250">

> Oh! This thing you guys made, excited!  ——— [Zemin Jiang](https://errrneist.github.io/elder/).    
### Current Release: [10.15.0-V3.3](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases)
#### Developer: [@Errrneist](https://www.tonymacx86.com/members/errrneist.1550861/)
#### Don't forget to star this project if you like it! 
#### READ THE ENTIRE README.MD BEFORE YOU TAKE ANY ACTION.
> 英语并非你的首选语言？[中文版文档（非最新）](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/README_zh_CN.md)

## Update
##### Recent | [Changelog Archive](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/UPDATES.md)
* [20191017] Solved eGPU. See "eGPU" section below. Now X1E is fully complete with everything supported. Yea!
* [20191016] Added "32 bit program" and "repasting guide" section in the resource section. Read them.
* [20191015] It looks like PB10(19A582a) is GM Seed and it is newest. My machine works normal on GM...

## Instructions
### Please read the `Post-Install` section. It is long, but really, really helpful.
##### Pre-Install
##### *FORK* the project to your own repository and clone it to your machine using Github Desktop to make changes.
* Windows drivers for Wifi Adapters:
    * [Windows Driver for BRCM943602CS](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v943602CS.1): If you try to use an [BCM943602CS/BCM94360CD Card To NGFF(M.2)Key A/E Adapter For macOS](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/IMG/Readme.MD) to install the native card used on Macbook Pro. 
    * [Windows Driver for BRCM943602BAED](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v943602BAED.1): To get DW1830 working in Windows. 
    * [Windows Driver for Asus USB-AC53](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/Softwares/ASUS_USB-AC53-Nano/Realtek-A1600_Comfast%20810-ASUS_AC53.zip): If you are using a ASUS usb wifi adapter, also make sure to download this. 
    * These cards are not natively supported by Microsoft so download it before you swap out your wireless card.

##### Issue Report
* We welcome people to submit issue and report them! This will help all of us to figure out what can be done to the laptop. Please file a issue in the **Issues** module.
* I recognize that there are a lot of Chinese speaking people participating in the discussion which is good! But if you can, please also leave an English version of your message when you post your discussion so we can have the world solve problems together.

##### Clover Bootloader
* [Configuration Release](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases): If you want to download the EFI Clover Bootloader .
* [Minimalism](https://github.com/Errrneist/Hackintosh-Theme-Minimalism): If you are interested in the theme I used, check it out over here.
* [Clover Configurator](https://mackie100projects.altervista.org/download-clover-configurator/): I recommend users to use to configure your config.plist in order to eliminate typos.
* [Guide for mounting EFI using TERMINAL](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/MOUNTEFI.MD): If you cannot mount EFI via Clover Configurator.

## Post-Install
#### Customize "About this Mac":
   * [How to customize the “About This Mac” section of a Mac, Joaquim Barbosa](https://www.idownloadblog.com/2017/01/13/how-to-modify-about-this-mac-hackintosh/).
#### Wifi & Wireless Card Adaptors:
   * [Problem with BCM94360CS2 (Issue #15)](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/15#issuecomment-477450037): 
       * BCM94360CS2 and BCM943602CS are two **DIFFERENT** cards. 
       * BCM94360CS2 is an ABSOLUTELY NIGHTMARE. DON'T buy.
       * If you are confused: The card with 3 antennas is good, with 2 antennas is bad.
#### Memory:
   * Normally, your memory on your machine should just work. However, with machines that has 64G of memory (ughhhh you rich people!!), you might need some workaround.([Issue #34](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/34#issuecomment-516447421))
   * Presented by [oreziam](https://github.com/oreziam), he gave a brief description of his solution in the above issue. 
      * Note that I do not know, and cannot help you with this issue since I have 32G of memory. You should contact oreziam if you have questions.
      * In order to make this work, you need to inject info of the system memory, but with one more sockets than usual.
      * That means you need to inject 4 channels and 5 sockets for memory info, 16G * 5.
      * When you boot into the system, it would detect 64G correctly.
#### Sound & AppleALC:
   * If your AppleALC.kext does not load using (for example, V3.0), then read the following passage.
      * V3.0 and many versions in the previous releases uses a special AppleALC.kext with alcid=7.
      * Note: In many cases, a simple restart will reload AppleALC and your audio will come back to normal.
      * However, if this does not work with you, you should try the following:
         * Download the newest AppleALC.kext from github.
         * Delete the old AppleALC and replace it with the new one.
         * Change boot argument alcid=7 to alcid=21.
#### 32 Bit Program Incompatibilities:
   * 32 bit program is no longer supported in macOS 10.15.0 Catalina.
   * Using 32 bit programs on macOS Catalina would cause reboot shortly after login.
   * Most common killer programs: Tuxera NTFS 2018 and Steam.
      * Tuxera NTFS 2019 still does the same thing. Hmmmmm. Be careful you have been warned.
   * Solution:
      * Keep rebooting until you can get into the system somehow.
      * I used Appcleaner to uninstall Tuxera, ans it is effective. So I would recommend that.
#### Battery:
   * There is an [Hibernation battery drain issue (Issue #36)](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/36) of battery draining and the machine does not fully hibernate when I want it to, for example, closing the lid. (It also makes a little bit of heat, not too much as fully turned on), approximately 5% per hour. You can read more in the link above.
   * To my knowledge, you only need to patch your own DSDT, and since this problem hasn't bothering me much and I am busy, fixing this issue has not been implemented.
      * Even if it is implemented, since everyone have different DSDT, it probably won't work for you anyway.
      * If you are curious, I am using zysuper's DSDT (Which might be the reason that caused this issue) since it just works on my laptop and I don't need to spend extra time in my busy life to make my own. ~~Netflix and chill is much more fun...or Panopto and chill?~~
#### Bluetooth:
   * Bluetooth is SOLVED (~~fuck~~, finally) using a ribbon cable connecting to Smartcard slot. 
      * A more in depth discussion of how to make it work is here: 
         * [Episode 1: Issue #3](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/3#issuecomment-471815481)
         * [Episode 2: Issue #11](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/11)
      * But now, it seems like you can buy a [Customized adapter card (Issue #11)](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/11#issuecomment-498715154) thanks to zysuper and wdxxfu's effort on taobao.com.
      * [Intel is embedding BT chips into PCH which does not work in macOS.](https://www.guru3d.com/news-story/intel-makes-wireless-ac-9560-a-bit-more-embedded.html) 
      * You can use an USB BT adapter mentioned above, or [DIY a board](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/IMG/Readme.MD) to make internal BT working. 
      * This requires some tech skills!!! You could toast your laptop if you do it wrong. I am serious.
   * If you don't want to go through these effort:
      * [Kinivo BTD-400 Bluetooth 4.0 Low Energy USB Adapter](https://www.amazon.com/Kinivo-BTD-400-Bluetooth-4-0-USB/dp/B007Q45EF4/ref=sr_1_fkmrnull_3?keywords=kinivo+bluetooth+dongle&qid=1555648213&s=gateway&sr=8-3-fkmrnull): This is the BlueTooth adapter I use before I got internal BT working. Read more about the internal BT [here](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/IMG/Readme.MD).This USB adapter works well with Airpods 2, but you can always use other compatible ones. Just here if you just want to buy a cheap and working BT for nobrainers. It's BT4.0, because it is cheap and not many BT5.0 dongle exist in the market yet.
#### Fan:
   * Some people experienced fan issues that the fan does not turn on during load. ([Issue #32](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/32))
   * This can be solved by applying a BIOS update (1.17 -> 1.23).
#### Time Sync Between Windows and macOS:
   * [Time sync issues](https://www.tonymacx86.com/threads/fix-incorrect-time-in-windows-osx-dual-boot.133719/): Some might also experience between Windows and macOS. Here is a [Fix](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/timesync-v1.0) (cr. [SwampFox82](https://www.tonymacx86.com/threads/fix-incorrect-time-in-windows-osx-dual-boot.133719/)).
#### Boot:
   * [Special Simplified Edition](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v10.14.0.SE): Many people are experiencing unknown issues to boot into macOS. 
   * I released a EFI configuration to at least boot into the OS and see what we can do. Read more in the release comment. (It is for 10.14.3 idk if it works in 10.14.4 or newer).
#### Touchpad, Touchscreen and Multi-Gesture:
   * Turns out Acidanthera's VoodooPS2Controller.kext is good enough for enabling multigesture and touchscreen.
      * No need for VoodooI2C.kext! (Change merged in the 10.15.0.3.2 release)
   * I was requested to make a video on how it works on the touch screen, link below.
      * [Touch screen gesture implementation on X1E, Errrneist, 2019.](https://youtu.be/mZ7sTGxccuc)
   * Touchpad in WINDOWS:
      * People are experiencing weird **touchpad issues** when boot windows from CLOVER. So far not much can be done, so I recommend you to just set auto boot time in clover be 2sec or -1sec, and just use F12 to switch OS.
   * VoodooI2C.kext:
      * NOTE: I used to say VoodooI2C is not working and unuseful, I was wrong. It works to enable gesture on the touch display.
      * A interesting [discussion](https://www.tonymacx86.com/threads/macos-10-15-0-thinkpad-x1-extreme-hackintosh.263916/post-1986487) with [jamesxxx1997](https://www.tonymacx86.com/members/jamesxxx1997.2184482/) implies that (At least on 10.14) you can use [VoodooI2C.kext](https://github.com/alexandred/VoodooI2C) to achieve touch screen and touchpad gesture support.
         * Optional Reading: A more through guide for VoodooI2C is here: [Guide(Chinese)](http://bbs.pcbeta.com/viewthread-1824033-1-2.html).
#### OpenGL:
   * For video editors who use FinalCutPro and Davenci be aware that updating to 10.14.3 might cause [**OpenGL issue**](https://www.tonymacx86.com/threads/macos-10-14-0-thinkpad-x1-extreme-hackintosh.263916/post-1900369) that makes rendering take forever. (cr. [cthetoy](https://www.tonymacx86.com/members/cthetoy.152906/)).
   * However, with macOS 10.15 going all in with Metal 2 I do not suspect this will be an issue from now on. Programs using OpenGL will soon switch to Metal on macOS Catalina.
#### Samsung PM981 SSD:
   * Recently, people on TonyMacX86 are having **issue with PM981**. PM981 is troublesome for Hackintosh and I am not using it for install. I'm using a Toshiba XG3. However, you can check out [zysuper's repo](https://github.com/zysuper/Thinkpad-X1-extreme-EFI/blob/master/readme.md) on ACPI files to make PM981 working.
#### External Graphics Processing Unit (eGPU):
   * I finally solved eGPU. It is running smooth as hell using a RX570 in a Razer Core X. 
      * [Pictures of my setup and eGPU](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/tree/master/IMG/eGPU)
      * All you need to do in BIOS is:
         1. Enable Thunderbolt 3 support for Linux
         2. Disable iGPU so switch Display from "Hybrid" to "Discrete".
      * Then plug in your AMD eGPU, boot my EFI as usual, no extra steps.
      * If you are having problems, try boot in verbose mode (-v).
   * Now that I disabled my iGPU, what do I do when I don't use an eGPU?
      * Well, you enable iGPU in BIOS when you need it. Disable it again in BIOS when you need eGPU.
      * Or you kinda just don't use it on the go (Or until one day Apple work themselves out with NVIDIA then 1050Ti will work).
      * It is a trade off for eGPU, but it is something you can easily tolerate. I don't think it is a big deal.
      * What if I am in emergency and I want to use it on the go?
         * Well, you can. Just boot macOS normally. You will only have a 3MB since your NVIDIA card now serves as a basic display controller and 1024x768 resolution, but everything else than the graphics card should work. Use that to tackle your macOS emergencies. Shouldn't be a big deal.
   * Thanks for desmomarco999's guide, he worked it out on his XPS 13, but I used a different way. 
      * For sole appreciation, here is [his approach to enable TB3 on XPS 13](https://www.tonymacx86.com/threads/macos-10-15-0-thinkpad-x1-extreme-hackintosh.263916/post-1998309), and here's his [full guide](https://www.tonymacx86.com/threads/guide-how-to-use-egpu-with-any-laptop-equipped-with-thunderbolt-3.283179/).
#### USB External DisplayLink Output (NOT eGPU): 
   * [Plugable USB3-6950-HDMI](https://www.amazon.com/Plugable-Ethernet-Supports-Displays-3840x2160/dp/B075HMWLJF/ref=sr_1_fkmrnull_1?keywords=Plugable+USB3-6950-HDMI&qid=1555380658&s=gateway&sr=8-1-fkmrnull): Inspired by [Issue #13](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/13) I bought an adapter and was able to achieve 4K60P via USB3.0 and HDMI2.0. Now output issue is solved. You can download the driver here: 
      * [DisplayLink Driver](https://www.displaylink.com/downloads/macos). 
   * Relative question: 
      * [Will USB3-6950-USBC with USB-C plug work? (Issue #20)](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/20) Short answer, I don't know. You can buy one and try if you want to, although I don't see why it won't work so it might just work fine.
   * Alternative [Lenovo USB Dock (Issue #13)](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/13#issuecomment-507499718), a dock by Lenovo and I believe darkal tested it. (cr. [darkal](https://github.com/darkal))
   * However, it has its own limitations of [not being able to scale 4K into 1080P with 60FPS](http://assets.displaylink.com/live/downloads/release-notes/f1303_DisplayLink+USB+Graphics+Software+for+macOS+5.1-Release+Notes.txt). This is a known issue and we can only hope future update fix this.
      * New discovery (20190920):
         * There is actually one way to have the external display to do 4K60 with scaling. Here's how:
         * Use the two screens as separate displays:
            * One, make sure that both display is on (so the laptop screen is flipped up and open)
            * Two, make sure that the laptop is the main display (aka the dock is in the laptop's screen), and if you go to System Preference -> Display Preferences -> Arrangement you can see that the menu bar is in the laptop's internal screen. 
            * As long as the menu bar is in the internal screen and use the external 4k display as secondary, 4k60 works.
         * Use the two screens as one display (Recommended):
            * Also, another way is by clicking the [Mirror Displays] checkbox and leave the laptop screen on, and that will also work with 4k60. I find this most useful! And a much better experience.
            * Animation might lag a bit (Especially launchpad) but by looking at the mouse pointer move speed the display is running at 4K60. 
#### Camera:
   * [Issue #33](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/33#issuecomment-514062099) discussed about that macOS would use the integrated IR camera to make video calls which does not quite work.
   * This is fixed in v10.15.0.1.2, credit to [flymin](https://github.com/flymin), [kk1987](https://github.com/kk1987), and [ColeXJ](https://github.com/ColeXJ).
#### Undervolting:
   * By undervolting the computer, the fan is MUCH quieter and more pleasant to use.
   * I am using an app called [volta](https://volta.garymathews.com). 
      * You can also google for undervolting using script which I hasn't tried so do it in your own risk.
      * Unfortunately intel does not have a XTU software for macOS.
   * It is not free, but it is cheap. Just two cups of coffee gives you a much better experience.
      * You can download a "trial version" and try it out on your laptop. 
      * I didn't get money for advertising this...it just works. 
#### Replace Thermal Paste:
   * Recently I replaced my X1E's thermal paste and by doing so it gained significant performance.
      * About 5-7 degrees cooler. Now the fan doesn't even turn on under normal daily use.
   * I used Thermal Grizzly Kryonaut Thermal Grease Paste. (Note: I have no business relationship with them)
      * But if Thermal Grizzly sees this send me your advertising money plzzzzzzzzz
   * This is the teardown and repasting guide I used when I repasted my machine.
      * [Lenovo X1 Extreme Disassembly Repaste, TechTubers, 2019.](https://www.youtube.com/watch?v=_iWLfo2t4_U)
   * WARNING: It is possible for you to toast your machine if you replace your thermal paste! 
      * If you are not sure how good your craftmanship is, give it to a 3rd party repair shop.
#### About This Machine:
   * [System Report](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/SPEC.md): If you want to see system specs.
   * [IORegistry](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/docs/X1E-IORegistry.ioreg): For researchers who want to see my IORegistry, updated 20191018, EFI version v10.15.0.3.3.
   
#### Other Configurations:
| Owner | CPU | Model | Link |
| --- | --- | --- | --- |
| zysuper | i7-8850H | X1EG1 | [Link](https://github.com/zysuper/Thinkpad-X1-extreme-EFI) | 
| xuzhao9 | i7-8750H | X1EG1 | [Link](https://github.com/xuzhao9/ThinkPad-X1E-Hackintosh) |
| darkal | i7-8750H | X1EG1 | [Link](https://github.com/darkal/Hackintosh-Thinkpad-X1-Extreme) |
| ergonyc | i7-8850H | X1EG1 | [Link](https://github.com/ergonyc/BlackMac-ThinkPad-X1E) |
| flymin | i7-8750H | X1EG1 | [Link](https://github.com/flymin/Hackintosh-Thinkpad-X1-Extreme) |
| denerworator | i7-9750H | X1EG2 | [Link](https://github.com/denerworator/Muzi-X1-carbon-extreme-Gen-2) |

#### More Hackintosh EFI Resource:
   * Hackintosh Laptop Index: EFI for other laptop might help as a useful reference. Navigate to [here](https://github.com/daliansky/Hackintosh) (cr. [daliansky](https://github.com/daliansky)) if you need more reference from other laptops. Note: The word “链接” in Chinese means “link” so click on it it will take you to the repo you are looking for.

## Other Contributors
* Note: There is no order in the ranking of names. This list may not be complete! Feel free to let me know. Sorry for any inconvience.

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
| [Joaquim Barbosa](https://www.idownloadblog.com/author/joebarbosa/) | Guide to customize "About this Mac". |
| [oreziam](https://github.com/oreziam) | Solution for memory that exceeds 64G. |
| [xuzhao9](https://github.com/xuzhao9) | i7-8750H Config & AppleALC layout-id=21 |
| [Techtubers](https://www.youtube.com/channel/UC3vslADykSTKyYQ316zJOGQ) | Teardown and repaste guide. |

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

