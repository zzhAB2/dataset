The data used comes from the data folder. 
According to the number of triples, the data is divided into 1_triples.json, 2_triples.json, etc. to evaluate the model’s extraction performance under different numbers of triples.
Based on the different patterns of the triples, the data is divided into SEO_triples.json, SOO_triples.json, EPO_triples.json, and Normal_triples.json to assess the model’s accuracy under different patterns.

all_data.json contains all the data.
all_triples.json includes all the extracted results. 

data_process_4classify.py and data_process_three_example.py are used for dividing the dataset. 
Files prefixed with train are used for training, those prefixed with dev are for validation, and those prefixed with test are for testing. 
Files suffixed with compare are used to calculate the F1-score, recall, and precision of different models.
