# Blender simulation
 
 The simulation primarily consists of the mobile robot following the pre-defined path while picking up, and dropping a ball on the way
 
 ## Base
  The base is made of a bevelled cuboid with metal materials, and 4 wheels with realistic materials.
  The wheels are driven by a driver that converts the current translational position to the proportional rotation of each wheel. This is done by using a driver in the rotation parameter and
  editing it in the Driver editor.
 
 ## 2 Degree of freedom arm
  The basic design of the arm is based on the CAD model prepared for the physical robot.
  The arm is contolled by an inverse kinematic armature that has "bones" linked to each link of the arm.
  The internal inverse kinematic solver within the software automatically sets the bone position and orientation according to the end effector position (after the setup has been completed)
 
 ## Gripper
  The gripper is also based on the CAD model prepared for the physical robot.
  The right gripper is controlled by the varying the rotation of the final link in the armature of the arm. The left gripper has a copy rotation constraint to mirror the rotation of the left half,
  this improves the accuracy and allows the control of both gripper halves using hard-coded values if needed.

 ## Path
  The path consists of a curve that is the parent of the base, applied by using a "Follow path" modifier.
  The path is set to update its curvature around the specific obstacles by essentially projecting it along the particular axes with a gap wherever the obstacles are present.
  The above projection along with a "smoothing" modifier allows the user to apply and update the path, taking obstacles into account.
  
 ## Ball pickup and dropping
  The ball is set to be the target of the end effector and is set to follow it through the use of object constraints,
  at the predefined point where the influence of said constraints is increased to the maximum value.
  Dropping the ball involves the opposite of the aforementioned operation, with the influence being decreased to the minimum, and a keyframe to lock the final position.
  
 Most of the functions performed by "TorHando" are procedural, and therefore are updated on the fly, except for a few particular keyframes that would have to be
 redefined/scaled manually according to the changes made.
