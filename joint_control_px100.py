# Copyright 2022 Trossen Robotics

import numpy as mp

from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS

def main():

    joint_1= 90    # -180 to 180 waist 90
    joint_1= joint_1*mp.pi/180

    joint_2=-45     #-111 to 107  shoulder -25
    joint_2= joint_2*mp.pi/180

    joint_3= 0    #-121 to 92   elbow  -45
    joint_3= joint_3*mp.pi/180

    joint_4= 45    #-100 to 123   waist angle 35
    joint_4= joint_4*mp.pi/180

    #gripper_joint = 50
       
    # TODO: Define the joint angles in radians considering the joint limits
    joint_positions = [joint_1, joint_2, joint_3, joint_4]

    bot = InterbotixManipulatorXS(
        robot_model='px100',
        group_name='arm',
        gripper_name='gripper'
    )
    bot.arm.go_to_home_pose()
    bot.arm.set_joint_positions(joint_positions)
    #bot.arm.go_to_home_pose()
    #bot.arm.go_to_sleep_pose()

    bot.shutdown()

if __name__ == '__main__':
    main()