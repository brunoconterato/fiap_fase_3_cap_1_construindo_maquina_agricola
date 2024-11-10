#define P_green_buttonPin 26
#define K_blue_buttonPin 22
#define LDR_PIN 35

const double rl10 = 50000.0; // LDR resistance at 10 lux
const double ldrGamma = 0.7;

void setup() {
  pinMode(P_green_buttonPin, INPUT_PULLUP);
  pinMode(K_blue_buttonPin, INPUT_PULLUP);
  pinMode(LDR_PIN, INPUT);

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

  Serial.print("Light: " + String(read_ldr()));


  Serial.println();

  delay(1000);
}

double calculate_resistance(int ldr_value) {
    double voltage_ratio = ldr_value / (4095.0 - ldr_value);
    return 10000.0 * voltage_ratio;
}

double calculate_lux(double resistance) {
    return 10.0 * pow(rl10 / resistance, 1.0 / ldrGamma);
}

double read_ldr() {
    int value = analogRead(LDR_PIN);
    double resistance = calculate_resistance(value);
    double light_level = calculate_lux(resistance);
    Serial.print("Luminosidade: ");
    Serial.println(light_level);
    return light_level;
}
