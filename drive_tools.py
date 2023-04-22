from shutil import *
from psutil import *

def open_physical_drive_read(
    number,
    mode="rb",
    buffering=-1,
    encoding=None,
    errors=None,
    newline=None,
    closefd=True,
    opener=None,
):
    """
    Opens a physical drive in read binary mode by default
    The numbering starts with 0
    """
    return open(
        fr"\\.\PhysicalDrive{number}",
        mode,
        buffering,
        encoding,
        errors,
        newline,
        closefd,
        opener,
    )

def get_list_of_drives():
    # drives = disk_partitions()
    drive_info = disk_usage("/dev/sda1")
    print(drive_info)
    for i in drive_info:
        print(i)