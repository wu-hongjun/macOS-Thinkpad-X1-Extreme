# Thinkpad X1 隐士一代 黑苹果
[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
> 你们搞的这个黑苹果啊, Excited!  ——— [那个改变了中国的男人](https://errrneist.github.io/elder/).
### 目前发布版本: [以首页为准](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases)
#### 开发者: [@厄尔尼斯特](https://www.tonymacx86.com/members/errrneist.1550861/)
#### 记得Star啊！先把这个读完再行动，不然很可能会搞爆电脑的！
#### 切记，中文页不会经常更新，一切以英文页面为最新，仅供参考！！！
<img align="middle" src="https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/IMG/sysinfo.png" alt="Sys Info" width="1000">

## 安装指示
##### 安装前
##### 你可以 *FORK* 这个仓库，方便你做关于你自己电脑的修改。
* Wifi转接器的Windows驱动:
    * [Windows Driver for BRCM94360CS2](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v943602CS.1): 如果你尝试使用 [BCM94360CS2/BCM94360CD 转 NGFF(M.2)Key A/E 转接卡](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/IMG/Readme.MD) 来安装原生Macbook网卡，请下载这个驱动。
    * [Windows Driver for BRCM943602BAED](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v943602BAED.1): 这个驱动是给戴尔DW1830的。
    * [Windows Driver for Asus USB-AC53](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/Softwares/ASUS_USB-AC53-Nano/Realtek-A1600_Comfast%20810-ASUS_AC53.zip): 这个驱动是给华硕USB-AC53 USB Wifi网卡驱动使用。
    * 和macOS免驱不同，在Windows下这些卡是没有默认驱动的，所以如果不事先下载好的话装完系统甚至会在Windows下无法联网。
* [Kinivo BTD-400 Bluetooth 4.0 Low Energy USB Adapter](https://www.amazon.com/Kinivo-BTD-400-Bluetooth-4-0-USB/dp/B007Q45EF4/ref=sr_1_fkmrnull_3?keywords=kinivo+bluetooth+dongle&qid=1555648213&s=gateway&sr=8-3-fkmrnull): 这是一个我自己之前买了试了挺好用的USB蓝牙接收器。如果你想买一个便宜的USB蓝牙接收器的话，可以试试这个。我之前用Airpods 2 很兼容。

##### 汇报问题
* 请将一切您的问题和新发现告诉我们！ 在 **Issues** 模块里写下您的新发现。
* 我也发现有很多同胞积极讨论，这很棒！但是如果可以的话请随手附上一份英语翻译，不会英语直接翻译器翻一下就好，这样我们就可以和全世界一起完善这个项目啦！

##### Clover启动器
* [我的配置文件](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases): 如果你想试试我自己用的配置文件，可以下载这个。
* [Minimalism-极简主题](https://github.com/Errrneist/Hackintosh-Theme-Minimalism): 这是我自用的极简主题。
* [Clover Configurator-启动器配置器](https://mackie100projects.altervista.org/download-clover-configurator/): 这个工具可以超级无敌十分方便地管理和配置你的config.plist文件。
* [用终端挂载EFI目录](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/MOUNTEFI.MD): 如果Clover Configurator不好用，可以试试用终端挂载EFI目录。
##### 安装后和已知问题
* Wifi问题:
    * [BCM94360CS2兼容性问题](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/15#issuecomment-477450037): 
       * BCM94360CS2和BCM943602CS是两张**不同的**卡！ 
       * BCM94360CS2简直是噩梦，千万不要买。
* 蓝牙问题:
   * **蓝牙**已经被搞定了！我们成功使用一根排线接入智能卡插槽解决了USB频道的问题。
   * 如果你想进一步阅读关于这个问题的更深细节，可以看看这个: [Issue #11](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/11)
   * 现在你可以在淘宝上购买到wdxxfu定制的[转接卡](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/11#issuecomment-498715154)了！感谢zysuper和wdxxfu做出的努力！
   * [这是一条关于英特尔将PCH芯片集成进CPU的新闻，解释了蓝牙问题的起因。](https://www.guru3d.com/news-story/intel-makes-wireless-ac-9560-a-bit-more-embedded.html) 
   * 你可以买一块定制板，或者像我自己一开始一样[自己焊](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/IMG/Readme.MD)来搞定蓝牙。
   * 不会焊别自己弄啊！很可能烧了你主板的！我不是开玩笑！
* 时间不同步问题:
   * [时间不同步问题](https://www.tonymacx86.com/threads/fix-incorrect-time-in-windows-osx-dual-boot.133719/): Windows和macOS切换时经常导致Windows时间不准，这里有一个[修复的方法](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/timesync-v1.0)，作者是 [SwampFox82](https://www.tonymacx86.com/threads/fix-incorrect-time-in-windows-osx-dual-boot.133719/)。
* 引导问题:
   * [极简特别版EFI配置文件](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/releases/tag/v10.14.0.SE): 好像很多人都莫名其妙的不能引导。
   * 我做了一个超级精简的仅用于引导的EFI配置文件，至少能让大家进系统，这个是给10.14.3写的，不知道更高的系统还好不好使。
* 触摸板问题:
    * 好多人通过Clover引导Windows都遇到了奇怪的**触摸板问题**。具体原因未知，但是也不是大问题，我推荐你在config里把auto boot设成2s或者-1s然后直接用F12切换硬盘来切换系统。
* OpenGL问题:
    * 如果您使用FinalCutPro或者Davenci，有可能在10.14.3（或更高）遇见[**OpenGL崩溃或者冻结**](https://www.tonymacx86.com/threads/macos-10-14-0-thinkpad-x1-extreme-hackintosh.263916/post-1900369)，或是渲染极慢。 (cr. [cthetoy](https://www.tonymacx86.com/members/cthetoy.152906/)).
* PM981问题:
    * 最近好多人都说**PM981**不认或者不好使。PM981一直都对黑苹果不怎么兼容，所以我自己用的是东芝XG3.但好像[zysuper](https://github.com/zysuper/Thinkpad-X1-extreme-EFI/blob/master/readme.md)搞定了，你可以去看看他的ACPI。
* 外接显示器问题: 
   * [Plugable USB3-6950-HDMI外界显示卡](https://www.amazon.com/Plugable-Ethernet-Supports-Displays-3840x2160/dp/B075HMWLJF/ref=sr_1_fkmrnull_1?keywords=Plugable+USB3-6950-HDMI&qid=1555380658&s=gateway&sr=8-1-fkmrnull): 有人提出了这个[问题](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/13)，我就去买了个USB外接显卡（真的有这种东西啊原来）而且还能做到4K 60FPS！！！你可以去他们的官网[下载驱动](https://www.displaylink.com/downloads/macos)。
   * 相关问题: [USB-C接口的6950好使吗？](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/issues/20) 简而言之，我也不知道，理论上应该没问题，但是我没买，所以咱也不敢说。
   * 但是这款卡不支持[视网膜分辨率的4K60FPS](http://assets.displaylink.com/live/downloads/release-notes/f1303_DisplayLink+USB+Graphics+Software+for+macOS+5.1-Release+Notes.txt)，只能靠后期厂商发布更新了。
* [系统参数](https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/SPEC.md): 如果你想看我电脑的配置可以点这个。
* 更多黑苹果资源:
   * [宁南的配置大全](https://github.com/daliansky/Hackintosh): 如果你需要找一些别的电脑做参考，这位[大佬](https://github.com/y010204025)整理出了一份非常全的笔记本配置合辑，可以去看看。

## 讨论与新闻
* [zysuper的配置](https://github.com/zysuper/Thinkpad-X1-extreme-EFI): 这位老哥写了一个非常棒的**另一个相似的X1E配置**。记得帮他也Star一下噢！
* [苹果并未与英伟达在10.14中合作发布N卡的驱动](https://www.macrumors.com/2018/11/01/nvidia-comment-on-macos-mojave-drivers/)。目前，只能等了，我的eGPU是英伟达的，所以也没办法测试eGPU了，有人有AMD的eGPU可以帮忙测试一下然后告诉我们！

## 许可
* 这个项目是基于[996许可](https://github.com/996icu/996.ICU/blob/master/LICENSE)，旨在支持程序员反996运动。

## 捐助
* 捐助这个开源的项目完全取决于您的个人意愿。
* 但是如果您想给我买杯咖啡的话，可以扫描下面的微信支付或Venmo二维码，谢啦！
<img align="middle" src="https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/IMG/wechatpay.jpg" alt="wechatpay" width="300">
<img align="middle" src="https://github.com/Errrneist/Hackintosh-Thinkpad-X1-Extreme/blob/master/IMG/venmo.jpg" alt="venmo" width="300">

### 厄尔尼斯特，二零一九年六月十五于西雅图

