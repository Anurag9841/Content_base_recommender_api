# import jit as jit
from numba import jit, cuda
import numpy as np
import pandas as pd
import itertools
from itertools import chain
from nltk.stem import PorterStemmer
import re
import nltk
import neattext.functions as nfx
from concurrent.futures import ThreadPoolExecutor
from googletrans import Translator
from .models import tag,preprocessedtag,course_list,preprocessedcourse
import warnings
warnings.filterwarnings("ignore")
import ast
def content_based_pipeline(course_list ,Tag):
  course_list = course_list[["id","Course_Name","tag",'Center_Code']]

  def parse_list(input_str):
      return ast.literal_eval(input_str)

  # Apply the function to the specified column using apply
  course_list['tag'] = course_list['tag'] .apply(lambda x: parse_list(x))
  def convert_to_int(lst):
    if len(lst) != 0 and lst !='[':
        return [int(i) for i in lst]
    else:
        return ''
  course_list['tag'] = course_list['tag'].apply(convert_to_int)
  Tag = Tag[["id","tag_name"]]
  Tag['tag_name'] = Tag['tag_name'].apply(str.lower)
  stemmer = PorterStemmer()
  tags_stem =[]
  tags = Tag['tag_name'].to_list()
  for word in tags:
    stem_word = stemmer.stem(word)
    tags_stem.append(stem_word)
  Tag['tag_name'] = [i for i in tags_stem]

  def mapping(list):
    if list!=None and len(list)!=0:
        return [Tag[Tag['id']==i]["tag_name"]for i in list]
    else:
        return ''
  course_list["tag"] = course_list["tag"].apply(mapping)
  for i in range(len(course_list["tag"])):
    if course_list["tag"][i] != []:
        course_list["tag"][i] = [item for sublist in course_list["tag"][i] for item in sublist]
    else:
        course_list["tag"][i] = []
  for i in range(len(course_list["tag"])):
    if course_list["tag"][i]!=[]:
        course_list["tag"][i]=' '.join(course_list["tag"][i])
    else:
        course_list["tag"][i]=' '.join(course_list["tag"][i])
  def clean(x):
    if isinstance(x,str):
        return str.lower(x)
    else:
        return ''
  course_list["tag"] = course_list["tag"].apply(clean)
  course_list["tag"]=course_list["tag"].apply(nfx.remove_stopwords)
  course_list["tag"]=course_list["tag"].apply(nfx.remove_special_characters)
  course_list["tag"]=course_list["tag"].apply(nfx.remove_puncts)
  course_list["tag"]=course_list["tag"].apply(nfx.remove_numbers)
  return course_list

def preprocessingTag(tag):
    tag = tag[['id','tag_name']]
    tag_names = tag['tag_name'].tolist()
    def preprocess_tag(tag_name):
        tag2 = re.sub(r'https?:\/\/.*[\r\n]*','.',tag_name)
        return tag2
    cleaned_tag = []
    for word in tag_names:
        cleaned_tag.append(preprocess_tag(word))

    @jit(target_backend='cuda')
    def translate_tag(cleaned_tag):
        translator = Translator()
        translated_tag = translator.translate(cleaned_tag, src='id', dest='en')

        if translated_tag is not None and translated_tag.text:
            return translated_tag.text
        else:
            return ''

    with ThreadPoolExecutor(max_workers=4) as executor:
        translated_tags = list(executor.map(translate_tag, cleaned_tag))
    tag['tag_name'] = translated_tags
    return tag
#
# tag = pd.DataFrame.from_records(tag.objects.all())
# tag = pd.read_pickle('C:/Users/acer/PycharmProjects/Content_Based_Recommendation/content_base/data/tag_Oct19.pkl')
# preprocessed = preprocessingTag(tag)
# print(preprocessed.head())

def taged():
    tags = pd.DataFrame.from_records(tag.objects.all().values())
    preprocessed = preprocessingTag(tags)
    return preprocessed

def coursed():
    course_lists = pd.DataFrame.from_records(course_list.objects.all().values())
    preprocess_tag = pd.DataFrame.from_records(preprocessedtag.objects.all().values())
    preprocessed = content_based_pipeline(course_lists,preprocess_tag)
    return preprocessed
def preprocess_pipeline(table_name:str):
    if table_name == 'tag':
        df = taged()
        model = preprocessedtag
        model_instance = [model(id = df_row['id'],
                                tag_name = df_row['tag_name'])for df_row in df.to_dict(orient='records')]
        if model.objects.all().exists():
            model.objects.all().delete()
        model.objects.bulk_create(model_instance)

    elif table_name == 'course_list':
        df = coursed()
        model = preprocessedcourse
        model_instance = [model(id = df_row['id'],
                                Course_Name = df_row['Course_Name'],
                                Center_Code = df_row['Center_Code'],

                                tag = df_row['tag'])for df_row in df.to_dict(orient = 'records')]
        if model.objects.all().exists():
            model.objects.all().delete()
        model.objects.bulk_create(model_instance)

    else:
        return {"status": "invalid table name."}

    return {"status": "preprocessed data updated."}


# hello this is anurag
