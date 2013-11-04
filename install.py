import os
import shutil

userPath = os.path.expanduser("~/Library/Developer/Xcode/Templates/File Templates/cocos2dx")
shutil.rmtree(userPath,True)
shutil.copytree("./cocos2dx",userPath)
