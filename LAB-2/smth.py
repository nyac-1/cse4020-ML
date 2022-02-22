class DecisionTreeClassifier:
    def __init__(self, X, feature_names, labels):
        self.X = X  # features or predictors
        self.feature_names = feature_names  # name of the features
        self.labels = labels  # categories
        self.labelCategories = list(set(labels))  # unique categories
        # number of instances of each category
        self.labelCategoriesCount = [list(labels).count(x) for x in self.labelCategories]
        self.node = None  # nodes
        # calculate the initial entropy of the system
        self.entropy = self._get_entropy([x for x in range(len(self.labels))])

    def _get_entropy(self, x_ids):
    # sorted labels by instance id
    labels = [self.labels[i] for i in x_ids]
    # count number of instances of each category
    label_count = [labels.count(x) for x in self.labelCategories]
    # calculate the entropy for each category and sum them
    entropy = sum([-count / len(x_ids) * math.log(count / len(x_ids), 2) if count else 0 for count in label_count ])
    return entropy