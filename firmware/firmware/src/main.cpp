#include <Arduino.h>
#include <RotaryEncoder.h>

#define SW 6

RotaryEncoder encoder(
    28,
    29,
    RotaryEncoder::LatchMode::TWO03
);

void setup() {

  Serial.begin(115200);
  pinMode(SW, INPUT_PULLUP);
}

void loop() {


    encoder.tick();

    if(digitalRead(SW) == LOW){
      
      Serial.println("select");

      delay(400);
    }

    static int pos = 0;

    int newPos = encoder.getPosition();

    if (pos < newPos) {
        Serial.println("volDWN");
        pos = newPos;
        
    } else if (pos > newPos){
      Serial.println("volUP");
      pos = newPos;
    }
}