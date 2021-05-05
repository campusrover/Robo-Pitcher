# Robo-Pitcher
A Robot which throws a ball to a specified distance

To run this program use the following steps:
  roslaunch rrbot_gazebo rrbot_world.launch
  roslaunch rrbot_control rrbot_control.launch 
  rosrun rrbot_control pitcher_stable.py 
Then simply place a ball into the carriage, enter the desired distance you want to throw the ball, and hit enter.
The ball must be resized to comfortably fit the receptacle. We recommend running the command:
  rosservice call /gazebo/set_model_state '{model_state: { model_name: unit_sphere, 
  pose: { position: { x: 1, y: 0.5 ,z: 4 }, orientation: {x: 0, y: 0.0, z: 0, w: 0.0 }
  }, twist: { linear: {x: 0.0 , y: 0 ,z: 0 } , angular: { x: 0.0 , y: 0 , z: 0.0 } } , 
  reference_frame: world } }'
This will automatically place the ball in the receptacle (so long as you have spawned in a unit_sphere, the default
sphere shape in gazebo).
The net model can simply be dragged, or reset using the same command given for the ball, but replacing unit_sphere 
with net under model_name, and changing the x y and z data under position. Note that the net is offset from the origin
by -5 meters, so your inputs should be translated accordingly.
