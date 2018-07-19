from gensim import corpora, models
import matplotlib.pyplot as plt

def getdata():
    #Getting the sample corpus
    corpus=corpora.BleiCorpus('D:/Projects/ap/ap.dat','D:/Projects/ap/vocab.txt')
    return corpus




def main():
    print("Topic Modelling started")
    data=getdata()
    topic(data)


def topic(corpus):
    print("Topic modelling method")
    model=models.ldamodel.LdaModel(corpus,num_topics=100,id2word=corpus.id2word,alpha=1)
    doc=corpus.docbyoffset(0)
    topics=model[doc]
    print(topics)
    num_topics=[(len(model[doc])) for doc in corpus]
    plt.hist(num_topics)
    plt.show()
    
    

    
if __name__=="__main__":
    main()
