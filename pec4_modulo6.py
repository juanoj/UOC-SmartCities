import pandas as pd
import pathlib
import os
import PIL

def scoring_maping(current: str,path: str, file: str):
    classes_scored = pd.read_csv(current+path+file, header=None)
    score = { k:v for(k,v) in zip(classes_scored[0], classes_scored[2])}
    return score

def image_score(current: str, path: str, city: str, images: pd.DataFrame):
    df=pd.DataFrame()
    scores = []
    df= images[(images['city'] == city)]
    score = scoring_maping(current,path,'class_name_scoring.csv')
    df['score'] = df['id'].map(score)
    group = df.groupby('image_id')
    for name_of_group, contents_of_group in group:
        temp = df[df['image_id'] == name_of_group]
        total_score = int(temp.groupby(['image_id']).sum()['score'])
        scores.append({name_of_group:total_score})
    return scores

def validate_img_file (current : str, path : str):
    directory = pathlib.Path(current+path)
    for file in directory.iterdir():
        if os.path.isfile(file):
            filename = str(file).split('\\')[-1]
            if filename.startswith('zurich'):
                img = PIL.Image.open(current+path+filename)
                wid, hgt = img.size
                if wid*hgt<2097152:
                    print(filename)
    return