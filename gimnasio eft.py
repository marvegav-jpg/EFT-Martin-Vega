planes={
'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 'tarde'],
'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche'],
}

inscripciones = {
'F001': [14990, 30],
'F002': [22990, 10],
'F003': [39990, 0],
'F004': [35990, 6],
'F005': [159990, 2],
'F006': [18990, 15],
}

def busqueda_precio(p_min, p_max, diccionario,diccionario2):
  lista=[]
  if p_min>0 and p_min<p_max:
    for clave, datos in diccionario.items():
      if p_min<=datos[0]<=p_max and datos[1]>0:
       lista=[diccionario2[clave][0],[clave]]
       print(lista)
    else:
      print("No hay planes en ese rango de precios.")
  else:
    print("No hay planes en ese rango de precios.")

def buscar_codigo(codigo, diccionario):
  for clave in diccionario:
    if clave==codigo.upper():
      return True
    else: 
      return False

def actualizar_precio(codigo,nuevo_precio,diccionario):
  cod=codigo.upper()
  if buscar_codigo(cod,diccionario):
    for clave, datos in diccionario.items():
      if clave == codigo.upper():
        datos[0]=nuevo_precio
        return True
  else:
    return False      


def leer():
  try:
     opcion=int(input("Ingrese una opcion: "))
     if 0<opcion<=6:
       return opcion
     else:
       print("Debe seleccionar una opción válida")
  except ValueError:
    print("Debe seleccionar una opción válida")

def cupos_tipo(plan,dicionario,diccionario2):
  total=0
  for clave, datos in dicionario.items():
    if datos[1].upper()==plan.upper():
      for clave2 in diccionario2:
        if clave2==clave:
          total+=diccionario2[clave2][1]
  if total>0:
        print(f"Planes disponibles: {total}") 
  else:
    print("No hay planes disponibles")

def codigo(codigo,diccionario):
  if len(codigo.strip())>0 and codigo not in diccionario:
    return True
  else:
    return False
  
def nombre(nombre):
  if len(nombre.strip())>0:
    return True
  else:
    return False
  
def tipo(tipo):
  if tipo=="mensual" or tipo=="trimestral" or tipo=="anual":
    return True
  else:
    return False
  
def duracion(duracion):
  if int(duracion)>0 :
    return True
  else:
    return False
  
def acceso(acceso):
  if acceso=="s":
    return True
  else:
    return False
  
def clases(clases):
  if clases=="s":
    return True
  else:
    return False
  
def horario(HORARIO):
   if len(HORARIO.strip())>0:
     return True
   else:
     return False
   
def precio(precio):
  if precio>0 and int(precio):
    return True
  else:
    return False
  
def cupos(cupos):
  if cupos>=0:
    return True
  else:
    return False
  
def agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina, incluye_clases, horario, precio, cupos,diccionario,diccionario2):
  diccionario[codigo][nombre, tipo, duracion, acceso_piscina, incluye_clases, horario,]
  diccionario2[codigo][precio,cupos]




  
      
def main():
 print("""
========== MENÚ PRINCIPAL ==========
1. Cupos por tipo de plan
2. Búsqueda de planes por rango de precio
3. Actualizar precio de plan
4. Agregar plan
5. Eliminar plan
6. Salir
=====================================
""")
 opcion=leer()
 match opcion:
   case 1:
     plan=input("Ingrese el plan: ").upper()
     cupos_tipo(plan,planes,inscripciones)
   case 2:
     while True:
      try:
         min=int(input("Ingrese precio minimo: "))
         max=int(input("Ingrese precio maximo: "))
      except ValueError:
       print("Debe ingresar un numero entero")
      else:
        break
      
      busqueda_precio(min,max,inscripciones,planes)
   case 3:
      try:
        cod=input("Ingrese codigo: ").upper()
        prec=int(input("Ingrese nuevo precio: "))
      except ValueError:
        print("El precio debe ser un numero entero")
      if actualizar_precio(cod,prec,inscripciones):
        print("Precio cambiado")
        print(inscripciones)
      else:
        print("El codigo no existe")     
   case 4:
     while True:
       codi=input("Ingrese codigo: ").upper()
       nombre=input("Ingrese nombre plan: ")
       tipo= input("Ingrese tipo mensualidad: ")
       duracion= int(input("Ingrese duracion: "))
       acesso=input("Ingrese acesso s/n: ")
       clases=input("Ingrese clases s/n: ")
       horario=input("Ingrese horario: ")
       precio=int(input("Ingrese precio: "))
       cupos=int(input("Ingrese cupos: "))
       if codigo(codi):
         True
       elif nombre(nombre):
         True
       elif tipo(tipo):
         True
       elif duracion(duracion):
         True
       elif acceso(acesso):
         True
       elif clases(clases):
         True
       elif horario(horario):
         True
       elif precio(precio):
         True
       elif cupos(cupos):
         True
       else:
         print("dato invalido")
         break
     
    
main()