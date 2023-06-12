import odrive
from odrive.utils import *
from odrive.enums import *

print("finding odrive")
my_drive = odrive.find_any()
print("Found Odrive")

my_drive.axis0.controller.config.vel_gain = 0.1666666716337204
my_drive.axis0.controller.config.vel_integrator_gain = 0.3333333432674408
my_drive.axis0.controller.config.control_mode = 2
my_drive.axis0.controller.config.vel_limit = 10
my_drive.axis0.motor.config.current_lim =  15
# velocity Control Mode
my_drive.axis0.controller.config.control_mode = CONTROL_MODE_VELOCITY_CONTROL
my_drive.axis0.controller.config.vel_ramp_rate = 0.2
my_drive.axis0.controller.config.input_mode = INPUT_MODE_VEL_RAMP

#clear errors (sometimes errors get left over even on startup)
my_drive.clear_errors()
# set pre calib encoders/motors to false on first setup
my_drive.axis0.encoder.config.pre_calibrated = False
my_drive.axis0.motor.config.pre_calibrated = False
# calibrate encoders (testing with index encoders)
my_drive.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
#dump errors after alibration sequence
time.sleep(15)
print("dumping errors")
dump_errors(my_drive)

my_drive.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
my_drive.axis0.controller.input_vel = 5.5
