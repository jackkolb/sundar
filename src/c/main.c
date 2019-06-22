// main.c, adapted from github.com/OrbitalBoson/

#include <unistd.h>
#include <stdio.h>
#include <dirent.h>
#include <wiringPi.h>
#include <wiringPiSPI.h>
#include <sys/time.h>

#include "adxl355.h"

FILE * fp;
int counter = 0;
int limit = 50000;

unsigned long long getMicrotime() {
  struct timeval tm;
  gettimeofday(&tm, NULL);
  return ((long long int) tm.tv_sec) * 1000000 + tm.tv_usec;
}

void my_callback(ADXL355Fifo * fifo)
{
  if (counter >= limit) {
    printf(counter); printf("\n");
    fprintf(fp, "%lld,", getMicrotime());
    fprintf(fp, "%d,", fifo->data[0].x);
    fprintf(fp, "%d,", fifo->data[0].y);
    fprintf(fp, "%d\n", fifo->data[0].z);
    counter = 0;
  }
  counter++;
}

int main(int argc, char * argv[])
{
  printf("                        [ADXL] Collecting\n");
  uint8_t t1 = 0b00010000;
  ADXL355_HANDLER spi = {};
  //ADXL355Status status = {};
  //ADXL355Temperature temp = {};
  spi.spi = 1;
  spi.spi_channel = 0;
  spi.speed = 2000000;
  wiringPiSetup();
  int res = wiringPiSPISetup(spi.spi_channel, spi.speed);
  //ADXL355Command cmd;
  //uint8_t r;
  //ADXL355Fifo fifo = {};
  //ADXL355Acceleration acc = {};
  adxl355_measurement_mode(&spi);
  
  fp = fopen(argv[1], "a");

  adxl355_fifo_stream(&spi, my_callback, FIFO_STREAM_OVR_BREAK|FIFO_STREAM_FIFO_READ_BREAK);

  fclose(fp);
  adxl355_standby_mode(&spi);
  adxl355_reset(&spi);

  return 0;
}
