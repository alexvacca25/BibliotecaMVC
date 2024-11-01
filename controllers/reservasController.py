
from controllers.usuariosController import usuarios
from controllers.inventarioController import inventario



def prestamo_material(usuario_id,material_id):
    usuario= next(u for u in usuarios if u.id==usuario_id)
    material=next(m for m in inventario if m.id==material_id)
    usuario.materiales_prestados.append(material)