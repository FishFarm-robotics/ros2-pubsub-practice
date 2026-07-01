# ROS 2 Pub/Sub Practice

> Part of [FishFarm Robotics](https://github.com/FishFarm-robotics) — SRCP (Semantic Robotics Control Platform)
>
> **Contributor**: 오현석

A minimal **ROS 2 (Python / rclpy)** package with a talker and a listener node —
a learning exercise for ROS 2 package structure, publishers, subscribers, and
timers. Kept for completeness alongside the larger robotics work.

## Nodes (`talker_listener/`)

- **`talker_node.py`** — publishes `std_msgs/String` (`"Hello, world! N"`) to
  `topic` every 0.5 s on a timer.
- **`listener_node.py`** — subscribes to `topic` and logs each message.

## Build & run

```bash
colcon build --packages-select talker_listener
source install/setup.bash
ros2 run talker_listener talker      # terminal 1
ros2 run talker_listener listener    # terminal 2
```
