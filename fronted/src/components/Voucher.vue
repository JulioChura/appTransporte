<script setup>
import { defineProps } from 'vue';

const props = defineProps({
  voucher: {
    type: Object,
    default: () => ({})
  },
  message: {
    type: String,
    default: ''
  }
});
</script>

<template>
  <div>
    <h2>{{ message }}</h2>
    <table>
      <tr>
        <th>ID</th>
        <td>{{ voucher.id }}</td>
      </tr>
      <tr>
        <th>Cost</th>
        <td>{{ voucher.cost }}</td>
      </tr>
      <tr>
        <th>Created At</th>
        <td>{{ voucher.created_at }}</td>
      </tr>
      <tr>
        <th>Updated At</th>
        <td>{{ voucher.updated_at }}</td>
      </tr>
      <tr>
        <th>Client</th>
        <td>{{ voucher.cliente }}</td>
      </tr>
      <tr>
        <th>Route</th>
        <td>
          <table>
            <tr>
              <th>Starting Place</th>
              <td>{{ voucher.ruta.startingPlace }}</td>
            </tr>
            <tr>
              <th>Destination Place</th>
              <td>{{ voucher.ruta.destinationPlace }}</td>
            </tr>
            <tr>
              <th>Distance</th>
              <td>{{ voucher.ruta.distance }}</td>
            </tr>
            <tr>
              <th>Stops</th>
              <td>{{ voucher.ruta.stops }}</td>
            </tr>
            <tr>
              <th>Horario</th>
              <td>{{ voucher.ruta.horario }}</td>
            </tr>
            <tr>
              <th>Fecha</th>
              <td>{{ voucher.ruta.fecha }}</td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
  </div>
</template>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  padding: 8px;
  border: 1px solid #ddd;
  text-align: left;
}

th {
  background-color: #f4f4f4;
}
</style>