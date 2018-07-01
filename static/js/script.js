$(document).ready(function(){
  $("#register").submit(function(){
    var nombre = $('#Rname').val();
    var apellido = $('#RlastName').val();
    var correo = $('#Remail').val();
    var contras = $('#Rpass').val();
    var Ccontras = $('#RCpass').val();
    if(nombre.trim() == ''){
      document.getElementById('alert-w').style.display = 'block';
      $('.alert-warning').text("El campo Nombre no puede estar vacío.");
      $('#Rname').focus();
      return false;
    }else if(apellido.trim() == ''){
      document.getElementById('alert-w').style.display = 'block';
      $('.alert-warning').text('El campo Apellido no puede estar vacío.');
      $('#RlastName').focus();
      return false;
    }else if(correo.trim() == ''){
      document.getElementById('alert-w').style.display = 'block';
      $('.alert-warning').text('El campo Correo no puede estar vacío.');
      $('#email').focus();
      return false;
    }else if(contras.trim() == ''){
      document.getElementById('alert-w').style.display = 'block';
      $('.alert-warning').text('El campo Contraseña no puede estar vacío.');
      $('#Rpass').focus();
      return false;
    }else if(Ccontras.trim() == ''){
      document.getElementById('alert-w').style.display = 'block';
      $('.alert-warning').text('El campo Repetir contraseña no puede estar vacío.');
      $('#RCpass').focus();
      return false;
    }else if(contras != Ccontras){
      document.getElementById('alert-w').style.display = 'block';
      $('.alert-warning').text('Contraseñas no coinciden. Verifique.');
      $('#Rpass').text('');
      $('#RCpass').text('');
      $('#Rpass').focus();
      return false;
    }else{
      return true;
    }
  });
});

$(document).ready(function(){
  $("#form-ini").submit(function(){
    var correo = $('#email').val();
    var contras = $('#pass').val();
    if(correo.trim() == ''){
      document.getElementById('alert-w-i').style.display = 'block';
      $('#alert-w-i').text("El campo Correo no puede estar vacío.");
      $('#email').focus();
      return false;
    }else if(contras.trim() == ''){
      document.getElementById('alert-w-i').style.display = 'block';
      $('#alert-w-i').text('El campo Contraseña no puede estar vacío.');
      $('#pass').focus();
      return false;
    }else{
      return true;
    }
  });
});