# Robo-Pitcher
A Robot that throws a ball to a specified distance

Example robots and code for interfacing Gazebo with ROS

## Quick Start

Gazebo:

    roslaunch rrbot_gazebo rrbot_world.launch

ROS Control:

    roslaunch rrbot_control rrbot_control.launch 
    
Control Algorithm:

    rosrun rrbot_control pitcher_stable.py 

Example of Moving Joints:

    rostopic pub /rrbot/joint2_position_controller/command std_msgs/Float64 "data: -0.9"

## Make a throwing ball:
    
   Click the ball icon in tool bar in Gazebo to create a sphere
   
   Click the scalling tool in Gazebo in tool bar
   
   Size it down small enough such that it fits inside the box cartriage
   
## Loading ball:

   Open a different terminal tab, and enter the following command

    rosservice call /gazebo/set_model_state '{model_state: { model_name: unit_sphere, 
    pose: { position: { x: 1, y: 0.5 ,z: 4 }, orientation: {x: 0, y: 0.0, z: 0, w: 0.0 }
    }, twist: { linear: {x: 0.0 , y: 0 ,z: 0 } , angular: { x: 0.0 , y: 0 , z: 0.0 } } , 
    reference_frame: world } }'
    
## Throwing ball:


## Changing Net distance
   Open a different terminal tab, and enter the following command. (0 is default of -5 unit away from net)
   
    rosservice call /gazebo/set_model_state '{model_state: { model_name: net, 
    pose: { position: { x: 0, y: 0 ,z: 0 }, orientation: {x: 0, y: 0.0, z: 0, w: 0.0 }
    }, twist: { linear: {x: 0.0 , y: 0 ,z: 0 } , angular: { x: 0.0 , y: 0 , z: 0.0 } } , 
    reference_frame: world } }'

   Note that the net is offset from the origin by -5 meters, so your inputs should be translated accordingly.
