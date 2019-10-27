const departs = {}
$.getJSON('http://0.0.0.0:5001/api/v1/departments', data => {
  data.forEach(d => {
    departs[d.id] = `${d.name}`
  })
})

function loadEmployee(obj) {
  $.ajax({
    url: 'http://0.0.0.0:5001/api/v1/employees_search/',
    type: 'POST',
    contentType: 'application/json',
    dataType: 'json',
    data: JSON.stringify(obj||{}),
    success: function(data) {
      populateLeft(data)
    }
  })
}

function populateLeft(data) {
  data.map(employee => {
    $('.display-left h4').after(`
      <ul class="employee-list"><b>Employee Name: ${employee.first_name} ${employee.last_name}</b>
      <li>Id: ${employee.id}</li>
      <li>Email: ${employee.email}</li>
	<li>Department: ${departs[employee.department_id]}</li>
		<br />
			     </ul>
			     `)
  })
}

function loadTodo(obj) {
  $.ajax({
    url: 'http://0.0.0.0:5001/api/v1/todos_get/',
    type: 'POST',
    contentType: 'application/json',
    dataType: 'json',
    data: JSON.stringify(obj||{}),
    success: function(data) {
      populateMid(data)
    }
  })
}

function populateMid(data) {
  data.map(todo => {
    $('.display-mid h4').after(`
			       <ul class="todo-list">
			       <b>Job Title: ${todo.title}</b>
			       <li>Id: ${todo.id}</li>
			       <li>Completed: ${!!todo.completed}</li>
			       <li>Due Date: ${todo.due_date}</li>
			       <br />
			       </ul>
			       `)
  })
}

function loadEmpTodo(obj) {
  $.ajax({
    url: 'http://0.0.0.0:5001/api/v1/employees_gettodo/',
    type: 'POST',
    contentType: 'application/json',
    dataType: 'json',
    data: JSON.stringify(obj||{}),
    success: function(data) {
      populateMid(data)
    }
  })
}

function loadTodoEmp(obj) {
  $.ajax({
    url: 'http://0.0.0.0:5001/api/v1/todos_search/',
    type: 'POST',
    contentType: 'application/json',
    dataType: 'json',
    data: JSON.stringify(obj||{}),
    success: function(data) {
      populateLeft(data)
    }
  })
}

function createTodo(obj) {
  $.ajax({
    url: 'http://0.0.0.0:5001/api/v1/todos/',
    type: 'POST',
    contentType: 'application/json',
    dataType: 'json',
    data: JSON.stringify(obj||{}),
    success: function(data) {
      $('.display-mid h4').after(`
      <ul class="todo-list">
      <b>Create Success !</b>
      </ul>
      `)
    },
    error: function(data) {
      $('.display-mid h4').after(`
      <ul class="todo-list">
      <b>Create Fail !</b>
      </ul>
      `)
    }
  })
  $(":input").val('')
  return false
}

$(document ).ready(function() {
  /*
  $.get('http://0.0.0.0:5001/api/v1/status', (data) => {
    if (data.status === 'OK') {
      $('span#api_status').addClass('available');
    }
    else {
      $('span#api_status').removeClass('available');
    }
  })
  */

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
  })

  $('button.left1').click( function() {
    const obj = {
      departments: [...Object.keys(check_left1d)],
      employees: [...Object.keys(check_left1e)]
    }
    $('ul.employee-list').remove()
    loadEmployee(obj)
  })
  $('button.mid1').click( function() {
    const obj = {
      todos: [...Object.keys(check_mid1t)]
    }
    $('ul.todo-list').remove()
    loadTodo(obj)
  })
  $('button.left2').click( function() {
    const obj = {
      employees: [...Object.keys(check_left2e)]
    }
    $('ul.todo-list').remove()
    loadEmpTodo(obj)
  })
  $('button.mid2').click( function() {
    const obj = {
      todos: [...Object.keys(check_mid2t)]
    }
    $('ul.employee-list').remove()
    loadTodoEmp(obj)
  })
  $('form').submit(function(envent) {
    event.preventDefault()
    var inputs = $(":input")
    var obj = {}
    inputs.each(function() {
      obj[this.name] = $(this).val()
    })
    $('ul.todo-list').remove()
    createTodo(obj)
  })
})
