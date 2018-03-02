from sklearn import tree

tree_clf = tree.DecisionTreeClassifier()

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
classification = classification.fit(x, y)

prediction = classification.predict([[190, 70, 43]])

print(prediction)