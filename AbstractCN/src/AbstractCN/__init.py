from xpinyin import Pinyin
from letterDict import oPinyin,Letter
p = Pinyin()
class AbstractCN():
    def pinyin(self,text):
        # default splitter is ` `
        return p.get_pinyin(text).split()  
    def get_abstractpinyin(self,text):
        for i in Pinyin(text):
            yield oPinyin[i]
