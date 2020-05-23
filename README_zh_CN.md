# Thinkpad X1 Extreme Gen I 黑苹果配置
[![macOS](https://img.shields.io/badge/macOS-10.15.2-orange)](https://www.apple.com/macos/catalina/)
[![Clover](https://img.shields.io/badge/Clover-5101-yellowgreen)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
[![BIOS](https://img.shields.io/badge/BIOS-N2EET43W%201.25-brightgreen)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
[![MODEL](https://img.shields.io/badge/Model-20MF000DUS-blue)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)

<img align="right" src="https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/IMG/catcritter.png" alt="Critter" width="250">

> 你们搞的这个黑苹果啊，excited!  ——— [他](https://hongjunwu.com/elder/).    
### 目前版本: [10.15-V3.7 LTS](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases)
#### 主要开发人员: [@厄尔尼斯特](https://www.tonymacx86.com/members/errrneist.1550861/)
#### 喜欢记得点个Star🤭
#### 把Readme.MD读了， 不然很容易搞爆电脑的！

## 更新

##### 最近 | [更新历史](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/UPDATES.md)
* [20200522] 把 10.15-V3.7 标为LTS版本，终于做完了，更一波中文翻译，圆满结束。

## 安装指示
##### 安装前
##### 你可以 *FORK* 这个仓库，方便你做关于你自己电脑的修改。
* Wifi转接器的Windows驱动:
    * [Windows Driver for BRCM943602CS](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v943602CS.1): 如果你尝试使用 [BCM94360CS2/BCM94360CD 转 NGFF(M.2)Key A/E 转接卡](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/IMG/Readme.MD) 来安装原生Macbook网卡，请下载这个驱动。
    * [Windows Driver for BRCM943602BAED](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v943602BAED.1): 这个驱动是给戴尔DW1830的。
    * [Windows Driver for Asus USB-AC53](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/Softwares/ASUS_USB-AC53-Nano/Realtek-A1600_Comfast%20810-ASUS_AC53.zip): 这个驱动是给华硕USB-AC53 USB Wifi网卡驱动使用。
    * 和macOS免驱不同，在Windows下这些卡是没有默认驱动的，所以如果不事先下载好的话装完系统甚至会在Windows下无法联网。

##### 汇报问题
* 请将一切您的问题和新发现告诉我们！ 在 **Issues** 模块里写下您的新发现。
* 我也发现有很多同胞积极讨论，这很棒！但是如果可以的话请随手附上一份英语翻译，不会英语直接翻译器翻一下就好，这样我们就可以和全世界一起完善这个项目啦！

##### Clover启动器
* [我的配置文件](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases): 如果你想试试我自己用的配置文件，可以下载这个。
* [Minimalism-极简主题](https://github.com/Errrneist/Hackintosh-Theme-Minimalism): 这是我自用的极简主题。
* [Clover Configurator-启动器配置器](https://mackie100projects.altervista.org/download-clover-configurator/): 这个工具可以超级无敌十分方便地管理和配置你的config.plist文件。
* [用终端挂载EFI目录](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/MOUNTEFI.MD): 如果Clover Configurator不好用，可以试试用终端挂载EFI目录。

## 安装后 和 已知问题
#### 定制 "关于本机":
   * 这里有一篇教程：[How to customize the “About This Mac” section of a Mac, Joaquim Barbosa](https://www.idownloadblog.com/2017/01/13/how-to-modify-about-this-mac-hackintosh/).

#### Wifi & Wifi转接卡:
  * Wifi问题:
      * [BCM94360CS2兼容性问题](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/15#issuecomment-477450037): 
         * BCM94360CS2和BCM943602CS是两张**不同的**卡！ 
         * BCM94360CS2简直是噩梦，千万不要买。
         * 简单来说，三根天线的好使，两根天线的不好使。
   * 一个macOS支持的无线网卡清单： [Inventory of supported/unsupported wireless cards, Hervé.](https://osxlatitude.com/forums/topic/11138-inventory-of-supportedunsupported-wireless-cards-2-sierra-catalina/)

#### 内存:
   * 一般来说内存是不会有什么问题的，除非你家里有矿用的64GB的内存，那可能会出点问题。([Issue #34](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/34#issuecomment-516447421))
   * 这个解决方法由 [oreziam](https://github.com/oreziam)提出，他简单说明了一下解决方法；
      * 注意：我并不清楚，也无法测试64GB内存的机器问题，你得直接去找oreziam（如果他有空的话）。
      * 你需要在注入系统内存多注入一条内存插槽，也就是你需要注入四条内存通道和五条内存插槽，然后理论上就没问题了。

#### 声卡 & AppleALC:
   * 如果你的声卡（即AppleALC.kext）不工作（例如v3.0）那就读一下下面的信息：
      * V3.0 和很多以前的版本使用了一个特别的 AppleALC.kext 并注入了 alcid=7.
      * 注意： 很多时候如果声卡不工作重启一下就ok了……
      * 如果AppleALC不工作:
         * 从Github下载最新的AppleALC.kext。
         * 删掉老的AppleALC换成新的AppleALC。
         * 把config里的注入 alcid=7 改成 alcid=21。
  
#### 32位程序不兼容问题:
   * 从macOS 10.15开始32位程序不再被兼容。
   * 32位程序在10.15上会导致登陆后自动重启。
   * 最常见的问题程序: Tuxera NTFS 2018 和 Steam.
      * Tuxera NTFS 2019 好像还是不太好使……？
   * 解决方法:
      * 疯狂重启，直到你能进系统。
      * 我用了Appcleaner来卸载Tuxera，好使。
  
#### 电池:
   * 在关闭盖子时电池有一个 [休眠掉电问题 (Issue #36)](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/36) (有稍微发热，但是没有完全启动那么热), 大概每小时掉5%电。
   * 如果出现这个问题，你需要patch你自己的DSDT。
      * 我懒得做了，因为我DSDT用的是zysuper的……日常不影响，反正就算我做了你们还是得自己做，我也就懒得动手了。~~有这个时间守望先锋和二次元老婆他不香吗~~

#### 蓝牙问题:
   * **蓝牙**已经被搞定了！我们成功使用一根排线接入智能卡插槽解决了USB频道的问题。
   * 如果你想进一步阅读关于这个问题的更深细节，可以看看这个: [Issue #11](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/11)
   * 现在你可以在淘宝上购买到wdxxfu定制的[转接卡](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/11#issuecomment-498715154)了！感谢zysuper和wdxxfu做出的努力！
   * [这是一条关于英特尔将PCH芯片集成进CPU的新闻，解释了蓝牙问题的起因。](https://www.guru3d.com/news-story/intel-makes-wireless-ac-9560-a-bit-more-embedded.html) 
   * 你可以买一块定制板，或者像我自己一开始一样[自己焊](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/IMG/Readme.MD)来搞定蓝牙。
   * 不会焊别自己弄啊！很可能烧了你主板的！我不是开玩笑！
  
#### 风扇:
   * 有些人可能遇到开机风扇不转的情况。 ([Issue #32](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/32))
   * 可以用BIOS更新解决 (1.17 -> 1.23).
  
#### Windows:
   * 再说一次，不要用Clover引导Windows！会导致莫名其妙的问题……
   * WINDOWS触摸板不响应:
     * 好多人通过Clover引导Windows都遇到了奇怪的**触摸板问题**。具体原因未知，但是也不是大问题，我推荐你在config里把auto boot设成2s或者-1s然后直接用F12切换硬盘来切换系统。
   * [时间不同步问题](https://www.tonymacx86.com/threads/fix-incorrect-time-in-windows-osx-dual-boot.133719/): Windows和macOS切换时经常导致Windows时间不准，这里有一个[修复的方法](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/timesync-v1.0)，作者是 [SwampFox82](https://www.tonymacx86.com/threads/fix-incorrect-time-in-windows-osx-dual-boot.133719/)。
  
#### 引导问题:
   * [极简特别版EFI配置文件](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v10.14.0.SE): 好像很多人都莫名其妙的不能引导。
   * 我做了一个超级精简的仅用于引导的EFI配置文件，至少能让大家进系统，这个是给10.14.3写的，不知道更高的系统还好不好使。
  
#### 触摸板，触摸屏，手势:
   * 最终我发现Acidanthera的VoodooPS2Controller.kext就足以开启触控和触摸板。
      * 但是还是需要VoodooI2C.kext! (Change merged in the 10.15.0.3.2 release)
   * 之前还做了一个触摸屏如何工作的视频，链接放在下面了：
      * [Touch screen gesture implementation on X1E, Errrneist, 2019.](https://youtu.be/mZ7sTGxccuc)
   * VoodooI2C.kext:
      * A interesting [discussion](https://www.tonymacx86.com/threads/macos-10-15-0-thinkpad-x1-extreme-hackintosh.263916/post-1986487) with [jamesxxx1997](https://www.tonymacx86.com/members/jamesxxx1997.2184482/) implies that (At least on 10.14) you can use [VoodooI2C.kext](https://github.com/alexandred/VoodooI2C) 可以用于开启触摸板和触摸屏手势。
         * 深度VoodoI2C教程: [Guide(Chinese)](http://bbs.pcbeta.com/viewthread-1824033-1-2.html).

#### OpenGL问题:
   * 如果您使用FinalCutPro或者Davenci，有可能在10.14.3遇见[**OpenGL崩溃或者冻结**](https://www.tonymacx86.com/threads/macos-10-14-0-thinkpad-x1-extreme-hackintosh.263916/post-1900369)，或是渲染极慢。 (cr. [cthetoy](https://www.tonymacx86.com/members/cthetoy.152906/)).
  
#### PM981问题:
   * 最近好多人都说**PM981**不认或者不好使。PM981一直都对黑苹果不怎么兼容，所以我自己用的是东芝XG3.
  
#### GPU 兼容:
   * AMD Radeon GPU 和 Intel UHD/Iris Pro Graphics 目前受 macOS 10.14.0 或更高支持。
   * 英伟达 RTX/GTX GPU 从10.14以后就不受支持了。
      * 帕斯卡 (GTX10XX series) 还能在10.13用web driver驱动, 图灵或更新 (RTX20XX series/GTX16XX series)就完全不能支持了。
   * 主要是英伟达和苹果闹掰了。希望以后能支持吧。
#### 外接显卡 (eGPU):
   * 终于搞定外接显卡了，丝滑。用的是一块RX570和一个Razer Core X. 
      * [我的设备照片](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/tree/master/IMG/eGPU)
      * 你需要干的事:
         1. 开启 Thunderbolt 3 support for Linux
         2. 禁用 iGPU - 把显卡从 "Hybrid" 切换到 "Discrete".
      * 插入AMD eGPU，开机，不需要额外步骤。
      * 如果有问题，试试看用 verbose mode (-v)引导.

#### USB DisplayLink 输出卡 (NOT eGPU): 
   * [Plugable USB3-6950-HDMI](https://www.amazon.com/Plugable-Ethernet-Supports-Displays-3840x2160/dp/B075HMWLJF/ref=sr_1_fkmrnull_1?keywords=Plugable+USB3-6950-HDMI&qid=1555380658&s=gateway&sr=8-1-fkmrnull): 在 [Issue #13](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/13) 讨论过DisplayLink，是确实好使的。  
      * 在这下载驱动: [DisplayLink Driver](https://www.displaylink.com/downloads/macos). 
   * 相关问题: 
      * [USB-C口的USB3-6950-USBC好使吗? (Issue #20)](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/20) 好使的！ [确认](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/13#issuecomment-573958928) by carlaiau.
   * 另外还有一款 [Lenovo USB Dock (Issue #13)](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/13#issuecomment-507499718), 联想的dock，darkal测试过。 (cr. [darkal](https://github.com/darkal))
   * 但它不能再4K下开Retina缩放并同时60帧（目测30） [not being able to scale 4K into 1080P with 60FPS](http://assets.displaylink.com/live/downloads/release-notes/f1303_DisplayLink+USB+Graphics+Software+for+macOS+5.1-Release+Notes.txt). 这是一个已知的软件问题，希望未来的驱动可以修复。
      * 绕过Bug实现4K缩放60帧 (20190920):
         * 镜像两个屏幕 (Recommended):
            * 只要勾选镜像两个屏幕（前提是你得有4K屏，FHD不清楚）就可以4K缩放60帧了。
            * 动画可能会卡（特别是Launchpad）但是从鼠标移速看确实是60帧了。
#### 摄像头:
   * [Issue #33](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/33#issuecomment-514062099) macOS会错误的使用红外摄像头（就没有影像了）
   * 我在 v10.15.0.1.2 里修复了, 感谢 [flymin](https://github.com/flymin), [kk1987](https://github.com/kk1987), 和 [ColeXJ](https://github.com/ColeXJ).
#### 降频:
   * 降个频发热会少很多。
   * 我用的工具是 [volta](https://volta.garymathews.com)，macOS没有Intel XTU。 
   * 付费软件，不过是一次性的也很便宜。

#### 换硅脂:
   * 最近换了硅脂，还是很有用的。温度降低5-7度。风扇都不怎么转了。用的是暴力熊的Thermal Grizzly Kryonaut Thermal Grease Paste. 
   * 拆机视频：
      * [Lenovo X1 Extreme Disassembly Repaste, TechTubers, 2019.](https://www.youtube.com/watch?v=_iWLfo2t4_U)
   * 警告：拆机有风险，不会拆就去找第三方维修人员吧。
      
#### OpenCore 及其他启动器相关:
   * 没有迁移到OpenCore启动器的计划。
   * 其他人对OpenCore做了适配： ([Issue #62](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/62)) 比如 1Revenger1 的配置 [链接](https://github.com/1Revenger1/X1-Extreme-OpenCore-Resources).
   * 我也不准备将 FakeSMC 替换为 VirtualSMC。我在2.x版本里做了一些尝试不过目前能用就继续用吧懒得折腾了。
   
#### 关于本机:
   * [系统报告](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/SPEC.md)
   * [IORegistry](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/docs/X1E-IORegistry.ioreg): 更新于 20191018, EFI version v10.15.0.3.3.
   
#### 其他配置文件:
| 开发者 | CPU | 机型 | 链接 |
| --- | --- | --- | --- |
| zysuper | Core i7-8850H | X1EG1 | [Link](https://github.com/zysuper/Thinkpad-X1-extreme-EFI) | 
| xuzhao9 | Core i7-8750H | X1EG1 | [Link](https://github.com/xuzhao9/ThinkPad-X1E-Hackintosh) |
| darkal | Core i7-8750H | X1EG1 | [Link](https://github.com/darkal/Hackintosh-Thinkpad-X1-Extreme) |
| ergonyc | Core i7-8850H | X1EG1 | [Link](https://github.com/ergonyc/BlackMac-ThinkPad-X1E) |
| flymin | Core i7-8750H | X1EG1 | [Link](https://github.com/flymin/Hackintosh-Thinkpad-X1-Extreme) |
| denerworator | Core i7-9750H | X1EG2 | [Link](https://github.com/denerworator/Muzi-X1-carbon-extreme-Gen-2) |
| p4555555555 | Xeon E-2176M | P1G1 | [Link](https://github.com/p455555555/Thinkpad-P1-EFI) |

#### 更多黑苹果资源:
   * [宁南的配置大全](https://github.com/daliansky/Hackintosh): 如果你需要找一些别的电脑做参考，这位[大佬](https://github.com/y010204025)整理出了一份非常全的笔记本配置合辑，可以去看看。

## 其他贡献者
* 注意： 排名不分前后！ 也许会有遗漏，欢迎私信。

| 名称 | 贡献 |
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

## 讨论与新闻
* [zysuper的配置](https://github.com/zysuper/Thinkpad-X1-extreme-EFI): 这位老哥写了一个非常棒的**另一个相似的X1E配置**。记得帮他也Star一下噢！
* [苹果并未与英伟达在10.14中合作发布N卡的驱动](https://www.macrumors.com/2018/11/01/nvidia-comment-on-macos-mojave-drivers/)。目前，只能等了，我的eGPU是英伟达的，所以也没办法测试eGPU了，有人有AMD的eGPU可以帮忙测试一下然后告诉我们！

## 许可
* 这个项目是基于[996许可](https://github.com/996icu/996.ICU/blob/master/LICENSE)，旨在支持程序员反996运动。

## 捐助
* 捐助这个开源的项目完全取决于您的个人意愿。
* 但是如果您想给我买杯咖啡的话，可以扫描下面的微信支付或Venmo二维码，谢啦！
<img align="middle" src="https://github.com/Errrneist/Hackintosh-Razer-Blade-Advanced/blob/master/IMG/donate.png" alt="donate" width="500">

### Cheers, Errrneist.

