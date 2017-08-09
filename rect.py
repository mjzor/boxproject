class Rect:
   'Common class for rectangles'
   rectCount = 0

   def __init__(self, startx, starty, width, height):
      self.startx = startx
      self.starty = starty
      self.endx = startx + width
      self.endy = starty + height 
      Rect.rectCount += 1
   
   def displayCount(self):
     print "Number of boxes: %d" % Rect.rectCount

   def rectInfo(self):
      print "Start X : ", self.startx, ", Start Y : ", self.starty, ", Width : ", self.width, ", Height : ", self.height

   @staticmethod
   def intersecttopleft(box1,box2):
      if (box2.startx < box1.startx < box2.endx and box1.starty < box2.starty < box1.endy):
         return "Top of box 2 intersects with left of box 1 at ", box1.startx, box2.starty

   @staticmethod
   def intersectbottomleft(box1,box2):
      if box2.startx < box1.startx < box2.endx and box1.starty < box2.endy < box1.endy:
         return "Bottom of box 2 intersects with left side of box 1 at ", box1.startx, box2.endy 

   @staticmethod
   def intersecttopright(box1,box2):
      if box2.startx < box1.endx < box2.endx and box1.starty < box2.starty < box1.endy:
         return "Top of box 2 intersects with right side of box 1 at ", box1.endx, box2.starty 

   @staticmethod
   def intersectbottomright(box1,box2):
      if box2.startx < box1.endx < box2.endx and box1.starty < box2.endy < box1.endy:
         return "Bottom of box 2 intersects with right side of box 1 at ", box1.endx, box2.endy 



   @staticmethod
   def intersectlefttop(box1,box2):
      if box1.startx < box2.startx < box1.endx and box2.starty < box1.starty < box2.endy:
         return "Left of box 2 intersects with top side of box 1 at ", box2.startx, box1.starty 

   @staticmethod
   def intersectleftbottom(box1,box2):
      if box1.endx < box2.startx < box1.endx and box2.starty < box1.endy < box2.endy:
         return "Left of box 2 intersects with bottom side of box 1 at ", box2.startx, box1.endy 

   @staticmethod
   def intersectrighttop(box1,box2):
      if box1.startx < box2.endx < box1.endx and box2.starty < box1.starty < box2.endy:
         return "Right of box 2 intersects with top side of box 1 at ", box2.endx, box1.starty

   @staticmethod
   def intersectrightbottom(box1,box2):
      if box1.startx < box2.endx < box1.endx and box2.starty < box1.endy < box2.endy:
         return "Right of box 2 intersects with bottom side of box 1 at ", box2.endx, box1.endy 


   @staticmethod
   def inside(box1,box2):
      if box1.startx < box2.startx and box1.endx > box2.endx and box1.starty < box2.starty and box1.endy > box2.endy:
         return "Box 2 is entirely inside Box 1!"


   @staticmethod
   def sharetop(box1,box2):
      if box1.starty == box2.starty and (box1.startx <= box2.startx or box1.endx >= box2.endx):
         return "Boxes 1 and 2 share the same top"
      if box1.starty == box2.endy and (box1.startx <= box2.startx or box1.endx >= box2.endx):
         return "Boxes 1 top is shared with 2 bottom" 
   
   @staticmethod
   def sharebottom(box1,box2):
      if box1.endy == box2.endy and (box1.startx <= box2.startx or box1.endx >= box2.endx):
         return "Boxes 1 and 2 share the same bottom"
      if box1.endy == box2.starty and (box1.startx <= box2.startx or box1.endx >= box2.endx):
         return "Boxes 1 bottom is shared with 2 top"        

   @staticmethod
   def shareleft(box1,box2):
      if box1.startx == box2.startx and (box1.starty <= box2.starty or box1.endy >= box2.endy):
         return "Boxes 1 and 2 share the same left"
      if box1.startx == box2.endx and (box1.starty <= box2.starty or box1.endy >= box2.endy):
         return "Boxes 1 left is shared with 2 right"        

   @staticmethod
   def shareright(box1,box2):
      if box1.endx == box2.endx and (box1.starty <= box2.starty or box1.endy >= box2.endy):
         return "Boxes 1 and 2 share the same right"
      if box1.endx == box2.startx and (box1.starty <= box2.starty or box2.endy >= box1.endy):
         return "Boxes 1 right is shared with 2 left"        





