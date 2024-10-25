def setup():
    fullScreen()
    
    
    
    

def draw(): 
    createShape()
    square = createShape(RECT, 0, 0, 50, 50)
    square.setFill(color(0, 0, 255))
    square.setStroke(False)
    shape(square, 25, 25)
    
