import cv2
import serial 


ser = serial.Serial('COM 6 ,9600,timeout=5)

face_classifier=cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")

video=cv2.VideoCapture(0)
def detect_bounding_box(vid):

    gray_image=cv2.cvtColor(vid,cv2.COLOR_BGR2GRAY)
    faces=face_classifier.detectMultiScale(gray_image,1.1,5,minisize=(40,40))
    cv2.rectangle(vid,(x,y),(x+w,y+h),(0,255,0),4)

    width,hieght,ch=vid.shape
    center_frame=(width/2) ,(hieght/2)
    x,y,w,h=faces[0]
    center_object=((x+w)/2),((y+h)/2)
    area_object=((x+w)*(y+h))
    adesired=((width-100)*(hieght-100))

    a,b=center_frame
    c,d=center_object
    if c<a-20:
        ser.write(str.encode("l"))
    elif c>a+20:
        ser.write(str.encode("r"))

    if area_object>adesired:
        ser.write(str.encode("b"))
    elif area_object<adesired:
        ser.write(str.encode("f"))


    return vid


while True:
    result,video_frame=video.read()
    if result is False:
        break
    faces= detect_bounding_box(video_frame)

    cv2.imshow("My Face Detection Project",faces)
    if cv2.waitKey(1)&0xFF==ord("q"):
        break

video.release()
cv2.destroyAllWindows


 87 changes: 87 additions & 0 deletions87  
cvrobot.ino
@@ -0,0 +1,87 @@

int ENA = 3;
int ENB = 11;
int IN1 = 8;
int IN2 = 9;
int IN3 = 5;
int IN4 = 4;
String data;

void setup() {
  
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    data = Serial.readString();
    Serial.println(data);

      if (data == "f") {
      forward(110);
    }
    else if (data == "b") {
      reverse(110);
    }
    else if (data == "r") {
      turn_right(110);
    }
    else if (data == "l") {
      turn_left(110);
    }
    else if (data == "s") {
      brake();
    }
  }
}
void turn_right(int Speed) {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(ENA, Speed / 2);
  analogWrite(ENB, Speed);
}

void turn_left(int Speed) {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(ENA, Speed);
  analogWrite(ENB, Speed / 2);
}

void brake() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
  analogWrite(ENA, 0);
  analogWrite(ENB, 0);
}

void forward(int Speed) {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(ENA, Speed);
  analogWrite(ENB, Speed);
}

void reverse(int Speed) {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  analogWrite(ENA, Speed);
  analogWrite(ENB, Speed);