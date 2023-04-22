sudo mkfs -t vfat /dev/sda1


sudo dd if=/dev/zero of=/dev/sda1 bs=4096 status=progress