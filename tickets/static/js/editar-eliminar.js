$(document).ready(function() {
    document.getElementById('btnEliminar').addEventListener('click', function() {
            $('.ui.modal').modal('show');
    })

    document.getElementById('btnModal').addEventListener('click', function() {
        document.getElementById('formulario').querySelector('[name="acciones"][value="eliminar"]').click();
    });

    document.getElementById('btnCancelar').addEventListener('click', function() {
        $('.ui.modal').modal('hide');
    });
});