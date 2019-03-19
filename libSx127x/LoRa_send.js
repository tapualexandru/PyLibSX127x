var SX127x =require('sx127x')

var frecventa = process.argv[2];
var mesaj= process.argv[3];


var sx127x = new SX127x({
  frequency: frecventa
});

var count = 0;

// open the device
sx127x.open(function(err) {
  console.log('open', err ? err : 'success');

  if (err) {
    throw err;
  }

  // send a message every second

   //console.log(mesaj);
   sx127x.write(new Buffer(mesaj), function(err) {
   console.log('transmission', err ? err : 'success');
	process.exit(1);
    });
	

});


