# Hackintosh for Thinkpad X1 Extreme
> This hackintosh you guys made, excited!  ——— [Zemin Jiang](https://errrneist.github.io/elder/).
### Current Release: [10.14.3-V1.3](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases)
#### *Current Clover Version: 4895*
#### *Current macOS Version: 10.14.3*
#### Developer: [@Errrneist](https://www.tonymacx86.com/members/errrneist.1550861/)
#### Don't forget to star this project if you like it!

## Update
##### Recent
* [20190320] Released [v10.14.3.1.3](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v10.14.3.1.3), a stable update.
* [20190317] darkal presented a somewhat decent [external display workaround](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/13) if you have a 1080P screen. 
* [20190315] So far so good with USB BT. The only issue left is display output, which so far nothing we can do.
* [20190314] Happy pi day humans.
* [20190311] Updated readme.MD regarding on an [OpenGL issue on 10.14.3](https://www.tonymacx86.com/threads/macos-10-14-0-thinkpad-x1-extreme-hackintosh.263916/post-1900369). 
* [20190307] New [VoodooPS2 Driver](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/3#issuecomment-470353880) add in multi-touch genture support. Released in [v10.14.3.1](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v10.14.3.1).
* [20190303] Updated to 10.14.3 and Clover v4895. 



##### Archive
* For earlier update logs, see [Past Update History Archive](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/tree/master/Updates).

## Instructions
##### Pre-Install
* *FORK* the project to your own repository and clone it to your machine using Github Desktop to make changes.
* For windows drivers, here is the [Driver for BRCM943602BAED](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v943602BAED.1) to get DW1830 working. Also, here is [Driver for BRCM943602CS](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v943602CS.1) if you try to use an [adapter](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/IMG/BCMAdapter.jpg) to install the native card used on macbook. If you are using a ASUS usb wifi adapter, also make sure to download [Driver for Asus USB-AC53](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/Softwares/ASUS_USB-AC53-Nano/Realtek-A1600_Comfast%20810-ASUS_AC53.zip). These cards are not natively supported by Microsoft so download it before you swap out your wireless card.
##### Clover Bootloader
* If you want to download the EFI Clover Bootloader, you can check out the [Configuration Release](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases).
* Or, if you are interested in the theme I used, check it out over here: [Minimalism](https://github.com/Errrneist/Hackintosh-Theme-Minimalism).
* I recommend users to use [Clover Configurator](https://mackie100projects.altervista.org/download-clover-configurator/) to configure your config.plist in order to eliminate typos.
* If you cannot mount EFI via Clover Configurator, then here is a *[Guide for mounting EFI using TERMINAL](https://github.com/Errrneist/Hackintosh-Aero-15W/blob/master/Mount%20EFI%20on%20macOS.MD).*
##### Post-Install 
* If you want to see system specs, check out [System Report](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/tree/master/Hardware).
* Some might also experience [Time sync issues](https://www.tonymacx86.com/threads/fix-incorrect-time-in-windows-osx-dual-boot.133719/) between Windows and macOS. Here is a [Fix](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/timesync-v1.0) credit to [SwampFox82](https://www.tonymacx86.com/threads/fix-incorrect-time-in-windows-osx-dual-boot.133719/).
* Many people are experiencing unknown issues to boot into macOS. I released a [special simplified edition](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v10.14.0.SE) EFI configuration to at least boot into the OS and see what we can do. Read more in the release comment.
## Discussions and News
* Here is another helpful **alternative Thinkpad X1 Extreme Clover EFI configuration** repository by [zysuper](https://github.com/zysuper/Thinkpad-X1-extreme-EFI). Please check out his work as well as some some issues are addressed in both of our repositories. Star his work as well!
* **Bluetooth** is not working. A lot of further work needs to be done here. [Intel is embedding BT chips into PCH which does not work in macOS.](https://www.guru3d.com/news-story/intel-makes-wireless-ac-9560-a-bit-more-embedded.html) We also have a long discussion in the issues so check it out if you are interested in this issue. Link below in the Pinned Discussions. After research (cr. [darkal](https://github.com/darkal)) we found out that using AC9560 and a USB-AC53 Nano would somehow implement the Bluetooth feature, so currently we are moving toward that direction. We are also exploring with BT USB adapter.
* [Apple won't work with NVIDIA to release graphics card driver for 10.14](https://www.macrumors.com/2018/11/01/nvidia-comment-on-macos-mojave-drivers/). Currently, there is nothing we can do. We also have not tweaked on Thunderbolt 3 since we don't have proper hardware to test it. However, if you just want to have a display output, a [USB3.0 to HDMI Adapter](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/13) is a decent option.
* Recently, people on TonyMacX86 are having **issue with PM981**. PM981 is troublesome for Hackintosh and I am not using it for install. I'm using a Toshiba XG3. However, you can check out [zysuper's repo readme.MD](https://github.com/zysuper/Thinkpad-X1-extreme-EFI/blob/master/readme.md) on ACPI files to make PM981 working.
* People are experiencing weird **touchpad issues** when boot windows from clover. So far not much can be done, so I recommend you to just set auto boot time in clover be 2sec or -1sec, and just use F12 to switch OS.
* For video editors who use FinalCutPro and Davenci be aware that updating to 10.14.3 might cause [**OpenGL issue**](https://www.tonymacx86.com/threads/macos-10-14-0-thinkpad-x1-extreme-hackintosh.263916/post-1900369) that makes rendering take forever. (cr. [cthetoy](https://www.tonymacx86.com/members/cthetoy.152906/)).

## Pinned Discussions
* [Main Post on TonyMacX86](https://www.tonymacx86.com/threads/macos-10-14-0-thinkpad-x1-extreme-hackintosh.263916/)
* [Bluetooth Issues with BCM94360 Devices](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/3) 


## Specifications
* [Hardware Specifications](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/tree/master/Hardware)

### Cheers, Errrneist.


