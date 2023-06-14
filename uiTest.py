import threading
import gi
import odrive
from odrive.utils import * # so that you can use dump_errors(odrive)
from odrive.enums import * # so that you can use "AXIS_STATE_..." without needing to put odrive.enums before

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


# func to calibrate in the background
def startCalib(odrive_instance):
    odrive_instance.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
    #dump errors after alibration sequence
    time.sleep(15)
    print("dumping errors")
    dump_errors(odrive_instance)

class MainWindow(Gtk.Window): 


    def __init__(self):
        super().__init__(title="MainWindow")
       
        # func to measure temp asynchronously (every 1.5 seconds)
        def measureTemp():
            threading.Timer(1.5, measureTemp).start()
            print("Measuring temp")
        
        #self.my_drive = None
        # connect to ODrive
        #print("finding ODrive")
        #self.my_drive = odrive.find_any()
        #print("found ODrive")

        #self.my_drive.axis0.controller.config.vel_gain = 0.1666666716337204
        #self.my_drive.axis0.controller.config.vel_integrator_gain = 0.3333333432674408
        #self.my_drive.axis0.controller.config.control_mode = 2
        #self.my_drive.axis0.controller.config.vel_limit = 10
        #self.my_drive.axis0.motor.config.current_lim =  15
        ## velocity Control Mode
        #self.my_drive.axis0.controller.config.control_mode = CONTROL_MODE_VELOCITY_CONTROL
        #self.my_drive.axis0.controller.config.vel_ramp_rate = 0.2
        #self.my_drive.axis0.controller.config.input_mode = INPUT_MODE_VEL_RAMP

        ##clear errors (sometimes errors get left over even on startup)
        #self.my_drive.clear_errors()
        ## set pre calib encoders/motors to false on first setup
        #self.my_drive.axis0.encoder.config.pre_calibrated = False
        #self.my_drive.axis0.motor.config.pre_calibrated = False

        ##start measuring temp 
        measureTemp() 

        ## calibrate encoders asynchronously (testing with index encoders)
        #calibration_thread = threading.Thread(target=startCalib, args=(self.my_drive,)) 
        #calibration_thread.start()

        # import image
        image = Gtk.Image()
        image.set_from_file("/home/standard/Downloads/PowerIcon.png")
        #image.set_pixel_size(70)

        # border around topmost level object in main window
        self.set_border_width(20)
        self.set_default_size(1280, 720)

        # top level box
        self.topBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.topBox)

        # box with buttons
        self.box1 = Gtk.Box(spacing=6)
        self.topBox.add(self.box1)

        # box with labels
        self.box2 = Gtk.Box(spacing=6)
        self.topBox.add(self.box2) 

        # box with power button
        self.powerBox = Gtk.Box(spacing=6)
        self.box1.add(self.powerBox)

        # button1 
        self.button1 = Gtk.Button(label="Low Regen")
        self.button1.connect("clicked", self.on_button1_clicked)
        # guessing "pack_start" is similar to leading_margin in iOS?
        self.box1.pack_start(self.button1, True, True, 0)

        # button2
        self.button2 = Gtk.Button(label="High Regen")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box1.pack_start(self.button2, True, True, 0)

        # button3
        self.button3 = Gtk.Button(label="Velocity 15 t/s")
        #self.button3.set_size_request(50, 50)
        #self.button3.add(image)
        self.button3.connect("clicked", self.on_button3_clicked)
        self.box1.pack_start(self.button3, True, True, 0)

        # label
        self.label1 = Gtk.Label(label="Label1")
        self.box2.pack_start(self.label1, True, False, 0)

    def on_button1_clicked(self, widget):
        print("Low Regen")
        self.label1.set_text("Low Regen")
        # doesn't work: self.button1.add(self.image)
        # ODrive: set regen to low (max negative current)
        self.my_drive.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
        self.my_drive.axis0.controller.input_vel = 0.0


    def on_button2_clicked(self, widget):
        print("High Regen")
        self.label1.set_text("High Regen")
        # ODrive: set regen to high (max negative current)


    def on_button3_clicked(self, widget):
        print("Velocity 15")
        self.label1.set_text("Velocity 15")
        self.my_drive.axis0.controller.input_vel = 15.0
    

    # func to measure temp asynchronously (every 1.5 seconds)
#    def measureTemp():
#        threading.Timer(1.5, measureTemp())
#        print("Measuring temp")
    #    m0Temp = self.my_drive.axis0.motor.fet_thermistor.temperature
    #    print("m0 temp: ", m0Temp)
    #    global m0FetTemp
    #    m0FetTemp = m0Temp


win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
