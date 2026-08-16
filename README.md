# Laboratorio 1: Primer Pipeline de Integración Continua

Este repositorio contiene la configuración del primer pipeline de CI/CD utilizando **GitHub Actions**, correspondiente al Laboratorio 1 de *Entornos de Integración y Entrega Continua*.

## 📁 Estructura del Repositorio

```text
.
├── .github/
│   └── workflows/
│       └── pipeline.yml    # Definición del pipeline en GitHub Actions
├── app/
│   └── hello.txt           # Archivo de texto requerido por la práctica
├── README.md               # Documentación del proyecto
└── laboratorio1.md         # Guía e instrucciones del laboratorio
```

## 🔄 Funcionamiento del Pipeline

El pipeline está configurado como *Pipeline as Code* y se dispara automáticamente tras cada evento de `push` a la rama `main`. Ejecuta las siguientes tareas:

1. **Checkout**: Clona y descarga el código fuente del repositorio en el runner utilizando `actions/checkout@v4`.
2. **Información del entorno**: Imprime el nombre del repositorio, la rama activa y el identificador SHA del commit.
3. **Fecha y hora**: Registra el timestamp exacto de la ejecución con `date`.
4. **Versión de Git**: Valida y muestra la versión de Git instalada en el entorno (`git --version`).
5. **Finalización**: Emite un mensaje de estado confirmando que el pipeline finalizó con éxito.
