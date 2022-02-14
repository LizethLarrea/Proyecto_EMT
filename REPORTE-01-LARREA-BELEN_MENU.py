
from Proyecto_bases import lifestore_products, lifestore_sales, lifestore_searches

# from Variables_base import * 

#Eliminamos los productos que tuvieron un refund

Ventas_reales =[[venta[0], venta[1], venta[2], venta[3], venta[4]] for venta in lifestore_sales if venta[4] == 0]

categorias=[]
for producto in lifestore_products:
    categoria=producto[3]
    categorias.append(categoria) 
categorias_unicas=set(categorias)

#Separamos por categorias, según lo obtenido en categorias únicas

Cat_Procesadores =[categoria[:4] for categoria in lifestore_products if categoria[3] == 'procesadores']
Cat_Discos_Duros =[categoria[0:4] for categoria in lifestore_products if categoria[3] == 'discos duros']
Cat_Tarjetas_Video =[categoria[0:4] for categoria in lifestore_products if categoria[3] == 'tarjetas de video']
Cat_Audifonos =[categoria[0:4] for categoria in lifestore_products if categoria[3] == 'audifonos']
Cat_Pantallas =[categoria[0:4] for categoria in lifestore_products if categoria[3] == 'pantallas']
Cat_Memorias_USB =[categoria[0:4] for categoria in lifestore_products if categoria[3] == 'memorias usb']
Cat_Tarjetas_Madre =[categoria[0:4] for categoria in lifestore_products if categoria[3] == 'tarjetas madre']
Cat_Bocinas =[categoria[0:4] for categoria in lifestore_products if categoria[3] == 'bocinas']

#Contamos las ventas por categorias

for i in Ventas_reales:
    if i[1] in [producto[0] for producto in Cat_Procesadores]:
        i.append("procesadores")
    elif i[1] in [producto[0] for producto in Cat_Discos_Duros]:
        i.append("discos duros")
    elif i[1] in [producto[0] for producto in Cat_Tarjetas_Video]:
        i.append("tarjetas de video")
    elif i[1] in [producto[0] for producto in Cat_Audifonos]:
        i.append("audifonos")
    elif i[1] in [producto[0] for producto in Cat_Pantallas]:
        i.append("pantallas")
    elif i[1] in [producto[0] for producto in Cat_Memorias_USB]:
        i.append("memorias usb")
    elif i[1] in [producto[0] for producto in Cat_Tarjetas_Madre]:
        i.append("tarjetas madre")
    elif i[1] in [producto[0] for producto in Cat_Bocinas]:
        i.append("bocinas")
    
categ_ventas_reales=[categoria[5] for categoria in Ventas_reales ]
Ventas_por_catg=[]
for categorias in categorias_unicas:
    ventas=categ_ventas_reales.count(categorias)
    Ventas_por_catg.append([categorias,ventas])
    
prod_ventas_reales=[producto[1] for producto in Ventas_reales]
Ventas_por_producto=[]
for prod in lifestore_products:
    ventas=prod_ventas_reales.count(prod[0])
    Ventas_por_producto.append([prod[3],prod[0],prod[1],ventas])

Total_Busquedas=len(lifestore_searches)

prod_busquedas=[producto[1] for producto in lifestore_searches]     

Busquedas_por_producto=[]
for prod in lifestore_products:
    Busquedas=prod_busquedas.count(prod[0])
    Busquedas_por_producto.append([prod[3],prod[0],prod[1], Busquedas])

prod_busquedas_n=[[producto[0],producto[1]] for producto in lifestore_searches]     
for i in prod_busquedas_n:
    if i[1] in [producto[0] for producto in Cat_Procesadores]:
        i.append("procesadores")
    elif i[1] in [producto[0] for producto in Cat_Discos_Duros]:
        i.append("discos duros")
    elif i[1] in [producto[0] for producto in Cat_Tarjetas_Video]:
        i.append("tarjetas de video")
    elif i[1] in [producto[0] for producto in Cat_Audifonos]:
        i.append("audifonos")
    elif i[1] in [producto[0] for producto in Cat_Pantallas]:
        i.append("pantallas")
    elif i[1] in [producto[0] for producto in Cat_Memorias_USB]:
        i.append("memorias usb")
    elif i[1] in [producto[0] for producto in Cat_Tarjetas_Madre]:
        i.append("tarjetas madre")
    elif i[1] in [producto[0] for producto in Cat_Bocinas]:
        i.append("bocinas")

categ_busquedas=[categoria[2] for categoria in prod_busquedas_n]
Busquedas_por_catg=[]
for categorias in categorias_unicas:
    Busquedas=categ_busquedas.count(categorias)
    Busquedas_por_catg.append([categorias,Busquedas])

def login():
    """
    Login
    credenciales:

    usuario:
        jimmy
    contrase;a:
        ymmij
    """

    usuarioAccedio = False
    intentos = 0

    # Bienvenida!
    mensaje_bienvenida = 'Bienvenide al sistema para colaboradores de Lifestore!\nAccede con tus credenciales'
    print(mensaje_bienvenida)

    # Recibo constantemente sus intentos
    while not usuarioAccedio:
        # Primero ingresa Credenciales
        usuario = input('Usuario: ')
        contras = input('Contrase;a: ')
        intentos += 1
        # Reviso si el par coincide
        if usuario == 'jimmy' and contras == 'ymmij':
            usuarioAccedio = True
            print('Hola de nuevo!')
        else:
            # print('Tienes', 3 - intentos, 'intentos restantes')
            print(f'Tienes {3 - intentos} intentos restantes')
            if usuario == 'jimmy':
                print('Te equivocaste en la contraseña')
            else:
                print(f'El usuario: "{usuario}" no esta registrado')

        if intentos == 3:
            exit()


def productos_más_vendidos(): 

    Mayores_ventas=sorted(Ventas_por_producto, key=lambda x:x[3], reverse=True) 
    print(f"Los productos con mayores ventas son:")
    
    for i in range(5):
        print(f"{Mayores_ventas[i][2]} (ID: {Mayores_ventas[i][1]}) ventas: {Mayores_ventas[i][3]}")

def productos_más_buscados(): 
    
    #Listado con los 10 productos más buscados
    
    prod_busquedas=[producto[1] for producto in lifestore_searches]     
    #Si quisieramos solo los que tienen ventas, se haria así:
    # Sacamos los únicos de ventas_reales y los ponemos en lugar de lifestore_products:
    # Ventas_por_producto=list(set(prod_ventas_reales))
    # Busquedas_por_producto=[]
    # for prod in Unicos_prod_ventas_reales:
    # Busquedas = prod_busquedas.count(prod[0])
    #Busquedas_por_producto.append([prod[3],prod[0],prod[1], Busquedas])
    Busquedas_por_producto=[]
    for prod in lifestore_products:
        Busquedas=prod_busquedas.count(prod[0])
        Busquedas_por_producto.append([prod[3],prod[0],prod[1], Busquedas])

    Mas_Buscados=sorted(Busquedas_por_producto, key=lambda x:x[3], reverse=True) 
    print(f"Los productos con mayores busquedas son:")
    for i in range(10):
        print(f"{Mas_Buscados[i][2]} (ID: {Mas_Buscados[i][1]}) con {Mas_Buscados[i][3]} busquedas")

