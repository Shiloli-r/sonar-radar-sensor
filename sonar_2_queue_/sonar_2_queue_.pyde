add_library('serial')
Distance = []
Angle = []
PixelDistance = []
font = PFont()

def setup():   # same as the arduino setup() function
    size(1366, 768)
    smooth()
    port = Serial(this, Serial.list()[0], 9600) # port = Serial(this, "COM3", 9600) - the port the arduino is on
    print Serial.list()
    port.clear()
    #port.buffer(15)
    port.bufferUntil(46)   
    font = loadFont("OldEnglishTextMT-35.vlw")
    #font = loadFont("Papyrus-Regular-35.vlw")
    #font = loadFont("OCRAExtended-30.vlw")
    textFont(font, 35)
    
def draw():   # Infinite loop. same as the arduino loop() function
   fill(98,245,31);
   fill(0,4);
   noStroke();
   rect(0, 0, width, height-height*0.065)
   radar()
   scanner()
   #object()
   labels()

def serialEvent(port):
    """This function is called automatically, once the serial function reads and buffers the data"""
    data = port.readStringUntil(46)  # reads until the fullstop, i.e angle,distance.
    commaIndex = data.index(",")  # gets the index of the comma
    angle = data[slice(0, commaIndex)]  # gets the angle
    distance = data[slice(commaIndex+1, len(data)-1)]  # gets the distance
    Angle.append(int(angle))
    Distance.append(int(distance))

      
def radar():
    """This function draws the radar system (protractor layout)"""
    pushMatrix()
    translate(width/2, height-height*0.074)
    stroke(0, 179, 0)
    strokeWeight(7)
    # Arcs
    arc(0, 0,  (width-width*0.0625), (width-width*0.0625), radians(180), radians(360))
    arc(0, 0,  (width-width*0.27), (width-width*0.27), radians(180), radians(360))
    arc(0, 0,  (width-width*0.479), (width-width*0.479), radians(180), radians(360))
    arc(0, 0,  (width-width*0.687), (width-width*0.687), radians(180), radians(360))
    #lines
    line(-width/2, 0, width/2, 0)
    line(0,0, (-width/2)*cos(radians(30)), (-width/2)*sin(radians(30)))
    line(0,0, (-width/2)*cos(radians(60)), (-width/2)*sin(radians(60)))
    line(0,0, (-width/2)*cos(radians(90)), (-width/2)*sin(radians(90)))
    line(0,0, (-width/2)*cos(radians(120)), (-width/2)*sin(radians(120)))
    line(0,0, (-width/2)*cos(radians(150)), (-width/2)*sin(radians(150)))
    line((-width/2)*cos(radians(30)),0,  width/2, 0)
    popMatrix()

def scanner():
    """This function defines the line that moves from 0 to 180 degrees"""
    pushMatrix()
    strokeWeight(7)
    stroke(30, 250, 60)
    translate(width/2, height-height*0.074)
    
    try:
        line(0,0, (height-height*0.12)*cos(radians(Angle[0])), -(height-height*0.12)*sin(radians(Angle[0])))
        Angle.remove(Angle[0])
    except IndexError:
        pass
    popMatrix()
    #print(Ang)

def object():
    """This function depicts the object detected distance and angle in red """
    pushMatrix()
    translate(width/2, height-height*0.074)
    strokeWeight(7)
    stroke(255, 10, 10)  # Red
    # converting distance from the sensor from cm to pixels 
    if len(Distance)>1:
        pixDistance = Distance[0]*((height-height*0.1666)*0.025)
        PixelDistance.append(pixDistance)
        if(Distance[0]<40):
            line(pixDistance*cos(radians(Angle[0])),-pixDistance*sin(radians(Angle[0])),(width-width*0.505)*cos(radians(Angle[0])),-(width-width*0.505)*sin(radians(Angle[0])));
        Distance.remove(Distance[0])
    popMatrix()
    
def labels():
    pushMatrix()
    textSize(25)
    try:
        if Distance[0]>40: 
            object = "Out of Range";
        else:
            object = "In Range";
    except IndexError:
        object = "Waiting for Sensor"
    fill(0,0,0)
    noStroke()
    rect(0, height-height*0.0698, width, height)
    #fill(98,245,31)
    fill(177,232,32)
    textSize(25)
    text("10cm",width-width*0.3854,height-height*0.0833)
    text("20cm",width-width*0.281,height-height*0.0833)
    text("30cm",width-width*0.177,height-height*0.0833)
    text("40cm",width-width*0.0729,height-height*0.0833)
    textSize(30)
    text("Object: " + object, width-width*0.875, height-height*0.0377)
    try:
        text("Angle: " + str(Angle[0]) +" \xb0", width-width*0.48, height-height*0.0377)
    except IndexError:
        text("Angle: " + str(0) +" \xb0", width-width*0.48, height-height*0.0377)
    text("Distance: ", width-width*0.26, height-height*0.0377)
    
    textSize(25)
    fill(98,245,60);
    translate((width-width*0.4994)+width/2*cos(radians(30)),(height-height*0.0907)-width/2*sin(radians(30)));
    rotate(-radians(-60));
    text("30\xb0",0,0);
    resetMatrix();
    translate((width-width*0.503)+width/2*cos(radians(60)),(height-height*0.0888)-width/2*sin(radians(60)));
    rotate(-radians(-30));
    text("60\xb0",0,0);
    resetMatrix();
    translate((width-width*0.507)+width/2*cos(radians(90)),(height-height*0.0833)-width/2*sin(radians(90)));
    rotate(radians(0));
    text("90\xb0",0,0);
    resetMatrix();
    translate(width-width*0.513+width/2*cos(radians(120)),(height-height*0.07129)-width/2*sin(radians(120)));
    rotate(radians(-30));
    text("120\xb0",0,0);
    resetMatrix();
    translate((width-width*0.5104)+width/2*cos(radians(150)),(height-height*0.0574)-width/2*sin(radians(150)));
    rotate(radians(-60));
    text("150\xb0",0,0);
    popMatrix()
    
