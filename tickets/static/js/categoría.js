const btnModificar = document.getElementById('btn_modificar');
const btnVer = document.getElementById('btn_ver');
const idCategoría = btnVer.value;
const formModif = document.getElementById('form_modif');

btnVer.addEventListener('click', function () {
    $.ajax({
        url: "categoría",
        type: "GET",
        data: { id_categoría: idCategoría },
        dataType: "json",

        success: function (datos) {
            console.log(datos);
            $('#modal_nombre').val(datos.categoría.nombre_cat);
            $('#id_categoría_modal').val(datos.categoría.id_categoría);
            $('.ui.modal').modal('show');
        },

        error: function (error) {
            console.log(error.responseText);
        }
    })
})

btnModificar.addEventListener('click', function () {
    formModif.submit();
})