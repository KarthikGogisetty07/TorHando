import datetime  
import telepot   
from telepot.loop import MessageLoop    
import RPi.GPIO as GPIO
import time
from time import sleep

# Use Board pin numbering
GPIO.setmode(GPIO.BOARD)

#Variable:
servoPin = 12

#setup of servo:
GPIO.setup(servoPin, GPIO.OUT)



# Getting date and time
now = datetime.datetime.now()


def handle(msg):
    # Receiving the message from telegram
    chat_id = msg['chat']['id'] 
    # Getting text from the message
    command = msg['text']   

    print ('Received:')
    print(command)

    # Comparing the incoming message to send a reply according to it
    if command == '/hi':
        bot.sendMessage (chat_id, str("Welcome to Torohando!!"))
    elif command == '/time':
        bot.sendMessage(chat_id, str("Time: ") + str(now.hour) + str(":") + str(now.minute) + str(":") + str(now.second))
    elif command == '/date':
        bot.sendMessage(chat_id, str("Date: ") + str(now.day) + str("/") + str(now.month) + str("/") + str(now.year))
    elif command == '/drop':
        #pwm setup:
        p = GPIO.PWM(servoPin, 50)
        p.start(0)
        
        def setAngle(angle):
            
            duty = (angle/18) + 2
            GPIO.output(servoPin, True)
            p.ChangeDutyCycle(duty)
            sleep(1)
            GPIO.output(servoPin, False)
            p.ChangeDutyCycle(duty) 
        
        # Set angle:
        setAngle(35)
        time.sleep(1)
        setAngle(30)
        time.sleep(1)
        #send a msg to bot after the task!
        bot.sendMessage(chat_id, str('TaskDone!'))
        
    elif command == '/thankyou':
        bot.sendMessage(chat_id, str('Your Welcome sir/mam!'))
        
    else:
        bot.sendMessage(chat_id, str('Sorry I cannot recognise that!'))
        
        

# Insert your telegram token below
bot = telepot.Bot('2119882606:AAEuEdm4Ro1Bg3tntPIPorCjNUx3xtQFKRM')
print (bot.getMe())

# Start listening to the telegram bot and whenever a message is  received, the handle function will be called.
MessageLoop(bot, handle).run_as_thread()
print ('Listening....')

while 1:
    sleep(10)
    