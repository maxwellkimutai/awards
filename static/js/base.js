$(document).ready(function () {
    var projects = []
    $.ajax({
        url: 'http://'+ window.location.host +'/api/projects',
        success: function (data) {
            $.each(data, function(index,value) {
                projects.push(value['title'])
            });
            $( "#search" ).autocomplete({
              source: projects
            });
        }
    });
    
});
