#include <DHT.h>
#include <cmath>  // For NAN

#define P_green_buttonPin 26
#define K_blue_buttonPin 22
#define LDR_PIN 35
#define DHT_PIN 17
#define DHT_TYPE DHT22   // DHT sensor type is DHT22
#define RELE_PIN 21  // Pino de controle do relé

const double rl10 = 50000.0; // LDR resistance at 10 lux
const double ldrGamma = 0.7;

DHT dht(DHT_PIN, DHT_TYPE);

void setup() {
  pinMode(P_green_buttonPin, INPUT_PULLUP);
  pinMode(K_blue_buttonPin, INPUT_PULLUP);
  pinMode(LDR_PIN, INPUT);
  pinMode(RELE_PIN, OUTPUT);  // Configura o pino do relé como saída

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

  double pH = read_ldr();

  double humidity = read_dht();

  if (humidity < 50.0) {
    liga_rele();
  } else {
    desliga_rele();
  }

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

double read_dht() {
    double humidity = dht.readHumidity();
    if (isnan(humidity)) {
        Serial.println("Erro ao ler o sensor DHT22");
        return NAN;
    } else {
        Serial.print("Umidade: ");
        Serial.print(humidity);
        Serial.println(" %");
        return humidity;
    }
}

void liga_rele() {
  // Liga o relé (ativa a bomba de água)
  Serial.println(("Ligando rele"));
  digitalWrite(RELE_PIN, HIGH);
}

void desliga_rele() {
  // Desliga o relé (ativa a bomba de água)
  Serial.println(("Desligando rele"));
  digitalWrite(RELE_PIN, LOW);
}