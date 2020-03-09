from ctypes import *
import numpy as np
from PIL import Image, ImageTk
from numpy import linalg as LA
import time



"""

"""
class DistXYZ(Structure):
    _fields_ = [("x", c_uint16),
              ("y", c_uint16),
              ("z", c_uint16)]
"""
------------------------
"""
class _U(Union):
    _fields_ = [("data", c_ubyte*6),
                ("DistXYZ", DistXYZ)]







def getPixel(data,x,y):
    """
    function to recover the 3d coordinates [X, Y, Z] of the pixel (y, x) of the color image\n
    data : numpy.array of imageXYZ.png : '  data=np.array(Image.open(ficXYZ)))  '\n
    x : pixel column number of image color \n
    y : pixel line number of image color \n
    """
    d0= data[y,x*2]
    
    if ( (d0[0]==255) and (d0[1]==127)):
        return [0.0,0.0,0.0]
    d1= data[y,x*2+1]
    test=_U()
    test.data=(c_ubyte * 6)(d0[0],d0[1],d0[2],d1[0],d1[1],d1[2])
    X=hex (test.DistXYZ.x)
    Y=hex (test.DistXYZ.y)
    Z=hex (test.DistXYZ.z)
    
    X=float(int(X,16)-int("0x7FFF",16))/1000.0
    Y=float(int(Y,16)-int("0x7FFF",16))/1000.0
    Z=float(int(Z,16)-int("0x7FFF",16))/1000.0
    return [X,Y,Z]




def loadDeth(ficXYZ):
    """
    function to transform an imageXYZ into numpy.array\n
    numpy.array(pixelLine,pixelColumn,(X,Y,Z))
    ficXYZ : file path of imageXYZ.png
    """
    data=np.array(Image.open(ficXYZ))
    cloud=data.reshape((-1)).view(dtype=np.uint16).reshape((data.shape[0],data.shape[1]/2,data.shape[2]))-0x7FFF
    # change of the type of the data to correspond to the encoding of the data in the imageXYZ + data refocusing
    cloud=cloud.astype('int16')
    cloud=cloud.astype('float32')/1000.0
    return cloud


if __name__ == '__main__':
    #cloud=loadDeth('/home/user/coffredetoit/transdev/usbDisk/2020_02_18/Kitty/datasOld/ImageXYZ_20200303_140933/data/0000000012.png')
    cloud=loadDeth('/home/user/coffredetoit/transdev/usbDisk/2020_02_18/Kitty/datasOld/ImageXYZ_20200303_140933/data/0000005515.png')
    #save to point cloud if necessary
    np.savetxt("./pointCloud.csv",cloud.reshape((-1,3)) )
    print ("end:",time.time()-t)




