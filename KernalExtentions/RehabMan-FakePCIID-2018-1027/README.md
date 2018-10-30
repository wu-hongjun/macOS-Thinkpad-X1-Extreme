## FakePCIID.kext

The purpose of this kext is to attach to any IOPCIDevice so it can provide alternate PCI ID when another driver attached to the same device requests them.  This technique can be used instead of patching binaries that may check for supported device-ids (or other PCI IDs) in their IOService::probe or IOService::start method.

In order to attach FakePCIID to a given IOPCIDevice, an injector kext must be built that IOKit can use to match against. 
The FakePCIID.kext Info.plist has no built-in IOKitPersonalities, as it is generic and not built to suit a specific purpose.  The distribution ZIP provide has four such injector kexts, which are described below.  Custom injector kexts can be created for other devices.

Note: FakePCIID_Intel_HD_Graphics.kext works for HD4400 mobile, HD4600 mobile, HD4200 mobile, and HD4600 desktop.

In any case, a DSDT patch, FakeID configuration (Clover), or FakeProperties dictionary in the injector's Info.plist will be required to inject the properties that FakePCIID can read on the IOPCIDevice.  The properties used by FakePCIID are described later in this post.  The properties must be present on the PCIDevice that is being hooked (the direct parent of FakePCIID).


### Downloads:

Downloads are available on Bitbucket:

https://bitbucket.org/RehabMan/os-x-fake-pci-id/downloads/


### How to Install

In all cases, FakePCIID.kext must be installed with a kext installer (such as Kext Wizard).  The Release build should be used for normal installs.  It has a minimum of output to system.log.  For troubleshooting, the Debug build can be used.

The separate folder 'injectors' in the distribution zip contains two extra codeless kexts:

- AppleIntelKBLGraphicsFramebufferInjector_3e9x.kext: Used for spoofing unsupported CoffeeLake as KabyLake

- BroadcomWiFiInjector.kext: Used to load the native Broadcom WiFi kexts for unsupported devices.  To be used with AirportBrcmFixup.kext as replacement for FakePCIID_Broadcom_WiFi.kext (both will work, but with AirportBrcmFixup.kext, full functionality of FakePCIID.kext is not needed)

In order to cause the kext to be loaded against a particular device, you must also install the appropriate FakePCIID injector kext.  Currently, seven injectors are provided:

- FakePCIID_Intel_HD_Graphics.kext (formerly FakePCIID_HD4600_HD4400.kext): 
This kext will attach to `8086:0412`, `8086:0416`, `8086:0a1e`, `8086:041e`, `8086:0a16`, `8086:041a`, `8086:016a`, `8086:191d`,  `8086:162a`, `8086:5917`, `8086:3e91`, `8086:3e92`, `8086:1626`, `8086:1616`

  - `8086:0412` is HD4600 desktop (now the only GT2 device supported in Yosemite as of 10.10.2)
  - `8086:0a16` is HD4400 mobile.
  - `8086:0416` is HD4600 mobile.
  - `8086:0a1e` is HD4200 mobile.
  - `8086:041e` is HD4400 desktop.
  - `8086:041a` is P4600 server.
  - `8086:016a` is P4000 server.
  - `8086:191d` is P530 server.
  - `8086:162a` is P6300 server.
  - `8086:1616` is HD5500.  Some CPUs (i3-5005U for example), must spoof as 0x1626 to avoid hang at boot
  - `8086:5917` is HD620 KabyLake-R.
  - `8086:3e91` is UHD630 CoffeLake (typical 3e91 with i3 or other low-end CPUs)
  
  For HD4600, normally fake device-id of `8086:0412` will be injected for Yosemite, as Yosemite does not natively recognize `8086:0416`.  `8086:0412` is the native device-id for HD4600 desktop.
  By injecting `0412`, `AppleIntelFramebufferAzul` and `AppleIntelHD5000Graphics` will load.
  And since, FakePCIID will also be attached to these devices, it will successfully fool both kexts that the device an Intel HD4600 Desktop IGPU (0412).

  For P4000 support, inject device-id 0166 (HD4000).
  For P530 support, inject device-id 1912 (HD530).
  For P6300 support, inject device-id 1622 (HD6200)
  For HD620 KabyLake-R, inject device-id 5916 (HD620)
  For UHD630 CoffeeLake, inject device-id 3e92 (UHD630)

