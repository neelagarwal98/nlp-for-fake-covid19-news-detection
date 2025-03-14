from sklearn.feature_extraction.text import CountVectorizer

def return_count_embeddings(text_data, ngram):
    # function that receives text_data and tuple (for n-gram combination) as input and returns an array of vectorized embeddings  
    
    vectorizer = CountVectorizer(analyzer = 'word', ngram_range = ngram, lowercase = True) 
    vectorized = vectorizer.fit_transform(text_data)
    vectorized_array = vectorized.toarray()
    
    return vectorized_array

 




