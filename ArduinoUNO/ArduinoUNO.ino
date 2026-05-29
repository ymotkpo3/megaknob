#include <Adafruit_NeoPixel.h>

int Power = 11;
int PIN  = 12;
#define NUMPIXELS 1

Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  Serial.begin(115200);

  pixels.begin();
  pinMode(Power,OUTPUT);
  digitalWrite(Power, HIGH);
  pinMode(6, INPUT);

}

void loop() {
    pixels.clear();
    
  if (digitalRead(6) == HIGH) {
    pixels.setPixelColor(0, pixels.Color(15, 25, 205));
    pixels.show();
  }
  pixels.setPixelColor(0, pixels.Color(0, 0, 0));
  pixels.show();
}