- FakePCIID_Intel_HDMI_Audio.kext:
This kext will attach to `8086:0c0c`, `8086:9d70`, `8086:9d71`, `8086:9d74`, `8086:a170`, `8086:a171`, `8086:a2f0`,  `8086:a348`, or `8086:9dc8`

  The purpose is to provide support for unsupported HDAU (native B0D3) or unsuppored HDEF (100-series, 200-series, 300-series) ) devices which provide HDMI-audio on Haswell(+) systems.  `8086:0c0c` is one such unsupported ID.  The other two `8086:0d0c`, and `8086:0a0c` are supported.  This kext, AppleHDAController, loads by PCI class, so you normally would not inject device-id for it, but to allow FakePCIID to work, you may need to inject RM,device-id (one of the supported IDs).  By default for Haswell HDAU, the kext injects RM,device-id=<0c 0a 00 00> (0x0a0c).  For 100-series and later HDEF, the kext injects RM,device-id=<70 a1 00 00> or <70 9d 00 00> depending on HDEF device-id (refer to the Info.plist).

  You can override it with a DSDT edit or ACPI injection via SSDT.

  For example (_DSM patch for HDAU device for FakePCIID and HDMI audio, if you wanted 0x0d0c instead of 0x0a0c):

```c
into method label _DSM parent_adr 0x00030000 remove_entry;
into device name_adr 0x00030000 insert
begin
Method (_DSM, 4, NotSerialized)\n
{\n
    If (LEqual (Arg2, Zero)) { Return (Buffer() { 0x03 } ) }\n
    Return (Package()\n
    {\n
        "RM,device-id", Buffer() { 0x0c, 0x0d, 0x00, 0x00 },\n
        "hda-gfx", Buffer() { "onboard-1" },\n
    })\n
}\n
end;
```

  In the case of Skylake 8086:9d70 or 8086:1a70, it is attaching to the HDEF device (usually called HDAS, but renamed to HDEF to match what Aple expects).  Skylake HDMI/DP audio codec is on HDEF along with onboard audio.  It injects RM,device-id=<70 a1 00 00> for 0x9d70 and RM,device-id=<70 9d 00 00> for 0xa170.  In other words, with these two device-ids, it will reverse them.  Try it if you have everything set correctly for HDMI/DP audio, but it is not working.  This was discovered by noting that Skylake HDMI audio works on the NUC6i7KYK (Skull Canyon), but not the other NUC6 devices.  It is quite system dependent.  Some computers need them swapped, others do not.  So test both with and without.

  This kext won't fix other problems/mistakes you may have with your HDMI/DP setup (eg. missing "hda-gfx", mismatched "layout-id" injection, incorrect or wrong framebuffer patches, or missing ACPI renames).


- FakePCIID_AR9280_as_AR946x:
  This kext will attach to `168c:0034` or `168c:002a`.

  This particular application of FakePCIID.kext is used in a situation where you have an AR9280 re-branded as some other device.  For example, with the Lenovo u430, it is useful to rebrand an AR9280 ias an AR946x as that device is allowed by the BIOS whitelist where AR9280 is not.
  By using FakePCIID, we can remap the PCI IDs back to AR9280 (`168c:002a`) even though the device itself is reporting `168c:0034`.


- FakePCIID_Broadcom_WiFi.kext (formerly FakePCIID_BCM94352Z_as_BCM94360CS2.kext)
  This kext will attach to `14e4:43b1`, `14e4:4357`, `14e4:4331`, `14e4:4353`, `14e4:432b`, `14e4:43ba`, `14e4:43a3`, or `14e4:43a0`.
  And also `106b:4e`, `14e4:4312`, `14e4:4313`, `14e4:4318`, `14e4:4319`, `14e4:431a`, `14e4:4320`, `14e4:4324`, `14e4:4325`, `14e4:4328`, `14e4:432c`, `14e4:432d`.

  Originally created for BCM94352Z, this particular application of FakePCIID.kext is used to emulate an authentic Apple Airport Extreme, when using a variety of supported Broadcom WiFi devices.


- FakePCIID_BCM57XX_as_BCM57765.kext:
   This kext will attach to numerous unsupported BCM57XX Ethernet devices in order to make the native drivers work for a wider variety of BCM Ethernet chipsets that are compatible, but not supported due to probe testing of PCI device-id/subdevice-id values.
   Further details here: http://www.tonymacx86.com/network/155984-fakepciid-broadcom-bcm57xx-network-oob.html