def productos_menos_vendidos_procesadores(): 
    
    
    Menores_ventas_procesadores=[categoria[0:4] for categoria in Ventas_por_producto if categoria[0]=="procesadores"]
    Menores_ventas_procesadores=sorted(Menores_ventas_procesadores, key=lambda x:x[3]) 
    print(f"Los productos con menores ventas para la categoria de procesadores, son:")
    for i in Menores_ventas_procesadores[0:5]:
        print(f"{i[2]} con {i[3]} ventas.")

    Menores_ventas_procesadores_0s=[categoria[3] for categoria in Menores_ventas_procesadores if categoria[3]==0]
    Menores_ventas_procesadores_0s_ID= [categoria[1] for categoria in Menores_ventas_procesadores if categoria[3]==0]
    print(f"Tenemos {len(Menores_ventas_procesadores_0s)} producto sin ventas con el siguiente IDs: {Menores_ventas_procesadores_0s_ID}")
    Ventas_procesadores=[categoria[1] for categoria in Ventas_por_producto if categoria[0]=="procesadores"]
    Ventas_procesadores=list(set(Ventas_procesadores))
    print(f"Tenemos {len(Ventas_procesadores)} productos en total")
    print(f"Por lo tanto, el {round(((len(Menores_ventas_procesadores)-len(Menores_ventas_procesadores_0s))/len(Menores_ventas_procesadores)*100),2)}% de los procesadores se vende")
    Total_P=[Total_p[1] for Total_p in Ventas_por_catg if Total_p[0]=="procesadores"]
    Total_P=sum(Total_P)
    Total_Ventas_Cat=[categoria[1] for categoria in Ventas_por_catg]
    Total_Ventas_Cat=sum(Total_Ventas_Cat)
    print(f"Sin embargo,representan el: {round(((Total_P/Total_Ventas_Cat)*100),2)}% de las ventas totales de lifestore")
    Ventas_procesadores=[[categoria[2], categoria[3]] for categoria in Ventas_por_producto if categoria[0]=="procesadores"]
    
def productos_menos_vendidos_DD(): 
    
    Menores_ventas_DD=[categoria[0:4] for categoria in Ventas_por_producto if categoria[0]=="discos duros"]
    Menores_ventas_DD=sorted(Menores_ventas_DD, key=lambda x:x[3]) 

    print(f"Los productos con mayores ventas para la categoria de Discos duros, son:")
    for i in range(5):
        print(f"{Menores_ventas_DD[i][2]} con {Menores_ventas_DD[i][3]} ventas.")
    Menores_ventas_DD_0s=[categoria[3] for categoria in Menores_ventas_DD if categoria[3]==0]
    Menores_ventas_DD_0s_ID= [categoria[1] for categoria in Menores_ventas_DD if categoria[3]==0]
    print(f"Tenemos {len(Menores_ventas_DD_0s)} productos sin ventas con los siguientes IDs: {Menores_ventas_DD_0s_ID}")
    Ventas_DD=[categoria[1] for categoria in Ventas_por_producto if categoria[0]=="discos duros"]
    Ventas_DD=list(set(Ventas_DD))
    print(f"Tenemos {len(Ventas_DD)} productos en total")
    print(f"Por lo tanto, el {round(((len(Ventas_DD)-len(Menores_ventas_DD_0s))/len(Ventas_DD)*100),2)}% de los discos duros se vende")
    Total_DD=[Total_p[1] for Total_p in Ventas_por_catg if Total_p[0]=="discos duros"]
    Total_DD=sum(Total_DD)
    Total_Ventas_Cat=[categoria[1] for categoria in Ventas_por_catg]
    Total_Ventas_Cat=sum(Total_Ventas_Cat)
    print(f"Sin embargo, representan el: {round(((Total_DD/Total_Ventas_Cat)*100),2)}% de las ventas totales de lifestore")

def productos_menos_vendidos_TV(): 
    
    Menores_ventas_TV=[categoria[0:4] for categoria in Ventas_por_producto if categoria[0]=="tarjetas de video"]
    Menores_ventas_TV=sorted(Menores_ventas_TV, key=lambda x:x[3]) 

    print(f"Los productos con menores ventas para la categoria de Tarjetas de video, son:")
    for i in range(5):
        print(f"{Menores_ventas_TV[i][2]} con {Menores_ventas_TV[i][3]} ventas.")
    Menores_ventas_TV_0s=[categoria[3] for categoria in Menores_ventas_TV if categoria[3]==0]
    Menores_ventas_TV_0s_ID= [categoria[1] for categoria in Menores_ventas_TV if categoria[3]==0]
    print(f"Tenemos {len(Menores_ventas_TV_0s)} productos sin ventas con los siguientes IDs: {Menores_ventas_TV_0s_ID}")
    Ventas_TV=[categoria[1] for categoria in Ventas_por_producto if categoria[0]=="tarjetas de video"]
    Ventas_TV=list(set(Ventas_TV))
    print(f"Tenemos {len(Ventas_TV)} productos en total")
    print(f"Por lo tanto, el {round(((len(Ventas_TV)-len(Menores_ventas_TV_0s))/len(Ventas_TV)*100),2)}% de las tarjetas de video se vende")
    Total_TV=[Total_p[1] for Total_p in Ventas_por_catg if Total_p[0]=="tarjetas de video"]
    Total_TV=sum(Total_TV)
    Total_Ventas_Cat=[categoria[1] for categoria in Ventas_por_catg]
    Total_Ventas_Cat=sum(Total_Ventas_Cat)
    print(f"Sin embargo, representan el: {round(((Total_TV/Total_Ventas_Cat)*100),2)}% de las ventas totales de lifestore")

def productos_menos_vendidos_Aud():
     
    Menores_ventas_Audifonos=[categoria[0:4] for categoria in Ventas_por_producto if categoria[0]=="audifonos"]
    Menores_ventas_Audifonos=sorted(Menores_ventas_Audifonos, key=lambda x:x[3]) 

    print(f"Los productos con menores ventas para la categoria de audifonos, son:")
    for i in range(5):
        print(f"{Menores_ventas_Audifonos[i][2]} con {Menores_ventas_Audifonos[i][3]} ventas.")
    Menores_ventas_Audifonos_0s=[categoria[3] for categoria in Menores_ventas_Audifonos if categoria[3]==0]
    Menores_ventas_Audifonos_0s_ID= [categoria[1] for categoria in Menores_ventas_Audifonos if categoria[3]==0]
    print(f"Tenemos {len(Menores_ventas_Audifonos_0s)} productos sin ventas con los siguientes IDs: {Menores_ventas_Audifonos_0s_ID}")
    Ventas_Audifonos=[categoria[1] for categoria in Ventas_por_producto if categoria[0]=="audifonos"]
    Ventas_Audifonos=list(set(Ventas_Audifonos))
    print(f"Tenemos {len(Ventas_Audifonos)} productos en total")
    print(f"Por lo tanto, el {round(((len(Ventas_Audifonos)-len(Menores_ventas_Audifonos_0s))/len(Ventas_Audifonos)*100),2)}% de los audifonos se vende")
    Total_Audifonos=[Total_p[1] for Total_p in Ventas_por_catg if Total_p[0]=="audifonos"]
    Total_Audifonos=sum(Total_Audifonos)
    Total_Ventas_Cat=[categoria[1] for categoria in Ventas_por_catg]
    Total_Ventas_Cat=sum(Total_Ventas_Cat)
    print(f"Sin embargo, representan el: {round(((Total_Audifonos/Total_Ventas_Cat)*100),2)}% de las ventas totales de lifestore")

