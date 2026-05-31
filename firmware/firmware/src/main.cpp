#include <Arduino.h>
#include <RotaryEncoder.h>

int MODE_SELECT = 0;
int MODE_VOLUME = 1;
int mode = 0;

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
      
      Serial.println("click");
      if(mode == MODE_VOLUME){
        mode = MODE_SELECT;
      } else if (mode == MODE_SELECT){
        mode = MODE_VOLUME;
      }
      delay(400);
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