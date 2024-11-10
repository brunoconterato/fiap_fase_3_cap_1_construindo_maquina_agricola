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

  if (deveIrrigar(K_buttonState == LOW, P_buttonState == LOW, pH, humidity)) {
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

// Função que retorna 'true' ou 'false' para irrigação
bool deveIrrigar(bool K, bool P, float pH, float humidity) {
  // Limites para pH e umidade
  float pH_min = 5.5;  // pH mínimo aceitável para o solo
  float pH_max = 7.5;  // pH máximo aceitável para o solo
  float humidity_threshold = 30.0;  // Umidade mínima aceitável (em %)

  // Lógica de decisão para irrigação
  if (humidity < humidity_threshold) {
    // Se a umidade estiver abaixo do limite, irrigar imediatamente
    Serial.println("Irrigação recomendada. Motivo: baixa umidade.");
    return true;
  }

  if (!K || !P) {
    // Se os níveis de Potássio ou Fósforo estiverem baixos, é necessário irrigar para ajudar na absorção de nutrientes
    Serial.println("Irrigação recomendada. Motivo: baixo nível de K ou P.");
    return true;
  }

  if (pH < pH_min || pH > pH_max) {
    // Se o pH estiver fora do intervalo ideal (5.5-7.5), irrigar para tentar corrigir o pH
    Serial.println("Irrigação recomendada. Motivo: pH fora da faixa recomendada.");
    return true;
  }

  // Se todos os parâmetros estiverem dentro do intervalo ideal, não é necessário irrigar
    Serial.println("Irrigação não recomendada. Motivo: todos os parâmetros normais.");
  return false;
}
