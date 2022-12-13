import os
import glob
import shutil
import webbrowser


#Pide al Usuario la Ruta a Ordenar


direccion= input ("Cual es la extencion que deseas Ordenar :    ")


# Valida que exista la extencion

if os.path.exists (direccion):
   
   # Se hace un ciclo para listar todos los archivos
    ordenar = os.scandir(direccion)
    print("Listado de Archivos  : "  )
    for entry in ordenar :
        if entry.is_dir() or entry.is_file():
            #print (entry.name)
            # separar el nombre  y la extencion  del archivo
            path = entry.name
            nombre, extension = os.path.splitext(path)
            print('Nombre del Archivo:', nombre)
            print('Extension:', extension)
       
       
        # Dentro del mismo Ciclo se pregunta si no existe la carpeta si da True Genera carpetas    
            
            if extension == ".txt" or extension ==".docx" or extension ==".pdf" or extension == ".odt" or extension == ".doc" :
                if not os.path.exists(direccion + "/Documentos")== True: 
                    os.mkdir(direccion +  "/Documentos")

            elif extension == ".png" or extension == ".jpg" or extension ==".jpeg" or extension == ".gif"  :
                if not os.path.exists(direccion + "/" + "Imagenes")== True: 
                    os.mkdir(direccion + "/Imagenes"  )

            elif extension == ".mp4" or extension ==".mkv" or extension ==".avi" or extension ==".mov" or extension == ".dvx" :
                if not os.path.exists(direccion + "/Videos")== True: 
                    os.mkdir(direccion + "/Videos")

            elif extension == ".wav" or extension == ".mp3" or extension ==".aac" or extension == ".aiff" or extension == "wma" :
                if not os.path.exists(direccion + "/Audios")== True: 
                    os.mkdir(direccion + "/Audios")

            else:
                if not os.path.exists(direccion + "/Otros")== True: 
                    os.mkdir(direccion + "/Otros")          

    
# para mover archivos, Creo una  Variable que gusrada todas las extensiones posibles



extensiones=["pdf","doc","docx","odt", "txt","png","jpg","jpeg","gif","wav","mp3","aac","aiff","wma", "plv","mp4","mkv","avi","mov","divx","py","rar","zip","exe","code-workspace "] # Lista de extensiones para documentos


# Se crea un ciblo para que revise cada extension

for ext in extensiones: # Por cada extension
    #ext = ext_original.lower
    files = glob.iglob(os.path.join(direccion, '*.' + ext)) # Lista de archivos
    for file in files: # Por cada archivo
        if os.path.isfile(file): 
            if ext == ext == "txt" or ext =="docx" or ext =="pdf" or ext == "odt" or ext == "doc" : 
                shutil.copy2(file, os.path.join(direccion +'/Documentos'))
            elif ext == "png" or ext == "jpg" or ext =="jpeg" or ext == "gif"  :
                shutil.copy2(file, os.path.join(direccion + '/Imagenes'))
            elif ext == "mp4" or ext =="mkv" or ext =="avi" or ext =="mov" or ext == "dvx" :
                shutil.copy2(file, os.path.join(direccion +'/Videos'))
            elif ext == "wav" or ext == "mp3" or ext =="aac" or ext == "aiff" or ext == "wma" :
                shutil.copy2(file, os.path.join(direccion +'/Audios'))
            elif ext == "py" or ext == "rar" or ext =="zip" or ext == "exe" :
                shutil.copy2(file, os.path.join(direccion +'/Otros'))
            os.remove(file)

 
# Abre una carpeta del escritorio en el explorador.

webbrowser.open(os.path.realpath(direccion))
          





