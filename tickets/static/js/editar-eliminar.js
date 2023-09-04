let btnEliminar = document.getElementById('btnEliminar').addEventListener('click', function(){
    $('.ui.modal').modal('show');
})

let botonModal = document.getElementById('btnModal').addEventListener('click', function(){
    let formulario = document.getElementById('formulario').querySelector('[name = "acciones"][value = "eliminar"]').click();
})