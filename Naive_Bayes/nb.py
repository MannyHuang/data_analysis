import os
import jieba
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

warnings.filterwarnings('ignore')

def cut_words(file_path):
  """
  cut words in the article
  :param: file_path: the location of the txt file
  :return: the string cut by space
  """
  text_with_spaces = ''
  text = open(file_path, 'r', encoding='gb18030').read()
  textcut = jieba.cut(text)
  for word in textcut:
    text_with_spaces += word + ' '
    return text_with_spaces

def load_file(file_dir, label):
  """
  load all the files in the directory
  :param1 file_dir: the path to save txt
  :param2 label: label of txt
  :return text list after wordcut, labels
  """
  file_list = os.listdir(file_dir)
  words_list = []
  labels_list = []
  for file in file_list:
    file_path = file_dir + '/' + file
    words_list.append(cut_words(file_path))
    labels_list.append(label)
    return words_list, labels_list

train_words_list1, train_labels1 = load_file('text_classification/train/女性', '女性')
train_words_list2, train_labels2 = load_file('text_classification/train/体育', '体育')
train_words_list3, train_labels3 = load_file('text_classification/train/文学', '文学')
train_words_list4, train_labels4 = load_file('text_classification/train/校园', '校园')

train_words_list = train_words_list1 + train_words_list2 + train_words_list3 +train_words_list4
train_labels = train_labels1 + train_labels2 + train_labels3 + train_labels4

test_words_list1, test_labels1 = load_file('text_classification/test/女性', '女性')
test_words_list2, test_labels2 = load_file('text_classification/test/体育', '体育')
test_words_list3, test_labels3 = load_file('text_classification/test/文学', '文学')
test_words_list4, test_labels4 = load_file('text_classification/test/校园', '校园')

test_words_list = test_words_list1 + test_words_list2 + test_words_list3 + test_words_list4
test_labels = test_labels1 + test_labels2 + test_labels3 + test_labels4

stop_words = open('text_classification/stop/stopword.txt', 'r', encoding='utf-8').read()
stop_words = stop_words.encode('utf-8').decode('utf-8-sig')
stop_words = stop_words.split('\n')

tf = TfidfVectorizer(stop_words=stop_words, max_df=0.5)

train_features = tf.fit_transform(train_words_list)
test_features = tf.transform(test_words_list)

clf = MultinomialNB(alpha=0.001).fit(train_features, train_labels)
predicted_labels = clf.predict(test_features)

print('Accuracy is ', metrics.accuracy_score(test_labels, predicted_labels))