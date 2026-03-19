Aquí tienes una guía estructurada y concisa con los comandos esenciales para gestionar entornos y paquetes con **Conda**.

---

## 1. Gestión de Entornos (Environments)

Es la parte más importante para mantener tus proyectos aislados y organizados.

| Acción | Comando |
| --- | --- |
| **Crear** un entorno | `conda create --name nombre_entorno` |
| **Crear** con versión de Python | `conda create -n nombre python=3.10` |
| **Activar** un entorno | `conda activate nombre_entorno` |
| **Desactivar** entorno actual | `conda deactivate` |
| **Listar** todos los entornos | `conda env list` |
| **Eliminar** un entorno | `conda remove -n nombre_entorno --all` |

---

## 2. Gestión de Paquetes

Comandos para instalar y administrar las librerías dentro del entorno activo.

* **Instalar un paquete:** `conda install nombre_paquete`
* **Instalar versión específica:** `conda install pandas=2.0`
* **Ver paquetes instalados:** `conda list`
* **Actualizar un paquete:** `conda update nombre_paquete`
* **Eliminar un paquete:** `conda remove nombre_paquete`

---

## 3. Mantenimiento y Configuración

Para asegurar que Conda funcione correctamente y no ocupe espacio innecesario.

* **Ver información de conda:** `conda info`
* **Actualizar Conda:** `conda update conda`
* **Limpiar caché y paquetes no usados:** `conda clean --all`
> *Nota: Útil para liberar espacio en disco de instalaciones antiguas.*



---

## 4. Exportación (Reproducibilidad)

Ideal para compartir tu configuración con otros desarrolladores.

* **Exportar a archivo YAML:**
`conda env export > ambiente.yml`
* **Crear entorno desde archivo:**
`conda env create -f ambiente.yml`

---

¿Te gustaría que te explique cómo configurar **canales (channels)** específicos como `conda-forge` para obtener paquetes más actualizados?