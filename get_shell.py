from subprocess import call
call(str('docker ps '),shell=True)
id_str = input('what is the container ID you would like to access?: ' )
call( str('docker exec -it '+ str(id_str) +' /bin/bash'),shell=True)
