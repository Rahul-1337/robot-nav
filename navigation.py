# navigating through poses

#!/usr/bin/env python3

from nav2_simple_commander.robot_navigator import BasicNavigator
from nav2_simple_commander.task_result import TaskResult
import rclpy

print("systumm paad denge")

def goThroughPoses(poses, behavior_tree=''):
    rclpy.init()
    nav = BasicNavigator()

    for pose in poses:
        # Set the initial pose
        init_pose = [0.0, 0.0, 0.0]  # Replace with your initial pose

        nav.setInitialPose(init_pose)
        nav.waitUntilNav2Active()  # If autostarted, else use lifecycleStartup()

        # Define the goal pose
        goal_pose = pose  # Uses the current pose in the list

        # Get the path and smooth it
        path = nav.getPath(init_pose, goal_pose)
        smoothed_path = nav.smoothPath(path)

        # Navigate to the goal pose
        nav.goToPose(goal_pose)
        while not nav.isTaskComplete():
            feedback = nav.getFeedback()
            if feedback.navigation_duration > 600:
                nav.cancelTask()

        # Check the navigation result
        result = nav.getResult()
        if result == TaskResult.SUCCEEDED:
            print('Goal succeeded!')
        elif result == TaskResult.CANCELED:
            print('Goal was canceled!')
        elif result == TaskResult.FAILED:
            print('Goal failed!')

    rclpy.shutdown()

poses = [[1.8, 1.5, 1.57], [2.0, -7.0, -1.57], [-3.0, 2.5, 1.57]] 
goThroughPoses(poses, behavior_tree='')
