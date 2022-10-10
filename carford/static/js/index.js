function add_vehicle(){
    var form = $("#form_add_vehicle");
    $.ajax({
        type     : "POST",
        cache    : false,
        data     : form.serialize(), // serializes the form's elements.
        url      :"/api/v1/addvehicles/",
        success  : function(data) {
            window.location = '/owner/'+data.owner_id;
            location.reload()
            alert("Vehicle added")
        },
        error: function(xhr, status, error){
            alert("Error!" + xhr.status);
        }
    });
}

function add_owner(){
    var form = $('#form_add_owner');
    $.ajax({
        type     : "POST",
        cache    : false,
        data     : form.serialize(), // serializes the form's elements.
        url      :"/api/v1/addowner/",
        success  : function(data) {
            window.location = '/';
            alert("Onwer added")
        },
        error: function(xhr, status, error){
            alert("Error!" + xhr.status);
        }
    });
}