def productos_menos_vendidos_Pan():
    
    Menores_ventas_Pantallas=[categoria[0:4] for categoria in Ventas_por_producto if categoria[0]=="pantallas"]
    Menores_ventas_Pantallas=sorted(Menores_ventas_Pantallas, key=lambda x:x[3]) 

    print(f"Los productos con menores ventas para la categoria de pantallas, son:")
    for i in range(5):
        print(f"{Menores_ventas_Pantallas[i][2]} con {Menores_ventas_Pantallas[i][3]} ventas.")
    Menores_ventas_Pantallas_0s=[categoria[3] for categoria in Menores_ventas_Pantallas if categoria[3]==0]
    ids_Menores_ventas_Pantallas_0s=[categoria[1] for categoria in Menores_ventas_Pantallas if categoria[3]==0]
    print(f"Tenemos {len(Menores_ventas_Pantallas_0s)} productos sin ventas con los siguientes IDs: {ids_Menores_ventas_Pantallas_0s}")
    Ventas_Pantallas=[categoria[1] for categoria in Ventas_por_producto if categoria[0]=="pantallas"]
    Ventas_Pantallas=list(set(Ventas_Pantallas))
    print(f"Tenemos {len(Ventas_Pantallas)} productos en total")
    print(f"Por lo tanto, el {round(((len(Ventas_Pantallas)-len(Menores_ventas_Pantallas_0s))/len(Ventas_Pantallas)*100),2)}% de las pantallas se venden")
    Total_pantallas=[Total_p[1] for Total_p in Ventas_por_catg if Total_p[0]=="pantallas"]
    Total_pantallas=sum(Total_pantallas)
    Total_Ventas_Cat=[categoria[1] for categoria in Ventas_por_catg]
    Total_Ventas_Cat=sum(Total_Ventas_Cat)
    print(f"Sin embargo, representan el: {round(((Total_pantallas/Total_Ventas_Cat)*100),2)}% de las ventas totales de lifestore")
        
def productos_menos_vendidos_USB():

    Menores_ventas_USB=[categoria[0:4] for categoria in Ventas_por_producto if categoria[0]=="memorias usb"]
    Menores_ventas_USB=sorted(Menores_ventas_USB, key=lambda x:x[3]) 

    print(f"Los productos con menores ventas para la categoria de memorias USB, son:")
    for ventas in Menores_ventas_USB:
        print(f"{ventas[2]} con {ventas[3]} ventas.")
    Menores_ventas_USB_0s=[categoria[3] for categoria in Menores_ventas_USB if categoria[3]==0]
    ids_Menores_ventas_USB_0s=[categoria[1] for categoria in Menores_ventas_USB if categoria[3]==0]
    print(f"Tenemos {len(Menores_ventas_USB_0s)} producto sin ventas con el siguiente ID: {ids_Menores_ventas_USB_0s}")
    Ventas_USB=[categoria[1] for categoria in Ventas_por_producto if categoria[0]=="memorias usb"]
    Ventas_USB=list(set(Ventas_USB))
    print(f"Tenemos {len(Ventas_USB)} productos en total")
    print(f"Por lo tanto, el {round(((len(Ventas_USB)-len(Menores_ventas_USB_0s))/len(Ventas_USB)*100),2)}% de las USBs se venden")
    Total_USB=[Total_p[1] for Total_p in Ventas_por_catg if Total_p[0]=="memorias usb"]
    Total_USB=sum(Total_USB)
    Total_Ventas_Cat=[categoria[1] for categoria in Ventas_por_catg]
    Total_Ventas_Cat=sum(Total_Ventas_Cat)
    print(f"Sin embargo, representan el: {round(((Total_USB/Total_Ventas_Cat)*100),2)}% de las ventas totales de lifestore")

def productos_menos_vendidos_TM():

    Menores_ventas_TM=[categoria[0:4] for categoria in Ventas_por_producto if categoria[0]=="tarjetas madre"]
    Menores_ventas_TM=sorted(Menores_ventas_TM, key=lambda x:x[3]) 

    print(f"Los productos con mayores ventas para la categoria de tarjetas madre, son:")
    for ventas in Menores_ventas_TM[0:5]:
        print(f"{ventas[2]} con {ventas[3]} ventas.")
    Menores_ventas_TM_0s=[categoria[3] for categoria in Menores_ventas_TM if categoria[3]==0]
    ID_Menores_ventas_TM_0s=[categoria[1] for categoria in Menores_ventas_TM if categoria[3]==0]
    print(f"Tenemos {len(Menores_ventas_TM_0s)} productos sin ventas con el siguiente ID: {ID_Menores_ventas_TM_0s}")
    Ventas_TM=[categoria[1] for categoria in Ventas_por_producto if categoria[0]=="tarjetas madre"]
    Ventas_TM=list(set(Ventas_TM))
    print(f"Tenemos {len(Ventas_TM)} productos en total")
    print(f"Por lo tanto, el {round(((len(Ventas_TM)-len(Menores_ventas_TM_0s))/len(Ventas_TM)*100),2)}% de las tarjetas madre se venden")
    Total_TM=[Total_p[1] for Total_p in Ventas_por_catg if Total_p[0]=="tarjetas madre"]
    Total_TM=sum(Total_TM)
    Total_Ventas_Cat=[categoria[1] for categoria in Ventas_por_catg]
    Total_Ventas_Cat=sum(Total_Ventas_Cat)
    print(f"Sin embargo, representan el: {round(((Total_TM/Total_Ventas_Cat)*100),2)}% de las ventas totales de lifestore")

