$(function() {
    // Busca os dados do backend
    $.ajax({
        url: 'http://localhost:5000/listar_carros',
        method: 'GET',
        dataType: 'json',
        success: listar, 
        error: function() {
            alert("Erro ao obter dados do backend");
        }
    });

    function listar(carros) {
        // Percorre os dados obtidos do backend e retorna para tela
        for (var c in carros) { 
            lin = '<tr>' + 
              '<td>' + carros[c].marca + '</td>' + 
              '<td>' + carros[c].modelo + '</td>' + 
              '<td>' + carros[c].ano + '</td>' + 
              '</tr>';
            $('#tabelaCarros').append(lin);
        }
    }

});