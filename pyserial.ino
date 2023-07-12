int in1 = 8
int in2 =9
int in3 = 5;
int in4 = 4;
int EnA = 3;
int EnB = 11;

void setup() {
  Serial.begin(9600);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);

  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(EnA, OUTPUT);
  pinMode(EnB, OUTPUT);
}

void loop() {
  if (Serial.available() > 0){
//Serial.print("My name is Arduino Uno \n");
  data = Serial.readString();
  if (data.indexOf ('forward') > -1){
    forward(100);
}
else if (data.indexOf ('backward') > -1{
  backward(100);
}
else if (data.indexOf ('turnLeft') > -1{
  turnLeft(100);
}
else if (data.indexOf ('turnRight') > -1{
  turnRight(100);
}
else if (dataStop".indexOf ('Stop')> -1){
  Stop();
}
else{
  Stop();
}
}
}

void forward() {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
 Serial.print("moving forward");
}

void backward() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);}

void turnLeft() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  analogWrite(EnA, 255);  // Set motor A speed to maximum
  analogWrite(EnB, 255);  // Set motor B speed to maximum
}

void turnRight() {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  analogWrite(EnA, 255);  // Set motor A speed to maximum
  analogWrite(EnB, 255);  // Set motor B speed to maximum
}

void Stop() {
  digitalWrite(in1 , LOW);
  digitalWrite(in2 , LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4 , LOW);
  analogWrite(EnA, LOW);
  analogWrite(EnB, LOW);
}
  Stop();
}
}
}

void forward() {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
 Serial.print("moving forward");
}

void backward() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);}

void turnLeft() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  analogWrite(EnA, 255);  // Set motor A speed to maximum
  analogWrite(EnB, 255);  // Set motor B speed to maximum
}
void turnRight() {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  analogWrite(EnA, 255);  // Set motor A speed to maximum
  analogWrite(EnB, 255);  // Set motor B speed to maximum
}

void Stop() {
  digitalWrite(in1 , LOW);
  digitalWrite(in2 , LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4 , LOW);
  analogWrite(EnA, LOW);
  analogWrite(EnB, LOW);
}
