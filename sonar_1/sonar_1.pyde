add_library('serial')
data = distance = angle = Angle = Distance = ""
def setup():
    size(1366, 768)
    smooth()
    port = Serial(this, Serial.list()[0], 9600) # port = Serial(this, "COM3", 9600)
    print Serial.list()
    port.bufferUntil(46)
    
def draw():
   fill(98,245,31);
   fill(0,4);
   noStroke();
   rect(0, 0, width, height-height*0.065)
   radar()
   scanner()
   #ang()
  
def serialEvent(port):
    global data, angle, distance, Angle, Distance
    parseInt = this.parseInt
    data = port.readStringUntil(46)  # reads until the fullstop, i.e angle,distance.
    commaIndex = data.index(",")  # gets the index of the comma
    angle = data[slice(0, commaIndex)]  # gets the angle
    #angle= parseInt(angle)
    #Angle= parseInt(angle)
    distance = data[slice(commaIndex+1, len(data)-1)]  # gets the distance
    #Distance=parseInt(distance)
    #print int(angle)  
    
def radar():
    pushMatrix()
    translate(width/2, height-height*0.074)
    stroke(0, 179, 0)
    strokeWeight(9)
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
    global Angle, angle
    parseInt = this.parseInt
    Angle= parseInt(angle)
    pushMatrix()
    strokeWeight(9)
    stroke(30, 250, 60)
    translate(width/2, height-height*0.074)
    line(0,0, (height-height*0.12)*cos(radians(Angle)), -(height-height*0.12)*sin(radians(Angle)))
    popMatrix()
    print Angle

       

def ang():
    global angle
    parseInt = this.parseInt
    Angle=str(angle)
    #angle = ord(Angle)
    print(Angle)
    iangle = parseInt(Angle)
    print(type(iangle))
