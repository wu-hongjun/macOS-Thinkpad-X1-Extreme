# How to mount your EFI partition on macOS
* 1. Find the identifier number for your EFI partition by running: [diskutil list]
* 2. Make a directory for EFI to mount by running: [sudo mkdir /Volumes/EFI]
* 3. Mount the EFI partition with: [sudo mount -t msdos /dev/disk0s1 /Volumes/EFI]
#### (Replace disk0s1 with whatever identifier you have, but if it is the same, leave it.)
#### Your EFI partition should now be mounted.
