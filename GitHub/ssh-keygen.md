# Привязка профиля GitHub к рабочей машине на Windows
1. Установить git  
~~~
https://git-scm.com
~~~

2. Сгенерировать ssh-key в PowerShell от имени администратора
~~~
ssh-key ssh-keygen -t ed25519
~~~
#### Если все хорошо видим такой вывод:  
Generating public/private ed25519 key pair.  
Enter file in which to save the key (C:\Users\ПК48/.ssh/id_ed25519):  
Enter passphrase (empty for no passphrase):  
Enter same passphrase again:  
Your identification has been saved in C:\Users\ПК48/.ssh/id_ed25519  
Your public key has been saved in C:\Users\ПК48/.ssh/id_ed25519.pub  
The key fingerprint is:  
SHA256:/cTduO/nIJo8iSyjwkPbsmlem3Fx14ME/DJkTwVTCso ПК48@DESKTOP-RM9FMUI  
The key's randomart image is:  
+--[ED25519 256]--+  
|       .o o+o    |  
|     . .+o.o     |  
|      Eo +o      |  
|        ooo+ . o |  
|      . So+ = o .|  
|  .    o . o . . |  
| o oo .. . .o o  |  
|  Bo.=o o.oo . o.|  
| o+=+. o  +.   o=|  
+----[SHA256]-----+  

3. Заходим в папку хранения ssh. Примерное расположение PS C:\Users\user\.ssh и выводим содержимое файла с публичным SSH-ключём  
~~~
cat .\id_ed25519.pub
~~~

4. Заходим на GitHub в раздел settings  
![settings](/image/settings.png)

5. Выбираем пункт меню ssh and GPG keys  
![ssh_and_gpg](/image/ssh_and_keys.png)

6. Выбираем пункт меню new ssh key  
![new_ssh](/image/new_ssh.png)

7. Заполняем Title и втсавляем ключ в поле Key  
![add_key](/image/add_key.png)

8. Проверка соединения  
~~~
ssh -T git@github.com
~~~

Успешный результат:  
`Hi! You've successfully authenticated, but GitHub does not provide shell access.`
