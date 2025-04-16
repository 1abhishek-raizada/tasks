string="abhishekraizada"
def answer(s):
    def occurance(s):
        freq={}
        for x in s:
            if x in freq:
                freq[x]+=1
            else:
                freq[x]=1    
        return freq

    jh=occurance(s)
    answer=list(jh.items())
    sorted_answer=sorted(answer,key=lambda x:x[1],reverse=True)
    top3_answer=sorted_answer[:3]
    for x,y in top3_answer:
        print(f"{x} {y}")

    

answer(string)    