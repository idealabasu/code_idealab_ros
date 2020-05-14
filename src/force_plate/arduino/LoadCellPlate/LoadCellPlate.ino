// code from: https://github.com/bogde/HX711
#include "HX711.h"

HX711 load1;
HX711 load2;
HX711 load3;
HX711 load4;

double cal1 = -893000;
double cal2 = -886000;
double cal3 = -901000;
double cal4 = -875000;

void setup() {
  Serial.begin(115200);
  Serial.println("Force Plate");

  load1.begin(52, 53);
  load2.begin(50, 51);
  load3.begin(48, 49);
  load4.begin(46, 47);
  
  load1.set_scale(cal1); 
  load1.tare();
  load2.set_scale(cal2); 
  load2.tare(); 
  load3.set_scale(cal3); 
  load3.tare(); 
  load4.set_scale(cal4); 
  load4.tare(); 

  Serial.println("Readings:");
}

void loop() {
  float force1 = load1.get_units();
  float force2 = load2.get_units();
  float force3 = load3.get_units();
  float force4 = load4.get_units();

  //double average = (force1+force2+force3+force4)/4.0;

  //Serial.print("Reading: ");
  //Serial.print(average, 4); //scale.get_units() returns a float
  //Serial.print(" kgs"); //You can change this to kg but you'll need to refactor the calibration_factor
//  Serial.print(force1);
//  Serial.print(", ");
//  Serial.print(force2);
//  Serial.print(", ");
//  Serial.print(force3);
//  Serial.print(", ");
//  Serial.println(force4);
  //Serial.println(force1+force2+force3+force4, 5);
  Serial.print(force1,DEC);
  Serial.print(",");
  Serial.print(force2,DEC);
  Serial.print(",");
  Serial.print(force3,DEC);
  Serial.print(",");
  Serial.print(force4,DEC);
  Serial.print("\r\n");
//  delay();
}
