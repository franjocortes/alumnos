const message_error = (data) => {
    let html = '';
    if (typeof (data) === 'object') {
        $.each(data, function (key, value) {
            html += `${value}<br>`;
        });
    } else {
        html = `<p>${data}</p>`;
    }
    Swal.fire({
        title: 'Se han encontrado errores',
        html: html,
        icon: 'error'
    });
};


// msj: El mensaje que quiero mostrar
// url: si quiero que me lleve a otro lado cuando termine de mostrar el mensaje
// function_ok: Funcion que quiero que se ejecute cuando termine de mostrar el mensaje
const message_info = (msg = 'Mensaje', url = '', function_ok = null) => {
    Swal.fire({
        position: 'top-end',
        icon: 'success',
        title: msg,
        showConfirmButton: false,
        timer: 1500
    }).then((r) => {
        if (url !== '') {
            location.href = url;
        }
        if (function_ok !== null) {
            function_ok();
        }
    });
};


const message_question = (msg = 'Mensaje', function_ok) => {
    Swal.fire({
        title: '¿Está seguro?',
        text: msg,
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si',
        cancelButtonText: 'No',
    }).then((result) => {
        if (result.isConfirmed) {
            function_ok();
        }
    })
};