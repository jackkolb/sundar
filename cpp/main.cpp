/*
Created on: 15/08/2018
Author: Rohan Gurav
        Valeria Toffoli
Code: Use the following code to read the ADXL355 values connected to the SPI channel 
      of the EV-COG4050-Expander board port0. Check the readme.md for connection info  
 
*/

#include <inttypes.h>
#include "ADXL355.h"
 
Serial pc(USBTX, USBRX);

 
ADXL355 accl(SPI1_CS0, SPI1_MOSI, SPI1_MISO, SPI1_SCLK);    // PMOD port
//ADXRS290 gyro(SPI0_CS2, SPI0_MOSI, SPI0_MISO, SPI0_SCLK);   // PMOD port
 
    
int main()
{
    pc.baud(9600);
    pc.printf("SPI ADXL355 and ADXL357 Demo\r\n");
    pc.printf("GET device ID\r\n");
   
    accl.reset();
    uint8_t d; 
    
    d=accl.read_reg(accl.DEVID_AD);
    pc.printf("AD id = %x \r\n",d);
    
    d=accl.read_reg(accl.DEVID_MST);
    pc.printf("MEMS id = %x \r\n",d);
    
    d=accl.read_reg(accl.PARTID);
    pc.printf("device id = %x \r\n",d);
    
    d=accl.read_reg(accl.REVID);
    pc.printf("revision id = %x \r\n",d);
    
    pc.printf("GET device data [x, y, z, t] \r\n");
    accl.set_power_ctl_reg(accl.MEASUREMENT);
    
    d=accl.read_reg(accl.POWER_CTL);
    pc.printf("power control on measurement mode = %x \r\n",d);
    
    float x, y,z;
    float t;
    
    /*The following part is used to perform 2's complemient and then display the data*/
    for(int i=0; i<50; i++) 
    {
        x = accl.convert(accl.scanx())*accl.axis355_sens;
        y = accl.convert(accl.scany())*accl.axis355_sens;
        z = accl.convert(accl.scanz())*accl.axis355_sens;
        t = 25+float(accl.scant()-1852)/(-9.05);
    
        pc.printf("%f \t %f \t %f  \t %f \r\n" , x,y,z,t);
        wait(0.1);
    }
    
/*-------------------------------------------------------------    
    // The following code will display the Raw data of the Axes 
     while(1) 
    {
        x = accl.scanx();
        y = accl.scany();
        z = accl.scanz();
        t = accl.scant();
        pc.printf("%u \t %u \t %u \t %u \r\n" , x,y,z,t);
        wait(1.0);
    }
----------------------------------------------------------------*/
}
 
 