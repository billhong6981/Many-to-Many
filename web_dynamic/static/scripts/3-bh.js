
$(document ).ready(function() {
  const check_left1d = {};
  const check_left1e = {};
  const check_left2e = {};
  const check_mid1t = {};
  const check_mid2t = {};
  $('.left1d INPUT:checkbox').change( function() {
    if ($(this).is(':checked')) {
      let k = $(this).attr('data-id');
      let v = $(this).attr('data-name');
      check_left1d[k] = v;
    }
    if (!$(this).is(':checked')) {
      delete check_left1d[$(this).attr('data-id')]
    }
    let s = "";
    const entries = Object.entries(check_left1d);
    entries.forEach(entry => {
      entry[1] += ', ';
      s += entry[1];
    });
    alert(s)
  })

  $('.left1e INPUT:checkbox').change( function() {
    if ($(this).is(':checked')) {
      let k = $(this).attr('data-id');
      let v = $(this).attr('data-name');
      check_left1e[k] = v;
    }
    if (!$(this).is(':checked')) {
      delete check_left1e[$(this).attr('data-id')]
    }
    let s1 = "";
    const entries = Object.entries(check_left1e);
    entries.forEach(entry => {
      entry[1] += ', ';
      s1 += entry[1];
    });
    alert(s1)
  })

  $('.left2e INPUT:checkbox').change( function() {
    if ($(this).is(':checked')) {
      let k = $(this).attr('data-id');
      let v = $(this).attr('data-name');
      check_left2e[k] = v;
    }
    if (!$(this).is(':checked')) {
      delete check_left2e[$(this).attr('data-id')]
    }
    let s = "";
    const entries = Object.entries(check_left2e);
    entries.forEach(entry => {
      entry[1] += ', ';
      s += entry[1];
    });
    alert(s)
  })

  $('.mid1t INPUT:checkbox').change( function() {
    if ($(this).is(':checked')) {
      let k = $(this).attr('data-id');
      let v = $(this).attr('data-name');
      check_mid1t[k] = v;
    }
    if (!$(this).is(':checked')) {
      delete check_mid1t[$(this).attr('data-id')]
    }
    let s = "";
    const entries = Object.entries(check_mid1t);
    entries.forEach(entry => {
      entry[1] += ', ';
      s += entry[1];
    });
    alert(s)
  })

  $('.mid2t INPUT:checkbox').change( function() {
    if ($(this).is(':checked')) {
      let k = $(this).attr('data-id');
      let v = $(this).attr('data-name');
      check_mid2t[k] = v;
    }
    if (!$(this).is(':checked')) {
      delete check_mid2t[$(this).attr('data-id')]
    }
    let s = "";
    const entries = Object.entries(check_mid2t);
    entries.forEach(entry => {
      entry[1] += ', ';
      s += entry[1];
    });
    alert(s)
  })

  $.get('http://0.0.0.0:5001/api/v1/status', (data) => {
    if (data.status === 'OK') {
      $('span#api_status').addClass('available');
    }
    else {
      $('span#api_status').removeClass('available');
    }
  });
})
  /**
  $.ajax({
    url: 'http://0.0.0.0:5001/api/v1/employees_search/',
    type: 'POST',
    contentType: 'application/json',
    dataType: 'json',
    data: JSON.stringify({}),
    success: function(data) {
      populateArticle(data);
    }
  });
});

function populateArticle(obj) {
  obj.map(employee => {
    $('.display-left').remove()
    $('.display-left').append(`
      <p></p>
  <ul><b>Employee Name: {{ employee.first_name + " " + employee.last_name }}</b>
      <li>Id: ${employee.id}</li>
      <li>Email: ${employee.email}</li>
      {% for department in departments.values() %}
    {% if employee in department.employees %}
      <li>Department: {{ department.name }}</li>
      <li>Id: {{ department.id }}</li>
      {% endif %}
    {% endfor %}
    </ul>
      {% endfor %}
			      `)

    $('.places h1').after(`<article>
			  <div class="title">
			  <h2>${place.name}</h2>
			  <div class="price_by_night">
			  $${place.price_by_night}
			  </div>
			  </div>
			  <div class="information">
			  <div class="max_guest">
			  <i class="fa fa-users fa-3x" aria-hidden="true"></i>
			  <br />
			  ${place.max_guest} Guests
			  </div>
			  <div class="number_rooms">
			  <i class="fa fa-bed fa-3x" aria-hidden="true"></i>
			  <br />
			  ${place.number_rooms} Bedrooms
			  </div>
			  <div class="number_bathrooms">
			  <i class="fa fa-bath fa-3x" aria-hidden="true"></i>
			  <br />
			  ${place.number_bathrooms} Bathroom
			  </div>
			  </div>
			  <!-- **********************
			  USER
			  **********************  -->
			  <div class="user">
			  <strong>Owner:&nbsp;</strong>
			  </div>
			  <div class="description">
			  ${place.description}
			  </div>
			  </article> <!-- End 1 PLACE Article -->
			  `)
  });
  */
