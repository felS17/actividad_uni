#En caso de fallar, se debe cambiar las rutas siguientes a lo que sea que está fallando o ns

ruta_py = "Git\\actividad_uni\\PyToCpp\\sample\\python.py"
ruta_cpp = "Git\\actividad_uni\\PyToCpp\\sample\\cpp.cpp"

#--------------------------------------------------------------

with open(ruta_py, "r") as archivo_py:
    codigo_py = archivo_py.readlines()

codigo_cpp = "#include <iostream>\nusing namespace std;\nint main() {\n\n"

for linea in codigo_py:
    
    if("print" in linea):
        i = linea.find("print")
        linea = linea[:i+5] + "f" + linea[i+5:].rstrip() + ";\n"
        codigo_cpp += linea


#--Write final al archivo .cpp--
with open(ruta_cpp, "w") as archivo_cpp:
    archivo_cpp.write(codigo_cpp)
    archivo_cpp.write("\n\n}")

print("Código ejecutado con éxito")