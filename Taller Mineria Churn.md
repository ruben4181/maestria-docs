  
  

# Taller Minería de Datos - Rubén Dario Vargas Yandy

## Churn Dataset

### 0. Preprocesamiento de datos:

Primeramente se abre el archivo en formato xlsx directamente en Excel, para darle un vistazo a los datos y encontrar relación entre los enunciados del apéndice y los nombres de las columnas.

  

![enter image description here](https://raw.githubusercontent.com/ruben4181/maestria-docs/refs/heads/main/mineria-datos-2025/figure_1_1.png)

*Figura 0.1: Previsualización en Excel*

  

Se procede a hacer la importación del dataset a AI Studio. En esta parte se presentaron problemas en el reconocimiento de la metadata del archivo arff, por lo que se obtó por usar la versión xlsx de este dataset.

  

En primer lugar, se elimina la columna de teléfono, que es un identificador pseudo-aleatorio, dado que fue asignado arbitrariamente en un principio y no demuestra ningún tipo de cualidad específica del cliente.

  

Después se continúa con la conversión de datos categóricos a numéricos. Se utiliza el método "dummy coding" para las columnas "State" y "Area Code". Para las columnas "Intern Plan" y "VoiceMail Plan" se mapean los valores "yes" y "no" por "1" y "0", dado que por defecto estos valores quedan nominales también, se hace, justo después, un paseo de estas dos columnas mencionadas anteriormente.

  

Consecuentemente, se normalizan las columnas no categóricas, que vendrían siendo las relacionadas con la información de consumo del servicio de telecomunicaciones. El diseño del *preprocesamiento* se encuentra en la figura 0.2, a continuación:

  

![enter image description here](https://github.com/ruben4181/maestria-docs/blob/main/mineria-datos-2025/figure_1_2.png?raw=true)

*Figura 0.2: Diseño preprocesamiento*

  

### 1. Análisis exploratorio:

1) Para el análisis inicial, primeramente se verifica que las variables a tomar en cuenta tengan una distribución adecuada (lo más similar posible a la distribución normal), con fines prácticos se hacen exploraciones visuales con histogramas, las cuales arrojan las variables de tipo continuo con está distribución, si bien es un análisis visual, basta para el alcance de este taller. Después, con ayuda del operador *Correlation Matrix* de *RapidMiner*, como se puede apreciar en la *Figura 1.1* y *Figura 1.2*, existen varias correlaciones evidentes a priori, como lo son la correlación entre los minutos gastados, en cualquier segmentación horaria, con los cargos aplicados a dicho espacio de tiempo, porque, de hecho, lo más común en este tipo de planes de telecomunicación, es que el cálculo de estos cargos se haga multiplicando la cantidad de minutos gastados por alguna constante, es decir, que sea una función lineal la que obtiene ese resultado. Otro valor de correlación fuerte, que se podría esperar con anticipación, es que las personas que tengan activo el plan con *Voice Mail* realizan más de estas operaciones que los que no. Ya que se optó en el preprocesamiento de usar *dummy codding* para el paso de variables nominales a númericas, no es posible agregar toda la tabla con los valores de la matriz de correlación en la *Figura 1.2*, sin embargo, en la *Figura 1.3*, se organizó cada relación para cada par de variables, en orden de mayor a menor y, obviando las perfectamente relacionadas positivamente, se pudo apreciar que *Churn* tiene como mayor correlación la variable que representa el plan internacional, junto con otras como el total de minutos en los diferentes lapsos de tiempo, sin embargo son correlaciones débiles. Por último, estas correlaciones pueden ser débiles porque el conjunto de datos está desbalanceado.

  

![enter image description here](https://github.com/ruben4181/maestria-docs/blob/main/mineria-datos-2025/figure_0_1.png?raw=true)

*Figura 1.1*

![enter image description here](https://github.com/ruben4181/maestria-docs/blob/main/mineria-datos-2025/figure_0_2.png?raw=true)

*Figura 1.2*

![enter image description here](https://github.com/ruben4181/maestria-docs/blob/main/mineria-datos-2025/figure_0_3.png?raw=true)

  

2) De los campos posibles a ser eliminados, se tomó la decisión de solamente eliminar el campo teléfono, por el hecho de que es de origen arbitrario y no aporta información de la condición o de los hábitos de consumo del cliente. En su momento se considero eliminar variables correlacionadas directamente, como por ejemplo la cantidad de llamadas en el transcurso del día y/o el cargo por el uso de estos, sin embargo, no fueron eliminados porque se consideró que los usuarios podrían cambiarse de operador porque sus precios alcanzaban algún tope o que los usuarios que más llaman, en zonas donde la cobertura presenta algún tipo de problema por concurrencia, etc..., serían más notorios para usuarios más frecuentes, que para usuarios más casuales.

  

3) Se seleccionan los atributos Churn e Intern Plan, además de la conversión de Churn, de nominal a numéricos, reemplazando TRUE por 1 y FALSE por 0, para después filtrar todo el dataset en las cuatro posibles combinaciones requeridas en este literal, que son las siguientes con sus respectivos resultados.

* Inter Plan = 1 AND Churn = 1 (Usuario con plan internacional y que se cambió de operador).

* Inter Plan = 1 AND Churn = 0 (Usuario con plan internacional que NO se cambió de operador)

* Inter Plan = 0 AND Churn = 1 (Usuario sin plan internacional que se cambió de operador)

* Inter Plan = 0 AND Churn = 0 (Usuario sin plan internacional que NO se cambió de operador).

**Diseño en RapidMiner:**

El diseño del proceso cuenta con la selección de atributos, para no cargar el resultado de información innecesaria. Continua con el filtro por cada una de las condiciones anteriores, cuyas comparaciones dependían de si el usuario tenía o no plan internacional, así que se procede con el conteo de estas mismas según las condiciones expuestas anteriormente en este punto. Se termina por el renombre de los dos resultados para que la generación de las gráficas sean mucho más sencilla y se unen mediante un ID genérico para tener la información en una sola fila. El proceso se realiza dos veces, primero para Intern Plan = 1 y después Intern Plan = 0, el diseño es igual, excepto en la condición de los filtros y en el renombre de las variables. Este proceso se ilustra en la *Figura 3.1*.

![enter image description here](https://github.com/ruben4181/maestria-docs/blob/main/mineria-datos-2025/figure_3_1.png?raw=true)

*Figura 3.1: Diseño Inter Plan vs Churn*

  

**Intern Plan = 1 (Usuarios con plan internacional)**

Para estas condiciones se obtuvieron como resultado una proporción a primera vista diferente, entre los dos grupos de usuarios con plan internacional, es decir, los que se cambiaron y los que no. Con un total de 323 usuarios con plan internacional, un porcentaje de 42.41% de usuarios que con plan internacional se cambiaron de operador y un 57.59% restante de usuarios que con plan internacional no se cambiaron de operador. Los totales los podemos apreciar en la *Figura 3.1.1* y en la *Figura 3.1.2*, siendo la *Figura 3.1.2* la que más permite apreciar la diferencia entre ambas.

![enter image description here](https://github.com/ruben4181/maestria-docs/blob/main/mineria-datos-2025/intern_plan_1_table.png?raw=true)

*Figura 3.1.1*

  

![enter image description here](https://github.com/ruben4181/maestria-docs/blob/main/mineria-datos-2025/intern_plan_1_bar.png?raw=true)

*Figura 3.1.2*

  

**Intern Plan = 0 (Usuarios sin plan internacional) **

En el caso de los usuarios sin plan internacional, la variación de un grupo con otro es mucho mayor con respecto a los usuarios con plan internacional. Los usuarios sin plan internacional, que corresponde a un total de 3010, que no se cambiaron son, aproximadamente 88.50%, mientras que los que si se cambiaron representan el 11.50% restante. La *Figura 3.1.3* y *

![enter image description here](https://github.com/ruben4181/maestria-docs/blob/main/mineria-datos-2025/inter_plan_0_table.png?raw=true)

*Figura 3.1.3*

  

![enter image description here](https://github.com/ruben4181/maestria-docs/blob/main/mineria-datos-2025/inter_plan_0_bar.png?raw=true)

*Figura 3.1.4*

  

**Conclusiones:**

Lo primero que se puede concluir de este análisis exploratorio, es que el dataset presenta un desbalance entre usuarios con Churn y sin Churn, esto puede ser porque este fenómeno no es muy común, aunque si significativo. Ahora bien, también es evidente que hay una mayor cantidad de usuarios, en proporción, que teniendo plan internacional, toman la decisión de cambiarse de operador, que las que no tienen dicho plan (**42.41%** vs **11.50%**)

  

4) Para los puntos 4, 5 y 6 se asumirá que la distribución de las variables, individualmente tiene una distribución normal y así poder usar la matriz de correlación como herramienta de apoyo. La matriz de correlación se puede apreciar en en la *Figura 4.1*. Correspondiente al punto 4, que intenta descifrar si existe una correlación entre la cantidad de llamadas y Churn, se observa que existe una correlación de 0.209 entre *CutServ Call* y *Churn*, lo que, de acuerdo a lo comúnmente aceptado en la literatura estadística, es una correlación positiva debía, es decir, existe algo de correlación entre las dos variables, pero no la suficiente como para tenerla en cuenta. Sin embargo, esto no implica que esta variable, en conjunto con otras, no representen una correlación moderada o fuerte. El proceso usado para los puntos 1.4, 1.5 y 1.6 está en la *Figura 4.2*

![enter image description here](https://github.com/ruben4181/maestria-docs/blob/main/mineria-datos-2025/figure_4_1.png?raw=true)

*Figura 4.1: Matriz de correlación variables puntos 1.4, 1.5 y 1.6*

  

![enter image description here](https://github.com/ruben4181/maestria-docs/blob/main/mineria-datos-2025/figure_4_2.png?raw=true)

*Figura 4.2: Proceso generación de matriz de correlación puntos 1.4, 1.5 y 1.6*

  

5) Con una relación de 0.205 (*Vease Figura 4.1*), entre el total de minutos durante el día y *Churn*, se puede concluir lo mismo del punto 1.4, existe una correlación positiva débil.

  

6) Para este caso, la correlación entre los minutos de llamadas en la tarde y *Churn* es tan baja, 0.093 (*Vease Figura 4.2*), se puede concluir que no hay relación entre estas variables.

  

7) Para este punto se utilizará la *Figura 1.1*, en la que es posible notar que *Churn* NO tiene una correlación fuerte con ninguna variable de manera individual, existen correlaciones pero son menores a 0.4, tanto positivas como negativas.

  

8) Resumén de hallazgos *Figura 8.1*

![enter image description here](https://github.com/ruben4181/maestria-docs/blob/main/mineria-datos-2025/figure_8_1.png?raw=true)

*Figura 8.1*

  

9) No se realiza el punto

  

10) Analizando como afectan De acuerdo a la *Figura 10.1* y teniendo en cuenta que el conjunto de datos **esta desbalanceado con más usuarios que NO hicieron *Churn***, se aprecia que después de la cuarta llamada hay más puntos verdes que azules, lo que indica que si hay un patrón con esa variable y *Churn*, también que después de la 4ta llamada los minutos de los usuarios se vieron afectados disminuyendo. Sin embargo, en conjunto no pareciese que afectan directamente, dado que en las primeras 3 llamadas también hubo muchos puntos verdes (Usuarios que cambiaron de proveedor). Como conclusión, después de la 4ta llamada existe un patrón, pero para nada es concluyente, porque el *Churn* se presenta en todas las étapas de los usuarios que llaman al servicio de cliente y también cuando hay más o menos minutos durante el día.

![enter image description here](https://github.com/ruben4181/maestria-docs/blob/main/mineria-datos-2025/figure_10_1.png?raw=true)

*Figura 10.1*

  

11) En este par de variables (*Total day minutes* y *Total evening min*) los valores están dispersos sin presentar clusters de puntos evidentes para ninguno de los dos colores (*Churn*). Cuando crecen los minutos en el día y los minutos en la tarde, hay más puntos verdes, pero también muchos azules (NO *Churn*). Como conclusión, más hacia la derecha y hacia arriba parece que existe un cluster de puntos, pero no es una afirmación trivial el decir que existe en esa zona una agrupación de puntos de algún color.

![enter image description here](https://github.com/ruben4181/maestria-docs/blob/main/mineria-datos-2025/figure_11_1.png?raw=true)

*Figura 11.1*

  

### Árbol de decisiones:

Se realiza el diseño de un árbol de decisiones, con las variables seleccionadas, sin normalizar, dado que este tipo de modelos no requiere que los valores estén normalizados y no afectan su desempeño. Fue entrenado con una muestra balanceada de 400 elementos por cada clase (*Churn* = TRUE, *Churn* = FALSE) Los resultados en las métricas de rendimiento del módelo están representados en la *Figura 12.1*, el árbol de decisión generado está en la *Figura 12.2* y los diseños están en las figuras 12.3 y 12.4.

  

12) 

![enter image description here](https://github.com/ruben4181/maestria-docs/blob/main/mineria-datos-2025/figure_12_1.png?raw=true)
*Figura 12.1: Métricas Árbol de decisiones*

  

![enter image description here](https://github.com/ruben4181/maestria-docs/blob/main/mineria-datos-2025/figure_12_2.png?raw=true)

*Figura 12.2: Árbol de decisión generado en RapidMiner*

![enter image description here](https://github.com/ruben4181/maestria-docs/blob/main/mineria-datos-2025/figure_12_3.png?raw=true)

*Figura 12.3: Diseño implementación RapidMiner Árbol de decisión*

  

![enter image description here](https://github.com/ruben4181/maestria-docs/blob/main/mineria-datos-2025/figure_12_4.png?raw=true)

*Figura 12.4: Diseño subproceso Cross Validation - Árbol de decisiones*

  

Al balancear el conjunto de datos con un 50% y 50% para ambas clases, usando una medida de Performance Binomial, se obtuvieron unos resultados bastante aceptables. El *class-precision* que ayuda a medir que las predicciones sean buena calidad y, para ejemplos de este problema en cuestión, no tomar la decisión de darle beneficios a usuarios que no se iban a ir, tuvo un rendimiento para ambas clases de más de 75%, como se observa en la *Figura 12.1*. Ahora bien, la otra métrica que aporta información de usuarios que piensan abandonar el operado, *class-recall*, entregó un rendimiento también de más de más de 75% en ambas clases. Si bien el rendimiento de la clase de más relevancia (*Churn = TRUE*) son las de menor porcentaje, siguen estando por encima de 75%, que es muy buena de acuerdo a la literatura.

**Comparación con anterior sección:** Si bien en el punto anterior se determinó que las variables no tenían una correlación directa, ninguna, con el label *Churn*, al balancear las clases el Árbol de decisión encontró caminos que dieron buenos resultados, lo que nos implica que el desbalanceo pudo haber jugado un papel determinante en el resultado final del Análisis exploratorio, y que tal vez si se hubiesen balanceado las clases antes de hacer el análisis exploratorio, hubiese sido más evidente la relación de los atributos con el atributo objetivo o *label*.

  

13) Las métricas por defecto que trae el operador *Performance* en RapidMiner, presentes en la tabla de la *Figura 12.1* son bastante útiles en este caso, porque tienen la medición general del modelo, el *class-recall* y *class-precision* de este mismo. El *class-recall* es de vital importancia en este modelo porque las personas que se van, son un grupo minoritario en el *dataset*, además, son las que más importan en este proceso porque son usuarios potencialmente perdibles para la empresa y, no solo eso, que se van directamente a la competencia, lo que es un doble problema. Perder esta cuota de mercado puede siginificar perdida de recursos importantes y la detección correcta de la clase minoritaria, pero de mayor relevancia, la representa muy bien la métrica *class-recall*(falsos negativos). Por otra parte, el class-precision ayuda a que no se trate como posible *Churn* a usuarios que no iban a abandonar el servicio, lo que implicaría posibles ofertas innecesarias a usuarios que NO iban a abandonar el servicio, algo que también implica posible perdida de dinero, aunque no tan crítica como el abandono del usuario.

  

14) La comparación, con las mismas métricas de un DummyClassifier, implementado en RapidMiner agregando el atributo por defecto en FALSE, nos da como resultado un *accuracy (average)* mayor al del árbol de decisión, pero evidentemente esto se debe al desbalanceo de las clases, sin embargo, las métricas clave para este problema, como lo son *class-recall* y *class-precision* tienen un rendimiento del 0%, como se puede observar en la *Figura 14.1*, lo que nos indica que va a predecir muy mal a los usuarios que si van a abandonar el servicio, como era de esperarse en este clasificador dummy.

![enter image description here](https://github.com/ruben4181/maestria-docs/blob/main/mineria-datos-2025/figure_14_1.png?raw=true)

*Figura 14.1*