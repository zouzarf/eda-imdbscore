import json
import pandas as pd

def parse_awards(movie):
    awards_kept = ['Oscar', 'BAFTA Film Award', 'Golden Globe', 'Palme d\'Or'] #We would like to keep only this type of awards 
    awards_category = ['won', 'nominated']
    parsed_awards = {}
    for category in awards_category:
        for awards_type in awards_kept:
            awards_cat = [award for award in movie['awards'][category] if award['category'] == awards_type]
            for k, award in enumerate(awards_cat):
                parsed_awards['{}_{}_{}'.format(awards_type, category, k+1)] = award["award"]
    return parsed_awards


def parse_actors(movie):
    # We would like to keep only the three most liked actors in the cast
    sorted_actors = sorted(movie['cast_info'], key=lambda x:x['actor_fb_likes'], reverse=True)
    top_k = 3
    parsed_actors = {}
    parsed_actors['total_cast_fb_likes'] = sum([actor['actor_fb_likes'] for actor in movie['cast_info']]) + movie['director_info']['director_fb_links']
    for k, actor in enumerate(sorted_actors[:top_k]):
        if k < len(sorted_actors):
            parsed_actors['actor_{}_name'.format(k+1)] = actor['actor_name']
            parsed_actors['actor_{}_fb_likes'.format(k+1)] = actor['actor_fb_likes']
        else:
            parsed_actors['actor_{}_name'.format(k+1)] = None
            parsed_actors['actor_{}_fb_likes'.format(k+1)] = None
    return parsed_actors

def parse_production_company(movie):
    # We'd like to keep only 3 companies
    parsed_production_co = {}
    top_k = 3
    production_companies = movie['production_co'][:top_k]
    for k, company in enumerate(production_companies):
        if k < len(movie['production_co']):
            parsed_production_co['production_co_{}'.format(k+1)] = company
        else:
            parsed_production_co['production_co_{}'.format(k+1)] = None
    return parsed_production_co

def parse_genres(movie):
    #Convert genres to a dictionnary
    parse_genres = {}
    g = movie['genres']
    with open('genre.json', 'r') as f:
        genres = json.load(f)
    for k, genre in enumerate(g):
        if genre in genres:
            parse_genres['genre_{}'.format(k+1)] = genres[genre]
    return parse_genres



def create_dataframe(movies_content_path, movie_budget_path):
    with open(movies_content_path, 'r') as fp:
        movies = json.load(fp)
    with open(movie_budget_path, 'r') as fp:
        movies_budget = json.load(fp)
    movies_list = []
    for movie in movies:
        content = {k:v for k,v in movie.items() if k not in ['awards', 'cast_info', 'director_info', 'production_co']}
        name = movie['movie_title']
        try:
            budget = [film for film in movies_budget if film['movie_name']==name][0]
            budget = {k:v for k,v in budget.items() if k not in ['imdb_url', 'movie_name']}
            content.update(budget)
        except: 
            pass
        try:
            content.update(parse_awards(movie))
        except:
            pass
        try:
            content.update(parse_genres(movie))
        except:
            pass
        try:
            content.update({k:v for k,v in movie['director_info'].items() if k!= 'director_link'})
        except:
            pass
        try:
            content.update(parse_production_company(movie))
        except:
            pass
        try:
            content.update(parse_actors(movie))
        except:
            pass
        movies_list.append(content)
    df = pd.DataFrame(movies_list)
    df = df[pd.notnull(df.idmb_score)]
    df.idmb_score = df.idmb_score.apply(float)
    return df