cmake_minimum_required(VERSION 3.5)
project(turtlebot_autonomous_nav)

# Encontrar pacotes necessários
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

# Instalar o diretório launch
install(
    DIRECTORY launch
    DESTINATION share/${PROJECT_NAME}
)

# Instalar scripts Python
install(
    PROGRAMS
    launch/main.launch.py
    DESTINATION lib/${PROJECT_NAME}
)

ament_package()
