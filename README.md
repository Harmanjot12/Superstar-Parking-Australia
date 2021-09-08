# Superstar-Parking-Australia


<p>The program will allow the operator to enter the details for each car parked during the day, and save these details into a file named 'cars-parked-w.bin'. The entered details are the car plate number, the car entrance time in hours:minutes and the car exit time in hours:minutes. The program must use a loop that allows the operator to enter another car details. </p>
<br>
The program should also check the input for validity according to the following rules:<br>

<ul>
<li>Car plate number must be an alpha numeric string of exactly six digits (e.g. ABC123).</li>
<li>Car entrance and exit times must be in the format hours:minutes and can take values from 00:00 to 23:59.</li>
<li>The exit time must be greater than the entrance time.</li>
</ul>

<br>

<p>The program sholud also open a file 'cars-parked-r.bin' for reading and read each record, splitting it into its component fields and checking each field for validity. The rules for validity are similar to those of Program A, with the additional rule that each record must contain exactly fields that helps to save the record that allow car to exits. Your program should print out each valid record it reads. Your program should terminate when it reads an invalid record, printing out on which line number the error occurred, and what the error was.</p>
