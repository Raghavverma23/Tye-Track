import networkx as nx
import matplotlib.pyplot as plt


# This function returns the words in the document read
def get_words():
    words = []
    with open('{User_document_here}', 'r') as file:
        for line in file:
            for word in line.split():
                words.append(word)
            return words


# This function adds edges to the consecutive words found in document
def get_connections(G):
    with open('{User_document_here}', 'r') as file:
        for line in file:
            words = line.strip().split()
            for word1, word2 in zip(words, words[1:]):
                if(G.has_edge(word1, word2) == True):
                    G[word1][word2]['weight'] += 1
                else:
                    G.add_edge(word1, word2, weight=1)


# This function plots the graph of all words and connections between them
def get_graph(G):
    pos = nx.circular_layout(G)
    nx.draw(G, with_labels=1,)
    plt.show()


# This function predicts the next word as per user input
def predict_word(G):
    prd = "nil"
    wrd = input("Enter the word: ")
    for each in G.nodes():
        if(G.has_edge(wrd, each) == True and prd == "nil"):
            prd = each
        elif(G.has_edge(wrd, each) and G[wrd][prd]['weight'] < G[wrd][each]['weight']):
            prd = each
        elif(G.has_edge(wrd, each) and G[wrd][prd]['weight'] == G[wrd][each]['weight'] and G.degree[each] > G.degree[prd]):
            prd = each
    l = []
    for x in G.nodes():
        l.append((G.degree(x), x))
    c = max(l)
    if(prd == 'nil'):
        prd = c[1]
    print("Next word could be : ", prd)


nodes = list(set(get_words()))
G = nx.DiGraph()
for each in nodes:
    G.add_node(each)
get_connections(G)
get_graph(G)
predict_word(G)
