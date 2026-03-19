Para que logres ese **90% de accuracy** y un informe de alta calidad, he desglosado la actividad en fases críticas, ordenadas por su impacto en el resultado final.

---

## 1. Fase de Datos (Cimiento del Modelo)

**Importancia: Crítica.** Si los datos están mal procesados, ninguna red llegará al objetivo.

* **Análisis Exploratorio (EDA):** Contar cuántas imágenes hay por personaje. Verás que hay un fuerte **desbalanceo** (Homer tiene ~2000, otros ~400).
* **Split (División):** Separar en **80% Entrenamiento / 20% Validación**. No uses el set de *Test* para ajustar el modelo, solo para la evaluación final.
* **Preprocesado:** * Redimensionar todas las imágenes (ej. $64 \times 64$ o $128 \times 128$).
* **Normalización:** Escalar píxeles de $[0, 255]$ a $[0, 1]$.



---

## 2. Fase de Arquitectura (Diseño de los 2 Modelos)

**Importancia: Alta.** Es el requisito principal del ejercicio.

* **Modelo 1 (Base):** Una CNN estándar con 2 o 3 bloques `Conv + Pool`. Sirve para demostrar que entiendes la estructura básica.
* **Modelo 2 (Avanzado):** Aquí es donde buscas el **+90%**. Debes añadir:
* **Dropout:** Para evitar que la red memorice el ruido de las imágenes (overfitting).
* **Batch Normalization:** Para que el entrenamiento sea más estable y rápido.
* **Data Augmentation:** Crear variaciones (giros, zoom) de las imágenes para que el modelo "vea" más ejemplos de los que realmente hay.



---

## 3. Fase de Evaluación y Métricas

**Importancia: Muy Alta (Para el Informe).** El profesor evaluará tu capacidad de análisis, no solo el código.

* **Matriz de Confusión:** Identificar qué personajes se confunden entre sí (ej. Bart y Lisa por el color de piel/pelo).
* **Precision & Recall:** No basta con el Accuracy total; debes ver si el modelo es malo detectando a personajes con pocas fotos.
* **Gráficas de Aprendizaje:** Mostrar las curvas de `Loss` y `Accuracy`. Si la de entrenamiento sube y la de validación baja, tienes **Overfitting**.

---

## 4. Fase de Informe (Redacción)

**Importancia: Media-Alta.** Es donde justificas tus decisiones.

* **Comparativa con Fully Connected:** Explicar por qué una red densa falla (no entiende la geometría) frente a una CNN.
* **Análisis de Errores:** Mostrar ejemplos de fotos donde la red falló y explicar por qué (ej. "La imagen estaba muy oscura" o "Había dos personajes").

---

## Resumen de Objetivos (Checklist)

1. [ ] **Superar el 90%** de accuracy en Test.
2. [ ] **Comparar 2 modelos** (uno simple y uno optimizado).
3. [ ] **Normalizar** las imágenes (dividir por 255).
4. [ ] **Realizar el Split** manual o mediante generadores.
5. [ ] **Análisis de balanceo** de las 18 clases.

**¿Quieres que te prepare el código para realizar el primer paso: el análisis de distribución y el split de carpetas?**