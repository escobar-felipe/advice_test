function delete_car(vehicle_id){
    $.ajax({
        type     : "DELETE",
        url      :"/api/v1/vehicles/"+vehicle_id,
        success  : function(data) {
            if(data.number_vehicle ==1){
                window.location = '/';
            }else {
                location.reload()
            }
            alert("Vehicle deleted")
        },
        error: function(xhr, status, error){
            alert("Error!" + xhr.status);
        }
    });
}

function update_owner(vehicle_id){
    var owner_id = $('#owner').val();
    let data= {'owner':owner_id}
    $.ajax({
        type    : "PUT",
        cache   : false,
        url     : "/api/v1/vehicles/"+vehicle_id,
        data    : JSON.stringify(data),
        contentType: 'application/json',
        success  : function(data) {
            if(data.number_vehicle ==1){
                window.location = '/';
            }else {
                location.reload()
            }
            alert("Owner updated")
        },
        error: function(xhr, status, error){
            alert("Error!" + xhr.status);
        }
    })
}

function delete_owner(id_owner){
    $.ajax({
        type     : "DELETE",
        url      :"/api/v1/deleteowner/"+id_owner,
        success  : function(data) {
                window.location = '/';
            },
        error: function(xhr, status, error){
            alert("Error!" + xhr.status);
        }
    });
}