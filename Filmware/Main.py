#include <LiquidCrystal.h>

// --- Definicje pinów ---
#define BUTTON1 2
#define BUTTON2 3
#define LED_PIN 4

#define RS 5
#define E 6
#define D4 7
#define D5 8
#define D6 9
#define D7 10

#define POT_PIN A0

// --- Inicjalizacja LCD ---
LiquidCrystal lcd(RS, E, D4, D5, D6, D7);

// --- Nazwy bramek ---
const char* gates[] = {"AND", "OR", "XOR", "NAND", "NOR", "XNOR"};
const int gateCount = 6;

void setup() {
  pinMode(BUTTON1, INPUT_PULLUP);
  pinMode(BUTTON2, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);

  lcd.begin(16, 2);
  lcd.print("Symulator bramek");
  delay(1500);
  lcd.clear();
}

void loop() {
  int potValue = analogRead(POT_PIN);
  int gateIndex = map(potValue, 0, 1023, 0, gateCount - 1);

  // Odczyt przycisków (odwrócone, bo INPUT_PULLUP)
  bool A = !digitalRead(BUTTON1);
  bool B = !digitalRead(BUTTON2);
  bool output = 0;

  // --- Oblicz wynik w zależności od wybranej bramki ---
  switch (gateIndex) {
    case 0: output = A && B; break;        // AND
    case 1: output = A || B; break;        // OR
    case 2: output = A ^ B; break;         // XOR
    case 3: output = !(A && B); break;     // NAND
    case 4: output = !(A || B); break;     // NOR
    case 5: output = !(A ^ B); break;      // XNOR
  }

  // --- LED ---
  digitalWrite(LED_PIN, output ? HIGH : LOW);

  // --- LCD Wyświetlanie ---
  lcd.setCursor(0, 0);
  lcd.print("Bramka: ");
  lcd.print(gates[gateIndex]);
  lcd.print("   ");  // czyszczenie końca linii

  lcd.setCursor(0, 1);
  lcd.print("A=");
  lcd.print(A);
  lcd.print(" B=");
  lcd.print(B);
  lcd.print(" Y=");
  lcd.print(output);
  lcd.print("   ");

  delay(100);
}
