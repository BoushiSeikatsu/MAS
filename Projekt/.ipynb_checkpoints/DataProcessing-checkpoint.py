#!/usr/bin/env python
# coding: utf-8

# In[50]:


import pandas as pd
import seaborn as sns
import numpy as np

# In[2]:


def getAdjacencyMatrix(df):
    adjacencyMatrix = []
    for i in range(0,34):
        adjacencyMatrix.append([])
        for j in range(0,34):
            adjacencyMatrix[i].append(0)
    for i in range(0,len(adjacencyMatrix)):
        for j in range(0, len(adjacencyMatrix[i])):
            for n in df.iterrows():
                if n[1][0] == i + 1 or n[1][1] == i + 1:
                    if n[1][0] == j + 1 or n[1][1] == j + 1:
                        adjacencyMatrix[i][j] = 1
    return adjacencyMatrix


# In[4]:


def printAdjacencyMatrix(adjacencyMatrix):
    for i in range(0,len(adjacencyMatrix)):
        print(adjacencyMatrix[i])


# In[5]:


def getAdjacencyList(dfEdges):
    adjacencyList = {}
    for n in dfEdges.iterrows():
        leftItem = n[1][0]
        rightItem = n[1][1]
        if leftItem not in adjacencyList.keys():
            adjacencyList[leftItem] = []
        if rightItem not in adjacencyList.keys():
            adjacencyList[rightItem] = []
        if rightItem not in adjacencyList[leftItem]:
            adjacencyList[leftItem].append(rightItem)
        if leftItem not in adjacencyList[rightItem]:
            adjacencyList[rightItem].append(leftItem)
    return adjacencyList


# In[115]:


def getMin(adjacencyList):
    result = 999
    for key in adjacencyList.keys():
        if(len(adjacencyList[key]) < result):
            result = len(adjacencyList[key])
    return result

def getMax(adjacencyList):
    result = -1
    for key in adjacencyList.keys():
        if(len(adjacencyList[key]) > result):
            result = len(adjacencyList[key])
    return result

def getAvg(adjacencyList):
    result = 0
    totalSum = 0
    for key in adjacencyList.keys():
        totalSum += len(adjacencyList[key])
    return totalSum/len(adjacencyList.keys())

def getFrequency(adjacencyList):
    vFrequency = {}
    min = getMin(adjacencyList)
    max = getMax(adjacencyList)
    for i in range(min, max + 1):
        vFrequency[i] = 0
    for key in adjacencyList.keys():
        if len(adjacencyList[key]) not in vFrequency.keys():
            vFrequency[len(adjacencyList[key])] = 0
        vFrequency[len(adjacencyList[key])] += 1
    return vFrequency


def getRelativeFrequency(adjacencyList):
    vFrequency = {}
    for key in adjacencyList.keys():
        if len(adjacencyList[key]) not in vFrequency.keys():
            vFrequency[len(adjacencyList[key])] = 0
        vFrequency[len(adjacencyList[key])] += 1
    for key in vFrequency.keys():
        vFrequency[key] = float(vFrequency[key]/34)
    return vFrequency


# In[116]:


def printCharacteristics(adjacencyList):
    print("Min: " + str(getMin(adjacencyList)))
    print("Max: " + str(getMax(adjacencyList)))
    print("Avg: " + str(getAvg(adjacencyList)))
    print("Četnost: " + str(getFrequency(adjacencyList)))
    print("Relativní četnost: " + str(getRelativeFrequency(adjacencyList)))


# In[117]:


def printFrequencyChart(adjacencyList):
    frequency = getFrequency(adjacencyList)
    keys = list(frequency.keys())
    vals = list(frequency.values())
    sns.barplot(x=keys, y=vals)


# In[ ]:
#Returns Density in percentile 
def getDensity(nodeConnections, countAllNodes):
    return round(len(nodeConnections)/(countAllNodes - 1) * 100, 2)

def getDensityForAll(adjacencyList):
    result = np.empty([len(adjacencyList),1])
    i = 0
    for value in adjacencyList.values():
        density = getDensity(value, len(adjacencyList))
        result[i] = density
        i += 1
    return pd.DataFrame(data=result, columns=["Hustota (%)"])
