import os
x = 0
while 1:
        os.system("scanimage -p --format jpg > Hoja%d.jpg" % x)
	os.system("convert Hoja%d.jpg -quality 80 Hoja%d.jpg" % (x,x))
        os.system("git add Hoja%d.jpg" % x)
        os.system('git commit -m "Hoja %d escaneada."' % x)
        os.system("git push")
	raw_input("Hoja %d completada. Presione enter para continuar." % x)
	x+=1
