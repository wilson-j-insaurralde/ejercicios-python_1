# Ejercicios de Python 🐍

Colección de ejercicios resueltos mientras aprendo **Python**.  
Organizados por temas: variables, condicionales, bucles, funciones, clases y proyectos prácticos.

## 🎯 Objetivo
Practicar Python paso a paso, entender la lógica de programación y registrar mi avance a lo largo del curso.

## 🧩 Cómo usar
1. Abrir cada archivo `.py` con tu editor de código favorito (por ejemplo, VS Code o PyCharm).  
2. Ejecutarlo con:
   ```bash
   python nombre_del_archivo.py
## ✍️ Cabecera de Autor (marca de agua)
Todos los archivos `.py` en este repositorio incluyen una cabecera con la información del autor.
Si estás colaborando, por favor conserva esa cabecera. Para mantenerla, el repositorio incluye comprobaciones automáticas
que fallarán en commits o pull requests si algún archivo pierde la cabecera.

### Comprobar manualmente
Puedes verificar localmente con:
```bash
python tools/verify_header.py
```

### Hooks y CI
- Se ha añadido un hook de `pre-commit` (en `.githooks/pre-commit`) que ejecuta la comprobación antes del commit.
- Se ha añadido un workflow de GitHub Actions (`.github/workflows/header-check.yml`) que verifica cabeceras en pushes/PRs.

### Nota sobre seguridad
Estos métodos dificultan la eliminación accidental de la cabecera, pero no son infalibles: cualquier persona con control del código puede quitar la verificación.
Si necesitas protección más fuerte (por ejemplo, distribuir binarios compilados), podemos revisar opciones avanzadas.

## 📜 Licencia
Este repositorio usa la licencia CC BY‑NC‑ND 4.0 International.
Esto permite compartir los ejercicios para fines educativos con atribución, pero no permite usos comerciales ni distribución de versiones modificadas.

Si encuentras una copia no autorizada del contenido en otro repositorio, el proyecto contiene un monitor automático que busca la cabecera y crea una issue si detecta coincidencias en repos públicos. Si necesitas que persiga un caso específico, contáctame.

## 🔐 Firma de commits y DMCA
- Firmar tus commits con GPG añade una prueba de autoría. Puedes habilitarlo con:
   ```bash
   git config --global user.signingkey <your GPG key id>
   git config --global commit.gpgsign true
   ```
- Si encuentras que alguien publicó tu trabajo sin permiso y en violación de la licencia, puedes enviar un reporte DMCA a GitHub: https://docs.github.com/en/site-policy/dmca

