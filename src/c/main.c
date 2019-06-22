// main.c, adapted from github.com/OrbitalBoson/

#include <unistd.h>
#include <stdio.h>
#include <dirent.h>
#include <wiringPi.h>
#include <wiringPiSPI.h>
#include <sys/time.h>

#include "adxl355.h"

FILE * fp;

unsigned long long getMicrotime() {
  struct timeval tm;
  gettimeofday(&tm, NULL);
  return ((long long int) tm.tv_sec) * 1000000 + tm.tv_usec;
}

int main(int argc, char * argv[])
{
  printf("                        [ADXL] Collecting\n");
  uint8_t t1 = 0b00010000;
  ADXL355_HANDLER spi = {};
  spi.spi = 1;
  spi.spi_channel = 0;
  spi.speed = 2000000;
  wiringPiSetup();
  int res = wiringPiSPISetup(spi.spi_channel, spi.speed);
  adxl355_measurement_mode(&spi);

  ADXL355Acceleration acc = {};

  fp = fopen(argv[1], "a");

  int sample_duration = 10; // sample time duration in seconds
  int sample_rate = 1000; // sample rate
  int samples = sample_duration * sample_rate;

  for (int i = 0; i < 20; i++){
    adxl355_read_acceleration(&spi, &acc);
    fprintf(fp, "%lld,", getMicrotime());
    fprintf(fp, "%d,", acc.x);
    fprintf(fp, "%d,", acc.y);
    fprintf(fp, "%d\n", acc.z);
    usleep((1.0 / sample_rate) * 1000000);
  }

  printf("Done reading\n");

  fclose(fp);
  adxl355_standby_mode(&spi);
  adxl355_reset(&spi);

  return 0;
}
