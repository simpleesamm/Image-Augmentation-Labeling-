import csv
import os
os.chdir("c:/Users/samue/OneDrive/Documents/Samuel_Studies/Y3 Sem 1/Machine Learning/Project/plant-seedlings-classification/Loose Silky-bent/Loose Silky Bent/train")
folder_path = 'train.csv'
def BndBox2YoloLine(width,height, imageClass,xmin,xmax,ymin,ymax, classList=[]):
        xcen = (float(xmax) + float(xmin)) / 2 / float(width)
        ycen = (float(ymax) + float(ymin)) / 2 / float(height)

        w = (float(xmax) - float(xmin)) / float(width)
        h = (float(ymax) - float(ymin)) / float(height)

        # PR387
        boxName = imageClass
        if boxName not in classList:
            classList.append(boxName)

        classIndex = classList.index(boxName)

        return classIndex, xcen, ycen, w, h

with open(folder_path) as f:
        csvFile = csv.reader(f)
        data = list(csvFile)
        data.pop(0)
        classList = ['Black-grass','Common wheat','Loose Silky-bent']
        with open('_darknet.labels','a') as labelFile:
                for label in classList :
                        labelFile.write(label)
                        labelFile.write('\n')

        for line in data:
                path=line[0].replace(" ","")
                pathstrings = path.split('.')
                txtPath = pathstrings[0]+'.txt'
                print(txtPath)
                width=line[1].replace(" ","")
                height=line[2].replace(" ","")
                imageClass = line[3].replace(" ","")
                xmin = line[4].replace(" ","")
                ymin = line[5].replace(" ","")
                xmax = line[6].replace(" ","")
                ymax = line[7].replace(" ","")
                classIndex,xcen,ycen,w,h = BndBox2YoloLine(width,height,imageClass,xmin,xmax,ymin,ymax,classList)
                with open(txtPath,'a') as file:
                        file.write(str(classIndex)+" "+str(round(xcen,1))+" "+str(round(ycen,1))+" "+str(w)+" "+str(h))

