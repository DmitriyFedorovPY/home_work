class WordsFinder():
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = dict()
        chage_singns = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                words = []
                for line in file:
                    for sign in chage_singns:
                        line = line.replace(sign, ' ')
                    line = line.lower()
                    for word in line.split():
                        words.append(word)
                file.close()
            all_words[file_name] = words
        return all_words

    def find(self,word):
        dict_of_words=dict()
        for name,words in self.get_all_words().items():
            if word.lower() in words:
                dict_of_words[name] = words.index(word.lower()) + 1
        return dict_of_words


    def count(self, word):
        dict_of_counts = dict()
        for name,words in self.get_all_words().items():
            if word.lower() in words:
                dict_of_counts[name] = words.index(word.lower()) + 1
        return dict_of_counts


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего