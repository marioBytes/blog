// Sidenav init
var navbarElems = document.querySelector('.sidenav');
var navbarInst = M.Sidenav.init(navbarElems, {
  'inDuration': 500,
  'outDuration': 450,
  'preventScrolling': false,
});

// Parallax init
var parallaxElems = document.querySelector('.parallax');
var parallaxInst = M.Parallax.init(parallaxElems, {});

// Collapsible init
var collapsibleElems = document.querySelector('.collapsible');
var collapsibleInst = M.Collapsible.init(collapsibleElems, {
  'accordion': true,
});

var collapsibleElems2 = document.querySelector('.col2');
var collapsibleInst2 = M.Collapsible.init(collapsibleElems2, {
  'accordion': true,
});

var collapsibleElems3 = document.querySelector('.col3');
var collapsibleInst3 = M.Collapsible.init(collapsibleElems3, {
  'accordion': true,
});

setTimeout(function () {
    $('#messages').fadeOut('slow');
}, 3000);