valorAnterior = 0;


if (localStorage['fixture']==null) {
		console.log("Nunca cargo el json");
		$.getJSON("mundial.json", cargarArchivo);
}

function cargarArchivo (value) {
	/* Utilizas el localStorage como un diccionario (clave, valor) .
	   JSON.stringify(value) se utiliza xq solamente puede guardar strings */
	console.log("Tratando de cargarlo");
	localStorage.setItem('fixture',JSON.stringify(value));
	console.log(value);
}

function cambioInput (input) {
	//alert('Cambio el texto del input: ' + parseInt(input.value));
	valorAnterior = parseInt(input.value);
}


/* Permite reconstruir funciones desde el string de la funcion */
function jsonfnParse(str) {
	return JSON.parse(str,
		function (key, value) {
			if ((typeof value) != 'string')
				return value;
			return (value.substring(0,8) == 'function') ? eval('('+value+')') : value;
		});
}


function anotarResultado (input) {
	/*if (!inputHabilitado)
		habilitarInputEliminatorias();*/

	var numPartido = input.parentElement.id;
	console.log('numPartido: ' + numPartido);
	var entradas = $('#'+numPartido+'.active').find('input');
	console.log('entradas: ' + entradas);
	console.log('4 padres: ' + input.parentElement.parentElement.parentElement.parentElement.id);
	var grupo = jsonfnParse(localStorage[input.parentElement.parentElement.parentElement.parentElement.id]);
	
	/*var partido = '';
	for (var i = 0; i < grupo.partidos.length; i++) {
		if (grupo.partidos[i].numPartido == input.parentElement.parentElement.id){
			// Obtengo el partido correspondiente 
			partido = grupo.partidos[i];
		}
	}
	var equipos = grupo.equipos;
	var equipo1 = '';
	var equipo2 = '';

	if (input.id==('goles1')){
		for (var i = 0; i < equipos.length; i++) {
				if (equipos[i].id == partido.equipo1)
				{
					grupo.equipos[i].setGolesFavor(parseInt(input.value), valorAnterior);
				}
		}
	}else{
		for (var i = 0; i < equipos.length; i++) {
				if (equipos[i].id == partido.equipo2)
				{
					grupo.equipos[i].setGolesFavor(parseInt(input.value), valorAnterior);
				}
		}
	}

	// Obteniendo los equipos //
	for (var i = 0; i < equipos.length; i++) {
		if (equipos[i].id == partido.equipo1)
			equipo1 = grupo.equipos[i];
		if (equipos[i].id == partido.equipo2)
			equipo2 = grupo.equipos[i];
	};
	if (!partido.jugado){
		equipo1.jugados = equipo1.jugados + 1;
		equipo2.jugados = equipo2.jugados + 1;
	}
	comprobarEstadoPartido(partido, parseInt(entradas[0].value), parseInt(entradas[1].value), equipo1, equipo2);
	grupo.anotarGol(numPartido, entradas[0].id, parseInt(entradas[0].value));
	grupo.anotarGol(numPartido, entradas[1].id, parseInt(entradas[1].value));
	partido.jugado = true;
	
	equipos.sort(function (a, b) {
		return a.getPuntos() < b.getPuntos();
	});

	if(comprobarPartidosJugados(grupo.partidos)==true){
		if (!localStorage.octavos)
			localStorage.octavos = JSON.stringify([]);
		cargarOctavos(grupo, equipos[0], 1);
		cargarOctavos(grupo, equipos[1], 2);
	}

	localStorage[input.parentElement.id] = JSON.stringify(grupo, jsonfnStringify);
	cargarPosGrupos(grupo.nombre);*/
}		