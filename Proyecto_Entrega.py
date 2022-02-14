"""
This is the LifeStore_SalesList data:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""
from Proyecto_bases import lifestore_products, lifestore_sales, lifestore_searches

#Quitamos aquellos productos que se devolvieron

Ventas_reales =[[venta[0], venta[1], venta[2], venta[3], venta[4]] for venta 
                in lifestore_sales if venta[4] == 0]

#Obtenemos las categorias únicas. 

categorias=[]
for producto in lifestore_products:
    categoria=producto[3]
    categorias.append(categoria) 
categorias_unicas=set(categorias)


#Separamos por categorias, según lo obtenido en categorias únicas

Cat_Procesadores =[categoria[:4] for categoria in lifestore_products if categoria[3] 
                   == 'procesadores']
Cat_Discos_Duros =[categoria[0:4] for categoria in lifestore_products if categoria[3] 
                   == 'discos duros']
Cat_Tarjetas_Video =[categoria[0:4] for categoria in lifestore_products if categoria[3] 
                     == 'tarjetas de video']
Cat_Audifonos =[categoria[0:4] for categoria in lifestore_products if categoria[3] 
                == 'audifonos']
Cat_Pantallas =[categoria[0:4] for categoria in lifestore_products if categoria[3] 
                == 'pantallas']
Cat_Memorias_USB =[categoria[0:4] for categoria in lifestore_products if categoria[3] 
                   == 'memorias usb']
Cat_Tarjetas_Madre =[categoria[0:4] for categoria in lifestore_products if categoria[3] 
                     == 'tarjetas madre']
Cat_Bocinas =[categoria[0:4] for categoria in lifestore_products if categoria[3] 
              == 'bocinas']

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


#Contamos las busquedas por categorias

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
 
#Listado con los 5 productos con mayores ventas 

prod_ventas_reales=[producto[1] for producto in Ventas_reales]

Ventas_por_producto=[]
for prod in lifestore_products:
    ventas=prod_ventas_reales.count(prod[0])
    Ventas_por_producto.append([prod[3],prod[0],prod[1],ventas])

Mayores_ventas=sorted(Ventas_por_producto, key=lambda x:x[3], reverse=True) 

print(f"Los productos con mayores ventas son:")
for i in range(5):
    print(f"{Mayores_ventas[i][2]} (ID: {Mayores_ventas[i][1]}) ventas: {Mayores_ventas[i][3]}")

#Listado con los 10 productos más buscados

prod_busquedas=[producto[1] for producto in lifestore_searches]     

#Si quisieramos solo los que tienen ventas, se haria así:
# Sacamos los únicos de ventas_reales y los ponemos en lugar de lifestore_products:
# Ventas_por_producto=list(set(prod_ventas_reales))
# Busquedas_por_producto=[]
# for prod in Unicos_prod_ventas_reales:
# Busquedas = prod_busquedas.count(prod[0])
# Busquedas_por_producto.append([prod[3],prod[0],prod[1], Busquedas])

Busquedas_por_producto=[]
for prod in lifestore_products:
    Busquedas=prod_busquedas.count(prod[0])
    Busquedas_por_producto.append([prod[3],prod[0],prod[1], Busquedas])

Mas_Buscados=sorted(Busquedas_por_producto, key=lambda x:x[3], reverse=True) 
print(f"Los productos con mayores busquedas son:")
for i in range(10):
    print(f"{Mas_Buscados[i][2]} (ID: {Mas_Buscados[i][1]}) con {Mas_Buscados[i][3]} busquedas")


#Listados con las categorias:

#Con menores ventas 

#Procesadores 

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


#Para ver el porcentaje de ventas por procesadores: 

Ventas_procesadores=[[categoria[2], categoria[3]] for categoria in Ventas_por_producto if categoria[0]=="procesadores"]
Total_p=[Total_p[1] for Total_p in Ventas_por_catg if Total_p[0]=="procesadores"]
Porcentaje_ventas=[]
for ventas in Ventas_procesadores:
    porcentaje_ventas_p=(ventas[1]/Total_p[0])*100
    Porcentaje_ventas.append([ventas[0], porcentaje_ventas_p])

Porcentaje_ventas=sorted(Porcentaje_ventas, key=lambda x:x[1], reverse=True)
for ventas in Porcentaje_ventas:    
    print(f"El producto: {ventas[0]}, tuvo el {round(ventas[1],2)}% de ventas")
         
Procesadores_unicos=[productos[1] for productos in Cat_Procesadores]            
Procesadores_unicos=set(Procesadores_unicos)

#Procesadores_unicos=list(Procesadores_unicos)
#Procesadores_unicos.sort("Intel")

#Discos duros

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

#Tarjetas de video 

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


#Audifonos

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
    
    
#Pantallas

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
    
#USB

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


#Tarjetas madre

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


        
#Bocinas

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

#Los mejores productos son los procesadores, discos duros y las tarjetas madre
#Los peores productos, son las USBs, las bocinas y las pantallas

#Total de busquedas: 

Total_Busquedas=len(lifestore_searches)

#Con menores busquedas 

#Procesadores 

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

#Discos duros

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


#Tarjetas de video 

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

#Audifonos

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
    
    
#Pantallas

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
    
#USB

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
   
#Tarjetas madre

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
  
        
#Bocinas

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
  
#PRODUCTOS POR RESEÑA EN EL SERVICIO 

#Productos generales

#Sacamos el total de reseñas por producto 

prod_ventas_reseñas=[producto[1] for producto in lifestore_sales]
productos_unicos=list(set(prod_ventas_reseñas))

Total_por_prod=[]
for prod in productos_unicos:
    reseñas_totales=prod_ventas_reseñas.count(prod)
    Total_por_prod.append([prod, reseñas_totales])

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


#Mejores reseñas 

Mejores_reseñas=sorted(Reseñas_Prom_PP, key=lambda x:x[2], reverse=True) 
print(f"Los productos con mejores reseñas son: ")
for i in range(5):
    print(f"{Mejores_reseñas[i][1]} con: {round(Mejores_reseñas[i][2])} estrellas de score promedio")

#Peores reseñas

Peores_reseñas=sorted(Reseñas_Prom_PP, key=lambda x:x[2]) 
print(f"Los productos con peores reseñas son: ")
for i in Peores_reseñas[0:5]:
    if i[2]==1:
        print(f"{i[1]} con: {round(i[2])} estrella de score promedio")
    elif i[2]>1:
        print(f"{i[1]} con: {round(i[2])} estrellas de score promedio")


#Categorias con mayores ventas


print("Las ventas por categoria se presentan a continuación: ")
for categ in Ventas_por_catg:
    print(f'La categoria {categ[0]} tuvo {categ[1]} ventas') 

Mayores_ventas_Cat=sorted(Ventas_por_catg, key=lambda x:x[1], reverse=True)
print(f"Las 3 categorias con mayores ventas fueron las siguientes:") 
for categ in Mayores_ventas_Cat[0:3]:
    print(f"{categ[0]} con: {round(categ[1])} ventas")
    

#Categorias con mayores busquedas 

print("Las busquedas por categoria se presentan a continuación: ")
for categ in Busquedas_por_catg:
    print(f'La categoria {categ[0]} tuvo {categ[1]} ventas') 

Mayores_busquedas_Cat=sorted(Busquedas_por_catg, key=lambda x:x[1], reverse=True)
print(f"Las 3 categorias con mayores busquedas fueron las siguientes:") 
for categ in Mayores_busquedas_Cat[0:3]:
    print(f"{categ[0]} con: {round(categ[1])} busquedas")
    

#Las mayores ventas y mayores busquedas tienen las mismas categorias 
#Por lo que se procederá a hacer el análisis de los productos por reseña en 
#estas tres categorias:


Cat_Procesadores_reseñas=[[procesadores[1], procesadores[2]] for procesadores in 
                          Reseñas_Prom_PP if procesadores[3]=="procesadores"]
Mejores_reseñas_procesadores=sorted(Cat_Procesadores_reseñas, key=lambda x:x[1], reverse=True)
print(f"Los 3 procesadores con mejores reseñas fueron los siguientes:") 
for categ in Mejores_reseñas_procesadores[0:3]:
    print(f"{categ[0]} con: {round(categ[1])} estrellas de score promedio")

Cat_Tarjetas_Madre_reseñas=[[procesadores[1], procesadores[2]] for procesadores in Reseñas_Prom_PP if procesadores[3]=="tarjetas madre"]
Mejores_reseñas_TM=sorted(Cat_Tarjetas_Madre_reseñas, key=lambda x:x[1], reverse=True)
print(f"Las 3 tarjetas madre con mejores reseñas fueron los siguientes:") 
for categ in Mejores_reseñas_TM[0:3]:
    print(f"{categ[0]} con: {round(categ[1])} estrellas de score promedio")

Cat_DD_reseñas=[[procesadores[1], procesadores[2]] for procesadores in Reseñas_Prom_PP if procesadores[3]=="discos duros"]
Mejores_reseñas_DD=sorted(Cat_DD_reseñas, key=lambda x:x[1], reverse=True)
print(f"Los 3 discos duros con mejores reseñas fueron los siguientes:") 
for categ in Mejores_reseñas_DD[0:3]:
    print(f"{categ[0]} con: {round(categ[1])} estrellas de score promedio")

#Total de ingresos y ventas anuales 

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
    print(f"En el año: {key}, los ingresos ascendieron a: {suma_venta} y las ventas totales a: {Ventas_totales}")


#Total de ingresos y ventas mensuales. 

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
        print(f"En enero:")
        print(f"Los ingresos fueron de {mes[1]}")
        print(f"Las ventas fueron {mes[2]}")
    elif mes[0]==2:
        print(f"En febrero:")
        print(f"Los ingresos fueron de {mes[1]}")
        print(f"Las ventas fueron {mes[2]}")
    elif mes[0]==3:
        print(f"En marzo:")
        print(f"Los ingresos fueron de {mes[1]}")
        print(f"Las ventas fueron:{mes[2]}")
    elif mes[0]==4:
        print(f"En abril")
        print(f"Los ingresos fueron:{mes[1]}")
        print(f"Las ventas fueron:{mes[2]}")
    elif mes[0]==5:
        print(f"En mayo")
        print(f"Los ingresos fueron:{mes[1]}")
        print(f"Las ventas fueron:{mes[2]}")
    elif mes[0]==6:
        print(f"En junio")
        print(f"Los ingresos fueron:{mes[1]}")
        print(f"Las ventas fueron:{mes[2]}")
    elif mes[0]==7:
        print(f"En julio")
        print(f"Los ingresos fueron:{mes[1]}")
        print(f"Las ventas fueron:{mes[2]}")
    elif mes[0]==8:
        print(f"En agosto")
        print(f"Los ingresos fueron:{mes[1]}")
        print(f"Las ventas fueron:{mes[2]}")
print("Los meses de septiembre, octubre, noviembre y diciembre no tienen ventas")

Meses_mas_ventas=sorted(Meses_Ing_Ventas, key=lambda x:x[2], reverse=True) 
Meses_mas_ingresos=sorted(Meses_Ing_Ventas, key=lambda x:x[2], reverse=True) 

print(f"Los meses con más ventas fueron:")
for ventas in Meses_mas_ventas[0:3]:
    if ventas[0]==4:    
        print(f"Abril, con {ventas[2]} ventas")
    elif ventas[0]==1:    
        print(f"Enero, con {ventas[2]} ventas")
    elif ventas[0]==3:    
        print(f"Marzo, con {ventas[2]} ventas")

print(f"Los meses con más ingresos fueron:")
for ingresos in Meses_mas_ingresos[0:3]:
    if ingresos[0]==4:    
        print(f"Abril, con {ingresos[1]} de ingresos")
    elif ingresos[0]==1:    
        print(f"Enero, con {ingresos[1]} de ingresos")
    elif ingresos[0]==3:    
        print(f"Marzo, con {ingresos[1]} de ingresos")


Meses_menos_ventas=sorted(Meses_Ing_Ventas, key=lambda x:x[2]) 
Meses_menos_ingresos=sorted(Meses_Ing_Ventas, key=lambda x:x[2]) 

print(f"Los meses con menores ventas fueron:")
for ventas in Meses_menos_ventas[0:3]:
    if ventas[0]==8:    
        print(f"Agosto, con {ventas[2]} ventas")
    elif ventas[0]==6:    
        print(f"Junio, con {ventas[2]} ventas")
    elif ventas[0]==7:    
        print(f"Julio, con {ventas[2]} ventas")

print(f"Los meses con menores ingresos fueron:")
for ingresos in Meses_menos_ingresos[0:3]:
    if ingresos[0]==8:    
        print(f"Agosto, con {ingresos[1]} de ingresos")
    elif ingresos[0]==6:    
        print(f"Junio, con {ingresos[1]} de ingresos")
    elif ingresos[0]==7:    
        print(f"Julio, con {ingresos[1]} de ingresos")

print(f"En total, los meses representaron los siguientes porcentajes de venta total:")
for ingresos in Meses_Ing_Ventas:
    if ingresos[0]==1:    
        print(f"Enero, con {round(ingresos[1]/ingresos[2],2)} en promedio de ingresos/ventas")
    elif ingresos[0]==2:    
        print(f"Febrero, con {round(ingresos[1]/ingresos[2],2)} en promedio de ingresos/ventas")
    elif ingresos[0]==3:    
        print(f"Marzo, con {round(ingresos[1]/ingresos[2],2)} en promedio de ingresos/ventas")
    elif ingresos[0]==4:    
        print(f"Abril, con {round(ingresos[1]/ingresos[2],2)} en promedio de ingresos/ventas")
    elif ingresos[0]==5:    
        print(f"Mayo, con {round(ingresos[1]/ingresos[2],2)} en promedio de ingresos/ventas")
    elif ingresos[0]==6:    
        print(f"Junio, con {round(ingresos[1]/ingresos[2],2)} en promedio de ingresos/ventas")
    elif ingresos[0]==7:    
        print(f"Julio, con {round(ingresos[1]/ingresos[2],2)} en promedio de ingresos/ventas")
    elif ingresos[0]==8:    
        print(f"Agosto, con {round(ingresos[1]/ingresos[2],2)} en promedio de ingresos/ventas")

col_ingresos = [ingresos[1] for ingresos in Meses_mas_ingresos]
col_ventas = [ventas[2] for ventas in Meses_mas_ingresos]
Promedio_ing=sum(col_ingresos)/8
Promedio_ven=sum(col_ventas)/8
Promedio_ing_ventas=Promedio_ing/Promedio_ven

print(f"Los ingresos promedio mensuales por los meses que se vendió, fueron: {Promedio_ing}")
print(f"Las ventas promedio mensuales por los meses que se vendió, fueron: {round(Promedio_ven)}")
print(f"Los ingresos/ventas promedio mensuales por los meses que se vendió, fueron: {round(Promedio_ing_ventas,2)}")
    
# Dados los resultados pedidos, veremos ahora otros datos para 
# realizar un mejor análisis 
# Categorias por mes


categorizacion_meses_2={}

for par in id_fecha:
    id = par[0]
    _, mes, _ = par[1].split('/')
    mes=int(mes)
    if mes not in categorizacion_meses_2.keys():
        categorizacion_meses_2[mes] = []
    categorizacion_meses_2[mes].append(id)
    

Meses_Ing_Ventas_2=[]

for key in categorizacion_meses_2.keys():
    lista_mes = categorizacion_meses_2[key]
    suma_venta = 0
    for id_venta in lista_mes:
        indice = id_venta - 1
        info_venta = lifestore_sales[indice]
        id_product = info_venta[1]
        categoria = lifestore_products[id_product-1][3]
        ID_P = lifestore_products[id_product-1][0]
        precio = lifestore_products[id_product-1][2]
        calificacion=lifestore_sales[info_venta[0]-1][2]
        Busquedas=Busquedas_por_producto[id_product-1][3]
        Meses_Ing_Ventas_2.append([key, ID_P, categoria, precio, calificacion, Busquedas])


#Procesadores

Procesadores_Meses=[proces[0:6] for proces in Meses_Ing_Ventas_2 if proces[2]=="procesadores"]    
Meses_P=[proces[0] for proces in Meses_Ing_Ventas_2 if proces[2]=="procesadores"]    

meses_unicos=list(set(Meses_P))
def extractDigits(meses_list):
    return list(map(lambda el:[el], meses_list))
      
meses_unicos_list=extractDigits(meses_unicos)

suma_ind=0
suma_ingresos=0
Calificacion=0
Procesadores_Meses_1=[]
for mes in meses_unicos_list:
    for procesador in Procesadores_Meses:
        if mes[0]==procesador[0]:
            suma_ind+=1
            suma_ingresos+=procesador[3]
            Calificacion += procesador[4]
            Categoria=procesador[2]
        continue
    Procesadores_Meses_1.append([mes[0], suma_ind,suma_ingresos, Calificacion, Categoria])
    suma_ind=0
    suma_ingresos=0
    Calificacion=0
Calificacion_promedio=0
Procesadores_Meses_2=[]
for procesador in Procesadores_Meses_1:
    Calificacion_promedio=round(procesador[3]/procesador[1],2)
    Procesadores_Meses_2.append([procesador[0], procesador[1],procesador[2],procesador[4],
                                 Calificacion_promedio])
    
Stock_procesadores_prod=[[procesador[0], procesador[1], procesador[4], procesador[3]] for 
                         procesador in lifestore_products if procesador[3]=="procesadores"]    
Procesadores_Mayor_Stock=sorted(Stock_procesadores_prod, key=lambda x:x[2], reverse=True) 

Stock_procesadores=[procesador[4] for procesador in lifestore_products if procesador[3]=="procesadores"]
Stock_procesadores=sum(Stock_procesadores)
print(f"El stock de procesadores en suma es: {Stock_procesadores}")
print(f"Los procesadores con mayor cantidad de stock son: ")

for i in Procesadores_Mayor_Stock[0:5]:
    print(f"{i[1]} (id: {i[0]}) con {i[2]} en stock")


#audifonos

Audifonos_Meses=[proces[0:6] for proces in Meses_Ing_Ventas_2 if proces[2]=="audifonos"]    
Meses_A=[proces[0] for proces in Meses_Ing_Ventas_2 if proces[2]=="audifonos"]    

meses_unicos=list(set(Meses_A))
def extractDigits(meses_list):
    return list(map(lambda el:[el], meses_list))
      
meses_unicos_list=extractDigits(meses_unicos)

suma_ind=0
suma_ingresos=0
Calificacion=0
Audifonos_Meses_1=[]
for mes in meses_unicos_list:
    for Audifonos in Audifonos_Meses:
        if mes[0]==Audifonos[0]:
            suma_ind+=1
            suma_ingresos+=Audifonos[3]
            Calificacion += Audifonos[4]
            Categoria=Audifonos[2]
        continue
    Audifonos_Meses_1.append([mes[0], suma_ind,suma_ingresos,Calificacion, Categoria])
    suma_ind=0
    suma_ingresos=0
    Calificacion=0
    
Calificacion_promedio=0
Audifonos_Meses_2=[]
for Audifonos in Audifonos_Meses_1:
    Calificacion_promedio=round(Audifonos[3]/Audifonos[1],2)
    Audifonos_Meses_2.append([Audifonos[0], Audifonos[1], Audifonos[2],Audifonos[4],Calificacion_promedio])

Audifonos_prod=[[Audifonos[0], Audifonos[1], Audifonos[4], Audifonos[3]] for Audifonos in lifestore_products if Audifonos[3]=="audifonos"]    
Audifonos_Mayor_Stock=sorted(Audifonos_prod, key=lambda x:x[2], reverse=True) 

Stock_Audifonos=[Audifonos[4] for Audifonos in lifestore_products if Audifonos[3]=="audifonos"]
Stock_Audifonos=sum(Stock_Audifonos)
print(f"El stock de audifonos en suma es: {Stock_Audifonos}")
print(f"Los audifonos con mayor cantidad de stock son: ")

for i in Audifonos_Mayor_Stock[0:5]:
    print(f"{i[1]} (id: {i[0]}) con {i[2]} en stock")



#memorias_usb

USB_Meses=[proces[0:5] for proces in Meses_Ing_Ventas_2 if proces[2]=="memorias usb"]    
Meses_A=[proces[0] for proces in Meses_Ing_Ventas_2 if proces[2]=="memorias usb"]    

meses_unicos=list(set(Meses_A))
def extractDigits(meses_list):
    return list(map(lambda el:[el], meses_list))
      
meses_unicos_list=extractDigits(meses_unicos)

suma_ind=0
suma_ingresos=0
Calificacion=0
USB_Meses_1=[]
for mes in meses_unicos_list:
    for USB in USB_Meses:
        if mes[0]==USB[0]:
            suma_ind+=1
            suma_ingresos+=USB[3]
            Calificacion += USB[4]
            Categoria=USB[2]
        continue
    USB_Meses_1.append([mes[0], suma_ind,suma_ingresos,Calificacion, Categoria])
    suma_ind=0
    suma_ingresos=0
    Calificacion=0


USB_Meses_2=[]
for USB in USB_Meses_1:
    Calificacion_promedio=round(USB[3]/USB[1],2)
    USB_Meses_2.append([USB[0],USB[1],USB[2],USB[4],Calificacion_promedio])



USB_prod=[[USB[0], USB[1], USB[4], USB[3]] for USB in lifestore_products if USB[3]=="memorias usb"]    
USB_Mayor_Stock=sorted(USB_prod, key=lambda x:x[2], reverse=True) 

Stock_USB=[USB[4] for USB in lifestore_products if USB[3]=="memorias usb"]
Stock_USB=sum(Stock_USB)
print(f"El stock de audifonos en suma es: {Stock_USB}")
print(f"Los audifonos con mayor cantidad de stock son: ")

for i in USB_Mayor_Stock[0:5]:
    print(f"{i[1]} (id: {i[0]}) con {i[2]} en stock")

#Tarjetas madre

TM_Meses=[TM[0:5] for TM in Meses_Ing_Ventas_2 if TM[2]=="tarjetas madre"]    
Meses_A=[TM[0] for TM in Meses_Ing_Ventas_2 if TM[2]=="tarjetas madre"]    

meses_unicos=list(set(Meses_A))
def extractDigits(meses_list):
    return list(map(lambda el:[el], meses_list))
      
meses_unicos_list=extractDigits(meses_unicos)

suma_ind=0
suma_ingresos=0
Calificacion=0
TM_Meses_1=[]
for mes in meses_unicos_list:
    for TM in TM_Meses:
        if mes[0]==TM[0]:
            suma_ind+=1
            suma_ingresos+=TM[3]
            Calificacion += TM[4]
            Categoria=TM[2]
        continue
    TM_Meses_1.append([mes[0], suma_ind,suma_ingresos,Calificacion, Categoria])
    suma_ind=0
    suma_ingresos=0
    Calificacion=0

Calificacion_promedio=0
TM_Meses_2=[]
for TM in TM_Meses_1:
    Calificacion_promedio=round(TM[3]/TM[1],2)
    TM_Meses_2.append([TM[0], TM[1],TM[2],TM[4],Calificacion_promedio])

TM_prod=[[TM[0], TM[1], TM[4], TM[3]] for TM in lifestore_products if TM[3]=="tarjetas madre"]    
TM_Mayor_Stock=sorted(TM_prod, key=lambda x:x[2], reverse=True) 

Stock_TM=[TM[4] for TM in lifestore_products if TM[3]=="tarjetas madre"]
Stock_TM=sum(Stock_TM)
print(f"El stock de tarjetas madre en suma es: {Stock_TM}")
print(f"Las tarjetas madre con mayor cantidad de stock son: ")

for i in TM_Mayor_Stock[0:5]:
    print(f"{i[1]} (id: {i[0]}) con {i[2]} en stock")

#Bocinas

Bocinas_Meses=[bocinas[0:5] for bocinas in Meses_Ing_Ventas_2 if bocinas[2]=="bocinas"]    
Meses_A=[bocinas[0] for bocinas in Meses_Ing_Ventas_2 if bocinas[2]=="bocinas"]    

meses_unicos=list(set(Meses_A))
def extractDigits(meses_list):
    return list(map(lambda el:[el], meses_list))
      
meses_unicos_list=extractDigits(meses_unicos)

suma_ind=0
suma_ingresos=0
Calificacion=0
Bocinas_Meses_1=[]
for mes in meses_unicos_list:
    for Bocinas in Bocinas_Meses:
        if mes[0]==Bocinas[0]:
            suma_ind+=1
            suma_ingresos+=Bocinas[3]
            Calificacion += Bocinas[4]
            Categoria = Bocinas[2]
        continue
    Bocinas_Meses_1.append([mes[0], suma_ind,suma_ingresos,Calificacion, Categoria])
    suma_ind=0
    suma_ingresos=0
    Calificacion=0

Calificacion_promedio=0
Bocinas_Meses_2=[]
for Bocinas in Bocinas_Meses_1:
    Calificacion_promedio=round(Bocinas[3]/Bocinas[1],2)
    Bocinas_Meses_2.append([Bocinas[0], Bocinas[1],Bocinas[2],Bocinas[4],Calificacion_promedio])

Bocinas_prod=[[Bocinas[0], Bocinas[1], Bocinas[4], Bocinas[3]] for Bocinas in lifestore_products if Bocinas[3]=="bocinas"]    
Bocinas_Mayor_Stock=sorted(Bocinas_prod, key=lambda x:x[2], reverse=True) 

Stock_Bocinas=[Bocinas[4] for Bocinas in lifestore_products if Bocinas[3]=="bocinas"]
Stock_Bocinas=sum(Stock_Bocinas)
print(f"El stock de bocinas en suma es: {Stock_Bocinas}")
print(f"Las bocinas con mayor cantidad de stock son: ")

for i in Bocinas_Mayor_Stock[0:5]:
    print(f"{i[1]} (id: {i[0]}) con {i[2]} en stock")


#Discos Duros

DD_Meses=[DD[0:5] for DD in Meses_Ing_Ventas_2 if DD[2]=="discos duros"]    
Meses_A=[DD[0] for DD in Meses_Ing_Ventas_2 if DD[2]=="discos duros"]    

meses_unicos=list(set(Meses_A))
def extractDigits(meses_list):
    return list(map(lambda el:[el], meses_list))
      
meses_unicos_list=extractDigits(meses_unicos)

suma_ind=0
suma_ingresos=0
Calificacion=0
DD_Meses_1=[]
for mes in meses_unicos_list:
    for DD in DD_Meses:
        if mes[0]==DD[0]:
            suma_ind+=1
            suma_ingresos+=DD[3]
            Calificacion += DD[4]
            Categoria = DD[2]
        continue
    DD_Meses_1.append([mes[0], suma_ind,suma_ingresos,Calificacion, Categoria])
    suma_ind=0
    suma_ingresos=0
    Calificacion=0

Calificacion_promedio=0
DD_Meses_2=[]
for DD in DD_Meses_1:
    Calificacion_promedio=round(DD[3]/DD[1],2)
    DD_Meses_2.append([DD[0], DD[1],DD[2],DD[4],Calificacion_promedio])

DD_prod=[[DD[0], DD[1], DD[4], DD[3]] for DD in lifestore_products if DD[3]=="discos duros"]    
DD_Mayor_Stock=sorted(DD_prod, key=lambda x:x[2], reverse=True) 

Stock_DD=[DD[4] for DD in lifestore_products if DD[3]=="discos duros"]
Stock_DD=sum(Stock_DD)
print(f"El stock de discos duros en suma es: {Stock_DD}")
print(f"Los discos duros con mayor cantidad de stock son: ")

for i in DD_Mayor_Stock[0:5]:
    print(f"{i[1]} (id: {i[0]}) con {i[2]} en stock")

#Tarjetas de video

TV_Meses=[TV[0:5] for TV in Meses_Ing_Ventas_2 if TV[2]=="tarjetas de video"]    
Meses_A=[TV[0] for TV in Meses_Ing_Ventas_2 if TV[2]=="tarjetas de video"]    

meses_unicos=list(set(Meses_A))
def extractDigits(meses_list):
    return list(map(lambda el:[el], meses_list))
      
meses_unicos_list=extractDigits(meses_unicos)

suma_ind=0
suma_ingresos=0
Calificacion=0
TV_Meses_1=[]
for mes in meses_unicos_list:
    for TV in TV_Meses:
        if mes[0]==TV[0]:
            suma_ind+=1
            suma_ingresos+=TV[3]
            Calificacion += TV[4]
            Categoria=TV[2]
        continue
    TV_Meses_1.append([mes[0], suma_ind,suma_ingresos,Calificacion, Categoria])
    suma_ind=0
    suma_ingresos=0
    Calificacion=0
    
Calificacion_promedio=0
TV_Meses_2=[]
for TV in TV_Meses_1:
    Calificacion_promedio=round(TV[3]/TV[1],2)
    TV_Meses_2.append([TV[0], TV[1],TV[2],TV[4],Calificacion_promedio])

TV_prod=[[TV[0], TV[1], TV[4], TV[3]] for TV in lifestore_products if TV[3]=="tarjetas de video"]    
TV_Mayor_Stock=sorted(TV_prod, key=lambda x:x[2], reverse=True) 

Stock_TV=[TV[4] for TV in lifestore_products if TV[3]=="tarjetas de video"]
Stock_TV=sum(Stock_TV)
print(f"El stock de tarjetas de video en suma es: {Stock_TV}")
print(f"Las tarjetas de video con mayor cantidad de stock son: ")

for i in TV_Mayor_Stock[0:5]:
    print(f"{i[1]} (id: {i[0]}) con {i[2]} en stock")

#Pantallas

Pantallas_Meses=[Pantallas[0:5] for Pantallas in Meses_Ing_Ventas_2 if Pantallas[2]=="pantallas"]    
Meses_A=[Pantallas[0] for Pantallas in Meses_Ing_Ventas_2 if Pantallas[2]=="pantallas"]    

meses_unicos=list(set(Meses_A))
def extractDigits(meses_list):
    return list(map(lambda el:[el], meses_list))
      
meses_unicos_list=extractDigits(meses_unicos)

suma_ind=0
suma_ingresos=0
Calificacion=0
Pantallas_Meses_1=[]
for mes in meses_unicos_list:
    for Pantallas in Pantallas_Meses:
        if mes[0]==Pantallas[0]:
            suma_ind+=1
            suma_ingresos+=Pantallas[3]
            Calificacion += Pantallas[4]
            Categoria=Pantallas[2]
        continue
    Pantallas_Meses_1.append([mes[0], suma_ind,suma_ingresos,Calificacion, Categoria])
    suma_ind=0
    suma_ingresos=0
    Calificacion=0

Calificacion_promedio=0
Pantallas_Meses_2=[]
for Pantallas in Pantallas_Meses_1:
    Calificacion_promedio=round(Pantallas[3]/Pantallas[1],2)
    Pantallas_Meses_2.append([Pantallas[0], Pantallas[1],Pantallas[2],Pantallas[4],Calificacion_promedio])

Pantallas_prod=[[Pantallas[0], Pantallas[1], Pantallas[4], Pantallas[3]] for Pantallas in lifestore_products if Pantallas[3]=="pantallas"]    
Pantallas_Mayor_Stock=sorted(Pantallas_prod, key=lambda x:x[2], reverse=True) 

Stock_Pantallas=[Pantallas[4] for Pantallas in lifestore_products if Pantallas[3]=="pantallas"]
Stock_Pantallas=sum(Stock_Pantallas)
print(f"El stock de pantallas en suma es: {Stock_Pantallas}")
print(f"Las pantallas con mayor cantidad de stock son: ")

for i in Pantallas_Mayor_Stock[0:5]:
    print(f"{i[1]} (id: {i[0]}) con {i[2]} en stock")


Meses=Procesadores_Meses_2+Audifonos_Meses_2+USB_Meses_2+TM_Meses_2+Bocinas_Meses_2+DD_Meses_2+TV_Meses_2+Pantallas_Meses_2
Stock=Stock_procesadores_prod+Audifonos_prod+USB_prod+TM_prod+Bocinas_prod+DD_prod+TV_prod+Pantallas_prod
Audifonos_Sin_Ventas=[[categoria[1],categoria[0]] for categoria in Menores_ventas_Audifonos 
                      if categoria[3]==0]
Procesadores_Sin_Ventas=[[categoria[1],categoria[0]] for categoria in Menores_ventas_procesadores if categoria[3]==0]
USB_Sin_Ventas=[[categoria[1],categoria[0]] for categoria in Menores_ventas_USB if categoria[3]==0]
TM_Sin_Ventas=[[categoria[1],categoria[0]] for categoria in Menores_ventas_TM if categoria[3]==0]
Bocinas_Sin_Ventas=[[categoria[1],categoria[0]] for categoria in Menores_ventas_Boc if categoria[3]==0]
TV_Sin_Ventas=[[categoria[1],categoria[0]] for categoria in Menores_ventas_TV if categoria[3]==0]
Pantallas_Sin_Ventas=[[categoria[1],categoria[0]] for categoria in Menores_ventas_Pantallas if categoria[3]==0]
DD_Sin_Ventas=[[categoria[1],categoria[0]] for categoria in Menores_ventas_DD if categoria[3]==0]

Audifonos_Con_Ventas=[[categoria[1],categoria[0]] for categoria in Menores_ventas_Audifonos if categoria[3]!=0]
Procesadores_Con_Ventas=[[categoria[1],categoria[0]] for categoria in Menores_ventas_procesadores if categoria[3]!=0]
USB_Con_Ventas=[[categoria[1],categoria[0]] for categoria in Menores_ventas_USB if categoria[3]!=0]
TM_Con_Ventas=[[categoria[1],categoria[0]] for categoria in Menores_ventas_TM if categoria[3]!=0]
Bocinas_Con_Ventas=[[categoria[1],categoria[0]] for categoria in Menores_ventas_Boc if categoria[3]!=0]
TV_Con_Ventas=[[categoria[1],categoria[0]] for categoria in Menores_ventas_TV if categoria[3]!=0]
Pantallas_Con_Ventas=[[categoria[1],categoria[0]] for categoria in Menores_ventas_Pantallas if categoria[3]!=0]
DD_Con_Ventas=[[categoria[1],categoria[0]] for categoria in Menores_ventas_DD if categoria[3]!=0]

Productos_Sin_Ventas=Audifonos_Sin_Ventas+Procesadores_Sin_Ventas+USB_Sin_Ventas+TM_Sin_Ventas+Bocinas_Sin_Ventas+TV_Sin_Ventas+Pantallas_Sin_Ventas+DD_Sin_Ventas
Productos_Con_Ventas=Audifonos_Con_Ventas+Procesadores_Con_Ventas+USB_Con_Ventas+TM_Con_Ventas+Bocinas_Con_Ventas+TV_Con_Ventas+Pantallas_Con_Ventas+DD_Con_Ventas
Meses=Procesadores_Meses_2+Audifonos_Meses_2+USB_Meses_2+TM_Meses_2+Bocinas_Meses_2+DD_Meses_2+TV_Meses_2+Pantallas_Meses_2
Stock=Stock_procesadores_prod+Audifonos_prod+USB_prod+TM_prod+Bocinas_prod+DD_prod+TV_prod+Pantallas_prod

#import pandas as pd 

#Stock = pd.DataFrame(Stock, columns = ['id_prod', 'nombre_prod', 'stock', 'Categoria'])
# Meses = pd.DataFrame(Meses, columns=['Mes_Id', 'Ventas', 'Ingresos', 'Categoria', 'Calificación'])
# Productos_Sin_Ventas=pd.DataFrame(Productos_Sin_Ventas, columns = ['id_prod', 'Categoria'])
# Productos_Con_Ventas=pd.DataFrame(Productos_Sin_Ventas, columns = ['id_prod', 'Categoria'])
# Stock.to_excel("Stock1.xlsx", index=False)
# Meses.to_excel("Meses.xlsx", index=False)
# Productos_Sin_Ventas.to_excel("Productos_Sin_Ventas.xlsx", index=False)
# Productos_Con_Ventas.to_excel("Productos_Con_Ventas.xlsx", index=False)

#Vamos a ver que pasó con las ventas de los productos que más se vendieron en el año:
# Discos Duros, Memorias USB, Procesadores y tarjetas de video por mes

# Procesadores_Meses_P=[proces[0:6] for proces in Meses_Ing_Ventas_2 if proces[2]=="procesadores"]    
# DD_Meses_P=[DD[0:6] for DD in Meses_Ing_Ventas_2 if DD[2]=="discos duros"]    
# USB_Meses_P=[USB[0:6] for USB in Meses_Ing_Ventas_2 if USB[2]=="memorias usb"]    
# TV_Meses_P=[TV[0:6] for TV in Meses_Ing_Ventas_2 if TV[2]=="tarjetas de video"]    

# Productos_por_Mes=Procesadores_Meses_P+DD_Meses_P+USB_Meses_P+TV_Meses_P
# Productos_por_Mes=pd.DataFrame(Productos_por_Mes, columns = ['Mes', 'ID_Producto', 'Categoria', Precio', 'Calificacion', 'Busquedas']