<script setup>
import { defineProps, onMounted, ref } from 'vue';

const props = defineProps({
  voucher: {
    type: Object,
    default: () => ({})
  },
  user: {
    type: Object,
    default: () => ({})
  },
  message: {
    type: String,
    default: ''
  }
});

const pdfContent = ref(null);

onMounted(() => {
  //jsPDF y html2canvas permiten capturar el html con css incluido(como imagen)
  const script1 = document.createElement('script');
  script1.src = 'https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.4.0/jspdf.umd.min.js';
  script1.onload = () => {
    const script2 = document.createElement('script');
    script2.src = 'https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js';
    script2.onload = () => console.log('jsPDF and html2canvas loaded');
    document.head.appendChild(script2);
  };
  document.head.appendChild(script1);
});

const generatePDF = async () => {
  if (window.jspdf && window.html2canvas) {
    const { jsPDF } = window.jspdf;

    // Capturar el contenido HTML
    const canvas = await html2canvas(pdfContent.value);
    const imgData = canvas.toDataURL('image/png');
    const doc = new jsPDF();
    doc.addImage(imgData, 'PNG', 10, 10);

    // Descargar pdf
    doc.save('voucher.pdf');
    
    // Enviar el PDF por correo
    const pdfData = doc.output('blob');
    await sendPDFByEmail(pdfData);
  }
};

const sendPDFByEmail = async (pdfBlob) => {
  const formData = new FormData();
  formData.append('pdf', pdfBlob, 'voucher.pdf');
  formData.append('to_email', props.user.email); // Añade el email del usuario

  try {
    const response = await fetch('http://127.0.0.1:8000/api/send-email/', {
      method: 'POST',
      body: formData,
      credentials: 'include',
      headers: {
        'X-Requested-With': 'XMLHttpRequest',
      },
    });
    
    if (response.ok) {
      const data = await response.json();
      alert(`PDF enviado con éxito desde a ${data.to_email}`);
    } else {
      const errorData = await response.json();
      alert(`Error al enviar el PDF por correo electrónico: ${errorData.error}`);
    }
  } catch (error) {
    console.error('Error:', error);
    alert('Error al enviar el PDF por correo electrónico');
  }
};
const calculateIGV = (costo) => {
  return parseFloat((costo * 0.18).toFixed(2));
};

const calculateSubtotal = (costo) => {
  var igv = calculateIGV(costo);
  var subtotal = parseFloat(costo) - igv;
  return subtotal;
};

</script>


<template>
  <div class="voucher-container" ref="pdfContent">
    <div class="header">
      <h1>AQPTransporte</h1>
      <p><strong>**Gracias por su compra**</strong></p>
      <p><strong>Agradecemos su confianza en nuestros servicios. Para cualquier consulta o asistencia, no dude en contactarnos. ¡Que tenga un excelente viaje!</strong></p>
    </div>

    <div class="voucher-content" >
      <div class="company-info">
        <h2><strong>TRANSPORTES AQPTransporte S.R.L</strong></h2>
        <h3>COMPROBANTE ELECTRÓNICO DE VENTA NO. {{ voucher.id }}</h3>
        <p>RUC: 0992639075001</p>
        <p>Av. Independencia, Arequipa, Perú</p>
      </div>

      <div class="client-info">
        <h4><strong>Datos del pasajero</strong></h4>
        <p><strong>Cliente:</strong> {{ user?.Name }} {{ user?.LastName }}</p>
        <p><strong>DNI:</strong> {{ user?.DNI }}</p>
        <p><strong>Dirección:</strong> (No hay) </p>
        <p><strong>Teléfono:</strong> {{ user?.Cellphone }}</p>
        <p><strong>E-mail:</strong> {{ user?.email }}</p>
        <h4><strong>Datos de viaje</strong></h4>
        <p><strong>Origen:</strong> {{ voucher.ruta.startingPlace }}</p>
        <p><strong>Destino:</strong> {{ voucher.ruta.destinationPlace }}</p>
        <p><strong>Fecha:</strong> {{ voucher.ruta.fecha }} <strong>Hora:</strong> {{ voucher.ruta.horario }}</p>
        <p><strong>Nro de asiento:</strong> (Falta )</p>
        <p><strong>Tipo Venta:</strong> Yape/Internet/Electronico</p>
      </div>

      <div class="totals">
        <p><strong>Subtotal:</strong> S/.{{ calculateSubtotal(voucher.ruta.cost) }}</p>
        <p><strong>IGV 18%:</strong> S/.{{ calculateIGV(voucher.ruta.cost) }}</p>
        <p><strong>Monto a pagar:</strong> S/.{{ voucher.ruta.cost }}</p>
      </div>

      <p class="note">ESTE DOCUMENTO ES UNA REIMPRESIÓN</p>
      <p class="note">UTILIZACION DEL SISTEMA FINANCIERO</p>
    </div>
    <button @click="generatePDF">Descargar Voucher</button>
  </div>
</template>

<style scoped>
.voucher-container {
  font-family: 'Times New Roman', serif;
  max-width: 800px;
  margin: 0 auto;
  padding: 30px;
  border: 2px solid #000;
  border-radius: 10px;
  background-color: #fff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  color: #333;
}

.header {
  text-align: center;
  border-bottom: 2px solid #000;
  padding-bottom: 15px;
  margin-bottom: 25px;
}

.header h1 {
  color: #000;
  font-size: 36px;
  margin: 0;
}

.header p {
  font-size: 18px;
  margin: 5px 0 0;
}

.company-info, .client-info, .totals {
  margin-bottom: 25px;
}

.company-info h2, .company-info h3 {
  color: #000;
  margin: 0 0 10px;
}

.company-info p {
  margin: 5px 0;
}

.client-info h4 {
  margin: 10px 0 5px;
  color: #000;
  font-size: 20px;
  border-bottom: 1px solid #000;
  padding-bottom: 5px;
}

.client-info p {
  margin: 5px 0;
  font-size: 16px;
}

.totals {
  text-align: right;
  font-size: 16px;
}

.totals p {
  margin: 5px 0;
}

.note {
  text-align: center;
  color: #555;
  font-size: 14px;
  margin-top: 20px;
}

button {
  display: block;
  width: 100%;
  max-width: 250px;
  margin: 30px auto 0;
  padding: 12px 20px;
  background-color: #000;
  color: #fff;
  border: 2px solid #000;
  border-radius: 5px;
  cursor: pointer;
  font-size: 18px;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #333;
}
</style>

