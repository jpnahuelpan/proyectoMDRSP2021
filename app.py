#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Integrantes : Juan Pablo Nahuelpán, Pelegrin Huichalaf
"""

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import tweepy
from textblob import TextBlob
import numpy as np
from sklearn.linear_model import LinearRegression


def obt(usuario, n, api):
    searched_tweets = [status for status in tweepy.Cursor(api.user_timeline,
                                                          screen_name=usuario,
                                                          include_rts=True).items(n)]
    datos = []
    for tweets in searched_tweets:
        autor = tweets.author.screen_name
        t_id = tweets.id
        texto = tweets.text
        like =  tweets.favorite_count
        retweet_count = tweets.retweet_count
        fecha = tweets.created_at
        
        datos.append([str(t_id),
                    str(autor),
                    str(texto),
                    int(like),
                    int(retweet_count),
                    fecha.isoformat()])

    headers = ['Id_Tweet',
                'Autor',
                'Texto',
                'Likes',
                'Número de retweets',
                'Fecha']

    return datos, headers

def sentimiento(usuario,n, api):
    searched_tweets = [status for status in tweepy.Cursor(api.user_timeline,
                                                          screen_name=usuario).items(n)]
    pos = 0
    neg = 0
    neu = 0
    for tweet in searched_tweets:
        text= TextBlob(tweet.text)
        if text.polarity < 0:
            neg += 1
        elif text.polarity > 0:
            pos += 1
        else:
            neu += 1

    labels = ['Positivo', 'Negativo', 'Neutro']
    sizes = [pos, neg, neu]
    return sizes, labels


app = FastAPI()
templates = Jinja2Templates(directory="templates")
global api

consumer_key = ""
consumer_key_secret = ""
access_token = ""
access_token_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

@app.get("/", response_class=HTMLResponse)
async def forma(request: Request):
    usuario = "escriba un usuario de tweeter"
    tweets = 0
    return templates.TemplateResponse("forma.html",
                                      {"request": request,
                                       "usuario": usuario,
                                       "tweets": tweets})

@app.post("/", response_class=HTMLResponse)
async def forma(request: Request,
                usuario: str=Form( None ),
                tweets: int=Form( 0 )):

    tweets = abs(tweets) 

    aux_data, aux_headers  = sentimiento(usuario, tweets, api)     
    data, headers = obt(usuario, tweets, api)
    max_retweet = np.array(data)[:, [4]]
    max_retweet = max_retweet.astype(int)
    max_like = np.array(data)[:, [3]]
    max_like = max_like.astype(int)

    # regresion lineal.
    lg = LinearRegression().fit(max_retweet, max_like)
    lg_y = [float(y) for y in lg.predict(max_retweet)]

    max_retweet = max(max_retweet)
    max_like = max(max_like)
    return templates.TemplateResponse("tweets.html",
                                        {"request": request,
                                        "usuario": usuario,
                                        "tweets": tweets,
                                        "data": data,
                                        "headers": headers,
                                        "max_like": int(max_like * 1.01),
                                        "max_retweet": int(max_retweet * 1.01),
                                        "lg_y": lg_y,
                                        "aux_data": aux_data,
                                        "aux_headers": aux_headers})
