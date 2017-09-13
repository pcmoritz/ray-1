import wikipedia
import csv
import gensim

with open("top.txt") as f:
    lines = f.readlines()

with open('wikipedia-summaries.csv', 'w') as csvfile:
    wikiwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for line in lines:
        # Remove the trailing viewcount
        words = line.split(" ")[:-1]
        # Combine again and remove trailing ":"
        title = (" ".join(words))[:-1]
        print(title)
        article = wikipedia.page(title).content
        summary = gensim.summarization.summarize(article, ratio=0.1)
        print("article len = ", len(article), "; summary len = ", len(summary))
        wikiwriter.writerow([article, summary])
        
    
