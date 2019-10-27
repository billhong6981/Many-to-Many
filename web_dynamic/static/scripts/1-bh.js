$(document ).ready(function() {
  const checkDict = {};
  $('LI INPUT:checkbox').change(function () {
    if ($(this).is(':checked')) {
      let k = $(this).attr('data-id');
      let v = $(this).attr('data-name');
      checkDict[k] = v;
    }
    if (!$(this).is(':checked')) {
      delete checkDict[$(this).attr('data-id')]
    }
    let s = "";
    const entries = Object.entries(checkDict);
    entries.forEach(entry => {
      entry[1] += ', ';
      s += entry[1];
    });
  });
});
