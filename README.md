# vt-ros-pipeline
Description
This project develops a low-latency communication pipeline using ROS 2 (Robot Operating System) to bridge the gap between neuro-signal acquisition and robotic actuation. Developed as a proof-of-concept for BCI (Brain-Computer Interface) research at Virginia Tech, the system translates classified EEG states into real-time motor commands.
Electrical Engineering & Systems Focus
Asynchronous Messaging: Utilized a Publisher/Subscriber architecture to handle non-blocking data streams between a Raspberry Pi (Sensor Node) and a PC-based Controller.
Signal Translation: Implemented a logic-gate inspired controller that maps discrete binary classifications (0/1) to continuous velocity vectors.
Hardware-in-the-Loop (HIL) Simulation: Validated the software stack in a virtualized environment to de-risk physical hardware integration and test timing jitter.
Repository Structure
mock_pi.py: Simulates the Raspberry Pi's GPIO output and EEG classification stream.
turtle_control.py: The "Control Brain" that processes incoming telemetry and publishes "geometry_msgs/Twist" commands.
