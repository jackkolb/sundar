// main.c, adapted from github.com/OrbitalBoson/

#include <unistd.h>
#include <stdio.h>

#include <wiringPi.h>
#include <wiringPiSPI.h>
#include <time.h>

#include "adxl355.h"

void my_callback(ADXL355Fifo * fifo)
{
  time_t now = time(0);
  float x = fifo->data[0].x;
  float y = fifo->data[0].y;
  float z = fifo->data[0].z;
  
  printf("X: %d\n", x);  
  
  FILE * fp;
  fp = fopen("./data/data_1.txt", "w");
  printf("a\n");
  fprintf(fp, "%f:%d,%d,%d",now,x,y,z);
  printf("b\n");
  fclose(fp);
  return;
}

int main(int argc, char * argv[])
{
  printf("Collecting ADXL355 data");

  uint8_t t1 = 0b00010000;

  ADXL355_HANDLER spi = {};
  ADXL355Status status = {};
  ADXL355Temperature temp = {};
  spi.spi = 1;
  spi.spi_channel = 0;
  spi.speed = 2000000;

  wiringPiSetup();
  int res = wiringPiSPISetup(spi.spi_channel, spi.speed);

  ADXL355Command cmd;
  uint8_t r;
  ADXL355Fifo fifo = {};
  ADXL355Acceleration acc = {};

  adxl355_measurement_mode(&spi);

  adxl355_fifo_stream(&spi, my_callback, FIFO_STREAM_OVR_BREAK|FIFO_STREAM_FIFO_READ_BREAK);

  adxl355_standby_mode(&spi);

  adxl355_reset(&spi);

  return 0;
}
