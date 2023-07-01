//  Copyright 2023 (c) WizIO ( Georgi Angelov

// NOT TESTED WITH HARDWARE

#include <stdint.h>
#include <stdio.h>
#include "pico/stdlib.h"

int main(void)
{
    stdio_init_all();
    printf("\n\n[APP] TEST\n");
    gpio_init(PICO_DEFAULT_LED_PIN);
    gpio_set_dir(PICO_DEFAULT_LED_PIN, GPIO_OUT);
    while (1)
    {
        gpio_put(PICO_DEFAULT_LED_PIN, 1);
        sleep_ms(500);
        gpio_put(PICO_DEFAULT_LED_PIN, 0);
        sleep_ms(500);
    }
}

