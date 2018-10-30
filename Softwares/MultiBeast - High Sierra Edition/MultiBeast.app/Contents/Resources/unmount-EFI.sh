#!/bin/bash
#
# Script for unmounting EFI partition
#
#	Usage:
#
#		unmount-EFI.sh
#
#	Return Codes:
#
#		0 - EFI partition was unmounted
#		1 - EFI partition was not mounted
#
#	Copyright (C) tonymacx86 LLC

if [ `mount | egrep -c 'EFI|ESP'` -eq 1 ]; then
	if [ `diskutil list / | grep -c "Physical Store"` -eq 1 ]; then
		diskutil quiet umount `( mount | egrep 'EFI|ESP' | grep -o /dev/disk.s. )`
		exit 0
	else 
		diskutil quiet umount `( mount | egrep 'EFI|ESP' | grep -o /dev/disk.s. )`
		exit 0
	fi
else
	exit 1
fi
