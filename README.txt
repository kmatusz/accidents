Accidents injury prediction for ML1 course
Authors: Bugra Duman, Kamil Matuszelanski

To be able to run the codes:
1. Download the dataset from kaggle: https://www.kaggle.com/ahmedlahlou/accidents-in-france-from-2005-to-2016
2. Unpack the datasets into data/ folder


Files contents:
- 01_Users.ipynb - cleaning and EDA of accident participants dataset
- 02_Accidents.ipynb - cleaning and EDA of accident general information dataset
- 03_Places.ipynb - cleaning and EDA of information about accident location dataset
- 04_join_tables.ipynb - joining of datasets obtained from 3 previous notebooks
- 05_data_to_model.ipynb - preparation of final dataset to modeling, train test split
- 06_eda_feature_generation.ipynb - EDA of preprocessed variables and playground for features generation
- 07_Modeling.ipynb - MAIN notebook with all modeling performed
- 07_Modeling.html - notebook saved as html to ensure readability
- mappings.py - dictionaries to translate french names and encoding of categorical variables from numeric to meaningful format
- spec-file.txt - requirements for conda environment for full reproducibility
- data/ - here downloaded dataset should be unpacked and put. Also preprocessed datasets are saved here.
- models_cache/ - folder with saved outputs from longest-running models and code chunks. This was neccessary as many things we tried took more than 1 hour (when running on the cloud with 32 cores)