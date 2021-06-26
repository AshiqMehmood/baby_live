#include <ArduinoJson.h>
#include <DHT_U.h>
#include <DHT.h>

#define DHTPIN 8
#define DHTTYPE DHT11
#define LED 2
#define SENSOR A2

DHT dht(DHTPIN, DHTTYPE);

int chk;
float hum = 0;
float temp = 0;
int value=0;
double lastEvent = 0;
int sound = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  dht.begin();

  pinMode(LED, OUTPUT);
  pinMode(SENSOR, INPUT);
  digitalWrite(LED, LOW);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  value = analogRead(SENSOR);
  delay(100);
  hum = dht.readHumidity();
  delay(100);
  temp = dht.readTemperature();
  delay(100);
  
  //prepare json data of sensor values...
  StaticJsonDocument<200> doc;
  doc["moisture"] = value;
  doc["temp"] = temp;
  doc["hum"] = hum;
  doc["cry"] = sound;

  delay(100);
  serializeJson(doc, Serial);
//  Serial.print(value);
//  Serial.print(",");
//  Serial.print(hum);
//  Serial.print(",");
//  Serial.print(temp);
  Serial.println("");
  
  
//  if(value < 700){
//      if(millis() - lastEvent > 25) 
//        {
//          //Serial.println("Diapers are wet !"); 
//          digitalWrite(LED, HIGH);
//        }
//   
//    }
//   else 
//      {
//        digitalWrite(LED, LOW);
//      }
//
//   lastEvent = millis();    


  delay(2000);
  

}
