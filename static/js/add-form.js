function updateradio(pk) {
    var pt = document.getElementsByName("address"+pk);
    if (pt[1].checked) {
        document.getElementById("id_address_other"+pk).disabled = false;
    } else {
        document.getElementById("id_address_other"+pk).disabled = true;
    }
}

function updateCut() {
    var cut = document.getElementById("cut");
    if (cut.checked) {
        document.getElementById("id_return_date").disabled = false;
    } else {
        document.getElementById("id_return_date").disabled = true;
    }
}