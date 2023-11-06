import pandas as pd
from .models import course_list,tag
course_list_path = 'C:/Users/acer/PycharmProjects/Content_Based_Recommendation/content_base/data/courseInfo_Oct19.pkl'
tag_path = 'C:/Users/acer/PycharmProjects/Content_Based_Recommendation/content_base/data/tag_Oct19.pkl'
def retrive_data(table_name: str):
    if table_name == 'course_lists':
        course_list_path = 'C:/Users/acer/PycharmProjects/Content_Based_Recommendation/content_base/data/courseInfo_Oct19.pkl'
        df = pd.read_pickle(course_list_path)

        model_instance = [
            course_list(
                id=df_row['id'],
                Course_Name=df_row['Course_Name'],
                course_code=df_row['course_code'],
                Course_Description=df_row['Course_Description'],
                Course_Cover_File=df_row['Course_Cover_File'],
                Course_Level=df_row['Course_Level'],
                Course_Info=df_row['Course_Info'],
                Use_Flag=df_row['Use_Flag'],
                Register_DateTime=df_row['Register_DateTime'],
                Updated_DateTime=df_row['Updated_DateTime'],
                Register_Agent=df_row['Register_Agent'],
                Course_Provider=df_row['Course_Provider'],
                Syllabus=df_row['Syllabus'],
                keyword=df_row['keyword'],
                Center_Code=df_row['Center_Code'],
                tag=df_row['tag'])
            for df_row in df.to_dict(orient='records')
        ]

        # Use the Django model to insert data into the database
        if course_list.objects.all().exists():
            course_list.objects.all().delete()
        course_list.objects.bulk_create(model_instance)
    else:
        return {"status": "invalid table name."}

    return {"status": "preprocessed data updated."}

# list = [for df_row in course_list.to_dict(orient='records')]