def productos_menos_vendidos_Bocinas():
    
    Menores_ventas_Boc=[categoria[0:4] for categoria in Ventas_por_producto if categoria[0]=="bocinas"]
    Menores_ventas_Boc=sorted(Menores_ventas_Boc, key=lambda x:x[3]) 

    print(f"Los productos con mayores ventas para la categoria de bocinas, son:")
    for ventas in Menores_ventas_Boc[0:5]:
        print(f"{ventas[2]} con {ventas[3]} ventas.")
    Menores_ventas_Boc_0s=[categoria[3] for categoria in Menores_ventas_Boc if categoria[3]==0]
    ID_Menores_ventas_Boc_0s=[categoria[1] for categoria in Menores_ventas_Boc if categoria[3]==0]
    print(f"Tenemos {len(Menores_ventas_Boc_0s)} productos sin ventas con el siguiente ID: {ID_Menores_ventas_Boc_0s}")
    Ventas_Boc=[categoria[1] for categoria in Ventas_por_producto if categoria[0]=="bocinas"]
    Ventas_Boc=list(set(Ventas_Boc))
    print(f"Tenemos {len(Ventas_Boc)} productos en total")
    print(f"Por lo tanto, el {round(((len(Ventas_Boc)-len(Menores_ventas_Boc_0s))/len(Ventas_Boc)*100),2)}% de las bocinas se venden")
    Total_Boc=[Total_p[1] for Total_p in Ventas_por_catg if Total_p[0]=="bocinas"]
    Total_Boc=sum(Total_Boc)
    Total_Ventas_Cat=[categoria[1] for categoria in Ventas_por_catg]
    Total_Ventas_Cat=sum(Total_Ventas_Cat)
    print(f"Sin embargo, representan el: {round(((Total_Boc/Total_Ventas_Cat)*100),2)}% de las ventas totales de lifestore")

def productos_menos_buscados_procesadores():
    Menores_Busquedas_Procesadores=[categoria[0:4] for categoria in Busquedas_por_producto if categoria[0]=="procesadores"]
    Menores_Busquedas_Procesadores=sorted(Menores_Busquedas_Procesadores, key=lambda x:x[3]) 

    print(f"Los productos con menores busquedas para la categoria de procesadores, son:")
    for i in Menores_Busquedas_Procesadores[0:10]:
        print(f"{i[2]} (ID:{i[1]}) con {i[3]} busquedas.")

    Menores_Busquedas_Procesadores_0s=[categoria[3] for categoria in Menores_Busquedas_Procesadores if categoria[3]==0]
    Menores_Busquedas_Procesadores_0s_ID= [categoria[1] for categoria in Menores_Busquedas_Procesadores if categoria[3]==0]
    print(f"Tenemos {len(Menores_Busquedas_Procesadores_0s)} producto sin busquedas con los siguientes IDs: {Menores_Busquedas_Procesadores_0s_ID}")
    Busquedas_procesadores=[categoria[1] for categoria in Busquedas_por_producto if categoria[0]=="procesadores"]
    Busquedas_procesadores=list(set(Busquedas_procesadores))
    print(f"Tenemos {len(Busquedas_procesadores)} productos en total")
    print(f"Por lo tanto, el {round(((len(Menores_Busquedas_Procesadores)-len(Menores_Busquedas_Procesadores_0s))/len(Menores_Busquedas_Procesadores)*100),2)}% de los procesadores se buscan")
    Total_P_Buscado=[Total_p[1] for Total_p in Busquedas_por_catg if Total_p[0]=="procesadores"]
    Total_P_Buscado=sum(Total_P_Buscado)
    print(f"Y representan el: {round(((Total_P_Buscado/Total_Busquedas)*100),2)}% de las busquedas totales de lifestore")
    
def productos_menos_buscados_DD():
    Menores_Busquedas_DD=[categoria[0:4] for categoria in Busquedas_por_producto if categoria[0]=="discos duros"]
    Menores_Busquedas_DD=sorted(Menores_Busquedas_DD, key=lambda x:x[3]) 

    print(f"Los productos con menores busquedas para la categoria de 'Discos duros', son:")
    for i in Menores_Busquedas_DD[0:10]:
        print(f"{i[2]} (ID:{i[1]}) con {i[3]} busquedas.")

    Menores_Busquedas_DD_0s=[categoria[3] for categoria in Menores_Busquedas_DD if categoria[3]==0]
    Menores_Busquedas_DD_0s_ID= [categoria[1] for categoria in Menores_Busquedas_DD if categoria[3]==0]
    print(f"Tenemos {len(Menores_Busquedas_DD_0s)} producto sin busquedas con los siguientes IDs: {Menores_Busquedas_DD_0s_ID}")
    Busquedas_DD=[categoria[1] for categoria in Busquedas_por_producto if categoria[0]=="discos duros"]
    Busquedas_DD=list(set(Busquedas_DD))
    print(f"Tenemos {len(Busquedas_DD)} productos en total")
    print(f"Por lo tanto, el {round(((len(Menores_Busquedas_DD)-len(Menores_Busquedas_DD_0s))/len(Menores_Busquedas_DD)*100),2)}% de los discos duros se buscan")
    Total_DD_Buscado=[Total_p[1] for Total_p in Busquedas_por_catg if Total_p[0]=="discos duros"]
    Total_DD_Buscado=sum(Total_DD_Buscado)
    print(f"Y representan el: {round(((Total_DD_Buscado/Total_Busquedas)*100),2)}% de las busquedas totales de lifestore")

def productos_menos_buscados_TV():
    Menores_Busquedas_TV=[categoria[0:4] for categoria in Busquedas_por_producto if categoria[0]=="tarjetas de video"]
    Menores_Busquedas_TV=sorted(Menores_Busquedas_TV, key=lambda x:x[3]) 

    print(f"Los productos con menores busquedas para la categoria de 'Tarjetas de video', son:")
    for i in Menores_Busquedas_TV[0:19]:
        print(f"{i[2]} (ID:{i[1]}) con {i[3]} busquedas.")

    Menores_Busquedas_TV_0s=[categoria[3] for categoria in Menores_Busquedas_TV if categoria[3]==0]
    Menores_Busquedas_TV_0s_ID= [categoria[1] for categoria in Menores_Busquedas_TV if categoria[3]==0]
    print(f"Tenemos {len(Menores_Busquedas_TV_0s)} producto sin busquedas con los siguientes IDs: {Menores_Busquedas_TV_0s_ID}")
    Busquedas_TV=[categoria[1] for categoria in Busquedas_por_producto if categoria[0]=="tarjetas de video"]
    Busquedas_TV=list(set(Busquedas_TV))
    print(f"Tenemos {len(Busquedas_TV)} productos en total")
    print(f"Por lo tanto, el {round(((len(Menores_Busquedas_TV)-len(Menores_Busquedas_TV_0s))/len(Menores_Busquedas_TV)*100),2)}% de las tarjetas de video se buscan")
    Total_TV_Buscado=[Total_p[1] for Total_p in Busquedas_por_catg if Total_p[0]=="tarjetas de video"]
    Total_TV_Buscado=sum(Total_TV_Buscado)
    print(f"Y representan el: {round(((Total_TV_Buscado/Total_Busquedas)*100),2)}% de las busquedas totales de lifestore")
    
