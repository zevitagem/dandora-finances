$("#name").blur(function () {
  var name = $(this).val();

  if (name === "") {
    $("#vname").text("X Nome").removeClass("ok").addClass("nok");
  } else {
    $("#vname").text("✔ Nome").removeClass("nok").addClass("ok");
  }
});

$("#lastname").blur(function () {
  var lastname = $(this).val();

  if (lastname === "") {
    $("#vlastname").text("X sobrenome").removeClass("ok").addClass("start");
  } else {
    $("#vlastname")
      .text("✔ Sobrenome")
      .removeClass("start")
      .addClass("ok");
  }
});

$(document).ready(function () {

  $("#cpf").blur(function () {
    var cpf = $(this).val();

    if (validateCPF(cpf)) {
      $("#vcpf").text("✔ CPF").removeClass("nok").addClass("ok");
    } else {
      $("#vcpf").text("X CPF").removeClass("ok").addClass("nok");
    }
  });

  function validateCPF(cpf) {
    cpf = cpf.replace(/[^\d]+/g, "");

    if (cpf === "") return false;

    // Validar CPF

    var sum = 0;
    var remainder;

    for (var i = 1; i <= 9; i++) {
      sum += parseInt(cpf.substring(i - 1, i)) * (11 - i);
    }

    remainder = (sum * 10) % 11;

    if (remainder === 10 || remainder === 11) {
      remainder = 0;
    }

    if (remainder !== parseInt(cpf.substring(9, 10))) {
      return false;
    }

    sum = 0;

    for (var i = 1; i <= 10; i++) {
      sum += parseInt(cpf.substring(i - 1, i)) * (12 - i);
    }

    remainder = (sum * 10) % 11;

    if (remainder === 10 || remainder === 11) {
      remainder = 0;
    }

    if (remainder !== parseInt(cpf.substring(10, 11))) {
      return false;
    }

    return true;
  }


  $("#email").blur(function () {
    var email = $(this).val();

    if (validateEmail(email)) {
      $("#vemail").text("✔ E-mail").removeClass("nok").addClass("ok");
    } else {
      $("#vemail")
        .text("X E-mail")
        .removeClass("ok")
        .addClass("nok");
    }
  });

  $("#cpassword").keyup(function () {
    var password = $("#password").val();
    var cpassword = $(this).val();

    if (password === cpassword && password !== "" && cpassword !== "") {
      $("#vpassword")
        .text("✔ Senhas coincidem")
        .removeClass("nok")
        .addClass("ok");
    } else {
      $("#vpassword")
        .text("X As senhas devem ser iguais.")
        .removeClass("ok")
        .addClass("nok");
    }
  });


  function validateEmail(email) {
    var regex = /^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$/;
    return regex.test(email);
  }

  function validate() {
    var fields = [
      { name: "lastname", validation: "vlastname" },
      { name: "name", validation: "vname" },
      { name: "cpf", validation: "vcpf" },
      { name: "email", validation: "vemail" },
      { name: "password", validation: "vpassword" },
      { name: "cpassword", validation: "vcpassword" },
    ];

    fields.forEach(function (field) {
      var value = $("#" + field.name).val();
      var validationElement = $("#" + field.validation);

      if (value === "") {
        validationElement.removeClass("ok").addClass("start");
      } else {
        validationElement.removeClass("start").addClass("ok");
      }
    });
  }
});
