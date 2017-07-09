var main;
var familyWanted;
var currentTable;
var currentTableID;

function loadSettings(){
	main.innerHTML = `<div class="container-fluid">
                            <div class="col-sm-1 sidenav " style="width: 12%">
		                      <h3>Ajustes</h3>
		                      <button onclick="loadTables()">Mesas</button>
		                      <button onclick="loadStaff()">Personal</button>
		                      <button  onclick="loadRestaurant()">Restaurante</button>
		                      <button>Otros</button>
                            </div>
                       <div class="col-sm-10">
		                  
	                       <div class="well" id="content">
                           </div>
                          </div>
                        
                    </div>`;
    
}

function loadTables(){
     frame = document.getElementById('content');
     frame.innerHTML = `<h4> Mesas </h4>
                        <p>Mesa actual : ${currentTable} </p>
                        
                        <div>
                            <label> Mesa </label> <button onclick="addTable('M')">Añadir</button>
                            <label> Terraza </label> <button onclick="addTable('T')">Añadir</button>
                            <label> Barra </label> <button onclick="addTable('B')">Añadir</button>
                            <button class='btn-danger' onclick="removeTable(${currentTable},${currentTableID})">Eliminar</button>
                        </div>
                
                        <div >
                            <ul id="tableList">Cargando...</ul>
	                    </div>`;
     get("tables", function(){
			"use strict";
			let list = document.getElementById('tableList');
			list.innerHTML = '';

			for (let table of this.response){
				list.insertAdjacentHTML('beforeend', `<li onclick="selectTable(${table.number},${table.id})">${table.type_table}${table.number}</li>`);
			}
	});
}

function selectTable(newTable,id){
    currentTable = newTable;
    currentTableID = id;
    loadTables();
}

function addTable(type){
   var valores = Object();
   valores.number=0;
   valores.type_table=type;
   valores.is_avaible = true;
   valores.restaurant = 3;
   
   post("tables/", function(){
		loadTables();
	}, valores, true);
}

function removeTable(num,id){
     if (confirm('¿Esta seguro de borrar la mesa '+num+'?')){
       _delete("tables/"+id+"/",function(){loadTables();},true);
    } 
    return false;
}

function loadStaff(){
     frame = document.getElementById('content');
     frame.innerHTML = `<h4> Personal </h4>
                        <div id='staffPanel'>
                            <table class='table'>
                            <thead>
                            <th></th>
                            <th>Nombre</th>
                            <th>Cargo</th>
                            <th>Sueldo/hora</th>
                            <th>Activo</th>
                            <th>Notas</th>
                            <tbody id='staffList'>
                            </tbody>
                            </table>
	                    </div>`;
     get("staff/", function(){
			"use strict";
			let list = document.getElementById('staffList');
			list.innerHTML = '';

			for (let table of this.response){
				list.insertAdjacentHTML('beforeend', `<tr>
                                                        <td><button onclick='removeStaff(${table.id})' id='staffInput' class="glyphicon glyphicon-remove btn-danger"></button></td>
                                                        <td><input type='text' class="form-control" name='first_name' id='first_name${table.id}' value=${table.first_name} readonly>
                                                        <input type='text' class="form-control" name='last_name' id='last_name${table.id}' value=${table.last_name} readonly></td>
                                                        <td><p id='rol${table.id}'>${table.staff_role_code.staff_role_code}</p></td>
                                                        <td><input type='text'  class="form-control-addon"  id='hourly_rate${table.id}' name='hourly_rate' value=${table.hourly_rate} readonly>
                                                        <td><input type='checkbox' readonly name='is_active${table.id}'  id='is_active${table.id}'  class="form-control" checked=${table.is_active}></td>
                                                        <td><input type='text'  readonly  class="form-control-addon" id='notes${table.id}' name='notes' value=${table.notes}></td>
                                                        <td id='editButton${table.id}'><button class="glyphicon glyphicon-pencil btn-warning" onclick='allowEditStaff(${table.id})'></button></td>
                                                       </tr>`);
			}
          list.insertAdjacentHTML('beforeend',`<tr><td><button onclick='showStaffForm()' class="glyphicon glyphicon-plus btn-success"></button></td></tr></table>`);
	});
}

function allowEditStaff(id_user){
    var rol = document.getElementById('rol'+id_user);
    
    rol.innerHTML = '';
    rol.insertAdjacentHTML('beforeend',` <select id='role${id_user}'>
                                            <option value='M'>Manager</option>
                                            <option value='W'>Camarero</option>
                                            <option value='B'>Barman</option>
                                            <option value='K'>Cocinero</option>
                                </select>`);
    
    document.getElementById('first_name'+id_user).readOnly=false;
    document.getElementById('last_name'+id_user).readOnly=false;
    document.getElementById('is_active'+id_user).readOnly=false;
    document.getElementById('hourly_rate'+id_user).readOnly=false;
    document.getElementById('notes'+id_user).readOnly=false;
    
    var button = document.getElementById('editButton'+id_user);
    button.innerHTML='';
    button.insertAdjacentHTML('beforeend',`<button class="btn-warning"  onclick='editStaff(${id_user})'>Editar</button>`);
}