def productos_menos_buscados_Aud():
    Menores_Busquedas_Audifonos=[categoria[0:4] for categoria in Busquedas_por_producto if categoria[0]=="audifonos"]
    Menores_Busquedas_Audifonos=sorted(Menores_Busquedas_Audifonos, key=lambda x:x[3]) 

    print(f"Los productos con menores busquedas para la categoria de 'Audifonos', son:")
    for i in Menores_Busquedas_Audifonos[0:10]:
        print(f"{i[2]} (ID:{i[1]}) con {i[3]} busquedas.")

    Menores_Busquedas_Audifonos_0s=[categoria[3] for categoria in Menores_Busquedas_Audifonos if categoria[3]==0]
    Menores_Busquedas_Audifonos_0s_ID= [categoria[1] for categoria in Menores_Busquedas_Audifonos if categoria[3]==0]
    print(f"Tenemos {len(Menores_Busquedas_Audifonos_0s)} producto sin busquedas con los siguientes IDs: {Menores_Busquedas_Audifonos_0s_ID}")
    Busquedas_Audifonos=[categoria[1] for categoria in Busquedas_por_producto if categoria[0]=="audifonos"]
    Busquedas_Audifonos=list(set(Busquedas_Audifonos))
    print(f"Tenemos {len(Busquedas_Audifonos)} productos en total")
    print(f"Por lo tanto, el {round(((len(Menores_Busquedas_Audifonos)-len(Menores_Busquedas_Audifonos_0s))/len(Menores_Busquedas_Audifonos)*100),2)}% de los audifonos se buscan")
    Total_Au_Buscado=[Total_p[1] for Total_p in Busquedas_por_catg if Total_p[0]=="audifonos"]
    Total_Au_Buscado=sum(Total_Au_Buscado)
    print(f"Y representan el: {round(((Total_Au_Buscado/Total_Busquedas)*100),2)}% de las busquedas totales de lifestore")
    
def productos_menos_buscados_Pan():
    Menores_Busquedas_Pantallas=[categoria[0:4] for categoria in Busquedas_por_producto if categoria[0]=="pantallas"]
    Menores_Busquedas_Pantallas=sorted(Menores_Busquedas_Pantallas, key=lambda x:x[3]) 

    print(f"Los productos con menores busquedas para la categoria de 'Pantallas', son:")
    for i in Menores_Busquedas_Pantallas[0:10]:
        print(f"{i[2]} con {i[3]} busquedas.")

    Menores_Busquedas_Pantallas_0s=[categoria[3] for categoria in Menores_Busquedas_Pantallas if categoria[3]==0]
    Menores_Busquedas_Pantallas_0s_ID= [categoria[1] for categoria in Menores_Busquedas_Pantallas if categoria[3]==0]
    print(f"Tenemos {len(Menores_Busquedas_Pantallas_0s)} producto sin busquedas con los siguientes IDs: {Menores_Busquedas_Pantallas_0s_ID}")
    Busquedas_Pantallas=[categoria[1] for categoria in Busquedas_por_producto if categoria[0]=="pantallas"]
    Busquedas_Pantallas=list(set(Busquedas_Pantallas))
    print(f"Tenemos {len(Busquedas_Pantallas)} productos en total")
    print(f"Por lo tanto, el {round(((len(Menores_Busquedas_Pantallas)-len(Menores_Busquedas_Pantallas_0s))/len(Menores_Busquedas_Pantallas)*100),2)}% de las pantallas se buscan")
    Total_Pant_Buscado=[Total_p[1] for Total_p in Busquedas_por_catg if Total_p[0]=="pantallas"]
    Total_Pant_Buscado=sum(Total_Pant_Buscado)
    print(f"Y representan el: {round(((Total_Pant_Buscado/Total_Busquedas)*100),2)}% de las busquedas totales de lifestore")
    
def productos_menos_buscados_USB():
    Menores_Busquedas_USB=[categoria[0:4] for categoria in Busquedas_por_producto if categoria[0]=="memorias usb"]
    Menores_Busquedas_USB=sorted(Menores_Busquedas_USB, key=lambda x:x[3]) 

    print(f"Los productos con menores busquedas para la categoria de 'Memorias USB', son:")
    for i in Menores_Busquedas_USB[0:10]:
        print(f"{i[2]} con {i[3]} busquedas.")

    Menores_Busquedas_USB_0s=[categoria[3] for categoria in Menores_Busquedas_USB if categoria[3]==0]
    Menores_Busquedas_USB_0s_ID= [categoria[1] for categoria in Menores_Busquedas_USB if categoria[3]==0]
    print(f"Tenemos {len(Menores_Busquedas_USB_0s)} producto sin busquedas con los siguientes IDs: {Menores_Busquedas_USB_0s_ID}")
    Busquedas_USB=[categoria[1] for categoria in Busquedas_por_producto if categoria[0]=="memorias usb"]
    Busquedas_USB=list(set(Busquedas_USB))
    print(f"Tenemos {len(Busquedas_USB)} productos en total")
    print(f"Por lo tanto, el {round(((len(Menores_Busquedas_USB)-len(Menores_Busquedas_USB_0s))/len(Menores_Busquedas_USB)*100),2)}% de las memorias USB se buscan")
    Total_USB_Buscado=[Total_p[1] for Total_p in Busquedas_por_catg if Total_p[0]=="memorias usb"]
    Total_USB_Buscado=sum(Total_USB_Buscado)
    print(f"Y representan el: {round(((Total_USB_Buscado/Total_Busquedas)*100),2)}% de las busquedas totales de lifestore")
    
def productos_menos_buscados_TM():
    Menores_Busquedas_TM=[categoria[0:4] for categoria in Busquedas_por_producto if categoria[0]=="tarjetas madre"]
    Menores_Busquedas_TM=sorted(Menores_Busquedas_TM, key=lambda x:x[3]) 

    print(f"Los productos con menores busquedas para la categoria de 'Tarjetas madre', son:")
    for i in Menores_Busquedas_TM[0:10]:
        print(f"{i[2]} con {i[3]} busquedas.")

    Menores_Busquedas_TM_0s=[categoria[3] for categoria in Menores_Busquedas_TM if categoria[3]==0]
    Menores_Busquedas_TM_0s_ID= [categoria[1] for categoria in Menores_Busquedas_TM if categoria[3]==0]
    print(f"Tenemos {len(Menores_Busquedas_TM_0s)} producto sin busquedas con los siguientes IDs: {Menores_Busquedas_TM_0s_ID}")
    Busquedas_TM=[categoria[1] for categoria in Busquedas_por_producto if categoria[0]=="tarjetas madre"]
    Busquedas_TM=list(set(Busquedas_TM))
    print(f"Tenemos {len(Busquedas_TM)} productos en total")
    print(f"Por lo tanto, el {round(((len(Menores_Busquedas_TM)-len(Menores_Busquedas_TM_0s))/len(Menores_Busquedas_TM)*100),2)}% de las tarjetas madre se buscan")
    Total_TM_Buscado=[Total_p[1] for Total_p in Busquedas_por_catg if Total_p[0]=="tarjetas madre"]
    Total_TM_Buscado=sum(Total_TM_Buscado)
    print(f"Y representan el: {round(((Total_TM_Buscado/Total_Busquedas)*100),2)}% de las busquedas totales de lifestore")

