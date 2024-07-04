document.addEventListener('DOMContentLoaded', function() {
    const cartaTextarea = document.getElementById('carta');
    const crearCartaBtn = document.getElementById('crear_carta');
    
    crearCartaBtn.addEventListener('click', function() {
        const datos = obtenerDatosFormulario();
        const carta = generarCarta(datos);
        cartaTextarea.value = carta;
    });

    function obtenerDatosFormulario() {
        return {
            rut: document.getElementById('rut').value,
            pnombre: document.getElementById('pnombre').value,
            appaterno: document.getElementById('appaterno').value,
            apmaterno: document.getElementById('apmaterno').value,
            edad: document.getElementById('edad').value,
            tipo_genero: document.getElementById('tipo_genero').value,
            email: document.getElementById('email').value,
            celular: document.getElementById('celular').value,
            especializacion: document.getElementById('especializacion').value,
            motivo: document.getElementById('motivo').value
        };
    }

    function generarCarta(datos) {
        return `Postulación, ${new Date().toLocaleDateString()}

    Estimado equipo del Taller Rayo McQueen,

    Mi nombre es ${datos.pnombre} ${datos.appaterno} ${datos.apmaterno}, con RUT ${datos.rut}, con ${datos.edad} años de edad. Me dirijo a ustedes para expresar mi interés en la posición de mecánico en su empresa.

    Mi especialización se encuentra en ${datos.especializacion}, y me motiva postular a este trabajo debido a ${datos.motivo}. Adjunto a este correo, pueden encontrar mi información de contacto: 
    - Email: ${datos.email}
    - Celular: ${datos.celular}

    Agradezco de antemano la oportunidad de participar en el proceso de selección y quedo a disposición para cualquier consulta adicional.

    Atentamente,
    ${datos.pnombre} ${datos.appaterno} ${datos.apmaterno}`;
    }
});
