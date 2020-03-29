add_library('serial')
port = Serial(this, "COM3", 9600)
font = PFont()

def setup():
    size(1366, 768)
    smooth()
    font = loadFont("OldEnglishTextMT-35.vlw")
    #font = loadFont("Papyrus-Regular-35.vlw")
    #font = loadFont("OCRAExtended-30.vlw")
    textFont(font, 35)
    
def draw():
    fill(98,245,31);
    fill(0,4);
    noStroke();
    rect(0, 0, width, height-height*0.065)
    radar()
    data = read()
    if data is not None:
        angle = data[0]
        distance = data[1]
        angle = int(angle)
        distance = int(distance)
        scanner(angle)  # The scanner function draws the scanning line
        labels(angle, distance)
        object(angle, distance)

def read():    
    """This function reads the data from the Serial port"""
    if port.available()>0:
        data = port.readStringUntil(46)  # reads until the fullstop, i.e angle,distance.
        if data is not None:
            commaIndex = data.index(",")  # gets the index of the comma
            angle = data[slice(0, commaIndex)]  # gets the angle
            distance = data[slice(commaIndex+1, len(data)-1)]  # gets the distance
            return [angle, distance]
    
            
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
    
def scanner(angle):
    """This function defines the line that moves from 0 to 180 degrees"""
    pushMatrix()
    strokeWeight(7)
    stroke(30, 250, 60) # red
    translate(width/2, height-height*0.074)
    line(0,0, (height-height*0.12)*cos(radians(angle)), -(height-height*0.12)*sin(radians(angle)))
    popMatrix()
    
    
def object(angle, distance):
    """This function depicts the object detected distance and angle in red """
    pushMatrix()
    translate(width/2, height-height*0.074)
    strokeWeight(7)
    stroke(255, 10, 10)  # Red
    # converting distance from the sensor from cm to pixels 
    pixelDistance = distance*((height-height*0.1666)*0.025)
    if(distance<40):
        line(pixelDistance*cos(radians(angle)),-pixelDistance*sin(radians(angle)),(width-width*0.505)*cos(radians(angle)),-(width-width*0.505)*sin(radians(angle)));
    popMatrix()
    
def labels(angle, distance):
    """This function contains the labels to the radar"""
    pushMatrix()
    textSize(25)
    if distance>40: 
        object = "Out of Range";
    else:
        object = "In Range";
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
    text("Angle: " + str(angle) +" \xb0", width-width*0.48, height-height*0.0377)
    if distance<40:
        text("Distance: " + str(distance), width-width*0.26, height-height*0.0377)
    else:
        text("Distance: " , width-width*0.26, height-height*0.0377)
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
    
    
