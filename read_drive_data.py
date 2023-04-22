from wipe_tools import *
from drive_tools import *
from psutil import *

def main():
    disks = get_list_of_drives()

    # for i in disks:
    #      print (i)


    # drive_to_analyse = input ("Enter Drive Number:")

    # if drive_to_analyse == 'c':
    #     print("Let's not mess with the main system")
    #     exit()
    # else:
    #     size = get_partition_size(drive_to_analyse)
    #     print("Drive Size:" + str(size) + " bytes")
    #     check_blank(drive_to_analyse,0, 3)
    #     # write_drive(drive_to_analyse, b'\x00', 1)
    #     # check_blank(drive_to_analyse,0, 2)


if __name__ == "__main__":
        main()  # Already an admin here.

# wmi = win32com.client.GetObject ("winmgmts:")
# for usb in wmi.InstancesOf ("Win32_USBHub"):
#     print (usb.DeviceID)

