// Variables y botones del template
const btnModificar = document.getElementById('btn_modificar');
const btnEliminar = document.getElementById('btn_eliminar');
const formModif = document.getElementById('form_modif');

// Función "Ver"
function ver(idPrioridad) {
    $.ajax({
        url: "prioridad",
        type: "GET",
        data: { id_prioridad: idPrioridad },
        dataType: "json",

        success: function (datos) {
            console.log(datos);
            $('#modal_nombre').val(datos.prioridad.nombre_prioridad);
            $('#id_prioridad_modal').val(datos.prioridad.id_prioridad);
            $('.ui.modal').modal('show');
        },

        error: function (error) {
            console.log(error.responseText);
        }
    })
}