function editStaff(id_user){
    var valores = Object();
    
    valores.first_name = document.getElementById('first_name'+id_user).value;
	valores.last_name = document.getElementById('last_name'+id_user).value;
    valores.staff_role_code = {staff_role_code: "B"};
    valores.hourly_rate = document.getElementById('hourly_rate'+id_user).value;
    valores.is_active =  document.getElementById('is_active'+id_user).checked;
    valores.notes = document.getElementById('notes'+id_user).value;
    valores.restaurant = 2;
    console.log(valores);
     put('staff/'+id_user+'/', function(){
		loadTables();
	}, valores, true);
}

function removeStaff(id_user){
    if(confirm("Confirme el borrado")){
        _delete('staff/'+id_user+'/',function(){loadStaff();},true);
    }
}

function showStaffForm(){
    let list = document.getElementById('staffPanel');
    list.innerHTML=''
    list.insertAdjacentHTML('beforeend',`<form onsubmit='return addStaff(this)'>
                                       
                                        <input type='text' class=class="input-group" name='first_name' placeholder='Nombre'>
                                        <input type='text' name='last_name' placeholder='Apellidos'>
                                        <label> Cargo </label><select name='role'>
                                            <option value='M'>Manager</option>
                                            <option value='W'>Camarero</option>
                                            <option value='B'>Barman</option>
                                            <option value='K'>Cocinero</option>
                                        </select>
                                        <input type='text' placeholder='Sueldo/hora' name='hourly_rate'>
                                        <label>Activo</label><input type='checkbox' name='is_active'>
                                        <input type='text' name='notes' placeholder='Notas'>
                                         <button type='submit'>Registrar</button>`);
}

function addStaff(form){
    var valores = Object();
    
	valores.first_name = form.first_name.value;
	valores.last_name = form.last_name.value;
    valores.staff_role_code = {id: 3,staf_role_description: "B"};
    valores.hourly_rate = form.hourly_rate.value;
    valores.is_active = form.is_active.checked;
    valores.restaurant = 2;
    valores.notes = form.notes.value;
    
       post("staff/", function(){
		loadStaff();
	}, valores, true);
    	return false;

}

function loadRestaurant(){
    frame = document.getElementById('content');
    frame.innerHTML=`<div id='restInfo'></div>`;
    get("restaurants/",function(){
        "use strict";
        let list = document.getElementById('restInfo');
        list.innerHTML = '';
        
        for (let table of this.response){
				list.insertAdjacentHTML('beforeend',`<div class='row'><div class='col-md-6'><input type='hidden' name='id' value='${table.id}'>
                                                            <label>Nombre</label><input type='text' class="form-group" name='name' value='${table.name}'><br>
                                                            <label>Propietario</label><input type='text' id='owner' class="form-group" name='owner' value='${table.owner}' ><br>
                                                            <fielset>
                                                                <legend>Dirección</legend>
                                                                <label>Calle</label><input type='text' name='street' id='address' class="form-group" value='${table.address}'><br>
                                                                <label>Localidad</label><input type='text' class="form-group" name='city' value='${table.city}'><br>
                                                                <label>Provincia</label><input type='text' name='province' value='${table.province}'>
                                                            </fielset></div>
                                                        <div class='col-md-6'>
                                                            <div><label>Lat:</label><input id='lat' value='${table.lat}' readonly>
                                                                 <label>Long:</label><input id='long' value='${table.lng}' readonly>
                                                            </div>
                                                            <div id='map'></div>
                                                        </div>
                                                    </div>
                                                        <div class='row'>
                                                            <button class='btn pull-right' onclick='getLatLong()'>Guardar</button>
                                                        </div>`);
			}
         
    });
}
/*
function initMap(){
    var my_rest = {lat: -25.363, lng: 131.044};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 4,
          center: my_rest
        });
        var marker = new google.maps.Marker({
          position: my_rest,
          map: map
        });

}

function getLatLong(){
    var address = document.getElementById('address').value.split(","); 
    console.log(address);
}*/

function loadFamily(name){
	familyWanted = name;
	document.getElementById('productsList').innerHTML = "Cargando...";

	get("products/?family=" + encodeURIComponent(name), function(){
			"use strict";
			if (familyWanted == name){
				let list = document.getElementById('productsList');
				list.innerHTML = '';

				for (let product of this.response){
					list.insertAdjacentHTML('beforeend', `<li onclick="void(0)">${product.name}</li>`);
				}
			}
	});
}

