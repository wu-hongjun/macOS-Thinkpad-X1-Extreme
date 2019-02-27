# Hackintosh for Thinkpad X1 Extreme
> This hackintosh you guys made, excited!  ——— [Zemin Jiang](https://errrneist.github.io/elder/).
### Developer: [@Errrneist](https://www.tonymacx86.com/members/errrneist.1550861/)
### *Current Clover Version: 4772*
### *Current macOS Version: 10.14.0*
#### Don't forget to star this project if you like it!

## Update
##### Recent
* [20190227] darkal presented a interesting research direction for BT. See [discussion.](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/3#issuecomment-467381308)
* [20190225] Lenovo is issueing me yet another replacement unit. Development paused.
* [20190224] F!ck. My laptop is not powering up...again.
* [20190215] Start to work on my researches in the wiki page [About Boot Issue](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/wiki/Unknown-Issue-for-booting-into-macOS).
* [20190215] There is an unknown issue to boot into macOS. [Temporary Fix](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v10.14.0.SE) Read more above. 
* [20190120] Released [v10.14.0.2](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v10.14.0.2) according to andyy24 in [Issue#9](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/9) to fix a trackpoint issue.

##### Archive
* For earlier update logs, see [Past Update History Archive](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/tree/master/Updates).

## Instructions
##### Pre-Install
* *FORK* the project to your own repository and clone it to your machine using Github Desktop to make changes.
* For windows drivers, here is the [Driver for BRCM943602BAED](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v943602BAED.1) to get DW1830 working. Also, here is [Driver for BRCM943602CS](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v943602CS.1) if you try to use an [adapter](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/IMG/BCMAdapter.jpg) to install the native card used on macbook. These cards are not natively supported by Microsoft so download it before you swap out your wireless card.
##### Clover Bootloader
* If you want to download the EFI Clover Bootloader, you can check out the [Configuration Release](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases).
* Or, if you are interested in the theme I used, check it out over here: [Minimalism](https://github.com/Errrneist/Hackintosh-Theme-Minimalism).
* I recommend users to use [Clover Configurator](https://mackie100projects.altervista.org/download-clover-configurator/) to configure your config.plist to eliminate typos.
* If you cannot mount EFI via Clover Configurator, then here is a *[Guide for mounting EFI using TERMINAL](https://github.com/Errrneist/Hackintosh-Aero-15W/blob/master/Mount%20EFI%20on%20macOS.MD).*
##### Post-Install 
* If you want to see system specs, check out [System Report](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/tree/master/Hardware).
* Some might also experience [Time sync issues](https://www.tonymacx86.com/threads/fix-incorrect-time-in-windows-osx-dual-boot.133719/) between Windows and macOS. Here is a [Fix](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/timesync-v1.0) credit to [SwampFox82](https://www.tonymacx86.com/threads/fix-incorrect-time-in-windows-osx-dual-boot.133719/).
* Many people are experiencing (Including me) unknown issues to boot into macOS. I released a [special edition](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v10.14.0.SE) EFI configuration to at least boot into the OS and see what we can do. Read more in the release comment.
##### Discussions and News
* Here is another helpful alternative Thinkpad X1 Extreme Clover EFI configuration repository by [zysuper](https://github.com/zysuper/Thinkpad-X1-extreme-EFI). Please check out his work as well as some some issues are addressed in both of our repositories. Star his work as well!
* Bluetooth is not working. A lot of further work needs to be done here. [Intel is embedding BT chips into PCH which does not work in macOS.](https://www.guru3d.com/news-story/intel-makes-wireless-ac-9560-a-bit-more-embedded.html) We also have a long discussion in the issues so check it out if you are interested in this issue. Link below in the Pinned Discussions. After research (cr. [darkal](https://github.com/darkal)) we found out that using AC9560 and a USB-AC53 Nano would somehow implement the Bluetooth feature, so currently we are moving toward that direction.
* [Apple won't work with NVIDIA to release graphics card driver for 10.14](https://www.macrumors.com/2018/11/01/nvidia-comment-on-macos-mojave-drivers/). Currently, there is nothing we can do.
* Recently, people on TonyMacX86 are having issue with PM981. PM981 is troublesome for Hackintosh and I am not using it for install. I'm using a Toshiba XG3. However, you can check out [zysuper's repo readme.MD](https://github.com/zysuper/Thinkpad-X1-extreme-EFI/blob/master/readme.md) on ACPI files to make PM981 working.
* People are experiencing weird touchpad issues when boot windows from clover. So far not much can be done, so I recommend you to just set auto boot time in clover be 2sec or -1sec, and just use F12 to switch OS.

## Pinned Discussions
* [Main Post on TonyMacX86](https://www.tonymacx86.com/threads/macos-10-14-0-thinkpad-x1-extreme-hackintosh.263916/)
* [Bluetooth Issues with BCM94360 Devices](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/3) 


## Specifications
* [Hardware Specifications](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/tree/master/Hardware)

### Cheers, Errrneist.