- FakePCIID_Intel_GbX.kext:
   This kext will attach to a number of Intel Ethernet devices in an attempt to make the Small Tree drivers for Intel chipset based cards work.
   Further details here: http://www.tonymacx86.com/network/156135-intel-network-adapters-os-x-small-tree-drivers.html


- FakePCIID_XHCIMux.kext
   This kext will attach to `8086:1e31`, `8086:9c31`, `8086:9cb1`, `8086:9c31`, and `8086:8cb1`
   This injector is a bit of an extension to normal FakePCIID duties.  It doesn't actually fake any PCI IDs.  Rather, it forces certain values to XUSB2PR (PCI config offset 0xD0) on the Intel XHCI USB3 controller.  The effect is to route any USB2 devices attached to the USB2 pins on the XHC ports to EHC1.  In other words, handle USB2 devices with the USB2 drivers instead of the USB3 drivers (AppleUSBEHCI vs. AppleUSBXHCI).

   So normally what is a complex "multiplex" DSDT patch (that is not well understood), is a simple kext install.

   Configuration properties and their defaults:
    RM,pr2-force <00 00 00 00>.  By default forces all XHCI ports to route USB2 devices to EHC1.
    RM,pr2-init <01>.  Will write RM,pr2-force value at startup if non-zero.
    RM,pr2-block <01>.  Will block writes to XUSB2PR if non-zero.
    RM,pr2m-block <01>.  No evidence that OS X drivers attempt to write XUSB2PRM (offset 0xD4), but since this kext relies on a valid value here (as provided by the BIOS), writes to it are blocked if non-zero.
    RM,pr2-honor-pr2m <01>:  Changes to XUSB2PR will be masked by XUSB2PRM if this is non-zero.
    RM,pr2-chipset-mask: Writes to XUSB2PR are masked by this value.  This is defined by the chipset documentation.  Default value depends on chipset.

   Refer to Intel 7/8/9-series chipset data sheet for more info.


In order to create your own injector, you should be familiar with IOKit matching and kext Info.plist files.  There is ample documentation available on developer.apple.com.  Use the existing injectors as a template to build your own.


### DSDT patches

FakePCIID.kext will return the vendor-id, device-id, subsystem-vendor-id, and subsystem-id as found in the IO registry under the associated IOPCIDevice.  In order to provide the correct/supported values, _DSM injection is employed (or FakeID with Clover).

For example, this is one such patch that might be used for HD4600:
```c
into method label _DSM parent_adr 0x00020000 remove_entry;
into device name_adr 0x00020000 insert
begin
Method (_DSM, 4, NotSerialized)\n
{\n
    If (LEqual (Arg2, Zero)) { Return (Buffer() { 0x03 } ) }\n
    Return (Package()\n
    {\n
        "device-id", Buffer() { 0x12, 0x04, 0x00, 0x00 },\n
        "AAPL,ig-platform-id", Buffer() { 0x06, 0x00, 0x26, 0x0a },\n
        "hda-gfx", Buffer() { "onboard-1" },\n
        "model", Buffer() { "Intel HD 4600" },\n
    })\n
}\n
end;
```

Note that the only property read by FakePCIID in the patch above is "device-id".  Also the "device-id" injection could have been provided by Clover's config.plist (FakeID) or by (as an example) Chimera's IGPDeviceID flag.

The "device-id" property is used both by FakePCIID and by IOKit matching. Generally this is OK, but for flexibility you can specify a different IDs to be used by FakePCIID by using the "RM," prefixed properties.  

So, a minimalist patch would be as follows:
```c
into method label _DSM parent_adr 0x00020000 remove_entry;
into device name_adr 0x00020000 insert
begin
Method (_DSM, 4, NotSerialized)\n
{\n
    If (LEqual (Arg2, Zero)) { Return (Buffer() { 0x03 } ) }\n
    Return (Package()\n
    {\n
        "RM,device-id", Buffer() { 0x12, 0x04, 0x00, 0x00 },\n
    })\n
}\n
end;
```

You would have to inject "device-id" and "ig-platform-id" to have working HD4600 using some other mechanism, of course.  But FakePCIID.kext can do its work with only "RM,device-id".

