#include <ncurses.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include "jr3pci-ioctl.h"

#include "read_jr3.h"

short f, b;
six_axis_array fm,ac;
force_array fs, as;
int ret,i,fd, sensors=0;
float values[DATA_LEN];

void read_local(float * values,int sensors,int fd,force_array * full_scale1, six_axis_array * filter1,force_array * full_scale2, six_axis_array * filter2)
{
	  if (sensors>0)
		  ioctl(fd,IOCTL0_JR3_FILTER0,filter1);
	  if (sensors>1)
		  ioctl(fd,IOCTL1_JR3_FILTER0,filter2);

    int ii;
    for (ii=0;ii<NUM_AXES;ii++)
    {
      values[ii+OFFSET_S1+OFFSET_FORCE] = (float)(*filter1).f[ii]*(*full_scale1).f[ii]/16384;
      values[ii+OFFSET_S1+OFFSET_MOMENT] = (float)(*filter1).m[ii]*(*full_scale1).m[ii]/16384;
      values[ii+OFFSET_S2+OFFSET_FORCE] = (float)(*filter2).f[ii]*(*full_scale2).f[ii]/16384;
      values[ii+OFFSET_S2+OFFSET_MOMENT] = (float)(*filter2).m[ii]*(*full_scale2).m[ii]/16384;
    }

    float Fx,Fy,Fz,Mx,My,Mz;
    Fx = values[OFFSET_S1+OFFSET_FORCE+0];
    Fy = values[OFFSET_S1+OFFSET_FORCE+1];
    Fz = values[OFFSET_S1+OFFSET_FORCE+2];
    Mx = values[OFFSET_S1+OFFSET_MOMENT+0];
    My = values[OFFSET_S1+OFFSET_MOMENT+1];
    Mz = values[OFFSET_S1+OFFSET_MOMENT+2];
    values[OFFSET_S1+OFFSET_SAFE+0] = Fx/SPEC_A + Fy/SPEC_A + Fz/SPEC_D + Mx/SPEC_E +My/SPEC_E +Mz/SPEC_H;
    values[OFFSET_S1+OFFSET_SAFE+1] = Fx/SPEC_B + Fy/SPEC_C + Fz/SPEC_D +Mx/SPEC_F +My/SPEC_G +Mz/SPEC_H;
    values[OFFSET_S1+OFFSET_SAFE+2] = Fx/SPEC_C + Fy/SPEC_B + Fz/SPEC_D +Mx/SPEC_G +My/SPEC_F +Mz/SPEC_H;

    Fx = values[OFFSET_S2+OFFSET_FORCE+0];
    Fy = values[OFFSET_S2+OFFSET_FORCE+1];
    Fz = values[OFFSET_S2+OFFSET_FORCE+2];
    Mx = values[OFFSET_S2+OFFSET_MOMENT+0];
    My = values[OFFSET_S2+OFFSET_MOMENT+1];
    Mz = values[OFFSET_S2+OFFSET_MOMENT+2];
    values[OFFSET_S2+OFFSET_SAFE+0] = Fx/SPEC_A + Fy/SPEC_A + Fz/SPEC_D + Mx/SPEC_E +My/SPEC_E +Mz/SPEC_H;
    values[OFFSET_S2+OFFSET_SAFE+1] = Fx/SPEC_B + Fy/SPEC_C + Fz/SPEC_D +Mx/SPEC_F +My/SPEC_G +Mz/SPEC_H;
    values[OFFSET_S2+OFFSET_SAFE+2] = Fx/SPEC_C + Fy/SPEC_B + Fz/SPEC_D +Mx/SPEC_G +My/SPEC_F +Mz/SPEC_H;


}
void read_global(float * values)
{
  read_local(values,sensors,fd,&fs,&fm,&as,&ac);
}


void init(void)
{
  //short f, b;
  //six_axis_array fm,ac;
  //force_array fs, as;
  //int ret,i,fd, sensors=0;
  //float values[16];

  if ((fd=open("/dev/jr3",O_RDWR)) < 0) 
  {
    perror("Can't open device. No way to read force!");
  }
  ret=ioctl(fd,IOCTL0_JR3_GET_FULL_SCALES,&fs);
  if (ret==0) sensors++;
  ret=ioctl(fd,IOCTL1_JR3_GET_FULL_SCALES,&as);
  if (ret==0) sensors++;
}


/*
int main(void)
{
  init();
  while (1)
  {
    //read_local(values,sensors,fd,&fs,&fm,&as,&ac);
    read_global(values);
    int ii;
    for (ii=0;ii<12;ii++)
    {
      printf("%+4.3f ", values[ii]); 
    }
    printf("\n");
    usleep(100000);
  }

  return 0;
}
*/


