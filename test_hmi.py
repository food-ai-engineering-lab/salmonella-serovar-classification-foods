import os
import bacterial_hmi as bhmi

# path to main folder and name of folders
main_path = "/mnt/data/Salmonella_serovars"  
# change to class names
serovars = ['Infantis', 'Kentucky', 'Johannesburg', 'I4', 'Enteritidis']

# iterate through each folder name
for serovar in serovars:
    serovar_path = os.path.join(main_path, serovar)
    
    # Iterate through all images for each folder
    for image_folder in os.listdir(serovar_path):
        image_folder_path = os.path.join(serovar_path, image_folder)
        
        # find dat file
        dat_file = None
        for file in os.listdir(image_folder_path):
            if file.endswith('.dat'):
                dat_file = os.path.join(image_folder_path, file)
                break
        
        # if dat found use bhmi (bacterial segmentation package) to get single cell spectra
        if dat_file:
            try:
                bhmi.extract_hmi_data(dat_file)
                print(f"Processed BHMI for {dat_file}")
            except Exception as e:
                print(f"Error processing {dat_file}: {e}")
        else:
            print(f"No .dat file found in {image_folder_path}")

