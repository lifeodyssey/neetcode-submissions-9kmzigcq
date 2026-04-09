class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res=[]
        i=0
        n=len(words)
        while i<n:
            line_words=[]
            line_len=0
            while i<n:
                word=words[i]
                if line_len+len(word)+len(line_words)<=maxWidth:
                    line_words.append(word)
                    line_len+=len(word)
                    i+=1
                else:
                    break
            is_last_line=(i==n)
            if is_last_line or len(line_words)==1:
                line=" ".join(line_words)
                line+=" "*(maxWidth-len(line))
                res.append(line)
            else:
                total_spaces=maxWidth-line_len
                gaps=len(line_words)-1
                base_spaces=total_spaces//gaps
                extra_spaces=total_spaces%gaps
                line=""
                for j in range(gaps):
                    line+=line_words[j]
                    spaces=base_spaces
                    if j<extra_spaces:
                        spaces+=1
                    line+=" "*spaces

                line+=line_words[-1]
                res.append(line)
        return res