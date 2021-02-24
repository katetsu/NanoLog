PROJECT(nanolog-wrapper)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_custom_target(nanolog COMMAND make run
                   WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/run_time
)