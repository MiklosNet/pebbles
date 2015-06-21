// Modified 6 21 2016
#include <Bridge.h>
#include <YunServer.h>
#include <YunClient.h>
#include <Wire.h>
#include <Miklos.h>
#include "MotorDriver.h"

YunServer server;
void setup(void) //////////////////////////////////////////////////////////////////////////////
{
  
Bridge.begin();
Serial.begin(9600);
server.listenOnLocalhost();
server.begin();
Serial.println("motorsTest");
motordriver.init();
motordriver.goForward();

delay(5000);
motordriver.stop();
Serial.println("motorTest .. done");
delay(5000);
}
///////////////////////////////////////////////////////////////////////////////////////////////
void loop(void){ //////////////////////////////////////////////////////////////////////////////
YunClient client = server.accept();

float ecValue = ecCommand();
float pHValue = phCommand();

if (client) {
    client.setTimeout(5);
    process(client);
    client.stop();
}


Serial.print("ecc: ");
Serial.println(ecValue);
Serial.print("ph: ");
Serial.println(pHValue,2);
delay(DELAY_READINGS);

}
//////////////////////////////////////////////////////////////////////////////////////////////////

void process(YunClient client) {
  String command = client.readStringUntil('\r');
  if (command == "m1on") {
    m1OnCommand(client);
  }
  if (command == "m1off") {
    m1OffCommand(client);
  }
  if (command == "m2on") {
    m2OnCommand(client);
  }
  if (command == "m2off") {
    m2OffCommand(client);
  }
  if (command == "getph") {
    getphCommand(client);
  }
  if (command == "getecc") {
    getecCommand(client);
  }    
}

void m1OnCommand(YunClient client){
if (client.read()) {
motordriver.setSpeed(200, MOTORA); 
motordriver.rotateWithID(MOTOR_CLOCKWISE, MOTORA);
Serial.print(F("Motor1 On"));
client.print(F("Motor1 On"));
String key = "M1";
Bridge.put(key, String("On"));
 }
}

void m1OffCommand(YunClient client){
if (client.read()) {
motordriver.stop(MOTORA);
Serial.print(F("Motor1 Off"));
client.print(F("Motor1 Off"));
String key = "M1";
Bridge.put(key, String("Off"));
 }
}

void m2OnCommand(YunClient client){
if (client.read()) {
motordriver.setSpeed(200, MOTORB); 
motordriver.rotateWithID(MOTOR_CLOCKWISE, MOTORB);
Serial.print(F("Motor2 On"));
client.print(F("Motor2 On"));
String key = "M2";
Bridge.put(key, String("On"));
 }
}

void m2OffCommand(YunClient client){
if (client.read()) {
motordriver.stop(MOTORB);
Serial.print(F("Motor2 Off"));
client.print(F("Motor2 Off"));
String key = "M2";
Bridge.put(key, String("Off"));
 }
}

void getecCommand(YunClient client) {
  if (client.read()) {
  float ecis = ecCommand();
  Serial.print("ECC:");
  Serial.println(ecis);
  client.print("ECC:");
  client.println(ecis);
  String key = "ECC";
  Bridge.put(key, String(ecis));
  }
}

void getphCommand(YunClient client) {
  if (client.read()) {
  float phis = phCommand();
  Serial.print("Ph:");
  Serial.println(phis);
  client.print("PH:");
  client.println(phis);
  String key = "PH";
  Bridge.put(key, String(phis));
  }
}

float phCommand(){
static float pHValue,voltage;
float pHSensor = analogRead(A3);
voltage = pHSensor *5.0/1024;
//pHValue = 3.5*voltage+PH_OFFSET; // use offset if needed
pHValue = 3.5*voltage;
String key = "PH";
Bridge.put(key, String(pHValue));
return pHValue;
}

float ecCommand(){
float Count = analogRead(ECC_PIN); //ec meter input
float Voltage = Count / 1023 * 5.0;// convert from count to raw voltage
float SensorReading= INTERCEPT + Voltage * SLOPE; //converts voltage to sensor reading  
String key = "ECC";
Bridge.put(key, String(SensorReading));
return SensorReading;
}

