## This contains additional function for content based

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import preprocessedcourse

course_list_df = pd.DataFrame.from_records(preprocessedcourse.objects.all().values())

def cosine_indices_maker(data = course_list_df):
    count = TfidfVectorizer()
    count_matrix = count.fit_transform(data['tag'])
    cosine_sim = cosine_similarity(count_matrix,count_matrix)
    indices = pd.series(data.index,index = data['id'])
    np.save('C:/Users/acer/PycharmProjects/Content_Based_Recommendation/content_base/data/cosine_sim.pkl',cosine_sim,allow_pickle=True, fix_imports=True)
    indices.to_pickle('C:/Users/acer/PycharmProjects/Content_Based_Recommendation/content_base/data/indices.pkl')
    return {{'status':'Cosine_sim and indices_saved'}}
