//FUNCION RUT

document.getElementById('rut').addEventListener('input', function (event) {
    let value = event.target.value.replace(/[^0-9kK]/g, '');

    if (value.length > 1) {
        value = value.slice(0, -1) + '-' + value.slice(-1);
    }

    if (value.length > 5) {
        value = value.slice(0, value.length - 5) + '.' + value.slice(value.length - 5);
    }

    if (value.length > 9) {
        value = value.slice(0, value.length - 9) + '.' + value.slice(value.length - 9);
    }

    event.target.value = value;
});
