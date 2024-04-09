from embedding import E5LargeEmbeddingFunction
import torch
import nltk
from nltk.tokenize import word_tokenize
import clickhouse_connect
import pandas as pd
import num2text
import numpy as np

def prep_query(query):
    '''Перевод цифр в тексте в слова'''
    temp = [num2text.num2text(int(word)) if word.isdigit() else word for word in nltk.word_tokenize(query, language='russian')]

    sentence = ''
    for word in temp:
        if word not in ',,.?!:)»':
            sentence += " " + word

    return sentence

def get_window_range(num, window_range):
    '''Вспомогательная функция для определения окна в _clickhouse_query_window()'''
    answer = [num]
    while len(answer) < window_range:
        f = 0
        left = answer[0] - 1
        right = answer[-1] + 1

        if left >= 0:
            answer = [left] + answer
            if len(answer) >= window_range:
                return answer

        answer.append(right)
    
    return answer

def _clickhouse_query_l2(query, client, emb_func, limit=5, table='KOAP_RF'):
    '''Поиск релевантного чанка из КОАП по евклидовому расстоянию'''
    emb_func.change_mode('query')
    embeddings = emb_func(query)[0]    
    result = client.query(f'''SELECT
        page_num,
        page_text,
        L2Distance(embedding, {embeddings}) AS score,
        ID
    FROM {table}
    ORDER BY score ASC
    LIMIT {limit}''')

    return result.result_rows

def _clickhouse_query_window(query, client, emb_func, limit_knn=1, docs_window=3, table='KOAP_RF'):
    '''Помимо найденного чанка возвращаем два чанка вокруг него'''
    res = _clickhouse_query_l2(query, client, emb_func, limit=limit_knn, table=table)
    window_sql_query = ''
    for i, row in enumerate(res):
        if i > 0:
            window_sql_query += ' UNION DISTINCT '
        
        window_sql_query += f'''SELECT * FROM {table} WHERE page_num IN {tuple(get_window_range(row[0], docs_window))}'''
    
    result = client.query(window_sql_query)
    return result.result_rows