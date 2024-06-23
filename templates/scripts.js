document.addEventListener('DOMContentLoaded', function () {
    // Daily Emissions Chart
    var ctx = document.getElementById('dailyEmissionsChart').getContext('2d');
    var dailyEmissionsChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            datasets: [{
                label: 'g CO2',
                data: [1500, 1300, 1700, 2100, 1800, 2000, 1900],
                backgroundColor: 'var(--primary-color)',
                borderColor: 'var(--primary-color)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    

    // Weekly Revenue Chart
    var ctx3 = document.getElementById('weeklyRevenueChart').getContext('2d');
    var weeklyRevenueChart = new Chart(ctx3, {
        type: 'line',
        data: {
            labels: ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July'],
            datasets: [{
                label: 'Net Emission',
                data: [200, -60, 100, 800, -91, -200, 0],
                backgroundColor: '#5ea63c',
                borderColor: 'var(--primary-color)',
                borderWidth: 1,
                fill: true
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});
