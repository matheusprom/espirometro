#include <stdio.h>
#include "HX710B.h"

#define HX710B_DOUT 2
#define HX710B_CLK  3
#define HX710B_GAIN 128
HX710B pressure_sensor;


void sendSensorData(void)
{
  printf("%f", pressure_sensor.pascal());
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
