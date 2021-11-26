## Telegram Bot to operate the End-effector-

#### Introduction:

##### The internet of things has seen a drastic climb in the past few years, it describes the physcial object that are embedded with sensors, actuators, software and many more. The level of IoT devices is often divided into different categories - Consumer, Commerical, Industrial and Infrastructure spaces.

![image](https://user-images.githubusercontent.com/69350191/143548231-d8170395-8644-43ed-b8b1-6ab8643b1abf.png)

##### In this project we focused on exchange of data from one device to another, replicating the concept of publish and subscribe that we learnt while exploring robot opereting system (ROS). The idea was to create a chat-bot to send data to the RPi-4. Hence, It comes under the category - consumer IoT which can be further developed and made an Industrial IoT system. Enormous growth is seen in the consumer application IoT devices dealing with home automations and bots with remote monitoring capabilities. The chat-bot is been created in Telegram using BotFather. 

![image](https://user-images.githubusercontent.com/69350191/143550061-74d4d42c-ca34-49c8-9920-3cc2565f6499.png)

##### BotFather is an open source platform to create custom bots. Once the chat-bot is created we need to write requried code for the Raspberry Pi that will make it respond to messages from the chat-bot. Before that, hook up the connections for the Raspberry Pi. We used a servo to move the endeffector to drop the ball, once it reached the desired location.

#### Process:

##### We need to first install teleport in the raspian, the requried library to establish communication between our Raspberry Pi-4 and our Telegram chat-bot. 

```
sudo pip install telepot
```

##### Once the libraries are installed, login to telegram using your mobile number. And create a chat-bot in BotFather. The process to create the chat-bot is as follows:

```
/start
```
###### Will start the Botfather chatbot.

```
/newbot
```
###### Will create a request pull to create a new chat-bot. Once the request is succeeded it will ask to give a unique name, and details of your chat-bot. Once done a token address will be generated which should be used in our code to establish the connection to our R-Pi and the telegram chat-bot.

#### Code explanation:

##### First, we added the required libraries for this project. The teleport library enables the Raspberry Pi to communicate with the Telegram bot using the API. The datetime library is used to get the date and time. The GPIO library is used to actuate the servo accordingly. 

```
import datetime  
import telepot   
from telepot.loop import MessageLoop    
import RPi.GPIO as GPIO
import time
from time import sleep
```

##### Now we are initialising and seting up few pins and variables requried in the code.

```
# Use Board pin numbering
GPIO.setmode(GPIO.BOARD)      
servoPin = 12
#setup of servo:
GPIO.setup(servoPin, GPIO.OUT)
```
##### The handle function is called each and every time the Pi recieves a message from the telegram bot, we read the message and separate the text from it and assign each text a case to perform a task.

```
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
    
        #start:
        
        p = GPIO.PWM(servoPin, 50) # GPIO 17 for PWM with 50Hz
        p.start(2.5) # Initialization
        i=0
        while i<2:
            #dutycycle!
    
            p.ChangeDutyCycle(5)
            time.sleep(0.5)
            p.ChangeDutyCycle(7.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(10)
            time.sleep(0.5)
            p.ChangeDutyCycle(12.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(10)
            time.sleep(0.5)
            p.ChangeDutyCycle(7.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(5)
            time.sleep(0.5)
            p.ChangeDutyCycle(2.5)
            time.sleep(0.5)
            
            #stop
            i=i+1
        
        # Clean all the gpio pins:
        GPIO.cleanup()
        
        #send a msg to bot after the task!
        bot.sendMessage(chat_id, str('TaskDone!'))        
    else:
        bot.sendMessage(chat_id, str('Thankyou!'))
```
##### We need to assign the bot token in the command below to start communication and perform the requried tasks. The bot.getMe() will check whether a connection between the Pi and the Telegram bot was made successfully by printing a response.

```
# Insert your telegram token below
bot = telepot.Bot('2119882606:AAEuEdm4Ro1Bg3tntPIPorCjNUx3xtQFKRM')
print (bot.getMe())
```

##### Now the below command will make sure that the RPi listens to the chat-bot, and when a message is recieved the handle function will be called to perform the called task.


#### Features of our Torhando:

```
/hi
```
##### Prints Welcome to Torhando.

```
/time
```
##### Prints the current time.

```
/date
```
##### Prints the date.

```
/drop
```
##### Performs the action requried - i.e. actuates the servo as per requriement and once the loop breaks, it prints TaskDone

##### An else block right now is kept to print thankyou but can be later used to add more features like integrating the bot with ros or any other APi's.

#### Conclusion:

##### Level-2 autonomy is been reached, where the commands are sent and the requried functionality is performed. The chat-bot can be trained more by adding sensor data there by identifying the spot on its own using the real-time data and drop the ball. A feature of picking the ball can also be added where the pose of the pick-up object is collected using the requried sensors like - ultrasonic sensor, 3D Sensors and many-more. We focus on proividing simulation results of results of level -4 autonomy in gazebo and Blender before prototyping and experimenting on the robot that we 3D printed.

###### Happy Experimenting :)
