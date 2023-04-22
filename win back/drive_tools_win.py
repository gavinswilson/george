import win32com.client
import win32api

def open_physical_drive(
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


def open_windows_partition_read(
    letter,
    mode="rb",
    buffering=-1,
    encoding=None,
    errors=None,
    newline=None,
    closefd=True,
    opener=None,
):
    """
    Opens a partition of a windows drive letter in read binary mode by default
    """
    return open(
        fr"\\.\{letter}:", mode, buffering, encoding, errors, newline, closefd, opener
    )

def open_windows_partition_write(
    letter,
    mode="wb",
    buffering=-1,
    encoding=None,
    errors=None,
    newline=None,
    closefd=True,
    opener=None,
):
    """
    Opens a partition of a windows drive letter in read binary mode by default
    """
    return open(
        fr"\\.\{letter}:", mode, buffering, encoding, errors, newline, closefd, opener
    )

def get_list_of_drives():
    drives = win32api.GetLogicalDrives()
    # print(drives)
    num_bits = 8
    bits = [(drives >> bit) & 1 for bit in range(num_bits - 1, -1, -1)]
    bits.reverse()
    return bits
