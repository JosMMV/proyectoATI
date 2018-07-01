$(document).ready(function(){
  $("#registrar").click(function(){
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
      $('#pass').focus();
      return false;
    }else if(Ccontras.trim() == ''){
      document.getElementById('alert-w').style.display = 'block';
      $('.alert-warning').text('El campo Repetir contraseña no puede estar vacío.');
      $('#Cpass').focus();
      return false;
    }else if(contras != Ccontras){
      document.getElementById('alert-w').style.display = 'block';
      $('.alert-warning').text('Contraseñas no coinciden. Verifique.');
      $('#pass').text('');
      $('#Cpass').text('');
      $('#pass').focus();
      return false;
    }else{
      $.ajax({
        url: '/register',
        data: $('#register').serialize(),
        type: 'POST',
        success: function(response){
          console.log(response);
        },
        error: function(error){
          console.log(error);
        }
      });
    }
  });
});

$(document).ready(function(){
  $("#iniciar").click(function(){
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
      $.ajax({
        url: '/home',
        data: $('#form-ini').serialize(),
        type: 'POST',
        success: function(response){
          console.log(response);
        },
        error: function(error){
          console.log(error);
        }
      });
    }
  });
});