$(document).ready(function() {
    $('#id_categoría').on('change', function() {
        const id_categoría = $(this).val();
        const subcategoríaSelect = $('#id_subcategoría');
        subcategoríaSelect.dropdown('clear');
        subcategoríaSelect.empty();
        console.log('Categoría seleccionada:', id_categoría);
        $.ajax({
            url: '../cargar_subcategorias',
            data: { 'id_categoría': id_categoría },
            dataType: 'json',
            success: function(data) {
                console.log(data);
                $.each(data, function(index, subcategoría) {
                    subcategoríaSelect.append($('<option>', {
                        value: subcategoría.id_subcategoría,
                        text: subcategoría.nombre_subCat
                    }));
                });
            }
        });
    });
});