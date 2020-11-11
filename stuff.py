import cv2,os

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
                   
dirs = [ 'C:\MERTVV\m1', 'C:\MERTVV\m2', 'C:\MERTVV\m3']

count = 0
count_h = 0
for path in dirs:
    files = os.listdir(path)    
    count += len(files)
    for pic in files:
        if pic[-4:]=='.png':
            img = cv2.imread(str(path+'/'+pic))
            scale_percent = 150 # percent of original size
            width = int(img.shape[1] * scale_percent / 100)
            height = int(img.shape[0] * scale_percent / 100)
            dim = (width, height)
            img = cv2.resize(img,dim)
            (rects, weights) = hog.detectMultiScale(img, scale = 1.4 , winStride = (1,1)) 
            print(pic)
            print(len(rects))
            count_h+=len(rects)
        
        
print("количество файлов: ",count)      
print("количество пешеходов: ",count_h)
print("соотношение пешеходв к количеству фотографий: ",count_h/count)

