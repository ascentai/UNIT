import os, argparse
import glob
import numpy as np

parser = argparse.ArgumentParser(description='generate a train and a test list of images')
parser.add_argument('-f', help='images folder',              dest='images_folder', type=str,   required=True)
parser.add_argument('-s', help='suffix for the list names',  dest='suffix',        type=str,   default='') 
parser.add_argument('-r', help='rate of images for training',dest='r',             type=float, default=0.8)
    
args = parser.parse_args()

ll = glob.glob(os.path.join(args.images_folder,'*'))
ll = [x.split('/')[-1] for x in ll] # keep only the name of the image
np.random.shuffle(ll)
separation_index = int(len(ll)*args.r)
ll_train = ll[:separation_index]
ll_test = ll[separation_index:]
with open('train_'+args.suffix+'.txt','w') as f:
    f.writelines('\n'.join(ll_train))
    f.close()
with open('test_'+args.suffix+'.txt','w') as f:
    f.writelines('\n'.join(ll_test))
    f.close()    

