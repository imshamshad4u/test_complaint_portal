

// window.addEventListener('DOMContentLoaded', event => {
//     // Simple-DataTables
//     // https://github.com/fiduswriter/Simple-DataTables/wiki

//     const datatablesSimple = document.getElementById('table_id');
//     if (datatablesSimple) {
//         new simpleDatatables.DataTable(datatablesSimple);
//     }
// });
// $(document).ready(function () {
//     $("#table_id").hide();

//     $("#table_id").click(function () {
//         $("#table_id").toggle();
//     });
// });

function toggleNav() {
    var sidenav = document.getElementById("mySidenav");
    var main = document.getElementById("main");
    var toggleButton = document.getElementById("toggleButton");

    if (sidenav.style.width === "250px") {
        sidenav.style.width = "0";
        main.style.marginLeft = "0";
        toggleButton.innerHTML = "&#9776; open";
    } else {
        sidenav.style.width = "250px";
        main.style.marginLeft = "250px";
        toggleButton.innerHTML = "&times; close";
    }
}
// var dataFetched = false;
// $(document).ready(function () {
//     $("#fromDate_toDate").hide();

//     $("#All_complaints").click(function () {

//         if (!dataFetched) {
//             $("#fromDate_toDate").show();
//             $.ajax({
//                 url: "/All_complaints/",
//                 type: "GET",
//                 data: {
//                     "csrfmiddlewaretoken": "{{ csrf_token }}",
//                 },
//                 success: function (response) {
//                     // Handle the response from the backend
//                     // var data = JSON.parse(response.data);
//                     console.log('response', response)


//                     // var data = response.data;
//                     var table = document.getElementById('table_id');
//                     var tbody = table.getElementsByTagName('tbody')[0];

//                     for (var i = 0; i < response.length; i++) {
//                         var row = document.createElement('tr');
//                         var cell;

//                         var object = JSON.parse(response[i]);
//                         // var user_id;
//                         for (var key in object) {
//                             cell = document.createElement('td');
//                             cell.innerHTML = object[key];
//                             row.appendChild(cell);
//                             // if (key==='id'){
//                             //     user_id=key
//                             // }
//                         }
//                         cell = document.createElement('td');
//                         cell.innerHTML = `<a href="track_status/${object['id']}">Track Status</a>`;

//                         row.appendChild(cell);

//                         tbody.appendChild(row);
//                     }
//                     new simpleDatatables.DataTable(table);
//                     dataFetched = true;
//                     // Add date filter

//                 },
//                 error: function (xhr, errmsg, err) {
//                     // Handle any errors
//                     console.log(xhr.status + ": " + xhr.responseText);
//                 }
//             });
//         }
//     });

// });

{/* <script> */}


// Below script is for customer raising complain and in that date should have current date value //
        // click_date = document.getElementById('date').addEventListener('click', setCurrentDate);
document.addEventListener('DOMContentLoaded', setCurrentDate)
function setCurrentDate() {
    var dt = new Date()
    console.log(dt)
    // date in format of mmddyy
    var currentDate = new Date().toISOString().split('T')[0];
    document.getElementById('date').value = currentDate;
}
    // </script>