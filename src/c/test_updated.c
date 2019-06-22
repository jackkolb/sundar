// main.c, adapted from github.com/OrbitalBoson/

#include <unistd.h>
#include <stdio.h>

#include <wiringPi.h>
#include <wiringPiSPI.h>

#include "adxl355.h"


int main(int argc, char * argv[])
{
  printf("Collecting ADXL355 data");

  uint8_t t1 = 0b00010000;

  ADXL355_HANDLER spi = {};
  ADXL355Status status = {};
  spi.spi = 1;
  spi.spi_channel = 0;
  spi.speed = 2000000;

  wiringPiSetup();
  int res = wiringPiSPISetup(spi.spi_channel, spi.speed);

  ADXL355Acceleration acc = {};

  adxl355_measurement_mode(&spi);

  for (int i=0; i<20; i++){
      adxl355_read_acceleration(&spi, &acc);
      printf("X: %d\n", acc.x);
      printf("Y: %d\n", acc.y);
      printf("Z: %d\n", acc.z);
      delay(500);
  }

  adxl355_get_status(&spi, &status);
  adxl355_print_status(&status);

  adxl355_reset(&spi);

  return 0;
}
