/**
 * Submits the form data to the server.
 *
 * @return {Promise} A promise that resolves when the form data is 
 * successfully submitted.
 */
async function submitForm() {
    const fields = ['first_name', 'last_name', 'email', 
                    'subject', 'message'];
    const formData = {};

    for (const field of fields) {
        formData[field] = document.getElementById(field).value;
        if (!formData[field]) {
            document.getElementById("formStatus").textContent =
                "Por favor, complete todos los campos antes de enviar.";
            return;
        }
    }

    try {
        const response = await fetch(
            'https://netflix.zeabur.app/contact/submit-form', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(formData),
            }
        );
        if (!response.ok) throw new Error('Network response was not ok.');

        const data = await response.json();
        console.log('Success:', data);

        fields.forEach(field => document.getElementById(field).value = '');
        document.getElementById("formStatus").textContent =
            "¡Formulario enviado con éxito!";
    } catch (error) {
        console.error('Error:', error);
        document.getElementById("formStatus").textContent =
            "No se ha podido enviar el formulario. " +
            "Vuelva a intentarlo más tarde.";
    }
}