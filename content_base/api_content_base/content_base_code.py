import pandas as pd
import numpy as np
from .models import preprocessedcourse

course_list = pd.DataFrame.from_records(preprocessedcourse.objects.all().values())
# course_list = pd.read_pickle('C:/Users/acer/PycharmProjects/Content_Based_Recommendation/content_base/data/courseInfo_Oct19.pkl')
cosine_sim = np.load('C:/Users/acer/PycharmProjects/Content_Based_Recommendation/content_base/data/cosine_sim.pkl.npy')
indices = pd.read_pickle('C:/Users/acer/PycharmProjects/Content_Based_Recommendation/content_base/data/indices.pkl')

def content_based(course_id:int,data = course_list,indices = indices,cosine_sim = cosine_sim)->list:
    id = indices[course_id]
    sim = [(index, cosine_sim[id][index]) for index in range(len(cosine_sim[id]))]
    sim = sorted(sim, key=lambda x: x[1], reverse=True)
    sim = sim[1:6]
    index = [i[0] for i in sim]
    return data['Course_Name'].iloc[index].to_list()

