bool selpressed = false;
bool dwnpressed = false;
bool uppressed = false;

void setup() {
  Serial.begin(9600);

  pinMode(2, INPUT_PULLUP);
  pinMode(4, INPUT_PULLUP);
  pinMode(7, INPUT_PULLUP);
}

void loop() {

    if (digitalRead(2) == HIGH) {
    dwnpressed = true;
  }

  if (digitalRead(2) == LOW && dwnpressed == true) {
    Serial.println("voldwn");
    dwnpressed = false;
    delay(500);
  }

  if (digitalRead(4) == HIGH) {
    selpressed = true;
  }

  if (digitalRead(4) == LOW && selpressed == true) {
    Serial.println("select");
    selpressed = false;
    delay(500);
  }

  if (digitalRead(7) == HIGH) {
    uppressed = true;
  }

  if (digitalRead(7) == LOW && uppressed == true) {
    Serial.println("volup");
    uppressed = false;
    delay(500);
  }

}