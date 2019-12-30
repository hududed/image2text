# Extract texts from images using tokens

This program aims to structure the extract texts from images that are typically jumbled when using Google OCR. In particular, we deal with texts from irregular table forms and store these electronically in a dataframe.

## Motivation

Although Google OCR output is often unstructured, we do get access to information about the entities and their positions in a JSON output file. However, the unstructured JSON data makes it difficult to extract tokens, i.e. characters without spaces in between. The objective is to postprocess the data so that extracting whole lines of text or phrases is possible. Once the tokens are extracted, we store them in a dataframe and clean the data according to our specifications. Note, the data clean-up here is strictly case-by-case and works relatively well for our problem.

## Requirements

This program uses google-cloud-vision. Try `pip install google-cloud-vision`.  
See [requirements](requirements.txt).   
This program assumes you have google credentials for google vision API setup (!).  


## Example Usage

Find the notebook [here](image2text_example.ipynb)
