# IMPORTS
from beagle_py import *

# GLOBALS
beagle = 0
Zero_Counter=0

# UTILITY FUNCTIONS
def TIMESTAMP_TO_NS (stamp, samplerate_khz):
    return (stamp * 1000L) / (samplerate_khz/1000L)

def print_general_status (status):
    """ General status codes """

    if (status == BG_READ_OK) :
        print "OK",

    if (status & BG_READ_TIMEOUT):
        print "TIMEOUT",

    if (status & BG_READ_ERR_MIDDLE_OF_PACKET):
        print "MIDDLE",

    if (status & BG_READ_ERR_SHORT_BUFFER):
        print "SHORT BUFFER",

    if (status & BG_READ_ERR_PARTIAL_LAST_BYTE):
        print "PARTIAL_BYTE(bit %d)" % (status & 0xff),

def print_i2c_status (status):
    """I2C status codes"""
    if (status & BG_READ_I2C_NO_STOP):
        print "I2C_NO_STOP",

# I2C DUMP FUNCTION
def i2cdump (max_bytes, num_packets):
    Zero_Counter=0    ####<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   Zero COuntetr
    # Get the size of the timing information for a transaction of
    # max_bytes length
    timing_size = bg_bit_timing_size(BG_PROTOCOL_I2C, max_bytes)

    # Get the current sampling rate
    samplerate_khz = bg_samplerate(beagle, 0)

    i = 0

    # Start the capture
    if (bg_enable(beagle, BG_PROTOCOL_I2C) != BG_OK):
        print "error: could not enable I2C capture; exiting..."
        #sys.exit(1)

    #print "index,time(ns),I2C,status,<addr:r/w>(*),data0 ... dataN(*)"
    sys.stdout.flush()

    # Allocate the arrays to be passed into the read function
    data_in = array_u16(max_bytes)
    timing  = array_u32(timing_size)

    # Capture and print each transaction
    while (i < num_packets or num_packets == 0):
        # Read transaction with bit timing data
        (count, status, time_sop, time_duration,
         time_dataoffset, data_in, timing) = \
            bg_i2c_read_bit_timing(beagle, data_in, timing)

        # Translate timestamp to ns
        time_sop_ns = TIMESTAMP_TO_NS(time_sop, samplerate_khz)

        #print "%d,%u,I2C,(" % (i, long(time_sop_ns)),    ##############################################

        if (count < 0):
            print "error=%d," % count,

        #print_general_status(status)  #######################################
        #print_i2c_status(status) ##########################################
        #sys.stdout.write( " )") #######################################

        # Check for errors
        i += 1
        if (count <= 0):
            print " "
            sys.stdout.flush()
            if (count < 0):
                break

            # If zero data captured, continue
            continue

        # Print the address and read/write
        #####sys.stdout.write(",")
        offset = 0
        if (not (status & BG_READ_ERR_MIDDLE_OF_PACKET)):
            # Display the start condition
            #####sys.stdout.write( "[S] ")

            if (count >= 10):
                # Determine if byte was NACKed
                nack = (data_in[0] & BG_I2C_MONITOR_NACK)

                # Determine if this is a 10-bit address
                if (count == 1 or (data_in[0] & 0xf9) != 0xf0 or nack):
                    # Display 7-bit address
                    print "%02x:" % (long(data_in[0] & 0xff) >> 1),   #####"<%02x:"
                    if (data_in[0] & 0x01):
                        sys.stdout.write("r>")
                    else:
                        sys.stdout.write("")  ######("w>")

                    if (nack):
                        sys.stdout.write("* ")
                    else:
                        sys.stdout.write(" ")
                    offset = 1

                else:
                    # Display 10-bit address
                    print "<%03x:" %  ((data_in[0] << 7) & 0x300) \
                                     | (data_in[1] & 0xff),
                    if (data_in[0] & 0x01):
                        sys.stdout.write("r>")
                    else:
                        sys.stdout.write("")  ######("w>")

                    if (nack):
                        sys.stdout.write("* ")
                    else:
                        sys.stdout.write(" ")
                    offset = 2

        # Display rest of transaction
        count = count - offset
        
        if (count >20):  ######################################################################################
            s=""
            for d in data_in:
                s +="%02x "%d
                #'{0:x}'.format(int(s))
            #print s
            
            f=open("E:\i2c_code_python\Python\LCDData.txt","wb")
            f.write(s)
            f.close
            Zero_Counter=Zero_Counter+1
            print ("ALPHA")
            

            
            #print (data_in)
            for n in range(count):
            # Determine if byte was NACKed
                nack = (data_in[offset] & BG_I2C_MONITOR_NACK)

                sys.stdout.write("%02x" % long(data_in[offset] & 0xff))
                if (nack):
                    sys.stdout.write("* ")
                else:
                    sys.stdout.write(" ")
                offset += 1
        

        # Display the stop condition
        #####if (not (status & BG_READ_I2C_NO_STOP)):
            #####sys.stdout.write("[P]")

        print ""
        sys.stdout.flush()

    # Stop the capture
    bg_disable(beagle)
    #return Zero_Counter
    if Zero_Counter==0:
        f=open("E:\i2c_code_python\Python\LCDData.txt","wb")
        f.write("7c 80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ")
        f.close
        print ("CLOSED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
import time
	
	
#######print "Searching for Beagle adapters..."

# Find all the attached devices
(num, ports, unique_ids) = bg_find_devices_ext(16, 16)

if num > 0:
    #print "%d device(s) found:" % num #####################################################
    # Print the information on each device
    for i in range(num):
        port      = ports[i]
        unique_id = unique_ids[i]

        # Determine if the device is in-use
        inuse = "(avail)"
        if (port & BG_PORT_NOT_FREE):
            inuse = "(in-use)"
            port  = port & ~BG_PORT_NOT_FREE

        # Display device port number, in-use status, and serial number
        #print "    port = %d   %s  (%04d-%06d)" % \
            (port, inuse, unique_id / 1000000, unique_id % 1000000)

else:
    print "No devices found."
	
	
	
	


# MAIN PROGRAM
port       = 0      # open port 0 by default
samplerate = 10000  # in kHz
timeout    = 500    # in milliseconds
latency    = 200    # in milliseconds
length     = 0
pullups    = BG_I2C_PULLUP_OFF
target_pow = BG_TARGET_POWER_OFF
num        = 0

print "Begin Program"






length = 1    #int(sys.argv[1])
num = 1   #int(sys.argv[2])

# Open the device
beagle = bg_open(0)
if (beagle <= 0):
    print "Unable to open Beagle device on port %d" % port
    print "Error code = %d" % beagle
    time.sleep (20)
    #sys.exit(1)

#######print "Opened Beagle device on port %d" % port

# Set the samplerate
samplerate = bg_samplerate(beagle, samplerate)
if (samplerate < 0):
    print "error: %s" % bg_status_string(samplerate)
    time.sleep (20)
    #sys.exit(1)

#######print "Sampling rate set to %d KHz." % samplerate

# Set the idle timeout.
# The Beagle read functions will return in the specified time
# if there is no data available on the bus.
bg_timeout(beagle, timeout)
#######print "Idle timeout set to %d ms." %  timeout

# Set the latency.
# The latency parameter allows the programmer to balance the
# tradeoff between host side buffering and the latency to
# receive a packet when calling one of the Beagle read
# functions.
bg_latency(beagle, latency)
#######print "Latency set to %d ms." % latency

bg_host_ifce_speed_string = ""

if (bg_host_ifce_speed(beagle)):
    bg_host_ifce_speed_string = "high speed"
else:
    bg_host_ifce_speed_string = "full speed"

#######print "Host interface is %s." % bg_host_ifce_speed_string

# There is usually no need for pullups or target power
# when using the Beagle as a passive monitor.
bg_i2c_pullup(beagle, pullups)
bg_target_power(beagle, target_pow)

x=0
Write_Zeros=0
while (x<100000000):
    print ""
    sys.stdout.flush()
    Counter= i2cdump (30,10)   #(length, num)
    time.sleep (.05)
    x=x+1
    print (Counter, "ZZZ")
    

# Close the device
print "I grow tired of this Sark. End of Line..."
time.sleep (2)
bg_close(beagle)

#sys.exit(0)

raw_input("P: ")
