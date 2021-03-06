cmake_minimum_required(VERSION 2.8.3)
project(slamdog_srv_slam)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  message_generation
)

add_message_files(FILES msgTutorial.msg)
add_service_files(FILES srvTutorial.srv)

generate_messages(DEPENDENCIES std_msgs)

catkin_package(
  #INCLUDE_DIRS include
  LIBRARIES ros_msgs_tutorial
  CATKIN_DEPENDS roscpp std_msgs
  DEPENDS system_lib
)

include_directories(include ${catkin_INCLUDE_DIRS})

add_executable(ros_tutorial_msg_publisher src/ros_tutorial_msg_publisher.cpp)
target_link_libraries(ros_tutorial_msg_publisher ${catkin_LIBRARIES})
add_dependencies(ros_tutorial_msg_publisher slamdog_srv_slam_generate_messages_cpp)

add_executable(ros_tutorial_msg_subscriber src/ros_tutorial_msg_subscriber.cpp)
target_link_libraries(ros_tutorial_msg_subscriber ${catkin_LIBRARIES})
add_dependencies(ros_tutorial_msg_subscriber slamdog_srv_slam_generate_messages_cpp)

#ros_tutorial_srv_server
add_executable(ros_tutorial_srv_server src/ros_tutorial_srv_server.cpp)
target_link_libraries(ros_tutorial_srv_server ${catkin_LIBRARIES})
add_dependencies(ros_tutorial_srv_server slamdog_srv_slam_generate_messages_cpp)

#ros_tutorial_srv_client
add_executable(ros_tutorial_srv_client src/ros_tutorial_srv_client.cpp)
target_link_libraries(ros_tutorial_srv_client ${catkin_LIBRARIES})
add_dependencies(ros_tutorial_srv_client slamdog_srv_slam_generate_messages_cpp)
