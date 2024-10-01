import numpy as np
import heapq

from sklearn.linear_model import SGDClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

def prequential_learning(x_test, y_test, classifier, feedback='immediate', trainOnError = True, randomSeed = None, maximumDelay = 20):
    """
    Given an input dataset, performs online training using the prequential approach (also known as interleaved test-then-train)
    
    x_test: an array representing the test data
    
    y_test: a vector containing the labels for the test data
    
    classifier: a scikit-learn object that contains a classifier trained with the initial training set
    
    feedback: type of feedback
    
    trainOnError: if True, training is only performed when there is a prediction error
    
    maximumDelay: defines the maximum time (in number of samples) to wait for the feedback of the sample to be given
    
    """
    
    c_testSamples = 0
    
    incrementalLearningSamples = []
    
    # heap for the delayed feedback
    heapq.heapify(incrementalLearningSamples)
      
    # list to store the predictions         
    y_pred = []
    for i in range(len(y_test)):

        if randomSeed is not None:
            
            ## updates the user-provided seed with the sample index
            randomSeed = randomSeed+1
                
        # make the prediction
        y_pred.append(classifier.predict(x_test[[i],:])[0])
        
        # training is only performed if the methodology is trainOnError and
        # the classification is incorrect, or if the methodology is not trainOnError
        if (trainOnError and (y_pred[i]!=y_test[i])) or (not trainOnError): 
            
            if feedback=='immediate':
                
                # updates the classifier
                classifier.partial_fit(x_test[[i],:], [y_test[i]])
                
            elif feedback=='uncertain': # also known as partial feedback              
                
                # if the random value equals 1, it means the classifier will receive feedback
                if np.random.RandomState(seed = randomSeed).randint(2)==1:
                    classifier.partial_fit(x_test[[i],:], [y_test[i]])
                
                
            elif feedback=='delayed':
                
                # insert delayed feedback code
                wait = np.random.RandomState(seed = randomSeed).randint(maximumDelay, size=1)

                heapq.heappush(incrementalLearningSamples,[(c_testSamples+wait), i])
                
                while (len(incrementalLearningSamples) > 0 and
                       incrementalLearningSamples[0][0] <= c_testSamples):
                                                           
                    # gets the sample with the highest priority
                    waitTime, j = heapq.heappop(incrementalLearningSamples)
  
                    # Train
                    classifier.partial_fit(x_test[[j],:], [y_test[j]])
                    

        c_testSamples = c_testSamples + 1            
        
    return y_pred, classifier


if __name__ == "__main__":
    
    """
    Test the function with a simple synthetic dataset. 
    """    
    
    # Creating a simple synthetic dataset
    X, y = make_classification(n_samples=1000,    
                               n_features=10,     
                               n_informative=5,   
                               n_redundant=2,    
                               n_classes=2,      
                               random_state=42)
    
    # Splitting the dataset into training and testing sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    classifier = SGDClassifier()
    
    # Train the classifier with the training data
    classifier.fit(X_train, Y_train) 
    
    # Use the prequenctial approach with immediate feedback
    y_pred, classifier = prequential_learning(X_test, Y_test, classifier, feedback='immediate', trainOnError = True, randomSeed=5)
    
    report = classification_report(Y_test, y_pred)
    print("Classification Report -- immediate fedback:\n", report)
    
    # Use the prequenctial approach with delayed feedback
    y_pred, classifier = prequential_learning(X_test, Y_test, classifier, feedback='delayed', trainOnError = True, maximumDelay = 20, randomSeed=5)
    
    report = classification_report(Y_test, y_pred)
    print("Classification Report -- delayed fedback:\n", report)
    
    # Use the prequenctial approach with delayed feedback
    y_pred, classifier = prequential_learning(X_test, Y_test, classifier, feedback='uncertain', trainOnError = True, randomSeed=5)
    
    report = classification_report(Y_test, y_pred)
    print("Classification Report -- delayed fedback:\n", report)







     
