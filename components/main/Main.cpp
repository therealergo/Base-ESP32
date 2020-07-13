#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

#include "driver/gpio.h"

extern "C" void app_main() {

    // Setup blinky for ESP-WROOM-32, which has an LED on GPIO2
    gpio_set_direction(GPIO_NUM_2, GPIO_MODE_OUTPUT);

    // Main loop
    while(1) {
        gpio_set_level(GPIO_NUM_2, 0);
		vTaskDelay(500 / portTICK_PERIOD_MS);
        gpio_set_level(GPIO_NUM_2, 1);
		vTaskDelay(500 / portTICK_PERIOD_MS);
	}
}