#!/bin/bash
# This script is written by : Himanshu Shekhar
# helped by : Colin Ian King
# first of all unmount the device 
umount /dev/sdX

# X can be identified using 
df -Th

# See if you can then clear the partition table, say by copying a bunch of zeros over the first few K
sudo dd if=/dev/zero of=/dev/sdX bs=512 count=16

# If that works, see if you can write zeros to the whole device without it failing.
#To easily see if the kernel can't write to the device, first clear the current kernel messages and throw them away using:

sudo dmesg -c > /dev/null

#..then zero the entire device:

sudo dd if=/dev/zero of=/dev/sdX bs=16M

#Then, check to see if the kernel has complained about the device, using:

dmesg

# However, if this works fine run fdisk or parted to create the partitions from clean, e.g. with fdisk I use:

sudo fdisk /dev/sdX
#Command (m for help): n
#Select (default p): p
#Partition number (1-4, default 1): 1
#First sector (2048-7796735, default 2048): <return>
#Last sector, +sectors or +size{K,M,G} (2048-7796735, default 7796735): <return>
#Command (m for help): t
#Hex code (type L to list codes): 6
#Command (m for help): w

#..note just press return for the First and Last sector questions,
#fdisk will chose the correct defaults (which will be different to my example above). And then format the partition with VFAT:

sudo mkfs.vfat /dev/sdX1

# and then remove and re-insert the drive. It should be cleanly formatted.
