/* Controle des relais depuis le raspberry */

#include "DHT.h"

#define DHTPIN 53
#define DHTTYPE DHT11   // DHT 11
#define SensorHumSolPin A0
#define SensorNiveauPin A1
#define SensorLightPin A2

// Initialize DHT sensor for normal 16mhz Arduino
DHT dht(DHTPIN, DHTTYPE);

// Déclaration des variables
const byte pin[] = {22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37}; // Pin de controle des relais
const byte LED = 13;      // Led embarqué sur la carte Arduino
byte etat[] = {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1}; // état des sorties
byte messageComplet = 48;

// Initialisation de la carte arduino
void setup()
{
  // initialisation des sorties
  for (byte i = 0; i < 16; i++)
  {
    pinMode(pin[i], OUTPUT);
  }
  // initialisation de l'état des sorties
  for (byte i = 0; i < 16; i++)
  {
    digitalWrite(pin[i], HIGH);
  }
  // entrer l'état des sorties dans un tableau
  for (byte i = 0; i < 16; i++)
  {
    etat[i] = digitalRead(pin[i]);
  }
  // initialisation de la led embarqué pin 13
  pinMode(LED, OUTPUT);
  // initialisation du capteur DHT11
  dht.begin();
  // initialisation de la liaison série (USB /dev/ttyACM0)
  Serial.begin(115200);
}

// Boucle du programme
void loop()
{ 
  delay(1000);
  if(Serial.available())
  {
    reception();
  }
  if (messageComplet != 48)
  {
      traitement();
  }
}


// Fonctions
void reception() // Fonction de reception des messages
{
  // recevoir un message et le traiter
  while (Serial.available())
  {
    byte message = 0;
    message = Serial.read();
    if(message == 10)
      {
        message = 0;
      }
    if (messageComplet == 48)
    {
      messageComplet = message;
    }
    else if (messageComplet != 48)
    {
      messageComplet = messageComplet + message;
    }
    delayMicroseconds(1000);
  }
}

void traitement() // Fonction de traitement de la commande
{
  byte changementEtatRelai = 0;
  // Fermer un relais
  if (messageComplet == 49)
  {
    digitalWrite(pin[0], LOW);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 50)
  {
    digitalWrite(pin[1], LOW);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 51)
  {
    digitalWrite(pin[2], LOW);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 52)
  {
    digitalWrite(pin[3], LOW);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 53)
  {
    digitalWrite(pin[4], LOW);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 54)
  {
    digitalWrite(pin[5], LOW);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 55)
  {
    digitalWrite(pin[6], LOW);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 56)
  {
    digitalWrite(pin[7], LOW);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 57)
  {
    digitalWrite(pin[8], LOW);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 97)
  {
    digitalWrite(pin[9], LOW);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 98)
  {
    digitalWrite(pin[10], LOW);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 99)
  {
    digitalWrite(pin[11], LOW);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 100)
  {
    digitalWrite(pin[12], LOW);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 101)
  {
    digitalWrite(pin[13], LOW);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 102)
  {
    digitalWrite(pin[14], LOW);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 103)
  {
    digitalWrite(pin[15], LOW);
    changementEtatRelai = 1;
  }
  // Ouvrir un relais
  if (messageComplet == 132)
  {
    digitalWrite(pin[0], HIGH);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 133)
  {
    digitalWrite(pin[1], HIGH);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 134)
  {
    digitalWrite(pin[2], HIGH);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 135)
  {
    digitalWrite(pin[3], HIGH);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 136)
  {
    digitalWrite(pin[4], HIGH);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 137)
  {
    digitalWrite(pin[5], HIGH);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 138)
  {
    digitalWrite(pin[6], HIGH);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 139)
  {
    digitalWrite(pin[7], HIGH);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 140)
  {
    digitalWrite(pin[8], HIGH);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 180)
  {
    digitalWrite(pin[9], HIGH);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 181)
  {
    digitalWrite(pin[10], HIGH);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 182)
  {
    digitalWrite(pin[11], HIGH);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 183)
  {
    digitalWrite(pin[12], HIGH);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 184)
  {
    digitalWrite(pin[13], HIGH);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 185)
  {
    digitalWrite(pin[14], HIGH);
    changementEtatRelai = 1;
  }
  else if (messageComplet == 186)
  {
    digitalWrite(pin[15], HIGH);
    changementEtatRelai = 1;
  }
  // Si l'état d'un relais a changé l'écrire dans un tableau
  if(messageComplet == 83)
  {
    surveillance();
  }
  // Lire le capteur de température et d'humidité de l'air
  if (messageComplet == 84)
  {
    // Reading temperature or humidity takes about 250 milliseconds!
    // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
    byte h = dht.readHumidity();
    // Read temperature as Celsius
    byte t = dht.readTemperature();
    // tester si il n'y a pas d'erreur de lecture et sinon réessayer
    if (isnan(h) || isnan(t))
    {
      Serial.print("Failed to read from DHT sensor!");
      return;
    }
    Serial.print(t);
    Serial.print(h);
  }
  // lire le capteur d'humidité du sol
  if(messageComplet == 85)
  {
    float sensorHumSolValue = analogRead(SensorHumSolPin);
    Serial.print(sensorHumSolValue);
  }
  // Lire le capteur de niveau du reservoir
  if(messageComplet == 86)
  {
    float sensorNiveauValue = analogRead(SensorNiveauPin);
    Serial.print(sensorNiveauValue);
  }
  // Lire le capteur de luminosité
  if(messageComplet == 87)
  {
    int sensorLightValue = analogRead(SensorLightPin);
    Serial.print(sensorLightValue);
  }
  messageComplet = 48;
}

void surveillance() // fonction de lecture et d'envoie des changements d'états des relais
{
  // Ecrire l'état des sorties dans un tableau
  for (byte i = 0; i < 16; i++)
  {
    etat[i] = digitalRead(pin[i]);
  } 
  // Envoyer l'état des sories via le port série
  for (byte i = 0; i < 16; i++)
  {
    Serial.println(etat[i]);
  }
}
