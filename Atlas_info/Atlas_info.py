import os
import nilearn
import nibabel as nib
import numpy as np

img = nib.load('/Users/oj/Desktop/post_fMRI/post_XCP-D_RBD/atlases/atlas-HCP/atlas-HCP_space-MNI152NLin2009cAsym_dseg.nii.gz')

data = img.get_fdata()

labels = np.unique(data)

print(len(labels))
