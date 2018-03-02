from sklearn import tree
from sklearn.naive_bayes import GaussianNB

tree_clf = tree.DecisionTreeClassifier()
gaussian_clf = GaussianNB()

# [height, weight, shoe size]
x = [
    [181, 80, 44],
    [177, 70, 43],
    [160, 60, 38],
    [154, 54, 37],
    [166, 65, 40],
    [190, 90, 47],
    [175, 64, 39],
    [177, 70, 40],
    [159, 55, 37],
    [171, 75, 42],
    [181, 85, 43]
    ]

y = ['male',
    'male',
    'female',
    'female',
    'male',
    'male',
    'female',
    'female',
    'female',
    'male',
    'male'
    ]

# Fit the data to the classifier
tree_clf = tree_clf.fit(x, y)
tree_pred = tree_clf.predict([[190, 70, 43]])
print('Desicion Tree prediction: {}'.format(tree_pred))

gaussian_clf = gaussian_clf.fit(x, y)
gaussian_pred = gaussian_clf.predict([[190, 70, 43]])
print('Gaussian Naive Bays prediction: {}'.format(gaussian_pred))
