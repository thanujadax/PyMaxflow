import numpy as np
from scipy.misc import imread
from matplotlib import pyplot as ppl
from PIL import Image
import glob
import os

import binarizeProbabilityImageGC

inputDir = '/home/thanuja/DATA/ISBI2012/gala/flatfiles/test/probMaps_rfc'
outputRoot = '/home/thanuja/RESULTS/isbi2012/graphcuts/rfc'

numImages = 10
k = 50
imagePath = sorted(glob.glob(inputDir+'/*.tif') )
for i in range(0,numImages):    
    imIn = np.array(Image.open(imagePath[i]).convert('L'), 'f')
    imOut = binarizeProbabilityImageGC.doGC(imIn,k)
    # save
    imFileName = str(i).zfill(3) + ".png"
    imFileName = os.path.join(outputRoot,imFileName)
    #scipy.misc.toimage(im, cmin=0.0, cmax=...).save(imFileName)
    imOut.save(imFileName)


