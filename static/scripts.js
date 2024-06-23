document.addEventListener('DOMContentLoaded', function () {
    // Daily Emissions Chart
    var ctx = document.getElementById('dailyEmissionsChart').getContext('2d');
    var dailyEmissionsChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            datasets: [{
                label: 'kg CO2',
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

    // Emissions Breakdown Pie Chart
    var ctx2 = document.getElementById('emissionsPieChart').getContext('2d');
    var emissionsPieChart = new Chart(ctx2, {
        type: 'pie',
        data: {
            labels: ['Transportation', 'Energy', 'Waste', 'Industry', 'Agriculture'],
            datasets: [{
                data: [25.5, 30.8, 15.3, 10.5, 18.2],
                backgroundColor: ['var(--primary-color)', 'var(--secondary-color)', 'var(--danger-color)', '#ffeb3b', '#4caf50'],
                borderColor: ['#fff', '#fff', '#fff', '#fff', '#fff'],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
        }
    });

    // Weekly Revenue Chart
    var ctx3 = document.getElementById('weeklyRevenueChart').getContext('2d');
    var weeklyRevenueChart = new Chart(ctx3, {
        type: 'line',
        data: {
            labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            datasets: [{
                label: 'Revenue',
                data: [5000, 6000, 7000, 8000, 9000, 10000, 11000],
                backgroundColor: 'rgba(46, 125, 50, 0.2)',
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
