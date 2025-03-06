// C++ code
//
int i=0;
void setup()
{
pinMode(12,OUTPUT);
pinMode(11,OUTPUT);
pinMode(10,OUTPUT);
pinMode(9,INPUT);
}

void loop()
{
  if(digitalRead(9)){
  switch(i){
    case 0:
  	digitalWrite(12,1);
  	digitalWrite(11,0);
  	digitalWrite(10,0);
    i+=1;
    break;
    case 1:
  	digitalWrite(12,0);
  	digitalWrite(11,1);
  	digitalWrite(10,0);
    i+=1;
    break;
    case 2:
  	digitalWrite(12,0);
  	digitalWrite(11,0);
  	digitalWrite(10,1);
    i=0;
    break;
    default:
    break;
  }
  }
  delay(200); // Delay a little bit to improve simulation performance
}