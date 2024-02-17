const anual = document.getElementById('anual');
const meses = document.getElementById('meses');
const horario = document.getElementById('horario');

// Gráfico con el consumo del último año
new Chart(anual, {
type: 'line',
data: {
    labels: fechas,
    datasets: [{ label: 'kWh', data: datos, borderWidth: 1 }]
},
options: { scales: { y: { beginAtZero: true } } }
});

// Gráfico con la comparación por meses
new Chart(meses, {
type: 'bar',
data: {
    labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    datasets: [{
        label: 'kWh 2023',
        data: curr,
        borderWidth: 1
    },
    {
        label: 'kWh 2022',
        data: prev,
        borderWidth: 1
    }]
},
options: { scales: { y: { beginAtZero: true } } }
});

new Chart(horario, {
type: 'polarArea',
data: {
    // labels: ['12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00', '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00'],
    labels: ['12:00-18:00 (Mediodía)', '18:00-00:00 (Tarde)', '00:00-06:00 (Noche)', '06:00-12:00 (Mañana)'],
    datasets: [{
        label: 'kWh',
        data: consumos,
        borderWidth: 1
    },
    ]
},
});

new Chart(derecha, {
type: 'polarArea',
data: {
    // labels: ['12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00', '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00'],
    labels: ['12:00-18:00 (Mediodía)', '18:00-00:00 (Tarde)', '00:00-06:00 (Noche)', '06:00-12:00 (Mañana)'],
    datasets: [{
        label: 'kWh',
        data: consumos,
        borderWidth: 1
    },
    ]
 },
});
