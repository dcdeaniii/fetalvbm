#!/usr/bin/env python
import os
from pathlib import Path
import ants

def get_template(gest_age):
    
    template_dir = Path(__file__).parent.resolve()

    template_t2w      = Path.joinpath(template_dir, 'templates/STA'+str(gest_age)+'.nii.gz')
    template_regional = Path.joinpath(template_dir, 'templates/STA'+str(gest_age)+'_regional.nii.gz')
    template_tissue   = Path.joinpath(template_dir, 'templates/STA'+str(gest_age)+'_tissue.nii.gz')
        
    return template_t2w, template_regional, template_tissue

def run(input_file, input_mask, gest_age, output_dir):

    #Check if output directory exists and if not, create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
      
    #Get the template based on the input gestational age
    template, regional, tissue = get_template(gest_age)
    

    #Load the data and perform the registration
    #
    # Fixed/Target Image  -> Input image
    # Moving Image        -> Template image
    #
    #
    
    fi   = ants.image_read(input_file)
    mask = ants.image_read(input_mask)
    
    mi   = ants.image_read(template.as_posix())
    
    
    #Apply the mask to the input
    fi = ants.utils.mask_image(fi, mask)
    
    mytx = ants.registration(fixed             = fi,
                             moving            = mi,
                             type_of_transform = 'SyN')
        
    
    #Now transform the labels to the input image
    regional_labels = ants.image_read(regional.as_posix())
    tissue_labels  = ants.image_read(tissue.as_posix())
    
    warped_regional = ants.apply_transforms(fixed=fi,
                                            moving=regional_labels,
                                            transformlist=mytx['fwdtransforms'],
                                            interpolator = 'genericLabel')
    
    warped_tissue = ants.apply_transforms(fixed=fi,
                                          moving=tissue_labels,
                                          transformlist=mytx['fwdtransforms'],
                                          interpolator = 'genericLabel')
                                          
    #Save the labels to the output-directory
    warped_regional.to_file(os.path.join(output_dir, "fetal-regional-labels.nii.gz"))
    warped_tissue.to_file(os.path.join(output_dir, "fetal-tissue-labels.nii.gz"))


def fetalvbm(input_img, input_mask, gest_age):

    output_dir = "/flyweel/v0/output"

    run(input_file = input_img,
        input_mask = input_mask,
        gest_age   = gest_age,
        output_dir = output_dir)
    

       
   
   








