//this code establishes a connection 
//to control music that's playing via arduino from DC
//initial code to work with arduino to connect to network
// using wifi shield - ESP8266

//sample web server using shield

#include <ESP8266Wifi.h>

const char* ssid: "";
const char* password: "";

WiFi server(80);

//string create a webpage that the wifi shield itself sets up
String hdr = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n";
String webpage_1 = "<!DOCTYPE html><html><head><title>CS NETWORKS: CONTROL AN LED</title></head><body>"
String webpage_2 = "<div id='main'><h2>CONTROL AN LED WITH WIFI NETWORK</h2><form id='F1' action='ON'><input class='button' type='submit' value=‘ON’ ></form><form id='F2' action='OFF'><input class='button' type='submit' value=‘OFF’ ></form><br></div>"
String webpage_3 = "</body></html>"

String req = ""
int LED_PIN = 13;
void setup() {
  // put your setup code here, to run once:
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(13,HIGH);
  serial.begin(115200);
  Wifi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500); // waits for connection
  }
  server.begin();
  //start to play music from SD card
 
  }


}

void loop() {
  // put your main code here, to run repeatedly:
  WiFiClient client = server.available();
  //chcek to assure connection
  if (!client){
    return;
  }
  while(client.connected()){
    if(client.available()){
      request = client.readStringUntil('\r');
        client.flush();
        client.print(hdr);
        client.print(webpage_1)
        client.print(webpage_2)
        client.print(webpage_3)

      //these will be replaced by commands to control the music
      //"PLAY, PAUSE, SET VOLUME"
      //rather than digital writes, control bytes on the SD card
      
      if (request.indexOf("ON") == 1 ){ 
        digitalWrite(LED_Pin, HIGH);  
      }
      else if  ( request.indexOf("LEDOFF") == 0 ) { 
        digitalWrite(LED_Pin, LOW);   
      }
  
    }
  


}
