/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

function myCreation() {
                var x = document.createElement("Button");
                var b1 = document.createTextNode("DONOR");
                var b2 = document.createTextNode("WORKER");
                var b3 = document.createTextNode("CAMP DETAIL");
                x.appendChild(b1);
                x.appendChild(b2);
                x.appendChild(b3);
                document.body.appendChild(x);
        }

        document.querySelector('create').addEventListener('click',()=>{
            document.querySelector('Donor').style.visibility = 'visible';
            document.querySelector('Worker').style.visibility = 'visible';
            document.querySelector('CampDetail').style.visibility = 'visible';
            document.querySelector('create').style.visibility = 'hidden';
        })
