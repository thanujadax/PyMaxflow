import numpy as np
from scipy.misc import imread
from matplotlib import pyplot as ppl
from PIL import Image
import glob
import os

import binarizeProbabilityImageGC

inputImg = '/home/thanuja/DATA/ISBI2012/gala/flatfiles/test/probMaps_rfc/020.tif'
outputRoot = '/home/thanuja/RESULTS/isbi2012/graphcuts/rfc/tryk'


for k in range(5,105,5):    
    imIn = np.array(Image.open(inputImg).convert('L'), 'f')
    imOut = binarizeProbabilityImageGC.doGC(imIn,k=k)
    # save
    imFileName = str(k).zfill(3) + ".png"
    imFileName = os.path.join(outputRoot,imFileName)
    #scipy.misc.toimage(im, cmin=0.0, cmax=...).save(imFileName)
    imOut.save(imFileName)
