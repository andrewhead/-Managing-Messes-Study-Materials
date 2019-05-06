import csv

def read_data(filename, encoding=None):
    data = []
    with open(filename, encoding=encoding) as f:
        reader = csv.DictReader(f)
        for row in reader:
            d = {
                'budget': float(row['budget']),
                'genres': row['genres'].split("|"),
                'original_language': row['original_language'],
                'original_title': row['original_title'],
                'overview': row['overview'],
                'production_companies': row['production_companies'],
                'production_countries': row['production_countries'],
                'revenue': float(row['revenue']),
                'spoken_languages': row['spoken_languages'],
                'tagline': row['tagline'],
                'title': row['title'],
                'vote_average': float(row['vote_average']),
                'vote_count': int(row['vote_count']),
                'spoken_languages_number': int(row['spoken_languages_number'])
            }
            if row['runtime'] != "":
                d['runtime'] = float(row['runtime'])
            else:
                d['runtime'] = 0
            if row['popularity'] != "":
                d['popularity'] = float(row['popularity'].replace("E", "e").replace(",", "."))
            else:
                d['popularity'] = 0
            if '-' in row['release_date']:
                d['release_day'] = int(row['release_date'].split('-')[2])
                d['release_month'] = int(row['release_date'].split('-')[1])
                d['release_year'] = int(row['release_date'].split('-')[0])
            elif row['release_date'] != '':
                d['release_day'] = int(row['release_date'].split('/')[1])
                d['release_month'] = int(row['release_date'].split('/')[0])
                d['release_year'] = int(row['release_date'].split('/')[2])
            else:
                d['release_day'] = None
                d['release_month'] = None
                d['release_year'] = None
            data.append(d)
        return data