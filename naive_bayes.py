import numpy as np
import functools
import pprint
import pandas as pd 


class naive_bayes_classifier():
    cp = {}
    probability_identifier = {}
    
    def __init__(self,filename,predictor):
        self.data = pd.read_csv(filename, sep=',', header =(0))
        self.predictor = predictor
                         

    def probability(self, data, data_type,label_set):
        class_val = self.data
        attribute = self.data[data]
        class_attr = list(attribute)
        val = self.predictor 
        label_data = list(class_val[val])
        counter = 1
        for i in range(0, len(class_attr)):
            if label_data[i] == label_set and class_attr[i] == data_type:
                counter += 1
        label_value = float(label_data.count(label_set))
        return counter/label_value
              
        
    def prioriprobability(self): 
        bayes = self.probability_identifier               
        val = self.predictor
        class_val = self.data
        value_set = set()
        value_set = class_val[val]
        class_label = []
        class_label = value_set
        label_data = list(class_val[val])
        label = float(len(label_data))
        for i in class_label:
            bayes[i] = label_data.count(i)/label
        

    def conditionalprobability(self, naive_values):
        bayes = self.probability_identifier  
        print ("\nProbability:")
        for i in self.probability_identifier:
            self.cp[i] = {}
            for j in naive_values:
                iter_item = self.probability
                iteration = iter_item(j, naive_values[j],i)
                self.cp[i].update({ naive_values[j]:iteration}) 
        pprint.pprint(self.cp)
        for i in self.cp:
            print ("\n", i, " = ", functools.reduce(lambda x, y: x*y,  self.cp[i].values())*bayes[i])


if __name__ == "__main__":
    c = naive_bayes_classifier(filename = '/Users/artipengoriya/Documents/Material/Fall_2016/DM/Project3/project3_dataset4.csv', predictor="prediction")
    c.prioriprobability()    
    c.naive_values = {"weather":"sunny", "temperature":"hot", "density":"high" , "wind":"weak"}
    c.naive_values1 = {"weather":"sunny", "temperature":"hot", "density":"high" , "wind":"strong"}
    c.naive_values2 = {"weather":"overcast", "temperature":"hot", "density":"high" , "wind":"weak"}
    c.naive_values3 = {"weather":"rain", "temperature":"mild", "density":"high" , "wind":"weak"}
    c.naive_values4 = {"weather":"rain", "temperature":"cool", "density":"normal" , "wind":"weak"}
    c.naive_values5 = {"weather":"rain", "temperature":"cool", "density":"normal" , "wind":"strong"}
    c.naive_values6 = {"weather":"overcast", "temperature":"cool", "density":"normal" , "wind":"strong"}
    c.naive_values7 = {"weather":"sunny", "temperature":"mild", "density":"high" , "wind":"weak"}
    c.naive_values8 = {"weather":"sunny", "temperature":"cool", "density":"normal" , "wind":"weak"}
    c.naive_values9 = {"weather":"rain", "temperature":"mild", "density":"normal" , "wind":"weak"}
    c.naive_values10 = {"weather":"sunny", "temperature":"mild", "density":"normal" , "wind":"strong"}
    c.naive_values11 = {"weather":"overcast", "temperature":"mild", "density":"high" , "wind":"strong"}
    c.naive_values12 = {"weather":"overcast", "temperature":"hot", "density":"normal" , "wind":"weak"}
    c.naive_values13 = {"weather":"rain", "temperature":"mild", "density":"high" , "wind":"strong"}
    
    c.conditionalprobability(c.naive_values)
    c.conditionalprobability(c.naive_values1)
    c.conditionalprobability(c.naive_values2)
    c.conditionalprobability(c.naive_values3)
    c.conditionalprobability(c.naive_values4)
    c.conditionalprobability(c.naive_values5)
    c.conditionalprobability(c.naive_values6)
    c.conditionalprobability(c.naive_values7)
    c.conditionalprobability(c.naive_values8)
    c.conditionalprobability(c.naive_values9)
    c.conditionalprobability(c.naive_values10)
    c.conditionalprobability(c.naive_values11)
    c.conditionalprobability(c.naive_values12)
    c.conditionalprobability(c.naive_values13)




