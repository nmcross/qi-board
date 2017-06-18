
# coding: utf-8

# In[ ]:


from RPi import GPIO
import time

# Cleanup at start is primarily used for iPython notebooks setting.  
#Otherwise no need to cleanup at start.
GPIO.cleanup()

# Set the LEDs and Button pins======
GPIO.setmode(GPIO.BOARD)
led5=7
led4=11
led3=13
led2=35
led1=37
reed=16
button5=18
button4=22
button3=15
button2=29
button1=31

GPIO.setup(led5, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led1, GPIO.OUT)

GPIO.setup(button5, GPIO.IN)
GPIO.setup(button4, GPIO.IN)
GPIO.setup(button3, GPIO.IN)
GPIO.setup(button2, GPIO.IN)
GPIO.setup(button1, GPIO.IN)
GPIO.setup(reed, GPIO.IN)


# In[ ]:


# Turn off all the LEDs as part of initialization.

GPIO.output(led5, GPIO.LOW)
GPIO.output(led4, GPIO.LOW)
GPIO.output(led3, GPIO.LOW)
GPIO.output(led2, GPIO.LOW)
GPIO.output(led1, GPIO.LOW)


# In[ ]:


def buttondown(input_pin):
    """
    Handles when a button is pressed.  
    Currently just handles the lighting of LED.
    
    Eventually this method should also handle sending/storing of message, 
    with LED lit only as confirmation of success.
    """;
#    print ("Down on pin", input_pin)
    if(input_pin == button5): 
        GPIO.output(led5, GPIO.HIGH)
        GPIO.output(led4, GPIO.LOW)
        GPIO.output(led3, GPIO.LOW)
        GPIO.output(led2, GPIO.LOW)
        GPIO.output(led1, GPIO.LOW)
    if(input_pin == button4): 
        GPIO.output(led4, GPIO.HIGH)
        GPIO.output(led5, GPIO.LOW)
        GPIO.output(led3, GPIO.LOW)
        GPIO.output(led2, GPIO.LOW)
        GPIO.output(led1, GPIO.LOW)
    if(input_pin == button3): 
        GPIO.output(led3, GPIO.HIGH)
        GPIO.output(led5, GPIO.LOW)
        GPIO.output(led4, GPIO.LOW)
        GPIO.output(led2, GPIO.LOW)
        GPIO.output(led1, GPIO.LOW)
    if(input_pin == button2): 
        GPIO.output(led2, GPIO.HIGH)
        GPIO.output(led5, GPIO.LOW)
        GPIO.output(led4, GPIO.LOW)
        GPIO.output(led3, GPIO.LOW)
        GPIO.output(led1, GPIO.LOW)
    if(input_pin == button1): 
        GPIO.output(led1, GPIO.HIGH)
        GPIO.output(led5, GPIO.LOW)
        GPIO.output(led4, GPIO.LOW)
        GPIO.output(led3, GPIO.LOW)
        GPIO.output(led2, GPIO.LOW)

    """
    Keep the LED lit for 500 ms and then turn everything off.
    Down side of using this mechanism is board is stalled while asleep and cannot register
    another button press.
    
    TODO: Suppose a user wants to record that a phone call has more than one purpose, may need to 
    create a mechanism that can handle multiple button presses.
    """;
    
    time.sleep(0.5)
    
    GPIO.output(led5, GPIO.LOW)
    GPIO.output(led4, GPIO.LOW)
    GPIO.output(led3, GPIO.LOW)
    GPIO.output(led2, GPIO.LOW)
    GPIO.output(led1, GPIO.LOW)
    

    
def reedconnect(input_pin):
    reed_on = GPIO.input(input_pin)
    if (reed_on): 
        #print ("Reed Disonnected")
        GPIO.output(led5, GPIO.LOW)
        GPIO.output(led4, GPIO.LOW)
        GPIO.output(led3, GPIO.LOW)
        GPIO.output(led2, GPIO.LOW)
        GPIO.output(led1, GPIO.LOW)

    else:
        #print ("Reed Connected")
        GPIO.output(led5, GPIO.HIGH)
        GPIO.output(led4, GPIO.HIGH)
        GPIO.output(led3, GPIO.HIGH)
        GPIO.output(led2, GPIO.HIGH)
        GPIO.output(led1, GPIO.HIGH)
        


# In[ ]:


# Add interrupt event detection.

GPIO.add_event_detect(button5, GPIO.FALLING, callback=buttondown,  bouncetime=500)
GPIO.add_event_detect(button4, GPIO.FALLING, callback=buttondown,  bouncetime=500)
GPIO.add_event_detect(button3, GPIO.FALLING, callback=buttondown,  bouncetime=500)
GPIO.add_event_detect(button2, GPIO.FALLING, callback=buttondown,  bouncetime=500)
GPIO.add_event_detect(button1, GPIO.FALLING, callback=buttondown,  bouncetime=500)
GPIO.add_event_detect(reed, GPIO.BOTH, callback=reedconnect, bouncetime=1000)


# In[ ]:


"""
switch = 0
count = 0
while(True):
    if (switch % 5 == 0):
        GPIO.output(led5, GPIO.LOW)
        GPIO.output(led4, GPIO.HIGH)
        switch=1
    elif (switch % 5 == 1):
        GPIO.output(led5, GPIO.HIGH)
        GPIO.output(led4, GPIO.LOW)
        switch=0
    time.sleep(0.1)

while GPIO.input(button1) == 1:
    time.sleep(0.01)
    
print("Blah")
""";

