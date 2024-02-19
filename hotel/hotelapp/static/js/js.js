
$('.owl-carousel').owlCarousel({
  loop: true,
  margin: 30,
  dots: true,
  nav: false,
  responsiveClass: true,
  responsive: {
    0: {
      items: 2,
      margin: 10,
      stagePadding: 20,
    },
    600: {
      items: 3,
      margin: 20,
      stagePadding: 50,
    },
    1000: {
      items: 4
    }
  }
});


// bar 
$(document).ready(function() {
  var ctx = $("#chart-line");
  var myLineChart = new Chart(ctx, {
  type: 'bar',
  data: {
  labels: [1500, 1600, 1700, 1750, 1800, 1850, 1900, 1950, 1999, 2050],
  datasets: [{
  data: [86, 114, 106, 106, 107, 111, 133, 221, 783, 2478],
  label: "Africa",
  borderColor: "#458af7",
  backgroundColor: '#458af7',
  fill: false
  }, {
  data: [282, 350, 411, 502, 635, 809, 947, 1402, 3700, 5267],
  label: "Asia",
  borderColor: "#8e5ea2",
  fill: true,
  backgroundColor: '#8e5ea2'
  }, {
  data: [168, 170, 178, 190, 203, 276, 408, 547, 675, 734],
  label: "Europe",
  borderColor: "#3cba9f",
  fill: false,
  backgroundColor: '#3cba9f'
  }]
  },
  options: {
  title: {
  display: true,
  text: 'World population per region (in millions)'
  }
  }
  });
  });


// tabs

    


    