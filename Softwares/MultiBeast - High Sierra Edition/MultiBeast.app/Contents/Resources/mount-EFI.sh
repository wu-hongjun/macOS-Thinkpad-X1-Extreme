#!/bin/bash
#
# Script for mounting EFI partition on $volume
#
#	Usage:
#
#		mount-EFI.sh "Destination volume name in double quotes"
#
#	Return Codes:
#
#		0 - EFI partition for $volume is present, mounted and contains Clover config.plist
#		1 - EFI partition for $volume does not contain a Clover config.plist
#		2 - Mount of EFI partition failed
#		3 - $volume is not formatted as GPT
#
# 	Copyright (C) tonymacx86 LLC

volume=$1

#
#	Function to test for Clover config.plist
#

plist () {
	if [ -s "/Volumes/EFI/EFI/CLOVER/config.plist" ]; then
		exit 0
	else
		diskutil quiet umount $1
		exit 1
	fi
}

#
#	Check $volume to see if it's a GPT disk
#

if [ `diskutil list "$volume" | grep -c FDisk_partition_scheme` -eq 1 ]; then
	exit 3
fi

#
#	If /Volumes/ESP/EFI/CLOVER/config.plist exists than Clover was just installed or updated
#

if [ -s "/Volumes/ESP/EFI/CLOVER/config.plist" ]; then	
	exit 0
fi

#
#	If there is more than one EFI partition mounted unmount all except for 1
#

if [ `mount | grep -c EFI` -gt 1 ]; then
	count=`mount | grep -c EFI`
	until [ $count -eq 1 ]; do
		let count-=1
		diskutil quiet umount "/Volumes/EFI $count"
		done
fi

#
#	Check for mounted EFI partition and see if it's for $volume
#	If the mounted EFI partition is not for $volume, unmount it
#

if [ `mount | grep -c EFI` -eq 1 ]; then
	EFI_Partition=`( mount | grep EFI | grep -o /dev/disk.s. )`
	if [ `mount | grep -c "$volume"` -eq 0 ]; then
		if [ `diskutil list / | grep -c "Physical Store"` -eq 1 ]; then		
			Destination_EFI=`diskutil list / | grep 'Physical Store' | awk '/disk?s?/{ print "/dev/"$3; }' | sed 's/s2/s1/'`
		else
			Destination_EFI=`(mount | grep " / " | awk '{gsub(/s2/,"s1"); print$1}')`
		fi
	else
		if [ `diskutil list "$volume" | grep -c "Physical Store"` -eq 1 ]; then			
			Destination_EFI=`diskutil list "$volume" | grep 'Physical Store' | awk '/disk?s?/{ print "/dev/"$3; }' | sed 's/s2/s1/'`
		else
			Destination_EFI=`mount | awk -v pattern="$volume" '$0 ~ pattern {sub(/s2 /, "s1 "); print$1}'`
		fi
	fi
	
	if [ "$EFI_Partition" == "$Destination_EFI" ]; then
		plist $EFI_Partition
	else
		diskutil quiet umount $EFI_Partition
	fi
fi

#
#	Find EFI partition for $volume
#

if [ `mount | grep -c "$volume"` -eq 0 ]; then
	if [ `diskutil list / | grep -c "Physical Store"` -eq 1 ]; then
		Destination_EFI=`diskutil list / | grep 'Physical Store' | awk '/disk?s?/{ print "/dev/"$3; }' | sed 's/s2/s1/'`
	else
		Destination_EFI=`(mount | grep " / " | awk '{gsub(/s2/,"s1"); print$1}')`
	fi
else
	if [ `diskutil list "$volume" | grep -c "Physical Store"` -eq 1 ]; then
		Destination_EFI=`diskutil list "$volume" | grep 'Physical Store' | awk '/disk?s?/{ print "/dev/"$3; }' | sed 's/s2/s1/'`
	else
		Destination_EFI=`mount | awk -v pattern="$volume" '$0 ~ pattern {sub(/s2 /, "s1 "); print$1}'`
	fi	
fi

#
#	Mount EFI partition for $volume and check for Clover config.plist
#

if diskutil quiet mount $Destination_EFI ; then
	plist $Destination_EFI
else
	exit 2
fi
