# Experts and Authorities receive disproportionate attention on Twitter during the COVID-19 crisis

This repository contains annotation data, ML models, and Twitter data related to the work "Experts and Authorities receive disproportionate attention on Twitter during the COVID-19 crisis".

If you intend to use any of these materials, please make sure to cite the work accordingly:
```
<citation to be added> 
```
## Annotation data
User descriptions have been annotated by `type` and `category`. Find the data [here](data/annotation_data/annotation_data.csv).

The CSV file has the following columns:
| Column        | Description                                            |
|---------------|--------------------------------------------------------|
| user.id       | Twitter user ID                                        |
| category      | Consensus category (collapsed*)                         |
| type          | Consensus type                                         |
| tweeting_lang | Language user is tweeting in usually                   |
| bio_lang      | Language bio (user description) is written in          |
| type_1        | Type annotation by annotator 1                         |
| type_2        | Type annotation by annotator 2                         |
| type_3        | Type annotation by annotator 3                         |
| type_4        | Type annotation by annotator 4 (if available)          |
| category_1    | Categories (uncollapsed) by annotator 1                |
| category_2    | Categories (uncollapsed) by annotator 2                |
| category_3    | Categories (uncollapsed) by annotator 3                |
| category_4    | Categories (uncollapsed) by annotator 4 (if available) |

The annotations contain the following labels:
* **Category (collapsed)**: Labels: "art", "business", "healthcare", "media", "ngo", "other", "political_supporter", "politics", "adult_content", "public_services", "religion", "science", "sports"
* **Type**: Labels: "individual", "institution", "unclear"

Additionally, the following category labels have a more fine-grainded annotation:
* "media": "Media: News", "Media: Scientific News and Communication", "Media: Other Media"
* "science": "Science: Engineering and Technology", "Science: Life Sciences", "Science: Social Sciences", "Science: Other Sciences"

Please refer to our paper for a more in-detail explanation for the individual annotations, and how the annotation was performed.

## Text classification models
Based on the annotation data provided above, several models have been trained on the **category** (collapsed) and **type** objectives (as described above).

The models made available are from two different model types (BERT-like and Fasttext). For more info regarding training procedure, please check the SI of the paper.

### BERT
The easiest way to use the BERT models is by using the PyTorch models together with the [huggingface/transformers](https://github.com/huggingface/transformers) library. To install run
```bash
pip install transformers
```

Then from the table below download a suitable PyTorch checkpoint, extract it using `tar -xzf <tar_file>` and run:
```python
from transformers import pipeline

path_to_model = './category_bert_multilang_pt/'

# We are using the sentiment-analysis type (even though our model is not a sentiment analysis model)
pipe = pipeline('sentiment-analysis', model=path_to_model, tokenizer=path_to_model)

# Feed an example input
pipe('artiste et paintre')
# output:
# [{'label': 'art', 'score': 0.9069588780403137}]
```

For the TF checkpoints you should use them with [tensorflow/models](https://github.com/tensorflow/models/tree/master/official/nlp/bert).

## FastText
To use the FastText models runs
```bash
pip install fasttext
```
Download & extract one of the FastText models and run
```python
import fasttext

model = fasttext.load_model('./category_fasttext/model.bin')
print(model.predict('virologist'))
# (('__label__science',), array([0.98916745]))
```

## Download models

| Description                                         | Language  | Dataset  | Identifier          | Size | Download |
|-----------------------------------------------------|-----------|----------|---------------------|------|----------|
| BERT multilingual category (BERT-multlingual cased) | multilang | category | `bert-multilang-pt` | 630MB | [PyTorch](https://digitalepidemiologylab-publications-public.s3.eu-central-1.amazonaws.com/experts-covid19-twitter/models/category_bert_multilang_pt.tar.gz) \| [TF](https://digitalepidemiologylab-publications-public.s3.eu-central-1.amazonaws.com/experts-covid19-twitter/models/category_bert_multilang_tf.tar.gz) |
| BERT multilingual type (BERT-multlingual cased)     | multilang | type     | `bert-multilang-pt` | 630MB | [PyTorch](https://digitalepidemiologylab-publications-public.s3.eu-central-1.amazonaws.com/experts-covid19-twitter/models/type_bert_multilang_pt.tar.gz) \| [TF](https://digitalepidemiologylab-publications-public.s3.eu-central-1.amazonaws.com/experts-covid19-twitter/models/type_bert_multilang_tf.tar.gz)  |
| BERT English category (BERT-large uncased)          | en        | category | `bert-english`      | 1.2GB | [PyTorch](https://digitalepidemiologylab-publications-public.s3.eu-central-1.amazonaws.com/experts-covid19-twitter/models/category_bert_en_pt.tar.gz) \| [TF](https://digitalepidemiologylab-publications-public.s3.eu-central-1.amazonaws.com/experts-covid19-twitter/models/category_bert_en_tf.tar.gz) |
| BERT English type (BERT-large uncased)              | en        | type     | `bert-english`      | 1.2GB | [PyTorch](https://digitalepidemiologylab-publications-public.s3.eu-central-1.amazonaws.com/experts-covid19-twitter/models/type_bert_en_pt.tar.gz) \| [TF](https://digitalepidemiologylab-publications-public.s3.eu-central-1.amazonaws.com/experts-covid19-twitter/models/type_bert_en_tf.tar.gz)  |
| FastText english category                           | en        | category | `fasttext-english`  | 200MB | [Download](https://digitalepidemiologylab-publications-public.s3.eu-central-1.amazonaws.com/experts-covid19-twitter/models/category_fasttext.tar.gz) |
| FastText english type                               | en        | type     | `fasttext-english`  | 426MB | [Download](https://digitalepidemiologylab-publications-public.s3.eu-central-1.amazonaws.com/experts-covid19-twitter/models/type_fasttext.tar.gz) |
