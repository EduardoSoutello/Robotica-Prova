#!/usr/bin/env python

import sys
import rospy
import time
from geometry_msgs.msg import Twist
from std_msgs.msg import String

PI = 3.1415926535897

velocidade_linear = 1
velocidade_angular = 1

def move():
	global velocidade_linear
	global velocidade_angular
		

	rospy.init_node('teleop_tartaruga_jose_eduardo', anonymous=True)
	velocidade_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
	vel_msg = Twist()

	while(1):
		
		temp = String()
		temp = getchar()
		
		vel_msg.linear.y = 0
		vel_msg.linear.z = 0
		vel_msg.angular.x = 0
		vel_msg.angular.y = 0
	

		if(temp == "w"):

			vel_msg.linear.x = abs(velocidade_linear)
			velocidade_publisher.publish(vel_msg)
			time.sleep(0.2)	
			vel_msg.linear.x = 0
			velocidade_publisher.publish(vel_msg)

		if(temp == "x"):

			vel_msg.linear.x = -abs(velocidade_linear)
       			velocidade_publisher.publish(vel_msg)
			time.sleep(0.2)
        		vel_msg.linear.x = 0
			velocidade_publisher.publish(vel_msg)

		if(temp == "a"):

         	       	vel_msg.angular.z = abs(velocidade_angular)
               		velocidade_publisher.publish(vel_msg)
			time.sleep(0.2)
        		vel_msg.angular.z = 0
        		velocidade_publisher.publish(vel_msg)

	
       		if(temp == "d"):

                	vel_msg.angular.z = -abs(velocidade_angular)
                	velocidade_publisher.publish(vel_msg)
			time.sleep(0.2)
        		vel_msg.angular.z = 0
        		velocidade_publisher.publish(vel_msg) 

		if(temp == "q"):

                	vel_msg.linear.x = abs(velocidade_linear)
                	vel_msg.angular.z = abs(velocidade_angular)
			velocidade_publisher.publish(vel_msg)
			time.sleep(0.2)
			vel_msg.linear.x = 0
        		vel_msg.angular.z = 0
        		velocidade_publisher.publish(vel_msg)

		if(temp == "z"):

                	vel_msg.linear.x = -abs(velocidade_linear)
                	vel_msg.angular.z = -abs(velocidade_angular)
                	velocidade_publisher.publish(vel_msg)
			time.sleep(0.2)
        		vel_msg.linear.x = 0
        		vel_msg.angular.z = 0
        		velocidade_publisher.publish(vel_msg)

		if(temp == "e"):

                	vel_msg.linear.x = abs(velocidade_linear)
                	vel_msg.angular.z = -abs(velocidade_angular)
                	velocidade_publisher.publish(vel_msg)
			time.sleep(0.2)
        		vel_msg.linear.x = 0
        		vel_msg.angular.z = 0
        		velocidade_publisher.publish(vel_msg)

		if(temp == "c"):

                	vel_msg.linear.x = -abs(velocidade_linear)
                	vel_msg.angular.z = abs(velocidade_angular)
                	velocidade_publisher.publish(vel_msg)
			time.sleep(0.2)
        		vel_msg.linear.x = 0
        		vel_msg.angular.z = 0
        		velocidade_publisher.publish(vel_msg)

		if(temp == "1"):
			velocidade_linear += 1

		if(temp == "2"):
               		if(velocidade_linear > 1):
		 		velocidade_linear -= 1
			else:
				print("Ja esta na velocidade 1! \n")
	
		if(temp == "3"):
                	velocidade_angular += 1

        	if(temp == "4"):
           		if(velocidade_angular > 1):
                 		velocidade_angular -= 1
               		else:
                        	print("Ja esta na velocidade 1! \n")


def cabecario():
	print("___________________________________________________________")
        print("|***********Comandos para Turtlesim Prova 771745**********|")
        print("|(w) = Frente 			(x) = Tras 		  |")
	print("|(a) = Vira hr 			(d) = Vira anti hr	  |")
	print("|(q) = Frente e vira anti hr	(e) = Frente e vira hr 	  |")
	print("|(z) = Tras e vira hr      	(c) = Tras e vira anti hr |")
	print("|(1) = + Vel Linear		(2) = - Vel Linear        |")
	print("|(3) = + Vel Angular       	(4) = - Vel Angular       |")
	print("|_________________________________________________________|")

def getchar():
	#Returns a single character from standard input
	import tty, termios, sys
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	if ord(ch) == 3 : quit() #manualmente ctrl + C
	return ch



if __name__ == '__main__':
	
	cabecario()	
	
	try:
		move()
	
	except rospy.ROSInterruptException: pass


