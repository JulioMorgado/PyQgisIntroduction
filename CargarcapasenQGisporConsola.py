# Cargar capas en QGis por medio de la consola de Python

# Se tiene dos formas de cargar las capas 
#Primer caso
#Se ingresa por medio de la interface con la key "iface"

#from hashlib import new


iface.addVectorLayer(path, nombre, key) #key en el caso de los shapes es ogr
#Se puede cargar la capa cuantas veces sea necesario


#Segundo caso
#Se entra por medio de un proyecto instanciado
#Se instancia el proyecto a la variable pry
pry =  QgsProject.instance()
#Se llaman a las capas
sett = QgsVectorLayer(r"D:\CentroGEO\Cuatrimestres\5to_cuatrimestre\7Ucrania_Mariupol\shape\official_ukraine_administrative_boundary_shapefile\SETTLEMENT.shp")
pry.addMapLayer(sett)
sett.setName("Asentamientos Ucrania")


#Se creó la variable can, para acceder a los atributos de mapCanvas
can = iface.mapCanvas()

#Accediendo a los campos entidades y geometrías
#Para acceder a los campos se debe de generr la variable para ello 
#por medio de un getFeatures
settfet = sett.getFeatures()
#Para obtener en número de atributos
len(list(settfet))

#Para acceder a los campos 
settfld = sett.fields()
len(settfld)

for i in settfld:
    i.name()



#Para trabajar con sus geometrías
sett.geometryType()


#Para convertir un iterador en una lista
listsett = list(settfet)
listsett[34]
listsett[34].geometry().asWtk()


#Crear capa de puntos temporales (memory)
sett = iface.activeLayer()
settcentro = sett.extent().center()
uri = "point?crs=EPSG:4326&field=id:integer"
newshp = QgsVectorLayer(uri, "Centro Ucrania", "memory")
entidad = QgsFeature()
entidad.setFields(sett.fields())
geom = QgsGeometry().fromPointXY(settcentro)
newshp.dataProvider().addAttributes(sett.fields())
newshp.isValid()
entidad.setGeometry(geom)
newshp.dataProvider().addFeatures([entidad])
QgsProject.instance().addMapLayer(newshp)





#Creando capas de líneas
#Crea una línea de 
def line_center():
    sett = iface.activeLayer()
    rios = iface.mapCanvas().layer(1)
    zonas = iface.mapCanvas().layer(2)
    puntosc = [sett.extent().center(), rios.extent().center(), zonas.extent().center()]

    uri = "linestring?crs=EPSG:4326&field=id:integer"
    capal = QgsVectorLayer(uri, "Center_line" "memory")
    capal.dataProvider().addAttributes(sett.fields())
    capal.updateFields()

    entidad = QgsFeature()
    entidad.setFields(capal.fields())
    geom = QgsGeometry().fromPolylineXY(puntosc)
    entidad.setGeometry(geom)
    capal.dataProvider().addFeatures([entidad])

    QgsProject.instance().addMapLayer(capal)





#Creando capas de polígonos
def polygon_center():
    sett = iface.activeLayer()
    rios = iface.mapCanvas().layer(1)
    zonas = iface.mapCanvas().layer(2)
    puntosc = [sett.extent().center(), rios.extent().center(), zonas.extent().center()]

    uri = "polygon?crs=EPSG:4326&field=id:integer"
    capal = QgsVectorLayer(uri, "Center_polygon", "memory")
    capal.dataProvider().addAttributes(sett.fields())
    capal.updateFields()

    entidad = QgsFeature()
    entidad.setFields(capal.fields())
    geom = QgsGeometry().fromPolygonXY([puntosc])
    entidad.setGeometry(geom)
    capal.dataProvider().addFeatures([entidad])

    QgsProject.instance().addMapLayer(capal)
