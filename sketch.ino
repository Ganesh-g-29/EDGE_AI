const int trig = 2;
const int echo = 3;
String objectLabel = "";

void setup() {
  Serial.begin(9600);     // For Nicla serial data
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
}

void loop() {
  // Read label from Nicla
  if (Serial.available()) {
    objectLabel = Serial.readStringUntil('\n');
    objectLabel.trim();
  }

  // Measure distance
  digitalWrite(trig, LOW); delayMicroseconds(2);
  digitalWrite(trig, HIGH); delayMicroseconds(10);
  digitalWrite(trig, LOW);

  long duration = pulseIn(echo, HIGH, 30000);
  float distance = duration * 0.034 / 2;

  if (objectLabel.length() > 0) {
    Serial.print("Detected: ");
    Serial.print(objectLabel);
    Serial.print(" at ");
    Serial.print(distance);
    Serial.println(" cm");
  }

  delay(1000);
}
