// Inicialización de variables y botónes

// Función del botón ver
function ver(idSubCat) {
    $.ajax({
        url: 'subcategoría',
        type: 'GET',
        data: { id_subCat: idSubCat },
        dataType: 'json',

        success: function (datos) {
            console.log(datos);
            $('#modal_nombre').val(datos.nombre_subCat);
            $('#id_id_categoría').dropdown('set selected', datos.id_categoría);
            $('.ui.modal').modal('show');
        },

        error: function (error) {
            console.log(error.responseText);
        }
    });
}