def productos_menos_buscados_Bocinas():
    Menores_Busquedas_Boc=[categoria[0:4] for categoria in Busquedas_por_producto if categoria[0]=="bocinas"]
    Menores_Busquedas_Boc=sorted(Menores_Busquedas_Boc, key=lambda x:x[3]) 

    print(f"Los productos con menores busquedas para la categoria de 'Bocinas', son:")
    for i in Menores_Busquedas_Boc[0:10]:
        print(f"{i[2]} con {i[3]} busquedas.")
    
    Menores_Busquedas_Boc_0s=[categoria[3] for categoria in Menores_Busquedas_Boc if categoria[3]==0]
    Menores_Busquedas_Boc_0s_ID= [categoria[1] for categoria in Menores_Busquedas_Boc if categoria[3]==0]
    print(f"Tenemos {len(Menores_Busquedas_Boc_0s)} producto sin busquedas con los siguientes IDs: {Menores_Busquedas_Boc_0s_ID}")
    Busquedas_Boc=[categoria[1] for categoria in Busquedas_por_producto if categoria[0]=="bocinas"]
    Busquedas_Boc=list(set(Busquedas_Boc))
    print(f"Tenemos {len(Busquedas_Boc)} productos en total")
    print(f"Por lo tanto, el {round(((len(Menores_Busquedas_Boc)-len(Menores_Busquedas_Boc_0s))/len(Menores_Busquedas_Boc)*100),2)}% de las bocinas se buscan")
    Total_Boc_Buscado=[Total_p[1] for Total_p in Busquedas_por_catg if Total_p[0]=="bocinas"]
    Total_Boc_Buscado=sum(Total_Boc_Buscado)
    print(f"Y representan el: {round(((Total_Boc_Buscado/Total_Busquedas)*100),2)}% de las busquedas totales de lifestore")

def reseñas_por_producto():
    #Sacamos el total de reseñas por producto 

    prod_ventas_reseñas=[producto[1] for producto in lifestore_sales]
    productos_unicos=list(set(prod_ventas_reseñas))

    Total_por_prod=[]
    for prod in productos_unicos:
        reseñas_totales=prod_ventas_reseñas.count(prod)
        Total_por_prod.append([prod, reseñas_totales])
    print(Total_por_prod)

    #Sacamos la suma de las calificaciones por producto 

    #Convertimos la lista en lista de listas para poder encontrar la suma 
    #de calificaciones por producto. 
    def extractDigits(productos_list):
        return list(map(lambda el:[el], productos_list))
        
    productos_unicos_list=extractDigits(productos_unicos)

    #Obtenemos la suma de calificaciones por producto 
                
    suma_ind=0
    calificacion_por_prod=[]
    for product in productos_unicos_list:
        for calificacion in lifestore_sales:
            if product[0]==calificacion[1]:
                suma_ind += calificacion[2]
            continue
        calificacion_por_prod.append([product[0], suma_ind])
        suma_ind=0
    #Obtenemos el promedio de la calificación por producto

    productos=[]
    for prod in Total_por_prod: 
        for product in calificacion_por_prod: 
            if prod[0]==product[0]:
                productos.append([prod[0],prod[1],product[1]])

    Promedio_reseñas=[]
    for prod in productos:
        Numero_Cal=prod[1]
        Suma_Cal=prod[2]
        Promedio=Suma_Cal/Numero_Cal    
        Promedio_reseñas.append([prod[0],prod[1],Promedio])

    #Ponemos el nombre de los productos 

    Reseñas_Prom_PP=[]
    for product in lifestore_products:
        for prod in Promedio_reseñas:
            if prod[0]==product[0]:
                Reseñas_Prom_PP.append([prod[0], product[1],prod[2], product[3]])
    print(Reseñas_Prom_PP)

    #Mejores reseñas 

    Mejores_reseñas=sorted(Reseñas_Prom_PP, key=lambda x:x[3], reverse=True) 
    print(f"Los productos con mejores reseñas son: ")
    for i in range(5):
        print(f"{Mejores_reseñas[i][1]} con: {round(Mejores_reseñas[i][2])} estrellas de score promedio")
    
    print('\n')
    
    #Peores reseñas 
    
    Peores_reseñas=sorted(Reseñas_Prom_PP, key=lambda x:x[3]) 
    print(f"Los productos con peores reseñas son: ")
    for i in Peores_reseñas[0:5]:
        if i[2]==1:
            print(f"{i[1]} con: {round(i[2])} estrella de score promedio")
        elif i[2]>1:
            print(f"{i[1]} con: {round(i[2])} estrellas de score promedio")
        
def mejores_categorias():
    #Categorias con mayores ventas
    print("Las ventas por categoria se presentan a continuación: ")
    for categ in Ventas_por_catg:
        print(f'La categoria {categ[0]} tuvo {categ[1]} ventas') 

    Mayores_ventas_Cat=sorted(Ventas_por_catg, key=lambda x:x[1], reverse=True)
    print(f"Las 3 categorias con mayores ventas fueron las siguientes:") 
    for categ in Mayores_ventas_Cat[0:3]:
        print(f"{categ[0]} con: {round(categ[1])} ventas")
    print('\n')
    #Categorias con menores busquedas 
    print("Las busquedas por categoria se presentan a continuación: ")
    for categ in Busquedas_por_catg:
        print(f'La categoria {categ[0]} tuvo {categ[1]} ventas') 

    Mayores_busquedas_Cat=sorted(Busquedas_por_catg, key=lambda x:x[1], reverse=True)
    print(f"Las 3 categorias con mayores busquedas fueron las siguientes:") 
    for categ in Mayores_busquedas_Cat[0:3]:
        print(f"{categ[0]} con: {round(categ[1])} busquedas")

