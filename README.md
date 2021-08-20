# Tye-Track

Type Track is a program which can be used to predict the successor word using the typing pattern. A text document written by a user which forms the basis for the dataset. A Word co-occurrence network is built using the dataset , with words as nodes and co-occurrence as edges. The initiation to build this network is to build a list of words appearing in the dataset ,which is achieved by reading a word file and then this set of words were made as nodes, then a direct graph was formed by putting an edge between the words which occur together. This network was then used to predict the next word to be followed as per the user input. Weight and degree of connectivity is used for word predictors.

### How to run
- Clone the repostory
- Change {User_document_here} in Line 8 and Line 17 with path of txt document written by the user.
- Run the code.
