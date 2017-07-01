# ランダムフォレストを用いてウィスコンシン州の乳癌診断テータを分類するプログラム

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation, metrics
import itertools
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix



# データの読み込み
mr = pd.read_csv("breastcancer2.csv")#, header=None)
#print(mr)
#exit

#用いる特徴量を設定する
#*****全ての特徴量を用いた時*****
data = mr[["ID number","radius(The mean)","texture(The mean)","perimeter(The mean)","area(The mean)","smoothness(The mean)","compactness(The mean)","concavity(The mean)","concave points(The mean)","symmetry(The mean)","fractal dimension(The mean)","radius(standard error)","texture(standard error)","perimeter(standard error)","area(standard error)","smoothness(standard error)","compactness(standard error)","concavity(standard error)","concave points(standard error)","symmetry(standard error)","fractal dimension(standard error)","radius(worst or largest)","texture(worst or largest)","perimeter(worst or largest)","area(worst or largest)","smoothness(worst or largest)","compactness(worst or largest)","concavity(worst or largest)","concave points(worst or largest)","symmetry(worst or largest)","fractal dimension(worst or largest)"]]


#labelの設定
label = mr["Diagnosis"]

#それぞれlabelの名前を設定
class_names = ["M","B"]

# 学習用とテスト用データに分ける
data_train, data_test, label_train, label_test = \
    cross_validation.train_test_split(data, label)

# クロスバリデーションを行う（ランダムフォレスト）
clf =  RandomForestClassifier()
scores = cross_validation.cross_val_score(
    clf, data, label, cv=10)

X_train, X_test, y_train, y_test = cross_validation.train_test_split(data,label)

classifier = RandomForestClassifier()
y_pred = classifier.fit(X_train, y_train).predict(X_test)


#コンフュージョンマトリックスを描画する
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):


      #コンフュージョンマトリックスを生成し、プロットする
    # Normalization can be applied by setting `normalize=True`.
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    
 # コンフュージョンマトリックスを計算する
cnf_matrix = confusion_matrix(y_test, y_pred)
np.set_printoptions(precision=2)

# Plot non-normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names,
                      title='Confusion matrix, without normalization')

# Plot normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names, normalize=True,
                      title='Normalized confusion matrix')

plt.show()


#出力させるレポートの設定
cl_report = metrics.classification_report(label_test,y_pred)

print("各正解率=" ,scores)
print("正解率=", scores.mean())
print("レポート=\n",cl_report)


