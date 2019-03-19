var SX127x =require('sx127x')
var frecventa = process.argv[2];

var sx127x = new SX127x({
  frequency: frecventa
});

var count = 0;

// open the device
sx127x.open(function(err) {
  console.log('open', err ? err : 'success');

  //if (err) {
    //throw err;
 // }

  // add a event listener for data events
  sx127x.on('data', function(data, rssi) {
    console.log(data.toString() + ';'+rssi);
  });

	process.stdout.on('error', function( err ) {
    if (err.code == "EPIPE") {
        process.exit(0);
    }
	});


  // enable receive mode
  sx127x.receive(function(err) {
    //console.log('receive', err ? err : 'success');
  });
});



