$(document).ready( function() {
    $(".admin-widget_header").hover(function() {
        $(this).attr('class', 'admin-widget_header bg-final');
        }, function() {
        $(this).attr('class', 'admin-widget_header bg-first');
    });
    $(".admin-widget_header").click(function() {
        var wid_name = $(this).attr('id');
        $("#admin-widget_box_" + wid_name).slideToggle("fast");
    });
});


function togglePublish(type, pk, what) {
    xhr = jQuery.post('/admin/incu',
                      {'pk':pk,
                        'published':what,
                      },
                      function (data){
                          $("#admin-widget_box_"+type).html(data);
                      });
}


function bootEditor(type, pk){
    xhr = jQuery.get('/admin/form/'+type, 
                     function (data) {
                        $("#editor").html(data);
                     });
}
