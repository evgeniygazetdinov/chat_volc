from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        counter = len(strs) - 1
        coincidence = []

        # def compare_to(first, second):
        #     first_len = len(first)
        #     second_lem = len(second)
        #     con = [x for x in second if x in first]
        #     return con
        
        # for w in range(1,1,len(strs)-1):
        #     compare_to(strs[w], strs[w+1])

        for word in range(len(strs)):
            print(strs[word])
            coincidence.append([])
            # перебираем слова
            for one_word in strs[word]:
                #перебираем каждую букву
                # как пофиксить сравненение не с самим собой
                print(strs[-counter])
                if one_word in strs[-counter]:
                    print(f'has same {one_word}')
                    coincidence[-1].append(one_word)
            counter-=1
        print(coincidence)
        # for s in strs:
        #     s 

                                    
if __name__ =='__main__':
    inc = Solution()
    print(inc.longestCommonPrefix(["flower","flow","flight"]))
    # print(inc.longestCommonPrefix(["dog","racecar","car"]))
