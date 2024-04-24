document.addEventListener('DOMContentLoaded', function() {
    const formulario = document.getElementById('formulario');
    const cartaTextarea = document.getElementById('carta');
    const crearCartaBtn = document.getElementById('crear_carta');

    formulario.addEventListener('submit', function(event) {
        event.preventDefault();
    });

    crearCartaBtn.addEventListener('click', function() {
        const datos = obtenerDatosFormulario();
        const carta = generarCarta(datos);
        cartaTextarea.value = carta;
    });

    function obtenerDatosFormulario() {
        return {
            rut: document.getElementById('rut').value,
            nombre: document.getElementById('nombre').value,
            apellidoPaterno: document.getElementById('apellido_paterno').value,
            apellidoMaterno: document.getElementById('apellido_materno').value,
            fechaNacimiento: document.getElementById('fecha_nacimiento').value,
            edad: document.getElementById('edad').value,
            genero: document.getElementById('genero').value,
            email: document.getElementById('email').value,
            celular: document.getElementById('celular').value,
            especializacion: document.getElementById('especializacion').value,
            motivacion: document.getElementById('motivacion').value
        };
    }

    function generarCarta(datos) {
        return `Postulación, ${new Date().toLocaleDateString()}

Estimado equipo del Taller Rayo McQueen,

Mi nombre es ${datos.nombre} ${datos.apellidoPaterno} ${datos.apellidoMaterno}, con RUT ${datos.rut}, nacido el ${datos.fechaNacimiento} y de ${datos.edad} años de edad. Me dirijo a ustedes para expresar mi interés en la posición de mecánico en su empresa.

Mi especialización se encuentra en ${datos.especializacion}, y me motiva postular a este trabajo debido a ${datos.motivacion}. Adjunto a este correo, pueden encontrar mi información de contacto: 
- Email: ${datos.email}
- Celular: ${datos.celular}

Agradezco de antemano la oportunidad de participar en el proceso de selección y quedo a disposición para cualquier consulta adicional.

Atentamente,
${datos.nombre} ${datos.apellidoPaterno} ${datos.apellidoMaterno}`;
    }
});
