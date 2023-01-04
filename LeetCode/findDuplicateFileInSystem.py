# https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_dir = defaultdict(list)

        for path in paths:
            _dir = path.split()
            root = _dir[0] + '/'
            
            for i in range(1, len(_dir)):
                file_content = _dir[i].split("(")
                content = file_content[1][:-1]
                file_dir = root + file_content[0]
                content_dir[content].append(file_dir)

        res = []
        
        for _dir in content_dir.values():
            if len(_dir) > 1:
                res.append(_dir)

        return res
    
# First we split the each path by spaces and place the returned list on _dir. 
# Then we can find the root directory at _dir[0] and we will append forward slash to it.
# Then we iterate in the remaining slices in _dir and split them by ( again. This separates
# the file names and the contents. We take the content discrading the last char i.e ). And 
# concatenate the root and the file name. Then insert the content as a key and the file_dir
# as value in dictionary. Then we will filter out the _dirs which contain the same content by 
# checking the value length.
