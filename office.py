
class psalm(object):
    def __init__(self,title=None,antiphon=None,pretext=None,text=None,psalmprayer=None):
        self.title = title
        self.antiphon = antiphon
        self.pretext = pretext
        self.text = text
        self.psalmprayer = psalmprayer
class hymn(object):
    def __init__(self,title=None,text=None,mdata=None):
        self.title = title
        self.text = text
        self.mdata = mdata
class _resp(object):
    def __init__(self):
        self.words = ""
class full_resp(_resp):
    def __init__(self,text1,text2,text3):
        _resp.__init__(self)
        self.words = text1+' '+text2+'\\\\\n'
        self.words = text3+' '+text2+'\\\\\n'
        self.words = 'Glory be to the Father and to the Son and to the Holy Spitit; '+text1+' '+text2+'\\\\\n'
class intercession(object):
    def __init__(self,introtext=None,resp=None,textlist=None):
        self.introtext = introtext
        self.resp = resp
        self.textlist = textlist
class office(object):
    def __init__(self,title):
        self.title = title
        

