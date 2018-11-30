#   create a string of objects that store image names and keywords/tags
#
#
from PIL import Image

from os import listdir
from os.path import isfile, join
from os import remove
from os import mkdir


class StoredImage:
    def __init__(self, imgString):

        self.image = imgString
        self.thumbnail = self.getThumbnailString(imgString)


        self.tagList = []

        self.updateThumbnail()

        #testing
        print("reading: " + self.image)
        print("created file: " + self.thumbnail)
        print()

    def addTag(self, tagString):
        self.tagList.append(tagString.capitalize())
        self.tagList.sort()

    def removeTag(self, tagString):
        self.tagList.remove(tagString.capitalize())


    def clearTags(self):
        self.tagList.clear()

    def getTags(self):
        return self.tagList

    def getThumbnailString(self, imgString):
        imgStringSplit = imgString.split(".")

        thumbnail = "thumbnails/"
        for n in range(0, len(imgStringSplit) - 1):
            thumbnail += imgStringSplit[n] + "."
        thumbnail +=  "thumbnail." + imgStringSplit[-1]

        return thumbnail

    def updateThumbnail(self):
        img = Image.open(self.image)
        size = img.size # (w, h)


        if(size[0] < size[1]):
            rate = 250 / float(size[0])
            adjustedSize = (250, rate*size[1])
            img.thumbnail(adjustedSize)
            img.save(self.thumbnail)


        else:
            rate = 250 / float(size[1])
            adjustedSize = (rate * size[0], 250)
            img.thumbnail(adjustedSize)
            img.save(self.thumbnail)

class StringOfStoredImages:
    def __init__(self):
        self.storedImgNamesList = [] # names as Strings
        self.storedImgList = [] # StoredImage Objects
        self.availableTags = {} # {tagName : quantity}

    def pushImage(self, imgName):
        self.storedImgList.append(StoredImage(imgName))
        self.storedImgNamesList.append(imgName)

    def removeImage(self, imgName):
        if(imgName in self.storedImgNamesList):
            index = self.storedImgNamesList.index(imgName)
            remove(self.storedImgList[index].thumbnail) # removes thumbnail file
            self.storedImgList.pop(index)
            self.storedImgNamesList.remove(imgName)


    def clearList(self):
        for name in self.storedImgList:
            self.removeImage(name)

    def importList(self): # how to export/save?
        pass

    def saveList(self):
        pass

    def getTagList(self):
        for tagName in self.availableTags:
            print(tagName)



groupOfImages = StringOfStoredImages()


onlyfiles = [f for f in listdir(".") if isfile(join(f))]


for name in onlyfiles:
    if ("thumbnails" not in listdir()):
        mkdir("thumbnails")

    nameSplit = name.split(".")
    if(     nameSplit[-1].lower() != "jpg" and # supported formats
            nameSplit[-1].lower() != "png" and
            nameSplit[-1].lower() != "gif" and
            nameSplit[-1].lower() != "webp" and
            nameSplit[-1].lower() != "bmp"):
        pass
    else:
        groupOfImages.pushImage(name)