def reseña_pp_mejcat():

    prod_ventas_reseñas=[producto[1] for producto in lifestore_sales]
    productos_unicos=list(set(prod_ventas_reseñas))

    Total_por_prod=[]
    for prod in productos_unicos:
        reseñas_totales=prod_ventas_reseñas.count(prod)
        Total_por_prod.append([prod, reseñas_totales])
    print(Total_por_prod)

    #Sacamos la suma de las calificaciones por producto 

    #Convertimos la lista en lista de listas para poder encontrar la suma 
    #de calificaciones por producto. 
    def extractDigits(productos_list):
        return list(map(lambda el:[el], productos_list))
        
    productos_unicos_list=extractDigits(productos_unicos)

    #Obtenemos la suma de calificaciones por producto 
                
    suma_ind=0
    calificacion_por_prod=[]
    for product in productos_unicos_list:
        for calificacion in lifestore_sales:
            if product[0]==calificacion[1]:
                suma_ind += calificacion[2]
            continue
        calificacion_por_prod.append([product[0], suma_ind])
        suma_ind=0

    productos=[]
    for prod in Total_por_prod: 
        for product in calificacion_por_prod: 
            if prod[0]==product[0]:
                productos.append([prod[0],prod[1],product[1]])

   
    Promedio_reseñas=[]
    for prod in productos:
        Numero_Cal=prod[1]
        Suma_Cal=prod[2]
        Promedio=Suma_Cal/Numero_Cal    
        Promedio_reseñas.append([prod[0],prod[1],Promedio])
    print(Promedio_reseñas)

    #Ponemos el nombre de los productos 

    Reseñas_Prom_PP=[]
    for product in lifestore_products:
        for prod in Promedio_reseñas:
            if prod[0]==product[0]:
                Reseñas_Prom_PP.append([prod[0], product[1],prod[2], product[3]])
       
    Cat_Procesadores_reseñas=[[procesadores[1], procesadores[2]] for procesadores in Reseñas_Prom_PP if procesadores[3]=="procesadores"]
    Mejores_reseñas_procesadores=sorted(Cat_Procesadores_reseñas, key=lambda x:x[1], reverse=True)
    print(f"Los 3 procesadores con mejores reseñas fueron los siguientes:") 
    for categ in Mejores_reseñas_procesadores[0:3]:
        print(f"{categ[0]} con: {round(categ[1])} estrellas de score promedio")
    print("\n")
    Cat_Tarjetas_Madre_reseñas=[[procesadores[1], procesadores[2]] for procesadores in Reseñas_Prom_PP if procesadores[3]=="tarjetas madre"]
    Mejores_reseñas_TM=sorted(Cat_Tarjetas_Madre_reseñas, key=lambda x:x[1], reverse=True)
    print(f"Las 3 tarjetas madre con mejores reseñas fueron los siguientes:") 
    for categ in Mejores_reseñas_TM[0:3]:
        print(f"{categ[0]} con: {round(categ[1])} estrellas de score promedio")
    print("\n")
    Cat_DD_reseñas=[[procesadores[1], procesadores[2]] for procesadores in Reseñas_Prom_PP if procesadores[3]=="discos duros"]
    Mejores_reseñas_DD=sorted(Cat_DD_reseñas, key=lambda x:x[1], reverse=True)
    print(f"Los 3 discos duros con mejores reseñas fueron los siguientes:") 
    for categ in Mejores_reseñas_DD[0:3]:
        print(f"{categ[0]} con: {round(categ[1])} estrellas de score promedio")

def ingresos_ventas_AM():
    
    id_fecha = [[sale[0], sale[3]] for sale in lifestore_sales if sale[4] == 0 ]
    categorizacion_años={}
    for par in id_fecha:
        id = par[0]
        _, _, ano = par[1].split('/')
        if ano not in categorizacion_años.keys():
            categorizacion_años[ano] = []
        categorizacion_años[ano].append(id)

    Meses_Ing_Ventas=[]
    for key in categorizacion_años.keys():
        lista_ids = categorizacion_años[key]
        suma_venta = 0
        for id_venta in lista_ids:
            indice = id_venta - 1
            info_venta = lifestore_sales[indice]
            id_product = info_venta[1]
            precio = lifestore_products[id_product-1][2]
            suma_venta += precio
            Ventas_totales=len(lista_ids)
        print("\n")
        print(f"En el año: {key}, los ingresos ascendieron a: {suma_venta} y las ventas totales a: {Ventas_totales}")
    print("\n")
    
    categorizacion_meses={}

    for par in id_fecha:
        id = par[0]
        _, mes, _ = par[1].split('/')
        mes=int(mes)
        if mes not in categorizacion_meses.keys():
            categorizacion_meses[mes] = []
        categorizacion_meses[mes].append(id)
        
    
    Meses_Ing_Ventas=[]

    for key in categorizacion_meses.keys():
        lista_mes = categorizacion_meses[key]
        suma_venta = 0
        for id_venta in lista_mes:
            indice = id_venta - 1
            info_venta = lifestore_sales[indice]
            id_product = info_venta[1]
            precio = lifestore_products[id_product-1][2]
            suma_venta += precio
            Ventas_totales=len(lista_mes)
        Meses_Ing_Ventas.append([key, suma_venta, Ventas_totales])

    Meses_Ing_Ventas=sorted(Meses_Ing_Ventas, key=lambda x:x[0]) 
    
    for mes in Meses_Ing_Ventas:
        if mes[0]==1:
            print("\n")
            print(f"En enero:")
            print("\n")
            print(f"Los ingresos fueron de {mes[1]}")
            print(f"Las ventas fueron {mes[2]}")
            print("\n")
        elif mes[0]==2:
            print("\n")
            print(f"En febrero:")
            print("\n")
            print(f"Los ingresos fueron de {mes[1]}")
            print(f"Las ventas fueron {mes[2]}")
            print("\n")
        elif mes[0]==3:
            print("\n")
            print(f"En marzo:")
            print("\n")
            print(f"Los ingresos fueron de {mes[1]}")
            print(f"Las ventas fueron:{mes[2]}")
            print("\n")
        elif mes[0]==4:
            print("\n")
            print(f"En abril")
            print("\n")
            print(f"Los ingresos fueron:{mes[1]}")
            print(f"Las ventas fueron:{mes[2]}")
            print("\n")
        elif mes[0]==5:
            print("\n")
            print(f"En mayo")
            print("\n")
            print(f"Los ingresos fueron:{mes[1]}")
            print(f"Las ventas fueron:{mes[2]}")
            print("\n")
        elif mes[0]==6:
            print("\n")
            print(f"En junio")
            print("\n")
            print(f"Los ingresos fueron:{mes[1]}")
            print(f"Las ventas fueron:{mes[2]}")
            print("\n")
        elif mes[0]==7:
            print("\n")
            print(f"En julio")
            print("\n")
            print(f"Los ingresos fueron:{mes[1]}")
            print(f"Las ventas fueron:{mes[2]}")
            print("\n")
        elif mes[0]==8:
            print("\n")
            print(f"En agosto")
            print("\n")
            print(f"Los ingresos fueron:{mes[1]}")
            print(f"Las ventas fueron:{mes[2]}")
            print("\n")
        print("Los meses de septiembre, octubre, noviembre y diciembre no tienen ventas")

