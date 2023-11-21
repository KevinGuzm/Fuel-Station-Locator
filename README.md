# Fuel Station Locator Project in Colombia

This project is a fuel station locator application in Colombia. The application allows users to select a location and find the nearest fuel station. In addition, it provides information about fuel prices, allowing users to identify the cheapest and most expensive options.

## Data

The application uses open data from Colombia about fuel. These data are enriched with location coordinates of the stations through an API.

## Technologies

The application is built with several Python libraries, including:

- **Streamlit** for the user interface.
- **Pandas** for data handling.
- **Folium** for map visualization.
- **Shapely** for manipulation and analysis of planar geometric objects.
- **Haversine** for geographic calculations.

In addition, the application is packaged in a Docker container for easy deployment and distribution.

## Features

In the application, users can select a city and a central location, and then choose a type of fuel. The application then displays a map with fuel stations within a selected radius, marking the stations on the map and providing information about the prices of the selected fuel.

## Code

The project code includes several useful functions for working with geospatial data and creating the fuel station locator application. Some of these functions include:

- `GetLatLon2(Address,YOUR_API_KEY)`: Uses the HERE geocoding API to get the latitude and longitude of a given address.
- `cal_dist(geo_source,point2,unit)`: Calculates the distance between two geographic points using the Haversine formula.
- `distance_estac(geo_source,df,radio,unit)`: Calculates the distance between a geographic point and all fuel stations in a given DataFrame, and returns the stations that are within a given radius.
- `transform_df_map(df_temp)`: Transforms a DataFrame of fuel stations, converting the latitude and longitude columns into a column of geographic points.
- `marker_rest(df,mapa,unit,oil,icono)`: Adds markers to a Folium map for each fuel station in a given DataFrame.

## Docker

The project includes a Dockerfile that defines how the Docker container for the application is built. The Dockerfile specifies that the base image of the container is Python 3.8, installs the Python dependencies specified in the `requirements.txt` file, and configures Streamlit to run in a headless environment.

## Conclusion

This project is an excellent example of how open data and geolocation technologies can be used to create useful and practical applications for users. 


===================================================================================
# Proyecto de Localización de Estaciones de Combustible en Colombia

Este proyecto es una aplicación de localización de estaciones de combustible en Colombia. La aplicación permite a los usuarios seleccionar una ubicación y encontrar la estación de combustible más cercana. Además, proporciona información sobre los precios del combustible, permitiendo a los usuarios identificar las opciones más baratas y más caras.

## Datos

La aplicación utiliza datos abiertos de Colombia sobre el combustible. Estos datos se enriquecen con coordenadas de ubicación de las estaciones a través de una API.

## Tecnologías

La aplicación está construida con varias bibliotecas de Python, incluyendo:

- **Streamlit** para la interfaz de usuario.
- **Pandas** para el manejo de datos.
- **Folium** para la visualización de mapas.
- **Shapely** para la manipulación y análisis de objetos geométricos planos.
- **Haversine** para cálculos geográficos.

Además, la aplicación se empaqueta en un contenedor Docker para facilitar su despliegue y distribución.

## Funcionalidades

En la aplicación, los usuarios pueden seleccionar una ciudad y una ubicación central, y luego elegir un tipo de combustible. La aplicación entonces muestra un mapa con las estaciones de combustible dentro de un radio seleccionado, marcando las estaciones en el mapa y proporcionando información sobre los precios del combustible seleccionado.

## Código

El código del proyecto incluye varias funciones útiles para trabajar con datos geoespaciales y crear la aplicación de localización de estaciones de combustible. Algunas de estas funciones incluyen:

- `GetLatLon2(Address,YOUR_API_KEY)`: Utiliza la API de geocodificación de HERE para obtener la latitud y la longitud de una dirección dada.
- `cal_dist(geo_source,point2,unit)`: Calcula la distancia entre dos puntos geográficos utilizando la fórmula de Haversine.
- `distance_estac(geo_source,df,radio,unit)`: Calcula la distancia entre un punto geográfico y todas las estaciones de combustible en un DataFrame dado, y devuelve las estaciones que están dentro de un radio dado.
- `transform_df_map(df_temp)`: Transforma un DataFrame de estaciones de combustible, convirtiendo las columnas de latitud y longitud en una columna de puntos geográficos.
- `marker_rest(df,mapa,unit,oil,icono)`: Agrega marcadores a un mapa de Folium para cada estación de combustible en un DataFrame dado.

## Docker

El proyecto incluye un Dockerfile que define cómo se construye el contenedor Docker para la aplicación. El Dockerfile especifica que la imagen base del contenedor es Python 3.8, instala las dependencias de Python especificadas en el archivo `requirements.txt`, y configura Streamlit para ejecutarse en un entorno sin cabeza.

## Conclusión

Este proyecto es un excelente ejemplo de cómo se pueden utilizar los datos abiertos y las tecnologías de geolocalización para crear aplicaciones útiles y prácticas para los usuarios.