function loadTPV(){
	main.innerHTML = `<div class="container-fluid">
		<div class="row content">
		 <div class="col-sm-1 sidenav " style="width: 12%">
		     <div class="btn-group-vertical" style="width: 110%">
		     <button type="button" class="btn btn-primary">Ver Mesas</button>
		     <button type="button" class="btn btn-warning" >Abrir Cajón</button>
		     <button type="button" class="btn btn-success">Efectivo <span class="badge"> 12.50€</span></button>
		     <button type="button" class="btn btn-success">Cobro Avanzado</button>
		     <button type="button" class="btn btn-primary">Dividir Ticket</button>
		     <button type="button" class="btn btn-basic">Enviar a Cocina</button>
		     <button type="button" class="btn btn-danger">Borrar Linea</button>
		     <button type="button" class="btn btn-info">Añadir Nota</button>
		     <button type="button" class="btn btn-warning">Transferir Mesa</button>
		     <button type="button" class="btn btn-primary">Buscar Ticket</button>
		     <button type="button" class="btn btn-info">Imprimir Ticket</button>
		     <button type="button" class="btn btn-danger">Cancelar Ticket</button>
		     </div><br>
		 </div>
		 <br>

		 <div class="col-sm-10">
		   <div class="row">
		     <div class="col-sm-8">
		       <div class="well">
		         <h4>Familias</h4>
		         <ul id="familiesList">Cargando...</ul>
		       </div>
		     </div>
		     <div class="col-sm-4">
		       <div class="well">
		         <h4>Contexto Actual</h4>
		         <p>Total cuenta</p>
		         <p>Camarero:  ${sessionStorage['username']}</p>
		         <p>Numero de Mesa</p>
		         <p>Numero de Ticket</p>
		       </div>
		     </div>
		   </div>
		   <div class="row">
		     <div class="col-sm-8">
		       <div class="well">
		         <h4>Productos</h4>
		         <ul id="productsList">Cargando...</ul>
		       </div>
		         <div class="well">
		         <h4> Sugerencias de productos </h4>
		         <p> Aqui aparece una lista de productos de varias familias que tienen una gran probabilidad de ser incluídos en el ticket</p>
		       </div>
		     </div>
		     <div class="col-sm-4">
		       <div class="well">
		         <h4>Ticket Actual</h4>
		         <p>Contiene una lista dinámica con todos los productos del ticket actual</p>
		       </div>
		     </div>
		   </div>
		 </div>
	  </div>
	</div>`;

	familyWanted = '';
    
	get("families/", function(){
			"use strict";
			let list = document.getElementById('familiesList');
			list.innerHTML = '';

			for (let family of this.response){
				list.insertAdjacentHTML('beforeend', `<li onclick="loadFamily('${family.name}')">${family.name}</li>`);
			}
	});

	get("products/", function(){
			"use strict";
			if (familyWanted == ''){
				let list = document.getElementById('productsList');
				list.innerHTML = '';

				for (let product of this.response){
					list.insertAdjacentHTML('beforeend', `<li onclick="void(0)">${product.name}</li>`);
				}
			}
	});
}

function loadApp(){
	document.body.innerHTML = `<header>
	<nav class="navbar navbar-inverse">
	<div class="container">
		<div class="navbar-header">
		  <a class="navbar-brand" href="#">Mappeat</a>
		</div>
			<div class="navbar-collapse collapse navbar-right ">
				<button>Almacén</button>
				<button>Menú</button>
				<button onclick="loadTPV()">TPV</button>
				<button>Informes</button>
				<button onclick="loadSettings()">Ajustes</button>
				<button onclick="location.reload()">Salir</button>
			</div>
	</div>
	</nav>
	</header>
	<main>
	</main>`;

	main = document.querySelector('main');
	loadTPV();
}

function register(form){
	if( form.pass.value != form.passRepeated.value ){
		alert("Error: Las contraseñas deben coincidir.");
		return false;
	}

	var valores = Object();
	valores.username = form.username.value;
	valores.email = form.mail.value;
	valores.password = form.pass.value;

	post("register/", function(){
		form.parentNode.innerHTML = "<p>Registro completado, comprueba tu email.</p>";
	}, valores, true, "/accounts_api/");

	return false;
}

function login(form){
	var valores = Object();
	valores.username = form.username.value;
	valores.password = form.pass.value;

	post("login/", function(){
		loadApp();
	}, valores, true, "/rest-auth/");
    
    sessionStorage['username']= valores.username;
	return false;
}
