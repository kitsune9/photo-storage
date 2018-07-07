#   create a string of objects that store image names and keywords/tags
#
#
from PIL import Image

from os import listdir

from os import listdir
from os.path import isfile, join

class StoredImage:
    def __init__(self, imgString):
        imgStringSplit = imgString.split(".")
        self.image = imgString
        self.thumbnail = "thumbnails/" + imgStringSplit[0] + ".thumbnail." + imgStringSplit[1]

        self.tagList = []

        #testing
        print(self.image)
        print(self.thumbnail)

    def addTag(self, tagString):
        self.tagList.append(tagString.capitalize())
        self.tagList.sort()

    def removeTag(self, tagString):
        self.tagList.remove(tagString.capitalize())


    def clearTags(self):
        self.tagList.clear()

    def getTags(self):
        return self.tagList

    def updateThumbnail(self):
        img = Image.open(self.image)
        size = img.size # (w, h)


        if(size[0] > size[1]):
            rate = 250 / size[0]
            adjustedSize = (250, rate*size[1])
            img.thumbnail(adjustedSize)
            img.save(self.thumbnail)


        else:
            rate = 250 / size[1]
            adjustedSize = (rate * size[0], 250)
            img.thumbnail(adjustedSize)
            img.save(self.thumbnail)








class StringOfStoredImages:
    pass




myImage = StoredImage("ilmina.jpg")
myImage.updateThumbnail()



onlyfiles = [f for f in listdir() if isfile(join(f))]
print(onlyfiles[1:])

