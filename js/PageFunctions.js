var summoner, server;

function enableDataView() {
    document.getElementById("inputView").style.display = "none";
    document.getElementById("dataView").style.display = "block";
}

function disableDataView() {
    document.getElementById("inputView").style.display = "block";
    document.getElementById("dataView").style.display = "none";
}

function processInput() {
    summoner = document.getElementById("summonerInput").value;
    server = document.getElementById("serverList").value;
    document.getElementById("summonerName").innerHTML = summoner;
    document.getElementById("serverName").innerHTML = server.toUpperCase();
    refreshData();
    enableDataView();
}

async function refreshData() {
    $("#championsList").empty();
    await getChestInfo(server, summoner);
    searchTable();
}

// Search through table
function searchTable() {
    var input = document.getElementById("championInput");
    var filter = input.value.toUpperCase();
    var expCheckbox = document.getElementById("remainingExpFilter");
    var chestCheckbox = document.getElementById("chestFilter");
    var table = document.getElementById("dataTable");
    var tr = table.getElementsByTagName("tr");
    
    // Loop through all table rows, and hide those which don't match the search query
    for (i = 0; i < tr.length; i++) {
        var tdName = tr[i].getElementsByTagName("td")[0];
        var tdNextLevel = tr[i].getElementsByTagName("td")[3];
        var tdChest = tr[i].getElementsByTagName("td")[4];
        if (tdName) {
            txtValue = tdName.textContent || tdName.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } 
            else {
                tr[i].style.display = "none";
            }
        }

        // Apply filters
        if ((tdNextLevel && (expCheckbox.checked == true)) && (tdChest && (chestCheckbox.checked == false)) && (tr[i].style.display == "")) {
            expValue = tdNextLevel.textContent || tdNextLevel.innerText;
            if (parseInt(expValue, 10) > 0) {
                tr[i].style.display = "";
            } 
            else {
                tr[i].style.display = "none";
            }
        }
        if ((tdNextLevel && (expCheckbox.checked == false)) && (tdChest && (chestCheckbox.checked == true)) && (tr[i].style.display == "")) {
            if (tdChest.getAttribute('data-chest-value') == "false") {
                tr[i].style.display = "";
            }
            else {
                tr[i].style.display = "none";
            }
        }
        if ((tdNextLevel && (expCheckbox.checked == true)) && (tdChest && (chestCheckbox.checked == true)) && (tr[i].style.display == "")) {
            expValue = tdNextLevel.textContent || tdNextLevel.innerText;
            if ((parseInt(expValue, 10) > 0) && (tdChest.getAttribute('data-chest-value') == "false")) {
                tr[i].style.display = "";
            } 
            else {
                tr[i].style.display = "none";
            }
        }
    }
}