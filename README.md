# Experts and Authorities receive disproportionate attention on Twitter during the COVID-19 crisis

This repository contains annotation data, ML models, and Twitter data related to the work "Experts and Authorities receive disproportionate attention on Twitter during the COVID-19 crisis".

If you intend to use any of these materials, please make sure to cite the work accordingly:
```
<citation to be added> 
```
## Annotation data

## Text classification models
Based on the annotation data provided above, several models have been trained on two different multiclass objectives:
* **Category**: Labels: "art", "business", "healthcare", "media", "ngo", "other", "political_supporter", "politics", "adult_content", "public_services", "religion", "science", "sports"
* **Type**: Labels: "individual", "institution", "unclear"

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

| Description                                         | Language  | Dataset  | Identifier          | Download |
|-----------------------------------------------------|-----------|----------|---------------------|----------|
| BERT multilingual category (BERT-multlingual cased) | multilang | category | `bert-multilang-pt` | [PyTorch](https://digitalepidemiologylab-publications-public.s3.eu-central-1.amazonaws.com/experts-covid19-twitter/models/category_bert_multilang_pt.tar.gz) \| [TF](https://digitalepidemiologylab-publications-public.s3.eu-central-1.amazonaws.com/experts-covid19-twitter/models/category_bert_multilang_tf.tar.gz) |
| BERT multilingual type (BERT-multlingual cased)     | multilang | type     | `bert-multilang-pt` | [PyTorch](https://digitalepidemiologylab-publications-public.s3.eu-central-1.amazonaws.com/experts-covid19-twitter/models/type_bert_multilang_pt.tar.gz) \| [TF](https://digitalepidemiologylab-publications-public.s3.eu-central-1.amazonaws.com/experts-covid19-twitter/models/type_bert_multilang_tf.tar.gz)  |
| BERT English category (BERT-large uncased)          | en        | category | `bert-english`      | [PyTorch](https://digitalepidemiologylab-publications-public.s3.eu-central-1.amazonaws.com/experts-covid19-twitter/models/category_bert_en_pt.tar.gz) \| [TF](https://digitalepidemiologylab-publications-public.s3.eu-central-1.amazonaws.com/experts-covid19-twitter/models/category_bert_en_tf.tar.gz) |
| BERT English type (BERT-large uncased)              | en        | type     | `bert-english`      | [PyTorch](https://digitalepidemiologylab-publications-public.s3.eu-central-1.amazonaws.com/experts-covid19-twitter/models/type_bert_en_pt.tar.gz) \| [TF](https://digitalepidemiologylab-publications-public.s3.eu-central-1.amazonaws.com/experts-covid19-twitter/models/type_bert_en_tf.tar.gz)  |
| FastText english category                           | en        | category | `fasttext-english`  | [Download](https://digitalepidemiologylab-publications-public.s3.eu-central-1.amazonaws.com/experts-covid19-twitter/models/category_fasttext.tar.gz) |
| FastText english type                               | en        | type     | `fasttext-english`  | [Download](https://digitalepidemiologylab-publications-public.s3.eu-central-1.amazonaws.com/experts-covid19-twitter/models/type_fasttext.tar.gz) |
