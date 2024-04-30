#include <stdio.h>
#include "HX710B.h"

#define HX710B_DOUT 13
#define HX710B_CLK  12
#define HX710B_GAIN 128
HX710B pressure_sensor;

// MAGIC NUMBERS
#define OFFSET  540000 // used for tare the weight
#define RES     2.98023e-7

void sendSensorData(void)
{
  // convert the raw read to pascal using magic numbers
  float read_pascal =  ( (pressure_sensor.read() - OFFSET) * RES) *20 - 50;
  printf("%X\n", read_pascal);
  delay(0);
}

void setup(void)
{ 
  Serial.begin(115200);
  pressure_sensor.begin(HX710B_DOUT, HX710B_CLK, HX710B_GAIN);
}

void loop(void)
{
  if(pressure_sensor.is_ready())
    sendSensorData();
}
