// main.c, adapted from github.com/OrbitalBoson/

#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
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

  long int sample_duration = strtol(argv[1], NULL, 10);
  long int sample_rate = strtol(argv[2], NULL, 10);
  fp = fopen(argv[3], "a");

  int samples = sample_duration * sample_rate;
  for (int i = 0; i < samples; i++){
    adxl355_read_acceleration(&spi, &acc);
    fprintf(fp, "%lld,", getMicrotime());
    fprintf(fp, "%d,", acc.x);
    fprintf(fp, "%d,", acc.y);
    fprintf(fp, "%d\n", acc.z);
    usleep((1.0 / sample_rate) * 1000000 - 185);  // 185 microseconds was found to be a "good enough" processing speed for flashdrive
  }

  fclose(fp);
  adxl355_standby_mode(&spi);
  adxl355_reset(&spi);

  return 0;
}
