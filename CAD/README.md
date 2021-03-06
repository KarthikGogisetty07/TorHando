

# PROJECT TORHANDO - ROBOTIC ARM SEGMENT

Brief Intro: This segment of the project deals with attaching a 2 Degree of Freedom robotic arm to the turtlebot to perform pick and place operation of a table tennis ball (fixed payload).
One DOF would be a turning pair between link 1 and link 2 and the other DOF would be the grasping movement of the gripper.
The entire robotic arm including the gripper will be 3D printed and assembled together.

Base:

To make this arm as a completely independent segment, a balsa wood plate of dimension 13.2x10x3 has been cut such that it can be attached to the upper plate of the turtlebot using removable double tape. 

An area in this plate has been marked such that the base of the manipulator (circular in shape having diameter 7.5 cm) can be stuck using suitable adhesives. Hence when the robotic arm is to be disassembled from the turtlebot, it could be done so without any damage to the arm or turtlebot.



Link 1: 
Link 1 of the robotic arm has a complex geometry and a large thickness which takes a quite a lot of time to 3D print.
The reason behind this complex design is the need to accomodate the base, servo motor, servo extension shaft and the second link.
It would even consist of the text "TORHANDO" for aesthetic purposes, negatively extruded to produce a cut.

Link 2:
Link 2 of the robotic arm is a simple design with hollow space at the center for light weight. The end of this link is made flat to make space to fit the gripper.

The entire geometries of both links together has been assembled in such a way that maximum reach can be attained to pick the payload. This was found by using line diagrams and testing for extension.

## Screenshots
Joining link 1 and link 2
![Link 1 +Link 2](https://user-images.githubusercontent.com/69980210/144361636-6496709b-ef8f-4329-be9b-828ac2d59ef6.png)

Full assembly of the arm with the turtlebot
![Full assembly](https://user-images.githubusercontent.com/69980210/144361695-9368a907-9eb8-4c47-8f68-6b98e5b47a0c.png)
# Project Torhando- Gripper Construction

A gripper is a device that enables the robot to pick and 
hold an object to be manipulated.We are able to use gripper for 
multiple purposes such as inspection , assembly , pick and place
and machine tending.

Here we are designing a gripper for pick and place and object 
that is attached to the manipulator using fusion 360.


## Parts to be created 
We  have to make different parts and assembly then together 
to complete the gripper as a whole.

Necessary parts:-

1. Link 1 & 2:
 This link is the main body of the gripper that 
grabs the object which we want and it is a symmetrical body .
Refer to Pic 1.

2. Revet Type 1:
 This type of revet is used to connect the spur gear,link 1 and the servo motor shaft.
 Refer to Pic 2.

3. Revet Type 2:
 Revet that connect only the second spur gear and the second link.
Refer to pic 3.

4. Spur Gear:
 Spur gear used in our project where two similar gears are attached to link 1 and link 2 
 respectively.The gears are in a mesh .Refer to pic 4.

5. Base body:
It is build level the spur gear that we are trying mesh and this 
base is attached on top of the servo motor.Refer to pic 5.

6. Gripper Manipulator connector:
We need some sort of mechanism to connect the gripper to the manipulator.Refer to pic 6.

7. Gripper Manipulator Screw:
 To fix the gripper to the manipulator we are using screws.Refer to pic 7.

8. Servo Motor:
Another important part is the servo motor for the gripper to function properly.
Refer to pic 8.
## Images

Pic 1 ![Screenshot (23)](https://user-images.githubusercontent.com/93376324/143675529-d645806d-ecbf-4131-8293-00b3820c01b9.png)

Pic 2 ![Screenshot (26)](https://user-images.githubusercontent.com/93376324/143675592-70bb20b3-05dd-4ca3-8486-9c2a5affc932.png)

Pic 3 ![Screenshot (27)](https://user-images.githubusercontent.com/93376324/143675605-7c720ab6-d332-47ae-a4b2-f3a8fc1f0f02.png)

Pic 4 ![Screenshot (24)](https://user-images.githubusercontent.com/93376324/143675632-4b62c7e7-a871-459b-baa2-af35708cb41e.png)

Pic 5 ![Screenshot (29)](https://user-images.githubusercontent.com/93376324/143675648-e80827ae-418e-4a43-ae9c-97f78ad8981e.png)

Pic 6 ![Screenshot (30)](https://user-images.githubusercontent.com/93376324/143675654-58b304b8-2a52-4b66-a0da-1dfe253d5e42.png)

Pic 7 ![Screenshot (31)](https://user-images.githubusercontent.com/93376324/143675683-6cd62497-bd42-4db6-a58b-b3741c22e2ef.png)

Pic 8 ![Screenshot (32)](https://user-images.githubusercontent.com/93376324/143675700-c35c3fd3-a952-4450-9d6b-979f45e2aa03.png)

## Assembly
Here we cearted all the parts using 3D printer.

The process to covert fusion 360 model :
 To 3D print each models we have to export file as ".sml" and save in your local space.
 After that open fracktory software and open the sml file and prepare where it will show the time it will take to 
 print that specific material . We can also change infill of the maaterial(filament,here we used FLA) that we are using to print ,customize the temperature of the bed and nozzle of the printer and many other options.
 After preparing it will save as a gcode file in your local space.We can use to methods to sent gcode file to printer.
 One it is via USB and second is by typing the ip address of the print in a browser.Finally wee are able to print.


Hence, when all parts are downloaded we can assemble them together.Refer to pic 9.

Pic 9: ![Screenshot (33)](https://user-images.githubusercontent.com/93376324/143676135-ecadf6d3-f70c-4df8-8d1a-89db9c8abddf.png)
## Result and Final Process
Here we were able to complete the 3D print all parts and perform a sucessful pick and hold function.

The image below shows some parts print using 3D printer:

![b6cd93a3-795f-4d09-b2e4-137fd0b0af3b](https://user-images.githubusercontent.com/93376324/143676382-2f469dc1-7f59-4abb-80e8-999ac5aa4d2a.jpg)

Partial Assembly of the Gripper:

![c3d860f8-0b0e-438a-8595-f5505ff9d452](https://user-images.githubusercontent.com/93376324/143676403-bf0db80d-5e4a-4bf0-b1f4-20bd18068334.jpg)

Complete Assembly of the Gripper:

![complete assembly](https://user-images.githubusercontent.com/93376324/144376723-2f0af580-ceed-4445-b0cc-abcc3b9d547b.jpeg)



