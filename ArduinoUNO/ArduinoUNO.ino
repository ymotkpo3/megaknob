bool pressed = false;

void setup() {
  Serial.begin(9600);

  pinMode(4, INPUT);
}

void loop() {

  if (digitalRead(4) == HIGH) {
    pressed = true;
  }

  if (digitalRead(4) == LOW && pressed == true) {
    Serial.println("select");
    pressed = false;
    delay(500);
  }

}