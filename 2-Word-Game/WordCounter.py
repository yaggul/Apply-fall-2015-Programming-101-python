

class WordCounter(object):
    def __init__(self):
        self.question=input('Please insert a word to seach in the pool: ')
        self.rown,self.coln=input('Insert number of rows and columns: ').split()
        self.rown=int(self.rown)
        self.coln=int(self.coln)
        self.pool=[]
        self.wmatrix=[]
        self.input=self.rown
        print('Please PASTE the search matrix and press ENTER:')
        print()
        while self.input>0:
            self.wmatrix+=input().split()
            self.input-=1
        self.aggregator=[]
        self.ind=0
        self.count=0
        self.rev_question=''
        for i in self.question:
            self.rev_question=i+self.rev_question
        self.searched=(self.question,self.rev_question)

    def gen_pool(self):
        for i in range(int(self.rown)):
            self.pool+=[self.wmatrix[self.ind:self.ind+int(self.coln)]]
            self.ind+=int(self.coln)

    def aggregate(self):
        pool=self.pool
        row=0
        col=0
        first_r=0
        first_c=0
        word=''
        #LEFT>DOWNRIGHT
        while row<self.rown:
            while col<self.coln and row<self.rown:
                word+=pool[row][col]
                row+=1
                col+=1
            self.aggregator+=[word]
            word=''
            col=0
            first_r+=1
            row=first_r
        #LEFT>UPRIGHT
        first_r=0
        first_c=1
        row=first_r
        col=first_c
        while first_c<self.coln:
            while col<self.coln and row<self.rown:
                word+=pool[row][col]
                row+=1
                col+=1
            self.aggregator+=[word]
            word=''
            row=0
            first_c+=1
            row=first_r
            col=first_c
        #LEFT>RIGHT
        row=0
        col=0
        while row<self.rown:
            while col<self.coln and row<self.rown:
                word+=pool[row][col]
                col+=1
            self.aggregator+=[word]
            word=''
            row+=1
            col=0
        #TOP>BOTTOM
        row=0
        col=0
        while col<self.coln:
            while col<self.coln and row<self.rown:
                word+=pool[row][col]
                row+=1
            self.aggregator+=[word]
            word=''
            row=0
            col+=1
        #RIGHT>DOWNLEFT
        row=0
        col=self.coln-1
        first_r=0
        first_c=4
        while row<self.rown:
            while col>=0 and row<self.rown:
                word+=pool[row][col]
                row+=1
                col-=1
            self.aggregator+=[word]
            word=''
            col=self.coln-1
            first_r+=1
            row=first_r
        #RIGHT>UPLEFT
        row=0
        first_c=self.coln-2
        col=first_c
        while col>=0:
            while col>=0 and row<self.rown:
                word+=pool[row][col]
                row+=1
                col-=1
            self.aggregator+=[word]
            word=''
            row=0
            first_c-=1
            col=first_c

    def finder(self):
        for i in self.searched:
            for j in self.aggregator:
                if i in j:
                    self.count+=1
                else:
                    pass
        if self.question==self.rev_question:
            print()
            print(int(self.count/2))
        else:
            print()
            print(self.count)




a=WordCounter()
a.gen_pool()
a.aggregate()
a.finder()

