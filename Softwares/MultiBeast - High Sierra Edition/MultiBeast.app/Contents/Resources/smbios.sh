#!/bin/bash
#
# Script for adding SMBIOS information into Clover
#
# Copyright (C) tonymacx86 LLC

# 1 = source plist
# 2 = destination folder containing config.plist
# 3 = fileName
# 4 = Python serial generator script

cp "${1}" "${2}"
cd "${2}"

/usr/libexec/PlistBuddy -c "Print SMBIOS:ProductName" "${2}/config.plist"
rc=$?
if [ $rc == "0" ]; then
	/usr/libexec/PlistBuddy -c "Delete SMBIOS" "${2}/config.plist"
	/usr/libexec/PlistBuddy -c "Add SMBIOS dict" "${2}/config.plist"
	/usr/libexec/PlistBuddy -c "Add SMBIOS:Trust bool" "${2}/config.plist"
fi

/usr/libexec/PlistBuddy -c "Merge ${3} SMBIOS" "${2}/config.plist"
rm "${2}/${3}"

# generate serial and replace
a=$("${4}" "${3}")
/usr/libexec/PlistBuddy -c "Set :SMBIOS:SerialNumber $a" "${2}/config.plist"

exit 0
