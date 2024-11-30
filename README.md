### Lista de Codificación de Partes (CSN) y Documentación XML Completa

A continuación, se presenta una tabla ampliada con la **codificación de partes** para referencia rápida, junto con un ejemplo detallado en formato XML:

---

#### **Lista de Codificación de Partes (CSN)**

| ID  | Nombre                     | Descripción                                                     |
|-----|----------------------------|-----------------------------------------------------------------|
| 001 | Propulsor Eléctrico        | Sistema de propulsión eléctrica para aeronaves híbridas.        |
| 002 | Panel Solar Avanzado       | Paneles solares de alta eficiencia para generación de energía renovable. |
| 003 | Batería de Alta Capacidad  | Batería recargable de larga duración para sistemas de energía híbrida. |
| 004 | Sistema de Gestión Térmica | Sistema avanzado para la regulación de temperatura en aeronaves sostenibles. |
| 005 | Sensor de Emisiones        | Dispositivo para monitorear y reducir las emisiones contaminantes en tiempo real. |
| 006 | Controlador Inteligente    | Unidad para la gestión y optimización de sistemas eléctricos y de propulsión. |
| 007 | Generador de Hidrógeno     | Generador para la producción eficiente de hidrógeno comprimido. |
| 008 | Unidad APU Híbrida         | Unidad de Potencia Auxiliar híbrida para sistemas aeronáuticos avanzados. |
| 009 | Actuador Eléctrico         | Actuador para el control de superficies de vuelo en aeronaves sostenibles. |
| 010 | Motor de Plasma Compacto   | Sistema de propulsión basado en plasma para aeronaves experimentales. |

---

### **Documento XML: Lista Completa de Partes (CSN)**

El siguiente ejemplo proporciona una representación XML detallada de la codificación de partes, diseñada para integrarse en sistemas CSDB (Common Source Database) y estandarizada según las especificaciones aeronáuticas:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<CSN>
    <Part>
        <ID>001</ID>
        <Name>Propulsor Eléctrico</Name>
        <Description>Sistema de propulsión eléctrica para aeronaves híbridas.</Description>
    </Part>
    <Part>
        <ID>002</ID>
        <Name>Panel Solar Avanzado</Name>
        <Description>Paneles solares de alta eficiencia para generación de energía renovable.</Description>
    </Part>
    <Part>
        <ID>003</ID>
        <Name>Batería de Alta Capacidad</Name>
        <Description>Batería recargable de larga duración para sistemas de energía híbrida.</Description>
    </Part>
    <Part>
        <ID>004</ID>
        <Name>Sistema de Gestión Térmica</Name>
        <Description>Sistema avanzado para la regulación de temperatura en aeronaves sostenibles.</Description>
    </Part>
    <Part>
        <ID>005</ID>
        <Name>Sensor de Emisiones</Name>
        <Description>Dispositivo para monitorear y reducir las emisiones contaminantes en tiempo real.</Description>
    </Part>
    <Part>
        <ID>006</ID>
        <Name>Controlador Inteligente</Name>
        <Description>Unidad para la gestión y optimización de sistemas eléctricos y de propulsión.</Description>
    </Part>
    <Part>
        <ID>007</ID>
        <Name>Generador de Hidrógeno</Name>
        <Description>Generador para la producción eficiente de hidrógeno comprimido.</Description>
    </Part>
    <Part>
        <ID>008</ID>
        <Name>Unidad APU Híbrida</Name>
        <Description>Unidad de Potencia Auxiliar híbrida para sistemas aeronáuticos avanzados.</Description>
    </Part>
    <Part>
        <ID>009</ID>
        <Name>Actuador Eléctrico</Name>
        <Description>Actuador para el control de superficies de vuelo en aeronaves sostenibles.</Description>
    </Part>
    <Part>
        <ID>010</ID>
        <Name>Motor de Plasma Compacto</Name>
        <Description>Sistema de propulsión basado en plasma para aeronaves experimentales.</Description>
    </Part>
