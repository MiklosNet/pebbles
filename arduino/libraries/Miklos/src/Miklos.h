//Miklos Module 5/4/2105 young.

#define MAIL_BIN "python /root/scripts/send_email.py"
#define SMTP_SERVER "smtp.cox.net";
//#define SMTP_USERNAME "mail_username";
//#define SMTP_PASSWORD "mail_password";
#define SMTP_FROM "arduino_yun_1";
#define SMTP_TO "marijuanos@gmail.com";

#define TANK_HEIGHT 35 //50; // in cm
#define TANK_SURFACE 1320 // in cm2
#define TANK_MAX_L 45 // in L
#define TANK_MIN_L 20 // in L

// pH deviation compensate
#define PH_OFFSET 0.00
#define PH_MIN 6
#define PH_MAX 8

// eCC params
#define INTERCEPT 0.0
#define SLOPE 960

// OVERALL 
#define DELAY_READINGS 800 // in ms

#define SEND_MAIL true
#define DEBUG true

// Read water level every (in ms) ...
//#define WATER_H_FREQ 60000
#define WATER_H_FREQ 600
// Check if the pump is working every...
//#define PUMP_OK_FREQ 30000
#define PUMP_OK_FREQ 600
// Read pH value every...
//#define PH_FREQ 60000
#define PH_FREQ 800

// WATER_FLOW_SENSOR
//#define WATER_FLOW_PIN 7
//#define WATER_FLOW_ITR 4 // Interruption number used
  // Min nb of pulse of the water wheel in one sec
  // to consider it is working
//#define WATER_WHEEL_MIN_PULSE 4

// Ultra sound sensor
//#define USND_ECHO_PIN 8
//#define USND_TRIG_PIN 9

// Pin definitions
// pH sensor
#define PH_PIN A3
#define ECC_PIN A0
#define MOTORCONTROL1 7    // Digital Arduino Pin used to control the motor
#define MOTORCONTROL2 6    // Digital Arduino Pin used to control the motor

//SENSOR ARRAY
#define SENSOR[] ECC

//DISPLAY SETUP
#define LCD_I2C lcd(0x27,16,4)
