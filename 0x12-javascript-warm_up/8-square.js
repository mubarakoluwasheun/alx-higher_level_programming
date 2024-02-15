#!/usr/bin/node

const size = Math.floor(Number(process.argv[2]));
if (isNAN(size)) {
	console.log('Missing size');
} else {
	for (let i = 0; i < size; i++) {
		let sqr = '';
		for (let j = 0; j < size; j++) sqr += 'X';
		console.log(sqr);
	}
}
