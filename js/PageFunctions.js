var summoner, server;

function enableDataView() {
    document.getElementById("inputView").style.display = "none";
    document.getElementById("dataView").style.display = "block";
    document.getElementById("dataTable").style.visibility = "visible";
    document.getElementById("championInput").style.visibility = "visible";
}

function disableDataView() {
    document.getElementById("inputView").style.display = "block";
    document.getElementById("dataView").style.display = "none";
    document.getElementById("dataTable").style.visibility = "hidden";
    document.getElementById("championInput").style.visibility = "hidden";
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
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("championInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("dataTable");
    tr = table.getElementsByTagName("tr");
    
    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } 
            else {
                tr[i].style.display = "none";
            }
        }
    }
}