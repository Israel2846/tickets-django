// Variables y botones del template
const btnModificar = document.getElementById('btn_modificar');
const btnEliminar = document.getElementById('btn_eliminar');
const formModif = document.getElementById('form_modif');

// Función del botón "Ver"
function ver(id_categoría) {
    $.ajax({
        url: "categoría",
        type: "GET",
        data: { id_categoría: id_categoría },
        dataType: "json",

        success: function (datos) {
            $('#modal_nombre').val(datos.categoría.nombre_cat);
            $('#id_categoría_modal').val(datos.categoría.id_categoría);
            $('.ui.modal').modal('show');
        },

        error: function (error) {
            console.log(error.responseText);
        }
    })
}

// Función del botón "Modificar"
btnModificar.addEventListener('click', function () {
    $('#acciones').val('aceptar');
    formModif.submit();
})

// Función del botón "Eliminar"
btnEliminar.addEventListener('click', function () {
    $('#acciones').val('eliminar');
    formModif.submit();
})