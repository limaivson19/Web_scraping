#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h>
#endif
#define NUM_LEDS 15
int OFFSET;
int incomingByte = 0;

Adafruit_NeoPixel strip(15, 13, NEO_GRB + NEO_KHZ800);

void setup() {
  #if defined(__AVR_ATtiny85__) && (F_CPU == 16000000)
  clock_prescale_set(clock_div_1);
  #endif
  strip.begin();
  strip.show();
  Serial.begin(9600);
}

void loop() {
  int cor = Serial.read();
  if(cor == 'p'){
    cor = Serial.read();
    //verde
    int cont = 0;
    while(cont<15){
    strip.setPixelColor((cont),strip.Color((0),(63.75),(0)));
    strip.show();
    cont=cont+1;
  }
  delay(300);
  cont = 0;
  while(cont<15){
    //branco
    strip.setPixelColor((cont),strip.Color((63.75),(63.75),(63.75)));
    strip.show();
    cont=cont+1;
  }
  delay(300);
  }
}
