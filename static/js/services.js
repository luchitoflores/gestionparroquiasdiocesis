var app = angular.module('app');

/////////------------------------------- FACTORIAS------------------------------------/////////////

app.factory("administrarCatalogos", ['$http', function ($http) {
    var catalogos = {};
    catalogos.getCatalogos = function () {
        return $http.get('/api-auth/catalogo/');
    };

    catalogos.getItemsPorCatalogo = function (codCatalogo) {
        return $http.get('/api-auth/item/?catalogo=' + codCatalogo);
    };

    catalogos.setCatalogo = function (data) {
        return $http.post('/api-auth/catalogo/', data);
    };

    catalogos.updateCatalogo = function (id, data) {
        return $http.put('/api-auth/catalogo/' + id, data);
    };

    return catalogos;
}]);

app.factory("administrarItems", ['$http', function ($http) {
    var items = {};

    items.getItemsPorCatalogo = function (codCatalogo) {
        return $http.get('/api-auth/item/?catalogo=' + codCatalogo);
    };

    items.getItemsPaginadosPorCatalogo = function (codCatalogo) {
        return $http.get('/api-auth/itemspaginados/?catalogo=' + codCatalogo);
    };

    items.setItem = function (data) {
        return $http.post('/api-auth/item/', data);
    };

    items.updateItem = function (id, data) {
        return $http.put('/api-auth/item/' + id, data);
    };

    return items;
}]);

app.factory("administrarParametros", ['$http', function ($http) {
    var parametros = {};

    parametros.getParametros = function () {
        return $http.get('/api-auth/parametro/');
    };

    parametros.setParametro = function (data) {
        return $http.post('/api-auth/parametro/', data);
    };

    parametros.updateParametro = function (id, data) {
        return $http.put('/api-auth/parametro/' + id, data);
    };

    return parametros;
}]);

app.factory("administrarModulos", ['$http', function ($http) {
    var modulos = {};

    modulos.getModulos = function () {
        return $http.get('/api-auth/modulo/');
    };

    modulos.setModulo = function (data) {
        return $http.post('/api-auth/modulo/', data);
    };

    modulos.updateModulo = function (id, data) {
        return $http.put('/api-auth/modulo/' + id, data);
    };

    return modulos;
}]);

app.factory("administrarFuncionalidades", ['$http', function ($http) {
    var funcionalidades = {};

    funcionalidades.getFuncionalidades = function () {
        return $http.get('/api-auth/funcionalidad/');
    };

    funcionalidades.setFuncionalidad = function (data) {
        return $http.post('/api-auth/funcionalidad/', data);
    };

    funcionalidades.updateFuncionalidad = function (id, data) {
        return $http.put('/api-auth/funcionalidad/' + id, data);
    };

    funcionalidades.getFuncionalidadesPorModulo = function (codModulo) {
        return $http.get('/api-auth/funcionalidad/?modulo=' + codModulo);
    };

    funcionalidades.getGrupos = function () {
        return $http.get('/api-auth/grupo/');
    };

    funcionalidades.getModulos = function () {
        return $http.get('/api-auth/modulo/');
    };

    return funcionalidades;
}]);


app.factory("AdministrarAgenda", ['$http', function ($http) {
    var eventos = {};

    eventos.getEventos = function (queryparams) {
        return $http.get('/api-auth/agenda/filters/?'+queryparams);
    };

    eventos.getEvento = function (id) {
        return $http.get('/api-auth/evento/'+id);
    };

    eventos.setEvento = function (data) {
        return $http.post('/api-auth/evento/', data);
    };

    eventos.updateEvento = function (id, data) {
        return $http.put('/api-auth/evento/' + id, data);
    };

    return eventos;
}]);