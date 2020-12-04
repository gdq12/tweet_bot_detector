import pandas as pd
import numpy as np
import os

tweet_columns = ['created_at', 'id', 'text', 'source', 'user_id', 'truncated', 'in_reply_to_status_id',
                 'in_reply_to_user_id', 'in_reply_to_screen_name', 'retweeted_status_id', 'geo', 'place',
                 'contributors', 'retweet_count', 'reply_count', 'favorite_count', 'favorited',
                 'retweeted', 'possibly_sensitive', 'num_hashtags', 'num_urls', 'num_mentions', 'timestamp']
user_columns = ['id', 'name', 'screen_name', 'statuses_count', 'followers_count', 'friends_count',
                'favourites_count', 'listed_count', 'created_at', 'url', 'lang', 'time_zone',
                'location', 'default_profile', 'default_profile_image', 'geo_enabled', 'profile_image_url',
                'profile_banner_url', 'profile_use_background_image', 'profile_background_image_url_https',
                'profile_text_color', 'profile_image_url_https', 'profile_sidebar_border_color',
                'profile_background_tile', 'profile_sidebar_fill_color', 'profile_background_image_url',
                'profile_background_color', 'profile_link_color', 'utc_offset', 'is_translator',
                'follow_request_sent', 'protected', 'verified', 'notifications', 'description',
                'contributors_enabled', 'following', 'updated']

def df_cleaner(directory):
    '''
    Creates 3 data frames from 9 csv files

    Parameters
    ----------
    directory: str
        string word of head directory name where files are

    Returns
    -------
    tweets: pandas df
        data frame of concatenated tweets
    users: pandas df
        data frame of concatenated user info
    user_index: pandas df
        data frame of user ids and corresponding their labels
    '''
    tweet_dfs = []
    user_dfs = []
    user_id = []
    label = []
    for folder in os.listdir(directory):
        if os.path.isdir(f'data/{folder}'):
            for subfolder in os.listdir(f'data/{folder}'):
                if 'tweet' in subfolder:
                    df = pd.read_csv(f'data/{folder}/{subfolder}')
                    tweet_dfs.append(df[tweet_columns])
                else:
                    df = pd.read_csv(f'data/{folder}/{subfolder}')
                    user_dfs.append(df[user_columns])
                    if 'accounts' in folder:
                        user_id.append(df['id'].unique())
                        label.append(np.full((len(df['id'].unique())), 0))
                    else:
                        user_id.append(df['id'].unique())
                        label.append(np.full((len(df['id'].unique())), 1))
    tweets = pd.concat(tweet_dfs, axis=0, ignore_index=True)
    users = pd.concat(user_dfs, axis=0, ignore_index=True)
    user_index = pd.DataFrame({'user_id': [item for sublist in user_id for item in sublist],
                              'label': [item for sublist in label for item in sublist]})
    return tweets, users, user_index

tweets, users, user_index=df_cleaner('../data')

tweets.to_csv('../data/tweets.csv')
users.to_csv('../data/users.csv')
user_index.to_csv('../data/user_index.csv')
