class WordsFinder:
    def __init__(self,*file_names):
        self.file_names=file_names

    def get_all_words(self):
        all_words={}
        for fname in self.file_names:
            with open(fname,encoding='utf-8') as file:
                words=[]
                for line in file:
                    new_line=''.join([x if x not in [',', '.', '=', '!', '?', ';', ':', ' - ','\n'] else '' for x in line.lower()])
                    words+=new_line.split(' ')
                all_words.update({fname:words})
        return all_words

    def find(self,word):
        found={}
        for name,words in self.get_all_words().items():
            if word.lower() in words:
                found.update({name:int(words.index(word.lower())+1)})
        return found

    def count(self,word):
        count=0
        found_count={}
        for name in self.get_all_words().keys():
            for i in range(len(self.get_all_words()[name])):
                if word.lower()==self.get_all_words()[name][i]:
                    count+=1
            found_count.update({name:count})
        return found_count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего