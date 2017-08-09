from rect import Rect
import sys



print("Welcome to the Box Program")
print("By MJZ 20170808")

def validate(suspectvar):
   if (isinstance(suspectvar, int)):
      if (suspectvar >= 0):
         return suspectvar
      print "Not a positive integer!"
      sys.exit()
   else:
      print "Invalid input"

def buildbox():
   box1x = validate(input('Enter the box start X value (upper left corner): '))
   box1y = validate(input('Enter the box start y value (upper left corner): '))
   box1width = validate(input('Enter the box width: '))
   box1height = validate(input('Enter the box height: '))
   return Rect(box1x, box1y, box1width, box1height)

print "First box:"
box1 = buildbox()
print "Second box:"
box2 = buildbox()

separate = 0


if Rect.inside(box1,box2):
   separate += 1
   print "Box 2 is inside of Box 1!"
   sys.exit()

if Rect.inside(box2,box1):
   separate += 1
   print "Box 1 is inside of Box 2!"
   sys.exit()

if Rect.intersecttopleft(box1,box2):
   separate += 1
   print Rect.intersecttopleft(box1,box2)

if Rect.intersectbottomleft(box1,box2):
   separate += 1
   print Rect.intersectbottomleft(box1,box2)

if Rect.intersecttopright(box1,box2):
   separate += 1
   print Rect.intersecttopright(box1,box2)

if Rect.intersectbottomright(box1,box2):
   separate += 1
   print Rect.intersectbottomright(box1,box2)

if Rect.intersectlefttop(box1,box2):
   separate += 1
   print Rect.intersectlefttop(box1,box2)

if Rect.intersectleftbottom(box1,box2):
   separate += 1
   print Rect.intersectlefttop(box1,box2)

if Rect.intersectrighttop(box1,box2):
   separate += 1
   print Rect.intersectrighttop(box1,box2)

if Rect.intersectrightbottom(box1,box2):
   separate += 1
   print Rect.intersectrightbottom(box1,box2)

if Rect.shareleft(box1,box2):
   separate += 1
   print Rect.shareleft(box1,box2)
if Rect.shareright(box1,box2):
   separate += 1
   print Rect.shareright(box1,box2)
if Rect.sharetop(box1,box2):
   separate += 1
   print Rect.sharetop(box1,box2)
if Rect.sharebottom(box1,box2):
   separate += 1
   print Rect.sharebottom(box1,box2)


if separate == 0:
   print "Boxes do not contain each other and do not intersect!"
   sys.exit()

