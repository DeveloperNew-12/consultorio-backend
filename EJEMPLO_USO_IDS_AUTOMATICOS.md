# 🔢 IDs Automáticos - Guía de Uso

## ✅ Cambios Implementados

### Modelos Actualizados
- **Usuario**: `idusuario` ahora es `AutoField` (genera IDs automáticamente: 1, 2, 3...)
- **Rol**: `idrol` ahora es `AutoField` (genera IDs automáticamente: 1, 2, 3...)

### Serializers Actualizados
- Los campos ID son ahora `read_only=True`
- No necesitas enviar IDs al crear usuarios o roles

## 🚀 Cómo Usar

### Crear Rol (API)
```bash
POST /api/usuarios/roles/
Content-Type: application/json

{
    "nombre": "Odontólogo",
    "descripcion": "Profesional odontólogo"
}

# Respuesta:
{
    "idrol": 1,  # ← ID generado automáticamente
    "nombre": "Odontólogo",
    "descripcion": "Profesional odontólogo"
}
```

### Crear Usuario (API)
```bash
POST /api/usuarios/usuarios/
Content-Type: application/json

{
    "nombre": "Dr. Juan Pérez",
    "correo": "juan.perez@consultorio.com",
    "contrasena": "password123",
    "estado": "ACTIVO"
}

# Respuesta:
{
    "idusuario": 1,  # ← ID generado automáticamente
    "nombre": "Dr. Juan Pérez",
    "correo": "juan.perez@consultorio.com",
    "estado": "ACTIVO",
    "ultimologin": null
}
```

### Crear desde Django Shell
```python
from usuarios.models import Rol, Usuario

# Crear rol - NO especificar idrol
rol = Rol.objects.create(
    nombre="Administrador",
    descripcion="Administrador del sistema"
)
print(f"Rol creado con ID: {rol.idrol}")  # ID: 1

# Crear usuario - NO especificar idusuario
usuario = Usuario.objects.create(
    nombre="María García",
    correo="maria@consultorio.com",
    contrasena="password456",
    estado="ACTIVO"
)
print(f"Usuario creado con ID: {usuario.idusuario}")  # ID: 1
```

## ⚠️ Importante

### ❌ NO Hagas Esto
```python
# NO especificar IDs manualmente
rol = Rol.objects.create(
    idrol=5,  # ← NO hacer esto
    nombre="Rol Manual"
)
```

### ✅ Haz Esto
```python
# Dejar que Django genere el ID automáticamente
rol = Rol.objects.create(
    nombre="Rol Automático",
    descripcion="Descripción del rol"
)
```

## 🔄 Migración Aplicada

La migración `0003_auto_increment_ids.py` fue aplicada exitosamente:
- Cambió `CharField` a `AutoField` para ambos modelos
- Los IDs ahora se generan automáticamente
- Secuencia comienza en 1 y se incrementa automáticamente

## 🧪 Prueba Realizada

Se probó exitosamente la creación de:
- 3 roles con IDs: 1, 2, 3
- 3 usuarios con IDs: 1, 2, 3

¡Todo funciona correctamente! 🎉