def meses_Ming_ventas():
    
    categorizacion_meses={}
    
    id_fecha = [[sale[0], sale[3]] for sale in lifestore_sales if sale[4] == 0 ]
    for par in id_fecha:
        id = par[0]
        _, mes, _ = par[1].split('/')
        mes=int(mes)
        if mes not in categorizacion_meses.keys():
            categorizacion_meses[mes] = []
        categorizacion_meses[mes].append(id)    
    
    Meses_Ing_Ventas=[]

    for key in categorizacion_meses.keys():
        lista_mes = categorizacion_meses[key]
        suma_venta = 0
        for id_venta in lista_mes:
            indice = id_venta - 1
            info_venta = lifestore_sales[indice]
            id_product = info_venta[1]
            precio = lifestore_products[id_product-1][2]
            suma_venta += precio
            Ventas_totales=len(lista_mes)
        Meses_Ing_Ventas.append([key, suma_venta, Ventas_totales])

    Meses_Ing_Ventas=sorted(Meses_Ing_Ventas, key=lambda x:x[0]) 
    Meses_mas_ventas=sorted(Meses_Ing_Ventas, key=lambda x:x[2], reverse=True) 
    Meses_mas_ingresos=sorted(Meses_Ing_Ventas, key=lambda x:x[2], reverse=True) 
    
    print(f"Los meses con más ventas fueron:")
    print("\n")
    for ventas in Meses_mas_ventas[0:3]:
        if ventas[0]==4:    
            print(f"Abril, con {ventas[2]} ventas")
            print("\n")
        elif ventas[0]==1:    
            print(f"Enero, con {ventas[2]} ventas")
        elif ventas[0]==3:
            print("\n")    
            print(f"Marzo, con {ventas[2]} ventas")
    print("\n")
    print(f"Los meses con más ingresos fueron:")
    for ingresos in Meses_mas_ingresos[0:3]:
        if ingresos[0]==4:
            print("\n")    
            print(f"Abril, con {ingresos[1]} de ingresos")
        elif ingresos[0]==1:
            print("\n")    
            print(f"Enero, con {ingresos[1]} de ingresos")
        elif ingresos[0]==3:
            print("\n")    
            print(f"Marzo, con {ingresos[1]} de ingresos")
    print("\n")
    Meses_menos_ventas=sorted(Meses_Ing_Ventas, key=lambda x:x[2]) 
    Meses_menos_ingresos=sorted(Meses_Ing_Ventas, key=lambda x:x[2]) 

    print(f"Los meses con menores ventas fueron:")
    for ventas in Meses_menos_ventas[0:3]:
        if ventas[0]==8:
            print("\n")    
            print(f"Agosto, con {ventas[2]} ventas")
        elif ventas[0]==6:
            print("\n")    
            print(f"Junio, con {ventas[2]} ventas")
        elif ventas[0]==7:
            print("\n")    
            print(f"Julio, con {ventas[2]} ventas")
    print("\n")
    print(f"Los meses con menores ingresos fueron:")
    for ingresos in Meses_menos_ingresos[0:3]:
        if ingresos[0]==8:
            print("\n")    
            print(f"Agosto, con {ingresos[1]} de ingresos")
        elif ingresos[0]==6:
            print("\n")    
            print(f"Junio, con {ingresos[1]} de ingresos")
        elif ingresos[0]==7:
            print("\n")    
            print(f"Julio, con {ingresos[1]} de ingresos")
    print("\n")
    col_ingresos = [ingresos[1] for ingresos in Meses_mas_ingresos]
    col_ventas = [ventas[2] for ventas in Meses_mas_ingresos]
    Promedio_ing=sum(col_ingresos)/8
    Promedio_ven=sum(col_ventas)/8
    Promedio_ing_ventas=Promedio_ing/Promedio_ven

    print(f"Los ingresos promedio mensuales por los meses que se vendió, fueron: {Promedio_ing}")
    print(f"Las ventas promedio mensuales por los meses que se vendió, fueron: {round(Promedio_ven)}")
    print(f"Los ingresos/ventas promedio mensuales por los meses que se vendió, fueron: {round(Promedio_ing_ventas,2)}")

    
def menu():
    login()
    while True:
        print('Bienvenido al sistema para colaboradores ¿Que datos solicitados desea ver?:')
        print('\t1. Productos más vendidos y más rezagados')
        print('\t2. Productos por reseña en el servicio')
        print('\t3. Ingresos y ventas anuales y mensuales')
        print('\t0. Salir')
        seleccion = input('> ')
        if seleccion == '1':
            print('\t1 Vista por productos')
            print('\t2 Vista por categorias')
            seleccion_2 = input('> ')
            if seleccion_2=="1":
                print('\t1 Productos más vendidos')
                print('\t2 Productos más buscados')
                seleccion_3 = input('> ')
                if seleccion_3=="1":
                    productos_más_vendidos()
                elif seleccion_3=="2":
                    productos_más_buscados()
            elif seleccion_2=="2":
                print('\t1 Productos menos vendidos')
                print('\t2 Productos menos buscados')
                seleccion_3_1= input('> ')
                if seleccion_3_1=="1":
                    print('\t1 Procesadores')
                    print('\t2 Discos duros')
                    print('\t3 Tarjetas de video')
                    print('\t4 Audifonos')
                    print('\t5 Pantallas')
                    print('\t6 Memorias USB')
                    print('\t7 Tarjetas madre')
                    print('\t8 Bocinas')
                    seleccion_4= input('> ')
                    if seleccion_4=="1":
                        productos_menos_vendidos_procesadores()
                    elif seleccion_4=="2":
                        productos_menos_vendidos_DD()
                    elif seleccion_4== "3":
                        productos_menos_vendidos_TV()
                    elif seleccion_4=="4":
                        productos_menos_vendidos_Aud()
                    elif seleccion_4=="5":
                        productos_menos_vendidos_Pan()
                    elif seleccion_4=="6":
                        productos_menos_vendidos_USB()
                    elif seleccion_4=="7":
                        productos_menos_vendidos_TM()
                    elif seleccion_4=="8":
                        productos_menos_vendidos_Bocinas()
                elif seleccion_3_1=="2":
                    print('\t1 Procesadores')
                    print('\t2 Discos duros')
                    print('\t3 Tarjetas de video')
                    print('\t4 Audifonos')
                    print('\t5 Pantallas')
                    print('\t6 Memorias USB')
                    print('\t7 Tarjetas madre')
                    print('\t8 Bocinas')
                    seleccion_4= input('> ')
                    if seleccion_4=="1":
                        productos_menos_buscados_procesadores()
                    elif seleccion_4=="2":
                        productos_menos_buscados_DD()
                    elif seleccion_4== "3":
                        productos_menos_buscados_TV()
                    elif seleccion_4=="4":
                        productos_menos_buscados_Aud()
                    elif seleccion_4=="5":
                        productos_menos_buscados_Pan()
                    elif seleccion_4=="6":
                        productos_menos_buscados_USB()
                    elif seleccion_4=="7":
                        productos_menos_buscados_TM()
                    elif seleccion_4=="8":
                        productos_menos_buscados_Bocinas()                
            continue
        elif seleccion == '2':
            print('\t1 Peores y mejores reseñas por producto')
            print("\t2 Mejores categorias")
            print('\t3 Productos por reseña de las mejores categorias')
            seleccion_2 = input('> ')
            if seleccion_2=="1":
                reseñas_por_producto()
            elif seleccion_2=="2":
                mejores_categorias()
            elif seleccion_2=="3":
                reseña_pp_mejcat()                
            continue
        elif seleccion == '3':
            print('\t1 Ingresos y ventas anuales y mensuales')
            print("\t2 Meses con más ingresos y ventas. Promedio mensual")
            seleccion_2 = input('> ')
            if seleccion_2=='1':
                ingresos_ventas_AM()
            elif seleccion_2=='2':
                meses_Ming_ventas()    
        elif seleccion == '0':
            exit()
        else:
            print('Opcion invalida!')
menu()
