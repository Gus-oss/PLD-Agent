# Transacciones de IBM para la lucha contra el blanqueo de capitales (AML)

## Descripción
El lavado de dinero es un problema multimillonario. La detección del blanqueo es muy difícil. La mayoría de los algoritmos automatizados tienen una alta tasa de falsos positivos: transacciones legítimas marcadas incorrectamente como lavado. Lo contrario también es un problema importante: los falsos negativos, es decir transacciones de lavado no detectadas. Naturalmente, los delincuentes trabajan duro para cubrir sus huellas.

El acceso a datos reales de transacciones financieras está muy restringido, tanto por razones de propiedad como de privacidad. Incluso cuando el acceso es posible, resulta problemático proporcionar una etiqueta correcta (blanqueo o legítima) a cada transacción, como se señaló anteriormente. Estos datos de transacciones sintéticas de IBM evitan estos problemas.

Los datos proporcionados aquí se basan en un mundo virtual habitado por individuos, empresas y bancos. Las personas interactúan con otras personas y empresas. Asimismo, las empresas interactúan con otras empresas y con particulares. Estas interacciones pueden adoptar muchas formas, por ejemplo: compra de bienes y servicios de consumo, órdenes de compra de suministros industriales, pago de salarios, reembolso de préstamos y más. Estas transacciones financieras generalmente se realizan a través de bancos, es decir tanto el pagador como el receptor tienen cuentas, y las cuentas adoptan múltiples formas, desde cheques hasta tarjetas de crédito y bitcoins.

Una (pequeña) fracción de los individuos y empresas del modelo generador participan en conductas delictivas, como el contrabando, el juego ilegal, la extorsión y más. Los delincuentes obtienen fondos de estas actividades ilícitas y luego intentan ocultar el origen de estos fondos ilícitos mediante una serie de transacciones financieras. Estas transacciones financieras para ocultar fondos ilícitos constituyen lavado de dinero. De esta forma, los datos disponibles aquí están etiquetados y pueden utilizarse para entrenar y probar modelos AML (Anti Lavado de Dinero) y para otros fines.

El generador de datos que creó los datos aquí no solo modela la actividad ilícita, sino que también rastrea los fondos derivados de la actividad ilícita a través de un número arbitrario de transacciones, creando así la capacidad de etiquetar las transacciones de lavado muchos pasos más allá de su fuente ilícita. Con esta base, es sencillo para el generador etiquetar transacciones individuales como lavado o legítimas.

Tenga en cuenta que este generador de IBM modela todo el ciclo de lavado de dinero:
- Colocación: Fuentes como el contrabando de fondos ilícitos
- Capas: Mezclar los fondos ilícitos con el sistema financiero.
- Integración: Gastar los fondos ilícitos.

Como otra capacidad posible sólo con datos sintéticos, tenga en cuenta que un banco real u otra institución normalmente tiene acceso sólo a una parte de las transacciones involucradas en el lavado: las transacciones que involucran a ese banco. No se ven transacciones que ocurren en otros bancos o entre otros bancos. Por lo tanto, los modelos construidos sobre transacciones reales de una institución sólo pueden tener una visión limitada del mundo.

Por el contrario, estas transacciones sintéticas contienen todo un ecosistema financiero. Por lo tanto, puede ser posible crear modelos de detección de lavado que comprendan la amplia gama de transacciones entre instituciones, pero aplicar esos modelos para hacer inferencias sólo sobre transacciones en un banco en particular.

Como otro punto de referencia, IBM publicó previamente datos de una versión muy temprana de este generador de datos:
https://ibm.box.com/v/AML-Anti-Money-Laundering-Data

El generador se ha vuelto significativamente más robusto desde que se publicaron los datos anteriores, y estas transacciones reflejan un realismo mejorado, correcciones de errores y otras mejoras en comparación con la versión anterior.

Los datos de transacciones con tarjeta de crédito etiquetados para fraude y creados con un generador relacionado también están disponibles en Kaggle:
https://www.kaggle.com/datasets/ealtman2019/credit-card-transactions

## Contenido
Aquí publicamos 6 conjuntos de datos divididos en dos grupos de tres:
- El grupo HI tiene una tasa de tráfico ilícito relativamente más alta (más lavado de dinero).
- El grupo LI tiene un ratio ilícito relativamente menor (menos blanqueo).

El objetivo es soportar un amplio grado de recursos computacionales y de modelado. Todos estos conjuntos de datos son independientes, por ejemplo. Los conjuntos de datos pequeños no son un subconjunto de los conjuntos de datos medianos. Sin embargo, cada uno de los seis conjuntos de datos individuales se puede subdividir cronológicamente para entrenar, validar y probar. Hemos descubierto que una división del 60%/20%/20% es efectiva y alentamos a otros a seguir esta división.

Esta tabla tiene algunas estadísticas adicionales sobre los seis conjuntos de datos:

```
..                                  SMALL           MEDIUM           LARGE
..                                  HI     LI        HI      LI       HI       LI
.. Date Range HI + LI (2022)         Sep 1-10         Sep 1-16        Aug 1 - Nov 5
.. # of Days Spanned                 10     10        16      16       97       97
.. # of Bank Accounts               515K   705K     2077K   2028K    2116K    2064K
.. # of Transactions                  5M     7M       32M     31M      180M    176M
.. # of Laundering Transactions     5.1K   4.0K       35K     16K      223K    100K
.. Laundering Rate (1 per N Trans)  981   1942       905    1948       807     1750
```

Tenga en cuenta que el "Rango de fechas" proporcionado es el período "principal" de la actividad de transacción. En la discusión, Marco Pianta observó que hay algunas transacciones posteriores al período de fecha especificado y que todas esas transacciones son lavado de dinero. 

Finalmente, proporcionamos dos archivos para cada uno de los seis conjuntos de datos:
- Una lista de transacciones en formato CSV
- Una lista de archivos de texto de transacciones de lavado que siguen uno de los 8 patrones particulares introducidos por Suzumura y Kanezashi en su simulador AMLSim (https://github.com/IBM/AMLSim).

Observamos que no todo el lavado de datos sigue uno de estos 8 patrones. Al igual que con otros aspectos de estos datos mencionados anteriormente, conocer todas las transacciones involucradas en patrones de lavado particulares es un desafío inmenso con datos reales.

Aquí hay una lista de los 12 archivos proporcionados:

1a. Transacciones HI-Small_Trans.csv 1b. Transacciones de patrones de lavado HI-Small_Patterns.txt
2a. Transacciones HI-Medium_Trans.csv 2b. Transacciones de patrones de lavado HI-Medium_Patterns.txt
3a. Transacciones HI-Large_Trans.csv 3b. Transacciones de patrones de lavado HI-Large_Patterns.txt
4a. Transacciones LI-Small_Trans.csv 4b. LI-Small_Patterns.txt Trans acciones de patrones de lavado
5a. Transacciones LI-Medium_Trans.csv 5b. LI-Medium_Patterns.txt Transacciones de patrones de lavado
6a. Transacciones LI-Large_Trans.csv 6b. LI-Large_Patterns.txt Transacciones de patrones de lavado


## Bibliografia

https://www.kaggle.com/datasets/ealtman2019/ibm-transactions-for-anti-money-laundering-aml/data
