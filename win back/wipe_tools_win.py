from  drive_tools import *
import win32com.client
import win32api
import sys
import traceback
import os

def get_partition_size(drive_name):
    return os.path.getsize(fr"\\.\{drive_name}:")

def check_blank(drive_name, offset, size):
    print("blank check in process")
    print("starting at:" + str(offset))
    try:
        with open_windows_partition_read(drive_name) as drive_to_read:
            # drive_to_read.seek(offset)
            drive_to_read.seek(-1,2)
            print(drive_to_read.tell())
            drive_to_read.seek(0,0)
            
            for i in range(size):
                print("posn:" + str(drive_to_read.tell()))
                data = drive_to_read.read(16)
                if data != 0:
                    print(data) 
    except:
        print ("Drive not found")

def write_drive(drive_name, write_bits, size):
    print("write in process")
    print("starting at: 0")
    print("Writing:" + str(write_bits))
    try:
        with open_windows_partition_write(drive_name) as drive_to_write:
            # drive_to_read.seek(offset)
            for i in range(size):
                print("posn:" + str(drive_to_write.tell()))
                data = drive_to_write.write(write_bits)
    except BaseException as ex:
    # Get current system exception
        ex_type, ex_value, ex_traceback = sys.exc_info()

        # Extract unformatter stack traces as tuples
        trace_back = traceback.extract_tb(ex_traceback)

        # Format stacktrace
        stack_trace = list()

        for trace in trace_back:
            stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))

        print("Exception type : %s " % ex_type.__name__)
        print("Exception message : %s" %ex_value)
        print("Stack trace : %s" %stack_trace)