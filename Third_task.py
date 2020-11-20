#1)	Написати програму на пітоні яка на вхід буде приймати шлях до директорії, а в консоль видавати всю структуру директорії.
import os

def list_files(startpath):
   for root, dirs, files in os.walk(startpath):
       if dir!= '.git':
           level = root.replace(startpath, '').count(os.sep)
           indent = ' ' * 4 * (level)
           print('{}{}/'.format(indent, os.path.basename(root)))
           subindent = ' ' * 4 * (level + 1)
           for f in files:
               print('{}{}'.format(subindent, f))

os.chdir('D:/ProjectsUNI')
enter_path = os.getcwd()
list_files(enter_path)