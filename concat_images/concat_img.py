import nilearn
from nilearn import image
import glob


def concat_3d_to_4d(input_dir, output_file):
    # Find all .nii or .nii.gz files in the input directory
    nifti_files = sorted(glob.glob(f"{input_dir}/*.nii.gz*"))

    if not nifti_files:
        print("No NIfTI files found in the specified directory.")
        return

    # Concatenate the images into a single 4D image
    concat_img = image.concat_imgs(nifti_files)

    # Save the resulting 4D image to the specified output file
    concat_img.to_filename(output_file)

    print(f"Concatenated {len(nifti_files)} files into {output_file}")


input_dir = '/Users/oj/Desktop/Yoo_Lab/pre_BIDS/BIDS_HC/sub-01/func'
output_dir = '/Users/oj/Desktop/Yoo_Lab/pre_BIDS/BIDS_HC/sub-01/func'

concat_3d_to_4d(input_dir,output_dir)
