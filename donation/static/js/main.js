/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function myFunction() {
    const x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

function myCreation() {
    document.querySelector(".Donor").style.visibility = "visible";
    document.querySelector(".Worker").style.visibility = "visible";
    document.querySelector(".CampDetail").style.visibility = "visible";
    document.querySelector(".create").style.visibility = "hidden";
}

