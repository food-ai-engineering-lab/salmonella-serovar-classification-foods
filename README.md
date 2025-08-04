# salmonella-serovar-classification-foods
This repository is for the article **"Rapid *Salmonella* Serovar Classification Using AI-Enabled Hyperspectral Microscopy with Enhanced Data Preprocessing and Multimodal Fusion"**, published in Foods.

- Preprint: [DOI: 10.20944/preprints202507.1691.v1](https://doi.org/10.20944/preprints202507.1691.v1)
- Final Paper: Link to be updated

## Datasets

The processed dataset (i.e., single-cell spectra and RGB composite images) is available on Zenodo at [DOI: 10.5281/zenodo.16740800](https://zenodo.org/records/16740800).

- `spectra_single_cell.csv`: Single-cell spectral data extracted from hyperspectral cubes. Each row contains the spectral features and serovar label of one bacterial cell. Note that each hyperspectral data cube contains multiple cells.
- `images.zip`: RGB composite images generated from each hyperspectral cube, with one image corresponding to one hyperspectral data cube. This image directory follows the PyTorch `ImageFolder`-style structure: 

```bash
images/
├── train/
│   ├── Enteritidis/
│   ├── Infantis/
│   └── ...
└── evaluate/
    ├── img001.png
    ├── img002.png
    └── ...
```


## Processing Raw Hypercube Data

- `requirements.txt`: Python packages and versions used for data processing, modeling, and visualization. Install with `pip install -r requirements.txt`.
- `test_hmi.py`:
- `Serovar_PCA_ML_111524.ipynb`:


## Workflow for Model Training and Testing

- `Serovar_PCA_ML_111524.ipynb`:
- `fusion_2_cpu.ipynb`: 


## Acknowledgments

- Funding: This work was supported by MSU Startup Funds and USDA ARS Research Support Agreement (No. 58-6040-3-017 and 58-6040-4-041). Any opinion, findings, conclusion, or recommendations expressed in this paper are those of the author(s) and do not necessarily reflect the view of USDA.
- The authors thank Teresa M. Bergholz for providing the *Salmonella* strains used in this study.
