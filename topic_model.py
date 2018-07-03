from gensim import corpora, models

def getdata():
    #Getting the sample corpus
    corpus=corpora.BleiCorpus('D:/Projects/ap/ap.dat','D:/Projects/ap/vocab.txt')
    return corpus




def main():
    print("Topic Modelling started")
    data=getdata()
    topic(data)


def topic(data):
    print("Topic modelling method")
    model=models.ldamodel.LdaModel(data,num_topics=100,id2word=data.id2word)
    doc=data.docbyoffset(0)
    topics=model[doc]
    print(topics)

    
if __name__=="__main__":
    main()