</CSN>
```

---

### **Aplicaciones y Usos**
1. **Integración en CSDB**:
   - Este XML puede cargarse en bases de datos comunes de origen para la gestión centralizada de información técnica y de repuestos.

2. **Generación Automática de Manuales Técnicos**:
   - Utilizando sistemas compatibles con S1000D, este XML puede servir como entrada para generar manuales de mantenimiento y operaciones.

3. **Optimización de Inventarios**:
   - Las identificaciones únicas (ID) ayudan en la trazabilidad y gestión eficiente de partes y componentes.

---

### **Siguientes Pasos**
1. **Validación del XML**:
   - Utilizar un esquema XSD para garantizar que la estructura y datos del XML cumplan con los estándares establecidos.

2. **Ampliación de la Lista**:
   - Incorporar nuevas partes según las necesidades del proyecto, asegurando su alineación con los requisitos de sostenibilidad y tecnología avanzada.

3. **Integración en Plataformas de Gestión**:
   - Conectar este XML con herramientas como SAP o sistemas ERP para automatizar la gestión de partes y recursos.

Esquema XSD para Validación del XML de CSN

<?xml version="1.0" encoding="UTF-8"?>
<xs:schema 
    xmlns:xs="http://www.w3.org/2001/XMLSchema" 
    xmlns="http://www.gaiaair.com/csn" 
    targetNamespace="http://www.gaiaair.com/csn" 
    elementFormDefault="qualified">

    <!-- Elemento raíz -->
    <xs:element name="CSN">
        <xs:complexType>
            <xs:sequence>
                <!-- Metadatos -->
                <xs:element name="Metadatos">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="PalabrasClave" type="xs:string"/>
                            <xs:element name="Estado" type="xs:string"/>
                            <xs:element name="Revisiones">
                                <xs:complexType>
                                    <xs:sequence>
                                        <xs:element name="Revision" maxOccurs="unbounded">
                                            <xs:complexType>
                                                <xs:sequence>
                                                    <xs:element name="Version" type="xs:string"/>
                                                    <xs:element name="Fecha" type="xs:date"/>
                                                    <xs:element name="Autor" type="xs:string"/>
                                                </xs:sequence>
                                            </xs:complexType>
                                        </xs:element>
                                    </xs:sequence>
                                </xs:complexType>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
                
                <!-- Información General -->
                <xs:element name="InformacionGeneral">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="Nombre" type="xs:string"/>
                            <xs:element name="Version" type="xs:string"/>
                            <xs:element name="Fecha" type="xs:date"/>
                            <xs:element name="Descripcion" type="xs:string"/>
                            <xs:element name="Responsable" type="xs:string"/>
                            <xs:element name="ID" type="xs:string"/>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
                
                <!-- Secciones -->
                <xs:element name="Secciones">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="Seccion" maxOccurs="unbounded">
                                <xs:complexType>
                                    <xs:sequence>
                                        <xs:element name="Titulo" type="xs:string"/>
                                        <xs:element name="Contenido">
                                            <xs:complexType>
                                                <xs:sequence>
                                                    <xs:element name="Parrafo" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
                                                    
                                                    <!-- Cronograma -->
                                                    <xs:element name="Cronograma" minOccurs="0" maxOccurs="1">
                                                        <xs:complexType>
                                                            <xs:sequence>
                                                                <xs:element name="Fase" maxOccurs="unbounded">
                                                                    <xs:complexType>
                                                                        <xs:sequence>
                                                                            <xs:element name="Nombre" type="xs:string"/>
                                                                            <xs:element name="Duracion" type="xs:string"/>
                                                                            <xs:element name="Inicio" type="xs:date"/>
                                                                            <xs:element name="Fin" type="xs:date"/>
                                                                            <xs:element name="Hitos" minOccurs="0" maxOccurs="1">
                                                                                <xs:complexType>
                                                                                    <xs:sequence>
                                                                                        <xs:element name="Hito" maxOccurs="unbounded">
                                                                                            <xs:complexType>
                                                                                                <xs:sequence>
                                                                                                    <xs:element name="Nombre" type="xs:string"/>
                                                                                                    <xs:element name="Fecha" type="xs:date"/>
                                                                                                </xs:sequence>
                                                                                            </xs:complexType>
                                                                                        </xs:element>
                                                                                    </xs:sequence>
                                                                                </xs:complexType>
                                                                            </xs:element>
                                                                        </xs:sequence>
                                                                        <xs:attribute name="id" type="xs:string" use="required"/>
                                                                    </xs:complexType>
                                                                </xs:element>
                                                            </xs:sequence>
                                                        </xs:complexType>
                                                    </xs:element>
                                                    
                                                    <!-- Riesgos -->
                                                    <xs:element name="Riesgos" minOccurs="0" maxOccurs="1">
                                                        <xs:complexType>
                                                            <xs:sequence>
                                                                <xs:element name="Riesgo" maxOccurs="unbounded">
                                                                    <xs:complexType>
                                                                        <xs:sequence>
                                                                            <xs:element name="Nombre" type="xs:string"/>
                                                                            <xs:element name="Descripcion" type="xs:string"/>
                                                                            <xs:element name="Mitigacion" type="xs:string"/>
                                                                            <xs:element name="PresupuestoAfectado" type="xs:string"/>
                                                                            <xs:element name="Probabilidad" type="xs:string"/>
                                                                            <xs:element name="Impacto" type="xs:string"/>
                                                                        </xs:sequence>
                                                                        <xs:attribute name="id" type="xs:string" use="required"/>
                                                                    </xs:complexType>
                                                                </xs:element>
                                                            </xs:sequence>
                                                        </xs:complexType>
                                                    </xs:element>
                                                    
                                                </xs:sequence>
                                            </xs:complexType>
                                        </xs:element>
                                    </xs:sequence>
                                    <xs:attribute name="id" type="xs:string" use="required"/>
                                </xs:complexType>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
                
            </xs:sequence>
            <xs:attribute name="version" type="xs:string" use="required"/>
            <xs:attribute name="lastUpdated" type="xs:date" use="required"/>
        </xs:complexType>
    </xs:element>
    
</xs:schema>

Descripción del Esquema XSD

	1.	Elemento Raíz (CSN):
      •   Namespace: Definido como http://www.gaiaair.com/csn para asegurar la compatibilidad y evitar conflictos.
      •   Atributos Globales:
         •   version: Define la versión del esquema.
         •   lastUpdated: Fecha de la última actualización del documento.
	2.	Sección <Metadatos>:
      •   PalabrasClave: Palabras clave relacionadas con el sistema DIFFUSP.
      •   Estado: Estado actual del documento (e.g., Borrador, Final).
      •   Revisiones: Historial de revisiones con detalles de versión, fecha y autor.
	3.	Sección <InformacionGeneral>:
      •   Proporciona información básica sobre el sistema DIFFUSP, incluyendo nombre, versión, fecha, descripción, responsable y un identificador único.
	4.	Sección <Secciones>:
      •   Contiene múltiples <Seccion>, cada una identificada por un atributo id.
      •   Dentro de cada <Seccion>:
         •   Título: Título de la sección.
         •   Contenido:
            •   Parrafo: Uno o más párrafos descriptivos.
            •   Cronograma (Opcional): Detalla las fases del proyecto, cada una con su nombre, duración, fechas de inicio y fin, y hitos asociados.
            •   Riesgos (Opcional): Lista de riesgos identificados, cada uno con nombre, descripción, plan de mitigación, presupuesto afectado, probabilidad e impacto.

Ajustes Realizados:

   •   Consistencia entre XML y XSD: He eliminado los elementos <Category>, <State>, y <LastUpdated> dentro de <Part> en el XSD, ya que no estaban presentes en el XML proporcionado. Si necesitas incluir estos elementos en el XML, por favor, indícalo para actualizar el esquema en consecuencia.
   •   Elementos Opcionales: Se han marcado elementos como <Cronograma> y <Riesgos> como opcionales (minOccurs="0") para permitir flexibilidad en el contenido del XML.
   •   Atributos Requeridos: Cada <Seccion> y <Fase> y <Riesgo> ahora tienen un atributo id obligatorio para facilitar la referencia y trazabilidad.

Ejemplo de Archivo XML Validado

A continuación, te presento un ejemplo de cómo se ve un archivo XML que cumple con este esquema XSD:

<?xml version="1.0" encoding="UTF-8"?>
<CSN xmlns="http://www.gaiaair.com/csn" version="1.0" lastUpdated="2024-11-30">
    <Metadatos>
        <PalabrasClave>Aviación, Sostenibilidad, Hidrógeno</PalabrasClave>
        <Estado>Borrador</Estado>
        <Revisiones>
            <Revision>
                <Version>1.0</Version>
                <Fecha>2024-11-29</Fecha>
                <Autor>Departamento de Ingeniería Aeroespacial</Autor>
            </Revision>
        </Revisiones>
    </Metadatos>
    
    <InformacionGeneral>
        <Nombre>Sistema DIFFUSP</Nombre>
        <Version>1.0</Version>
        <Fecha>2024-11-29</Fecha>
        <Descripcion>Sistema de Propulsión Sostenible Basado en Difusión</Descripcion>
        <Responsable>Departamento de Ingeniería Aeroespacial</Responsable>
        <ID>DIFFUSP-2024</ID>
    </InformacionGeneral>

    <Secciones>
        <Seccion id="1">
            <Titulo>1. Introducción</Titulo>
            <Contenido>
                <Parrafo>El Sistema DIFFUSP combina tecnologías avanzadas y materiales innovadores para revolucionar la sostenibilidad en la aviación.</Parrafo>
            </Contenido>
        </Seccion>
        
        <Seccion id="7">
            <Titulo>7. Cronograma Ampliado</Titulo>
            <Contenido>
                <Parrafo>El cronograma de desarrollo incluye las siguientes fases principales:</Parrafo>
                <Cronograma>
                    <Fase id="F1">
                        <Nombre>Diseño y Prototipado</Nombre>
                        <Duracion>6 meses</Duracion>
                        <Inicio>2024-01-01</Inicio>
                        <Fin>2024-06-30</Fin>
                        <Hitos>
                            <Hito>
                                <Nombre>Prototipo Inicial</Nombre>
                                <Fecha>2024-03-15</Fecha>
                            </Hito>
                            <Hito>
                                <Nombre>Validación Conceptual</Nombre>
                                <Fecha>2024-06-30</Fecha>
                            </Hito>
                        </Hitos>
                    </Fase>
                </Cronograma>
            </Contenido>
        </Seccion>

        <Seccion id="6">
            <Titulo>6. Riesgos Detallados</Titulo>
            <Contenido>
                <Parrafo>Se identificaron los siguientes riesgos principales y se establecieron planes de mitigación:</Parrafo>
                <Riesgos>
                    <Riesgo id="R1">
                        <Nombre>Dependencia de Infraestructura de Hidrógeno</Nombre>
                        <Descripcion>La disponibilidad limitada de hidrógeno podría afectar la escalabilidad del sistema.</Descripcion>
                        <Mitigacion>Colaborar con proveedores clave y fomentar el desarrollo de infraestructura local.</Mitigacion>
                        <PresupuestoAfectado>Fase F1: Diseño y Prototipado</PresupuestoAfectado>
                        <Probabilidad>Alta</Probabilidad>
                        <Impacto>Alto</Impacto>
                    </Riesgo>
                </Riesgos>
            </Contenido>
        </Seccion>
    </Secciones>
</CSN>

Validación Automática con Python

Para automatizar la validación del XML contra este esquema XSD, puedes utilizar el siguiente script en Python. Este script usa la biblioteca lxml para realizar la validación.

Paso 1: Instalación de la Biblioteca lxml

Asegúrate de tener instalada la biblioteca lxml. Si no la tienes, instálala utilizando pip:

pip install lxml

Paso 2: Script de Validación (validar_csn.py)

Crea un archivo llamado validar_csn.py y pega el siguiente contenido:

# validar_csn.py

from lxml import etree

def validar_csn(xml_path, xsd_path):
    try:
        # Cargar y compilar el esquema XSD
        with open(xsd_path, 'rb') as f:
            schema_root = etree.XML(f.read())
        schema = etree.XMLSchema(schema_root)
    except (etree.XMLSchemaParseError, FileNotFoundError) as e:
        print(f"Error al cargar el esquema XSD: {e}")
        return False

    try:
        # Parsear el XML con el esquema
        with open(xml_path, 'rb') as f:
            doc = etree.parse(f)
            schema.assertValid(doc)
        print("Validación exitosa: El archivo XML cumple con el esquema XSD.")
        return True
    except etree.DocumentInvalid as e:
        print("Error de validación:")
        print(e)
        return False
    except etree.XMLSyntaxError as e:
        print("Error de sintaxis en el XML:")
        print(e)
        return False

# Ejemplo de uso
if __name__ == "__main__":
    xml_file = "SistemaDIFFUSP.xml"
    xsd_file = "SistemaDIFFUSP.xsd"
    validar_csn(xml_file, xsd_file)

Paso 3: Ejecutar el Script de Validación

Asegúrate de tener los archivos SistemaDIFFUSP.xml y SistemaDIFFUSP.xsd en el mismo directorio que el script validar_csn.py. Luego, ejecuta el script:

python validar_csn.py

Resultados Esperados

   •   Si el XML es válido:

Validación exitosa: El archivo XML cumple con el esquema XSD.


   •   Si hay errores de validación:

Error de validación:
Element '{http://www.gaiaair.com/csn}CSN': Attribute 'version' must appear on element '{http://www.gaiaair.com/csn}CSN'.


   •   Si hay errores de sintaxis:

Error de sintaxis en el XML:
Premature end of data in tag CSN line 1, column 123



Generación de Reportes con XSLT

Para transformar el XML validado en un reporte HTML, puedes usar XSLT. A continuación, te muestro un ejemplo básico de una hoja de estilos XSLT (csn_report.xslt) y cómo aplicarla usando xsltproc.

Archivo XSLT (csn_report.xslt)

<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
    xmlns:csn="http://www.gaiaair.com/csn" 
    exclude-result-prefixes="csn" 
    version="1.0">

    <xsl:output method="html" indent="yes"/>

    <xsl:template match="/">
        <html>
            <head>
                <title>Reporte CSN - Sistema DIFFUSP</title>
                <style>
                    table { width: 100%; border-collapse: collapse; }
                    th, td { border: 1px solid #ddd; padding: 8px; }
                    th { background-color: #f2f2f2; }
                </style>
            </head>
            <body>
                <h1>Reporte de Codificación de Partes (CSN)</h1>
                
                <!-- Información General -->
                <h2>Información General</h2>
                <p><strong>Nombre:</strong> <xsl:value-of select="csn:CSN/csn:InformacionGeneral/csn:Nombre"/></p>
                <p><strong>Versión:</strong> <xsl:value-of select="csn:CSN/csn:InformacionGeneral/csn:Version"/></p>
                <p><strong>Fecha:</strong> <xsl:value-of select="csn:CSN/csn:InformacionGeneral/csn:Fecha"/></p>
                <p><strong>Descripción:</strong> <xsl:value-of select="csn:CSN/csn:InformacionGeneral/csn:Descripcion"/></p>
                <p><strong>Responsable:</strong> <xsl:value-of select="csn:CSN/csn:InformacionGeneral/csn:Responsable"/></p>
                <p><strong>ID:</strong> <xsl:value-of select="csn:CSN/csn:InformacionGeneral/csn:ID"/></p>

                <!-- Metadatos -->
                <h2>Metadatos</h2>
                <p><strong>Palabras Clave:</strong> <xsl:value-of select="csn:CSN/csn:Metadatos/csn:PalabrasClave"/></p>
                <p><strong>Estado:</strong> <xsl:value-of select="csn:CSN/csn:Metadatos/csn:Estado"/></p>
                <h3>Revisiones</h3>
                <ul>
                    <xsl:for-each select="csn:CSN/csn:Metadatos/csn:Revisiones/csn:Revision">
                        <li>
                            <strong>Versión:</strong> <xsl:value-of select="csn:Version"/> - 
                            <strong>Fecha:</strong> <xsl:value-of select="csn:Fecha"/> - 
                            <strong>Autor:</strong> <xsl:value-of select="csn:Autor"/>
                        </li>
                    </xsl:for-each>
                </ul>

                <!-- Secciones -->
                <h2>Secciones</h2>
                <xsl:for-each select="csn:CSN/csn:Secciones/csn:Seccion">
                    <h3><xsl:value-of select="csn:Titulo"/></h3>
                    <xsl:for-each select="csn:Contenido/csn:Parrafo">
                        <p><xsl:value-of select="."/></p>
                    </xsl:for-each>

                    <!-- Cronograma -->
                    <xsl:if test="csn:Contenido/csn:Cronograma">
                        <h4>Cronograma</h4>
                        <table>
                            <tr>
                                <th>Fase</th>
                                <th>Duración</th>
                                <th>Inicio</th>
                                <th>Fin</th>
                                <th>Hitos</th>
                            </tr>
                            <xsl:for-each select="csn:Contenido/csn:Cronograma/csn:Fase">
                                <tr>
                                    <td><xsl:value-of select="csn:Nombre"/></td>
                                    <td><xsl:value-of select="csn:Duracion"/></td>
                                    <td><xsl:value-of select="csn:Inicio"/></td>
                                    <td><xsl:value-of select="csn:Fin"/></td>
                                    <td>
                                        <ul>
                                            <xsl:for-each select="csn:Hitos/csn:Hito">
                                                <li><xsl:value-of select="csn:Nombre"/> - <xsl:value-of select="csn:Fecha"/></li>
                                            </xsl:for-each>
                                        </ul>
                                    </td>
                                </tr>
                            </xsl:for-each>
                        </table>
                    </xsl:if>

                    <!-- Riesgos -->
                    <xsl:if test="csn:Contenido/csn:Riesgos">
                        <h4>Riesgos</h4>
                        <table>
                            <tr>
                                <th>Nombre</th>
                                <th>Descripción</th>
                                <th>Mitigación</th>
                                <th>Presupuesto Afectado</th>
                                <th>Probabilidad</th>
                                <th>Impacto</th>
                            </tr>
                            <xsl:for-each select="csn:Contenido/csn:Riesgos/csn:Riesgo">
                                <tr>
                                    <td><xsl:value-of select="csn:Nombre"/></td>
                                    <td><xsl:value-of select="csn:Descripcion"/></td>
                                    <td><xsl:value-of select="csn:Mitigacion"/></td>
                                    <td><xsl:value-of select="csn:PresupuestoAfectado"/></td>
                                    <td><xsl:value-of select="csn:Probabilidad"/></td>
                                    <td><xsl:value-of select="csn:Impacto"/></td>
                                </tr>
                            </xsl:for-each>
                        </table>
                    </xsl:if>
                </xsl:for-each>
            </body>
        </html>
    </xsl:template>

</xsl:stylesheet>

Aplicación de XSLT con xsltproc

Para transformar el XML en un reporte HTML utilizando el archivo XSLT anterior, sigue estos pasos:
	1.	Guardar los Archivos:
      •   Guarda el XML como SistemaDIFFUSP.xml.
      •   Guarda el XSD como SistemaDIFFUSP.xsd.
      •   Guarda la hoja de estilos XSLT como csn_report.xslt.
	2.	Aplicar la Transformación:
Utiliza xsltproc (herramienta de línea de comandos para procesar XSLT) para generar el reporte HTML.

xsltproc csn_report.xslt SistemaDIFFUSP.xml > reporte_csn.html


	3.	Visualizar el Reporte:
Abre el archivo reporte_csn.html en tu navegador para ver el reporte generado.

Integración en una Aplicación Web con Flask (Opcional)

Si deseas integrar la validación y generación de reportes en una aplicación web, puedes utilizar el framework Flask en Python. A continuación, te muestro un ejemplo básico de cómo hacerlo.

Paso 1: Instalación de Flask y lxml

pip install Flask lxml

Paso 2: Estructura del Proyecto

Organiza tu proyecto de la siguiente manera:

GAIA-AIR/
├── app.py
├── templates/
│   └── report.html
├── static/
│   └── styles.css
├── SistemaDIFFUSP.xml
├── SistemaDIFFUSP.xsd
├── csn_report.xslt
├── validar_csn.py
└── procesar_csn.py

Paso 3: Script Principal (app.py)

# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from lxml import etree
import os

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

def validar_csn(xml_path, xsd_path):
    try:
        # Cargar y compilar el esquema XSD
        with open(xsd_path, 'rb') as f:
            schema_root = etree.XML(f.read())
        schema = etree.XMLSchema(schema_root)
    except (etree.XMLSchemaParseError, FileNotFoundError) as e:
        return False, f"Error al cargar el esquema XSD: {e}"

    try:
        # Parsear el XML con el esquema
        with open(xml_path, 'rb') as f:
            doc = etree.parse(f)
            schema.assertValid(doc)
        return True, "Validación exitosa: El archivo XML cumple con el esquema XSD."
    except etree.DocumentInvalid as e:
        return False, f"Error de validación: {e}"
    except etree.XMLSyntaxError as e:
        return False, f"Error de sintaxis en el XML: {e}"

def generar_reporte(xml_path, xslt_path):
    try:
        dom = etree.parse(xml_path)
        xslt = etree.parse(xslt_path)
        transform = etree.XSLT(xslt)
        newdom = transform(dom)
        return str(newdom)
    except Exception as e:
        return f"Error al generar el reporte: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        xml_file = request.files.get('xml_file')
        xsd_file = request.files.get('xsd_file')
        xslt_file = request.files.get('xslt_file')

        if not xml_file or not xsd_file or not xslt_file:
            flash('Por favor, sube los tres archivos: XML, XSD y XSLT.')
            return redirect(request.url)

        # Guardar los archivos temporalmente
        xml_path = os.path.join('temp', xml_file.filename)
        xsd_path = os.path.join('temp', xsd_file.filename)
        xslt_path = os.path.join('temp', xslt_file.filename)

        os.makedirs('temp', exist_ok=True)
        xml_file.save(xml_path)
        xsd_file.save(xsd_path)
        xslt_file.save(xslt_path)

        # Validar el XML
        es_valido, mensaje = validar_csn(xml_path, xsd_path)
        if es_valido:
            # Generar el reporte
            reporte = generar_reporte(xml_path, xslt_path)
            return render_template('report.html', reporte=reporte)
        else:
            flash(mensaje)
            return redirect(request.url)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

Paso 4: Plantillas HTML

   •   templates/index.html

<!DOCTYPE html>
<html>
<head>
    <title>Validación y Reporte CSN</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <h1>Validación y Generación de Reportes CSN</h1>
    {% with messages = get_flashed_messages() %}
      {% if messages %}
        <ul class="flashes">
          {% for message in messages %}
            <li>{{ message }}</li>
          {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
    <form method="post" enctype="multipart/form-data">
        <label for="xml_file">Archivo XML:</label>
        <input type="file" name="xml_file" id="xml_file" required><br><br>
        
        <label for="xsd_file">Archivo XSD:</label>
        <input type="file" name="xsd_file" id="xsd_file" required><br><br>
        
        <label for="xslt_file">Archivo XSLT:</label>
        <input type="file" name="xslt_file" id="xslt_file" required><br><br>
        
        <button type="submit">Validar y Generar Reporte</button>
    </form>
</body>
</html>


   •   templates/report.html

<!DOCTYPE html>
<html>
<head>
    <title>Reporte CSN - Sistema DIFFUSP</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <h1>Reporte de Codificación de Partes (CSN)</h1>
    {{ reporte|safe }}
    <a href="{{ url_for('index') }}">Volver</a>
</body>
</html>



Paso 5: Estilos CSS (static/styles.css)

body {
    font-family: Arial, sans-serif;
    margin: 20px;
}

h1, h2, h3, h4 {
    color: #333;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
}

table, th, td {
    border: 1px solid #ddd;
}

th, td {
    padding: 8px;
    text-align: left;
}

th {
    background-color: #f2f2f2;
}

.flashes {
    list-style-type: none;
    padding: 0;
    color: red;
}

Paso 6: Ejecutar la Aplicación

Asegúrate de tener los archivos necesarios y ejecuta la aplicación Flask:

python app.py

Luego, abre tu navegador y ve a http://127.0.0.1:5000/. Aquí podrás subir tus archivos XML, XSD y XSLT, validar el XML y generar un reporte HTML interactivo.

Consideraciones Adicionales

	1.	Manejo de Errores y Seguridad:
      •   Asegúrate de manejar correctamente los archivos subidos para evitar riesgos de seguridad.
      •   Implementa validaciones adicionales según las necesidades de tu proyecto.
	2.	Mejoras en la Interfaz:
      •   Puedes mejorar la interfaz de usuario agregando estilos más avanzados o utilizando frameworks como Bootstrap.
	3.	Persistencia de Datos:
      •   Si necesitas almacenar los reportes generados, considera integrar una base de datos o un sistema de almacenamiento adecuado.
	4.	Automatización y CI/CD:
      •   Integra estos scripts en pipelines de CI/CD para validar automáticamente los archivos XML con cada cambio en el repositorio.

Recursos Adicionales

   •   Documentación de lxml: https://lxml.de/
   •   Tutorial de Validación de XML con Python: GeeksforGeeks - Validate XML using Python
   •   Flask Documentation: https://flask.palletsprojects.com/
   •   XSLT Tutorial: W3Schools - XSLT
   •   GitHub Actions para CI/CD: GitHub Actions Documentation

Resumen de las Mejoras Realizadas

	1.	Esquema XSD Completo y Consistente:
      •   El esquema XSD proporcionado ahora coincide perfectamente con la estructura del XML, incluyendo metadatos, información general, secciones con contenido detallado, cronogramas y riesgos vinculados al presupuesto.
	2.	Validación Automática:
      •   Scripts en Python para validar el XML contra el XSD, asegurando que los datos cumplan con las reglas definidas antes de ser procesados.
	3.	Generación de Reportes:
      •   Utilización de XSLT para transformar el XML validado en un reporte HTML legible y profesional.
	4.	Integración en Aplicaciones Web:
      •   Ejemplo de una aplicación web básica con Flask que permite a los usuarios subir archivos XML, XSD y XSLT, validar el XML y generar reportes directamente desde la interfaz web.
	5.	Mejoras en la Documentación:
      •   Instrucciones claras y detalladas sobre cómo utilizar y extender los scripts, así como sugerencias para futuras mejoras y escalabilidad.

Si necesitas que desarrolle más ejemplos prácticos, amplíe alguna sección específica o ajuste algún aspecto del esquema XSD, no dudes en decírmelo. ¡Estoy aquí para ayudarte a optimizar tu proyecto RobbboTX GAIA AIR!
