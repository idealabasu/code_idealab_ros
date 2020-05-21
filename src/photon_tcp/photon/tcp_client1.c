TCPClient tcp_client;

const unsigned long SEND_INTERVAL_MS = 100;

// Global variables
int counter = 0;
unsigned long lastSend = 0;

byte server[] = { 192, 168, 0, 131 }; // Google

int port = 5555;

int data[4];



void setup()
{
  // Make sure your Serial Terminal app is closed before powering your device
  Serial.begin(9600);
  // Wait for a USB serial connection for up to 30 seconds
  waitFor(Serial.isConnected, 30000);
  if (Serial.isConnected()){
        
        String serial_in="";
        char byte_in=0;
        Serial.println("enter ip address: ");
        while (1)
        {
            if (Serial.available()>0)
            {
                byte_in = Serial.read();
                serial_in.concat(byte_in);
                //Serial.write(byte_in);
                if (serial_in.indexOf("\r")>0) break;
            }
        }
        
        int jj = 0;
        while (1)
        {
            int ii = serial_in.indexOf(".");
            
            if (ii>0)
            {
                server[jj]=serial_in.substring(0,ii).toInt();
                serial_in = serial_in.substring(ii+1);
                jj++;
            }
            else
            {
                if (serial_in.length()==0) break;
                else
                {
                    server[jj]=(byte)serial_in.toInt();
                    jj++;
                }
            }

            if (jj>3) break;
        }
        Serial.print("\r\nYou typed: \r\n");
        
        //Serial.println(serial_in);
        Serial.print(String(server[0]));
        Serial.print(",");
        Serial.print(String(server[1]));
        Serial.print(",");
        Serial.print(String(server[2]));
        Serial.print(",");
        Serial.print(String(server[3]));
        Serial.print("\r\n");
        
        serial_in = "";
        Serial.println("enter port: ");
        while (1)
        {
            if (Serial.available()>0)
            {
                byte_in = Serial.read();
                serial_in.concat(byte_in);
                //Serial.write(byte_in);
                if (serial_in.indexOf("\r")>0) break;
            }
        }
        
        port=serial_in.toInt();

        Serial.print("\r\nYou typed: \r\n");
        
        //Serial.println(serial_in);
        Serial.print(String(port));
        Serial.print("\r\n");
  
  }
}

void loop()
{

    data[0]=1;
    data[1]=2;
    data[2]=3;
    data[3]=4;
    
    
    if (millis() - lastSend >= SEND_INTERVAL_MS)
    {
        lastSend = millis();

        Serial.printf("Ping: %d \r\n", counter);

        if (tcp_client.connected())
        {
            String mystring = "";
            for (int ii=0;ii<4;ii++)
            {
                mystring.concat(String(data[ii]));
                if (ii<3) mystring.concat(",");
            }
            mystring.concat("\r\n");
    
    
            tcp_client.print(mystring);
            //Serial.println(WiFi.localIP());
            //tcp_client.print(12,DEC);
            //tcp_client.print(",");
            //tcp_client.print(34,DEC);
            //tcp_client.print(",");
            //tcp_client.print(56,DEC);
            //tcp_client.print(",");
            //tcp_client.print(78,DEC);
            //tcp_client.print("\r\n");
            //tcp_client.print("123,456,789,100\r\n");
            counter++;
        }
    }

    if (tcp_client.connected())
    {
        if (tcp_client.available())
        {
            char c = tcp_client.read();
            Serial.print(c);
        }
        
        if (!tcp_client.connected())
        {
            Serial.println();
            Serial.println("disconnecting.");
            tcp_client.stop();
            //for(;;);
        }        
    }
    else{
        Serial.println("connecting...");

      if (tcp_client.connect(server, port))
      {
        Serial.println("connected");
        //tcp_client.println("GET /search?q=unicorn HTTP/1.0");
        //tcp_client.println("Host: www.google.com");
        //tcp_client.println("Content-Length: 0");
        //tcp_client.println();
      }
      else
      {
        Serial.println("connection failed");
        delay(100);
      }
        
        
    }

}