And this is the patch used in the AR9280 as AR946x scenario:
```c
into method label _DSM parent_label PXSX remove_entry;
into device label PXSX parent_label RP03 insert
begin
Method (_DSM, 4, NotSerialized)\n
{\n
    If (LEqual (Arg2, Zero)) { Return (Buffer() { 0x03 } ) }\n
    Return (Package()\n
    {\n
        "vendor-id", Buffer() { 0x8c, 0x16, 0x00, 0x00 },\n
        "device-id", Buffer() { 0x2a, 0x00, 0x00, 0x00 },\n
        "subsystem-id", Buffer() { 0x8F, 0x00, 0x00, 0x00 },\n
        "subsystem-vendor-id", Buffer() { 0x6B, 0x10, 0x00, 0x00 },\n
        "compatible", "pci168c,2a",\n
        "IOName", "pci168c,2a",\n
        "name", "pci168c,2a",\n
        "AAPL,slot-name", Buffer() { "AirPort" },\n
        "device_type", Buffer() { "AirPort" },\n
        "model", Buffer() { "Atheros 928x 802.11 b/g/n Wireless Network Adapter" },\n
    })\n
}\n
end;
```

For BCM94352Z as BCM94360CS2 the following DSDT patch is used:
```c
into device Label PXSX parent_label RP03 replace_content begin
Method (_DSM, 4, NotSerialized)\n
{\n
	If (LEqual(Arg2, Zero)) { Return (Buffer() { 0x03 } ) }\n
	Return (Package()\n
	{\n
		"vendor-id", Buffer() { 0xe4, 0x14, 0x00, 0x00 },\n
		"device-id", Buffer() { 0xa0, 0x43, 0x00, 0x00 },\n
		"subsystem-vendor-id", Buffer() { 0x6b, 0x10, 0x00, 0x00 },\n
		"subsystem-id", Buffer() { 0x34, 0x01, 0x00, 0x00 },\n
		"compatible", "pci14e4,43a0",\n
		"IOName", "pci14e4,43a0",\n
		"name", "pci14e4,43a0"
	})\n
}\n
end;
```

Please realize that the nodes PXSX and RP03 are specific to the subject DSDT.  In this case a Lenovo u430 laptop.

Again, a minimalist patch for the WiFi scenario would look like this:
```c
into method label _DSM parent_label PXSX remove_entry;
into device label PXSX parent_label RP03 insert
begin
Method (_DSM, 4, NotSerialized)\n
{\n
    If (LEqual (Arg2, Zero)) { Return (Buffer() { 0x03 } ) }\n
    Return (Package()\n
    {\n
        "RM,vendor-id", Buffer() { 0x8c, 0x16, 0x00, 0x00 },\n
        "RM,device-id", Buffer() { 0x2a, 0x00, 0x00, 0x00 },\n
        "RM,subsystem-id", Buffer() { 0x8F, 0x00, 0x00, 0x00 },\n
        "RM,subsystem-vendor-id", Buffer() { 0x6B, 0x10, 0x00, 0x00 },\n
    })\n
}\n
end;
```

Assuming that the function "compatible" served in the original example is with some other mechanism (an injector kext, or Clover configuration).

Properties supported by FakePCIID and their corresponding PCI configuration space offsets are listed below:

- Offset `0x00`: "vendor-id", "RM,vendor-id"
- Offset `0x02`: "device-id", "RM,device-id"
- Offset `0x2c`: "subsystem-vendor-id", "RM,subsystem-vendor-id"
- Offset `0x2e`: "subsystem-id", "RM,subsystem-id"

For more information on the PCI configuration space: http://en.wikipedia.org/wiki/PCI_configuration_space

### Build Environment

My build environment is currently Xcode 6.1, using SDK 10.6, targeting OS X 10.6.

### 32-bit Builds

This project does not support 32-bit builds, although it is probably not difficult to build one given the proper tools.

### Source Code:

The source code is maintained at the following sites:

https://bitbucket.org/RehabMan/os-x-fake-pci-id

https://github.com/RehabMan/OS-X-Fake-PCI-ID

### History

This kext was forked from the project originally named IntelHDMobileGraphics, and was first discussed here: http://www.tonymacx86.com/yosemite-laptop-support/145427-fix-intel-hd4400-hd4600-mobile-yosemite-47.html#post952079

The original repo is now renamed: https://github.com/the-darkvoid/OS-X-Fake-PCI-ID

So, originally a single purpose kext for Intel HD46000 graphics, it has been modified into a general purpose kext that can be used in many different scenarios.

Note: So far, https://github.com/the-darkvoid/OS-X-Fake-PCI-ID, and https://github.com/RehabMan/OS-X-Fake-PCI-ID are being kept in sync.

