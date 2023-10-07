/*
 * File:          IESL_controller.c
 * Date:
 * Description:
 * Author:
 * Modifications:
 */

/*
 * You may need to add include files like <webots/distance_sensor.h> or
 * <webots/motor.h>, etc.
 */
#include <webots/robot.h>
#include <webots/motor.h>

/*
 * You may want to add macros here.
 */
#define TIME_STEP 64
#define MAX_SPEED 6.28

/*
 * This is the main program.
 * The arguments of the main function can be specified by the
 * "controllerArgs" field of the Robot node
 */
int main(int argc, char **argv) {
  /* necessary to initialize webots stuff */
  wb_robot_init();

  /*
   * You should declare here WbDeviceTag variables for storing
   * robot devices like this:
   *  WbDeviceTag my_sensor = wb_robot_get_device("my_sensor");
   *  WbDeviceTag my_actuator = wb_robot_get_device("my_actuator");
      */
      
      WbDeviceTag f_r = wb_robot_get_device("front_right");
      WbDeviceTag f_l = wb_robot_get_device("front_left");
       WbDeviceTag b_r = wb_robot_get_device("right_back");
      WbDeviceTag b_l = wb_robot_get_device("left_back");
      
      
      wb_motor_set_position(f_r,INFINITY);
      wb_motor_set_position(f_l,INFINITY);
      wb_motor_set_position(b_r,INFINITY);
      wb_motor_set_position(b_l,INFINITY);


      wb_motor_set_velocity(f_r,0.0);
      wb_motor_set_velocity(f_l,0.0);
      wb_motor_set_velocity(b_r,0.0);
      wb_motor_set_velocity(b_l,0.0);
  /* main loop
   * Perform simulation steps of TIME_STEP milliseconds
   * and leave the loop when the simulation is over
   */
   
   void delay(int time){
   float current_time_1 = float(robot->getTime());

    float current_time_2= float(robot->getTime());

   do {

    current_time_2 = float(robot->getTime());

     robot->step(1);

    } while(current_time_2 < (current_time_1 + time));
   
   }
   
   void forward(float speed){
     wb_motor_set_velocity(f_r,-speed);
     wb_motor_set_velocity(f_l,-speed);
     wb_motor_set_velocity(b_r,-speed);
     wb_motor_set_velocity(b_l,-speed);
   
   }
   
   void reverse(float speed){
     wb_motor_set_velocity(f_r,speed);
     wb_motor_set_velocity(f_l,speed);
     wb_motor_set_velocity(b_r,speed);
     wb_motor_set_velocity(b_l,speed);

   }
   
    void left(float speed){
     wb_motor_set_velocity(f_r,-speed);
     wb_motor_set_velocity(f_l,speed);
     wb_motor_set_velocity(b_r,-speed);
     wb_motor_set_velocity(b_l,speed);

   }
   
       void right(float speed){
     wb_motor_set_velocity(f_r,speed);
     wb_motor_set_velocity(f_l,-speed);
     wb_motor_set_velocity(b_r,speed);
     wb_motor_set_velocity(b_l,-speed);

   }
   
  while (wb_robot_step(TIME_STEP) != -1) {
    /*
     * Read the sensors :
     * Enter here functions to read sensor data, like:
     *  double val = wb_distance_sensor_get_value(my_sensor);
     */

    /* Process sensor data here */

    /*
     * Enter here functions to send actuator commands, like:
     * wb_motor_set_position(my_actuator, 10.0);
     */
     
     forward(MAX_SPEED);
     delay(5);
     reverse(MAX_SPEED);
     delay(5);
     left(MAX_SPEED);
     delay(5);
     right(MAX_SPEED);
     delay(5);
   
     
  };

  /* Enter your cleanup code here */

  /* This is necessary to cleanup webots resources */
  wb_robot_cleanup();

  return 0;
}
