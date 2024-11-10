const int P_green_buttonPin = 26;
const int K_blue_buttonPin = 22;


void setup() {
  pinMode(P_green_buttonPin, INPUT_PULLUP);
  pinMode(K_blue_buttonPin, INPUT_PULLUP);

  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println("Hello, ESP32!");
  Serial.println();
}

void loop() {
  int P_buttonState = digitalRead(P_green_buttonPin);
  int K_buttonState = digitalRead(K_blue_buttonPin);

  if (P_buttonState == LOW) {
    Serial.println("Button P Pressed");
  } else {
    Serial.println("Button P Not Pressed");
  }

  if (K_buttonState == LOW) {
    Serial.println("Button K Pressed");
  } else {
    Serial.println("Button K Not Pressed");
  }

  Serial.println();

  delay(1000);
}
