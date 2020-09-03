# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 17:37:48 2015

@author: DGA
"""
import numpy as np
# calcul le lift tx de rep dans la classe / tx de reponse global sur le prmier quantile de score (proba décroissante)
# si on met 10, cela renvoie le premier decile
# si on met 20 cela renvoie le premier vingtile
def lift(proba,X,reponse,p=10):
    #p = 10
    sorted_proba = np.array(list(reversed(np.argsort(proba))))
    positives = sum(reponse)
    tp = sum(np.array(reponse)[sorted_proba[:int(round((p*X_train.shape[0])/100,0))]])
    lift = round(100*tp/(float(positives)*p),2)
    print("lift at " '{} percent : {}'.format(p,lift))
    return lift
  
    

    
#    sorted_proba = np.array(list(reversed(np.argsort(probas_train))))
#    positives = sum(y_train)
#    tp = sum(np.array(y_train)[sorted_proba[:int(round((10*X_train.shape[0])/100,0))]])
#    lift = 100*tp/(float(positives)*10)
#    print("lift at %e"  %(10) ) 
#    print("lift at " '{} percent : {}'.format(5,3.5))
#
#    return lift

  
def poids_manquant(DF):
    poids_manquant = 100*(DF.shape[0] - DF.count())/DF.shape[0]
    print("Taux de NA par var dans la DataFrame")
    print(poids_manquant)
    return poids_manquant

#http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html#example-model-selection-plot-confusion-matrix-py
import matplotlib.pyplot as plt

def plot_confusion_matrix(cm,target_names, title='Confusion matrix', cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(target_names))
    plt.xticks(tick_marks, target_names, rotation=45)
    plt.yticks(tick_marks, target_names)
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
 
from sklearn.metrics import confusion_matrix

def spec_sens(actuals, proba, labels):
    cutoff = list()
    sensitivity = list()
    specificity = list()
    for i in range(0,101):
        prob = proba > i/100
        prob = prob.astype(int)
        cm = confusion_matrix(actuals, prob, labels = labels)
        cutoff.append(float(i/100))
        sensitivity.append(float(cm[1][1]) / float(cm[1][0]+cm[1][1]))
        specificity.append(float(cm[0][0]) / float(cm[0][0]+cm[0][1]))
    return pnd.DataFrame({'sensibilite':sensitivity,'specificite':specificity},index = cutoff)

def AUC_modele(proba,reponse):
    import matplotlib.pyplot as plt
    from sklearn.metrics import confusion_matrix,roc_curve ,auc ,classification_report
    fpr, tpr, thresholds = roc_curve(reponse,proba)
    AUC_modele = auc(fpr,tpr)

    plt.plot(fpr, tpr)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Courbe ROC (Aire = %0.2f)' % AUC_modele)
    plt.legend(loc="lower right")
    plt.show()    
    
    print("AUC: %f" %(AUC_modele))
    return fpr,tpr,AUC_modele

def F1_score(proba,actual,cutoff):
    from sklearn.metrics import f1_score
    predict = proba > cutoff
    predict = predict.astype(int)
    F1_score = f1_score(actual,predict)
    print("F1 score: %f" %(F1_score))
    return F1_score
    
    from sklearn.metrics import  roc_curve , auc
import pylab as pl
def auc_et_roc(Y,proba):
    fpr, tpr, thresholds = roc_curve(Y,proba)
    roc_auc = auc(fpr, tpr)
    print("auc=",roc_auc)
    pl.clf()
    pl.plot(fpr, tpr, label='Courbe ROC (Aire = %0.2f)' % roc_auc)
    pl.plot([0, 1], [0, 1], 'k--')
    pl.xlim([0.0, 1.0])
    pl.ylim([0.0, 1.0])
    pl.xlabel('False Positive Rate')
    pl.ylabel('True Positive Rate')
    pl.title('Receiver operating characteristic example')
    pl.legend(loc="lower right")
    pl.show()