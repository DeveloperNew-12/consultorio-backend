### Paso 1: Clonar el Repositorio

```bash
git clone <url-del-repositorio>
cd "Proyecto 2"
```

### Paso 2: Crear un Entorno Virtual

Es recomendable crear un entorno virtual para aislar las dependencias del proyecto:

#### En Windows:
```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
venv\Scripts\activate
```

#### En macOS/Linux:
```bash
# Crear el entorno virtual
python3 -m venv venv

# Activar el entorno virtual
source venv/bin/activate
```

### Paso 3: Instalar Dependencias

Con el entorno virtual activado, instala las dependencias:

```bash
pip install -r requirements.txt
```

### Paso 4: Configurar Variables de Entorno

1. **Crear archivo de configuración:**
   ```bash
   # Copia el archivo de ejemplo
   copy env.example .env
   ```
   
   En Linux/macOS:
   ```bash
   cp env.example .env
   ```

2. **Editar el archivo `.env`:**
   Abre el archivo `.env` y configura tus variables:
   ```env
   # Configuración de Django
   SECRET_KEY=tu_secret_key_personalizado_aqui
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1

   # Configuración de Base de Datos PostgreSQL
   DB_NAME=clinicadb
   DB_USER=postgres
   DB_PASSWORD=tu_password_aqui
   DB_HOST=localhost
   DB_PORT=5432

   # Configuración de Email (opcional)
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=tu_email@gmail.com
   EMAIL_HOST_PASSWORD=tu_password_email
   ```

3. **Crear la base de datos en PostgreSQL:**
   ```sql
   CREATE DATABASE clinicadb;
   CREATE USER postgres WITH PASSWORD 'tu_password_aqui';
   GRANT ALL PRIVILEGES ON DATABASE clinicadb TO postgres;
   ```

### Paso 5: Aplicar Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### Paso 6: Crear un Superusuario

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para crear un usuario administrador.

### Paso 7: Ejecutar el Servidor de Desarrollo

```bash
python manage.py runserver
```

El servidor estará disponible en: `http://127.0.0.1:8000/`

## 📚 Uso del Sistema

### Panel de Administración

Accede al panel de administración de Django en:
- **URL**: `http://127.0.0.1:8000/admin/`
- **Usuario**: El superusuario creado en el paso 6

## 🔒 Seguridad

### Variables de Entorno
- **NUNCA** subas el archivo `.env` al repositorio
- Usa el archivo `env.example` como plantilla
- Genera una SECRET_KEY única para cada entorno
- Cambia las credenciales por defecto en producción

### Generar Nueva SECRET_KEY
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Configuración de Producción
Para producción, asegúrate de:
- Cambiar `DEBUG=False`
- Configurar `ALLOWED_HOSTS` con tu dominio
- Usar una base de datos segura
- Configurar HTTPS
- Usar variables de entorno del servidor

---

**¡Gracias por usar el Sistema de Información de Tu Clínica!** 🦷✨

