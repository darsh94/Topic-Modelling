from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

import pandas as pd
from sqlalchemy import create_engine



def preprocessed(email):

    data=word_tokenize(email)
    if "Forwarded" in data:
        data=data[data.index('Forwarded')+2:]
        try:
            data=data[data.index('Subject')+2:]
        except Exception as e:
            print(e)
            # print(data)
            # data=data[data.index('From'):]
            # exit()
            # print(data)
    elif ".pst" in data:
        data=data[data.index('.pst')+1:]

    else:
        data=data[data.index('X-FileName')+3:]
    stop_words=set(stopwords.words('English'))
    filtered_data=[]
    stemmer = PorterStemmer()
    for d in data:
        if d not in stop_words:
            filtered_data.append(stemmer.stem(d))

    # print(data)

    return " ".join(filtered_data)



def get_preprocessed_data():
    emails=pd.read_csv('D:/Projects/Data/enron-email-dataset/emails.csv',chunksize=1000)


    for email in emails:
        print(type(email))
        # print(email['message'])
        for index,row in email.iterrows():
            # print(row['message'])
            temp=preprocessed(row['message'])
            # temp=" ".join(temp[temp.index('X-FileName')+3:])
            print(temp)
            # break

            # print(row['message'])
        # for index,row in email.iteritems():
        #     print()
            # email[index]['preprocessed_data']=preprocessed(row['message'])
            # print(email['preprocessed_data'])
            # break
        break



def main():
    print("in main method")
    get_preprocessed_data()
    # Using chunksize to handle memory issues
    # Chunksize gives adataframe, having records equal to the size described
    # print(len(temp))

    # for i in temp:
    #     print(i['message'])
    #     break
        # print(i['message'])


        # break
        # print(i.keys())
        # print(i['message'][0])
        # print(type(i))


        # count=count+1
        # if count==2:
        #   break
        # print(i)
      # break
    # print(len(temp))



if __name__=="__main__":

    main()