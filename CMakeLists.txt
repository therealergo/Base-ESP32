cmake_minimum_required(VERSION 3.5)

# Start adding external ESP-IDF component libraries to the project
set(EXTRA_COMPONENT_DIRS
)

# Example: Add LittleVGL library
# get_filename_component(EXTRA_COMPONENT_DIRS_LIB_LVGL
#     "./libraries/lv_port_esp32_ili9341/components" ABSOLUTE
# )
# list(APPEND EXTRA_COMPONENT_DIRS ${EXTRA_COMPONENT_DIRS_LIB_LVGL})

# Example: Add Espressif esp-aws-iot library
# get_filename_component(EXTRA_COMPONENT_DIRS_LIB_AWS
#     "./libraries/esp-aws-iot" ABSOLUTE
# )
# list(APPEND EXTRA_COMPONENT_DIRS ${EXTRA_COMPONENT_DIRS_LIB_AWS})

# Bring in the ESP-IDF build system
include($ENV{IDF_PATH}/tools/cmake/project.cmake)

# Create the cmake project
project(sb_base_esp32)