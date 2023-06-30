//  Copyright 2023 (c) WizIO ( Georgi Angelov
#include <stdint.h>
#include "ring-buffer.h"
static ring_buffer_t RX;
static char ring_buffer[256] __attribute__((aligned(16))) = {0};

void __attribute__((weak)) _init()
{
    ring_buffer_init(&RX, sizeof(ring_buffer), ring_buffer);
}

int main(void)
{
    while (1)
        continue;
}
