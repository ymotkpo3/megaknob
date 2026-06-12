#include <Arduino.h>
#include <RotaryEncoder.h>

int MODE_SELECT = 0;
int MODE_VOLUME = 1;
static int mode = 0;


#define SW 0

RotaryEncoder encoder(
    7,
    6,
    RotaryEncoder::LatchMode::TWO03
);

void setup() {
  Serial.begin(115200);
  pinMode(SW, INPUT_PULLUP);
}

bool buttonPressed = false;
bool longPressSent = false;
unsigned long pressStart = 0;

void loop() {

  encoder.tick();

  bool currentState = digitalRead(SW) == LOW;

  if (currentState && !buttonPressed) {
    
    delay(30);

    if (digitalRead(SW) != LOW)
        return;

     Serial.println("PRESS");

    buttonPressed = true;
    longPressSent = false;
    pressStart = millis();
  }

  if (currentState && !longPressSent && millis() - pressStart >= 700) {

    Serial.println("master");
    mode = MODE_VOLUME;

    longPressSent = true;
  }

  if (!currentState && buttonPressed) {

    delay(30);

    if (digitalRead(SW) == LOW)
        return;
    
    Serial.println("RELEASE");


    buttonPressed = false;

    if (!longPressSent) {
      Serial.println("click");
      if(mode == MODE_VOLUME){
        Serial.println("update");
        mode = MODE_SELECT;
      } else if (mode == MODE_SELECT){
        mode = MODE_VOLUME;
      }
      delay(400);
    }
  }

  static int pos = 0;

  int newPos = encoder.getPosition();

  if (pos < newPos && mode == MODE_VOLUME) {
    Serial.println("volDWN");
    pos = newPos;
  } else if (pos > newPos && mode == MODE_VOLUME){
    Serial.println("volUP");
    pos = newPos;
  } else if (pos < newPos && mode == MODE_SELECT){
    Serial.println("appDWN");
    pos = newPos;
  } else if (pos > newPos && mode == MODE_SELECT){
    Serial.println("appUP");
    pos = newPos;
  }
}